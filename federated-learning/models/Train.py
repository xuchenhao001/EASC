import torch
from torch import nn


def train_cnn_mlp(net, my_dataset, idx, local_ep, device, lr, momentum, local_bs):
    net.train()
    optimizer = torch.optim.SGD(net.parameters(), lr=lr, momentum=momentum)
    ldr_train = my_dataset.load_train_dataset(idx, local_bs)
    loss_func = nn.CrossEntropyLoss()

    epoch_loss = []
    for _ in range(local_ep):
        batch_loss = []
        for batch_idx, (images, labels) in enumerate(ldr_train):
            images = images.detach().clone().type(torch.FloatTensor)
            if device != "cpu":
                images, labels = images.to(device), labels.to(device)
            net.zero_grad()
            log_probs = net(images)
            loss = loss_func(log_probs, labels)
            loss.backward()
            optimizer.step()
            batch_loss.append(loss.item())
        epoch_loss.append(sum(batch_loss) / len(batch_loss))
    return net.state_dict(), sum(epoch_loss) / len(epoch_loss)

