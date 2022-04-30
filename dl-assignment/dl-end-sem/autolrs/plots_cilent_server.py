import matplotlib.pyplot as plt
import sys
import os

if (len(sys.argv) < 3):
    print(f'format: python {sys.argv[0]} <FILEPATH> <FLAG>')  
    exit(0)

client_file = os.path.join(sys.argv[1],"client_log")
server_file = os.path.join(sys.argv[1],'server_log')
flag = int(sys.argv[2])

def read_file(file_name):
    with open(file_name,'r') as f:
        for line in f.readlines():
            yield line


def plot_loss_vs_iterations():
    file_data = read_file(server_file)
    steps = []
    loss = []
    for idx, line in enumerate(file_data):
        line = line.replace('\n','')
        if ('loss' in line and 'step' in line):
            line = line.split(' ')
            step = int(line[-1])
            los = float(line[-4][:-1])
            steps.append(step)
            loss.append(los)
    
    plt.figure(figsize=(5,4))
    plt.plot(steps,loss)
    plt.xlabel('iterations')
    plt.ylabel('loss')
    if flag == 10:
        plt.title('loss vs iterations (cifar10)')
        plt.savefig('lvi_cifar10.svg',format='svg')
    else:
        plt.title('loss vs iterations (cifar100)')
        plt.savefig('lvi_cifar100.svg',format='svg')
    plt.show()


def plot_client_file():
    file_data = read_file(client_file)
    epochs = []
    acc = []
    iterations = []
    lrs = []
    for idx, line in enumerate(file_data):
        line = line.replace('\n','')
        if ('Epoch' in line):
            line = line.split(' ')
            epoc = int(line[-1])
            epochs.append(epoc)
        elif ('Test acc' in line):
            line = line.split(' ')
            ac = float(line[-1])
            acc.append(ac)
        elif ('AutoLRS' in line and 'Received data' in line):
            line = line.split(' ')
            try:
                lr = float(line[-1])
                itera = int(line[-4][:-1])
                iterations.append(itera)
                lrs.append(lr)
            except Exception as e:
                continue;

    plt.figure(figsize=(5,4))
    plt.plot(epochs,acc,color='red')
    plt.xlabel('epochs')
    plt.ylabel('accuracy')
    if flag == 10:
        plt.title('acc vs epochs (cifar10)')
        plt.savefig('cva_cifar10.svg',format='svg')
    else:
        plt.title('acc vs epochs (cifar100)')
        plt.savefig('cva_cifar100.svg',format='svg')
    plt.show()

    plt.figure(figsize=(5,4))
    plt.plot(iterations,lrs,color='orange')
    plt.xlabel('iterations')
    plt.ylabel('learning rate')
    if flag == 10:
        plt.title('lr vs steps (cifar10)')
        plt.savefig('lvs_cifar10.svg',format='svg')
    else:
        plt.title('lr vs steps (cifar100)')
        plt.savefig('lvs_cifar100.svg',format='svg')
    plt.show()

        

plot_client_file()
plot_loss_vs_iterations()

