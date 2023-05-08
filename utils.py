import torch
from matplotlib import pyplot as plt
def plot_curve(data):
    fig = plt.figure()
    plt.plot(range(len(data)), data, color='blue')
    plt.legend(['value'], loc='upper right')
    plt.xlabel('step')
    plt.ylabel('value')
    plt.show()

def plot_image(image, label, name):
    fig = plt.figure()
    for i in range(6):
        plt.subplots(2, 3, i + 1)
        plt.tight_layout()
        plt.imshow(image[i][0]*0.3181+0.3107, cmap='grey', interpolation='none')
        plt.title('{}:{}'.format(name, label[i].item()))
        plt.xticks([])
        plt.yticks([])
    plt.show()

def one_hot(label, depth=10):
    out = torch.zeros(label.size(0), depth)
    idx = torch.LongTensor(label).view(-1, 1)
    out.scatter_(dim=1, index=idx, value=1)
    return out

