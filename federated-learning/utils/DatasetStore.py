import logging
import os
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import datasets, transforms

from utils.sampling import noniid_onepass
from datasets.IMAGENET import IMAGENETDataset
from datasets.REALWORLD import REALWORLDDataset
from datasets.UCI import UCIDataset
from utils.util import ColoredLogger

logging.setLoggerClass(ColoredLogger)
logging.getLogger("werkzeug").setLevel(logging.ERROR)
logger = logging.getLogger("DatasetStore")


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


class LocalDataset:
    def __init__(self):
        self.initialized = False
        self.dataset_name = ""
        self.dataset_train = None
        self.dataset_test = None
        self.image_shape = None
        self.dict_users = None
        self.test_users = None
        self.skew_users = None

    def init_local_dataset(self, dataset_name, num_users):
        dataset_train = None
        dataset_test = None
        real_path = os.path.dirname(os.path.realpath(__file__))
        # load dataset and split users
        if dataset_name == 'mnist':
            trans = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])
            data_path = os.path.join(real_path, "../../data/mnist/")
            dataset_train = datasets.MNIST(data_path, train=True, download=True, transform=trans)
            dataset_test = datasets.MNIST(data_path, train=False, download=True, transform=trans)

        elif dataset_name == 'fmnist':
            trans = transforms.Compose([transforms.ToTensor()])
            data_path = os.path.join(real_path, "../../data/fashion-mnist/")
            dataset_train = datasets.FashionMNIST(data_path, train=True, download=True, transform=trans)
            dataset_test = datasets.FashionMNIST(data_path, train=False, download=True, transform=trans)

        elif dataset_name == 'cifar10':
            trans = transforms.Compose(
                [transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
            data_path = os.path.join(real_path, "../../data/cifar10/")
            dataset_train = datasets.CIFAR10(data_path, train=True, download=True, transform=trans)
            dataset_test = datasets.CIFAR10(data_path, train=False, download=True, transform=trans)

        elif dataset_name == 'cifar100':
            trans = transforms.Compose(
                [transforms.ToTensor(), transforms.Normalize((0.5074, 0.4867, 0.4411), (0.2011, 0.1987, 0.2025))])
            data_path = os.path.join(real_path, "../../data/cifar100/")
            dataset_train = datasets.CIFAR100(data_path, train=True, download=True, transform=trans)
            dataset_test = datasets.CIFAR100(data_path, train=False, download=True, transform=trans)

        elif dataset_name == 'imagenet':
            # https://towardsdatascience.com/pytorch-ignite-classifying-tiny-imagenet-with-efficientnet-e5b1768e5e8f#4195
            # https://github.com/kennethleungty/PyTorch-Ignite-Tiny-ImageNet-Classification
            # Retrieve data directly from Stanford data source
            # !wget http://cs231n.stanford.edu/tiny-imagenet-200.zip
            trans = transforms.Compose(
                [transforms.Resize(256), transforms.CenterCrop(224), transforms.RandomHorizontalFlip(),
                 transforms.ToTensor()])
            data_path = os.path.join(real_path, "../../data/imagenet/")
            train_dir = os.path.join(data_path, 'train')
            # test_dir = os.path.join(data_path, 'test')
            dataset_full = datasets.ImageFolder(train_dir, transform=trans)
            train_size = int(0.8 * len(dataset_full))
            test_size = len(dataset_full) - train_size
            subset_train, subset_test = torch.utils.data.random_split(dataset_full, [train_size, test_size])
            dataset_train = IMAGENETDataset(subset_train)
            dataset_test = IMAGENETDataset(subset_test)

        elif dataset_name == 'uci':
            # https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones
            uci_data_path = os.path.join(real_path, "../../data/uci/")
            dataset_train = UCIDataset(data_path=uci_data_path, phase='train')
            dataset_test = UCIDataset(data_path=uci_data_path, phase='eval')

        elif dataset_name == 'realworld':
            # https://sensor.informatik.uni-mannheim.de/#dataset_realworld
            realworld_data_path = os.path.join(real_path, "../../data/realworld/")
            dataset_train = REALWORLDDataset(data_path=realworld_data_path, phase='train')
            dataset_test = REALWORLDDataset(data_path=realworld_data_path, phase='eval')

        dict_users, test_users, skew_users = noniid_onepass(dataset_train, dataset_test, num_users,
                                                            dataset_name=dataset_name)

        self.dataset_name = dataset_name
        self.dataset_train = dataset_train
        self.dataset_test = dataset_test
        self.image_shape = dataset_train[0][0].shape
        self.dict_users = dict_users
        self.test_users = test_users
        self.skew_users = skew_users
        self.initialized = True

    def load_train_dataset(self, idx, local_bs):
        split_ds = DatasetSplit(self.dataset_train, self.dict_users[idx])
        return DataLoader(split_ds, batch_size=local_bs, shuffle=True)

    def load_test_dataset(self, idxs, local_test_bs):
        split_ds = DatasetSplit(self.dataset_test, idxs)
        return DataLoader(split_ds, batch_size=local_test_bs)
