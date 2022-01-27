import os

import torch
from torch.utils.data import Dataset
from torchvision import datasets, transforms


class IMAGENETDataset(Dataset):
    def __init__(self, subset):
        self.subset = subset
        self.targets = self.get_targets()

    def __len__(self):
        return len(self.subset.indices)

    def __getitem__(self, idx):
        return self.subset.dataset[self.subset.indices[idx]]

    def get_targets(self):
        target_mapping = map(self.subset.dataset.targets.__getitem__, self.subset.indices)
        return list(target_mapping)


if __name__ == '__main__':
    real_path = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(real_path, "../../data/imagenet/")
    train_dir = os.path.join(data_path, 'train')
    trans = transforms.Compose(
        [transforms.Resize(256), transforms.CenterCrop(224), transforms.RandomHorizontalFlip(),
         transforms.ToTensor()])
    dataset_full = datasets.ImageFolder(train_dir, transform=trans)
    print("dataset_full")
    train_size = int(0.8 * len(dataset_full))
    test_size = len(dataset_full) - train_size
    subset_train, subset_test = torch.utils.data.random_split(dataset_full, [train_size, test_size])
    print("subset_train and subset_test")

    dataset_train = IMAGENETDataset(subset_train)
    dataset_test = IMAGENETDataset(subset_test)
    print("dataset train: {}".format(dataset_train))
    print("dataset test: {}".format(dataset_test))
    print(dataset_train[0][0].shape, dataset_train[0][1])
    print(len(dataset_train))
    print(len(dataset_test))
    print("dataset train targets len: {}".format(len(dataset_train.targets)))
