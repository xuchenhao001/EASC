import logging
import os
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import datasets, transforms

from utils.sampling import noniid_onepass
from datasets.REALWORLD import REALWORLDDataset
from datasets.UCI import UCIDataset
from utils.util import ColoredLogger

logging.setLoggerClass(ColoredLogger)
logging.getLogger("werkzeug").setLevel(logging.ERROR)
logger = logging.getLogger("Datasets")


class DatasetSplit(Dataset):
    def __init__(self, dataset, idxs):
        self.dataset = dataset
        self.idxs = list(idxs)
        self.targets = torch.Tensor([self.dataset.targets[idx] for idx in idxs])

    def classes(self):
        return torch.unique(self.targets)

    def __len__(self):
        return len(self.idxs)

    def __getitem__(self, item):
        data, label = self.dataset[self.idxs[item]]
        return data, label


class MyDataset:
    def __init__(self, dataset_name, dataset_train_size, num_users):
        self.dataset_train_size = dataset_train_size
        dataset_test_size = int(dataset_train_size * 0.2)
        self.dataset_test_size = dataset_test_size
        dataset_train = None
        dataset_test = None
        real_path = os.path.dirname(os.path.realpath(__file__))
        # load dataset and split users
        if dataset_name == 'mnist':
            trans_mnist = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])
            mnist_data_path = os.path.join(real_path, "../../data/mnist/")
            dataset_train = datasets.MNIST(mnist_data_path, train=True, download=True, transform=trans_mnist)
            dataset_test = datasets.MNIST(mnist_data_path, train=False, download=True, transform=trans_mnist)

        elif dataset_name == 'fmnist':
            trans_fashion = transforms.Compose([transforms.ToTensor()])
            mnist_data_path = os.path.join(real_path, "../../data/fashion-mnist/")
            dataset_train = datasets.FashionMNIST(mnist_data_path, train=True, download=True, transform=trans_fashion)
            dataset_test = datasets.FashionMNIST(mnist_data_path, train=False, download=True, transform=trans_fashion)

        elif dataset_name == 'cifar':
            trans_cifar = transforms.Compose(
                [transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
            cifar_data_path = os.path.join(real_path, "../../data/cifar/")
            dataset_train = datasets.CIFAR10(cifar_data_path, train=True, download=True, transform=trans_cifar)
            dataset_test = datasets.CIFAR10(cifar_data_path, train=False, download=True, transform=trans_cifar)

        elif dataset_name == 'uci':
            # https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones
            uci_data_path = os.path.join(real_path, "../../data/uci/")
            dataset_train = UCIDataset(data_path=uci_data_path, phase='train')
            dataset_test = UCIDataset(data_path=uci_data_path, phase='eval')

        elif dataset_name == 'realworld':
            # https://sensor.informatik.uni-mannheim.de/#dataset_realworld
            realworld_data_path = os.path.join(real_path, "../../data/realworld_client/")
            dataset_train = REALWORLDDataset(data_path=realworld_data_path, phase='train')
            dataset_test = REALWORLDDataset(data_path=realworld_data_path, phase='eval')

        dict_users, test_users, skew_users = noniid_onepass(dataset_train, dataset_test, num_users,
                                                            dataset_name=dataset_name)

        self.dataset_name = dataset_name
        self.dataset_train = dataset_train
        self.dataset_test = dataset_test
        self.dict_users = dict_users
        self.test_users = test_users
        self.skew_users = skew_users

    def load_train_dataset(self, idx, local_bs):
        split_ds = DatasetSplit(self.dataset_train, self.dict_users[idx])
        return DataLoader(split_ds, batch_size=local_bs, shuffle=True)

    def load_test_dataset(self, idxs, local_test_bs):
        split_ds = DatasetSplit(self.dataset_test, idxs)
        return DataLoader(split_ds, batch_size=local_test_bs)
