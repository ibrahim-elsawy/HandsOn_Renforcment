# This is a sample Python script.
# setting device on GPU if available, else CPU
import torch
import gym
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Using device:', device)
print()

#Additional Info when using cuda
if device.type == 'cuda':
    print(torch.cuda.get_device_name(0))
    print('Memory Usage:')
    print('Allocated:', round(torch.cuda.memory_allocated(0)/1024**3,1), 'GB')
    print('Cached:   ', round(torch.cuda.memory_cached(0)/1024**3,1), 'GB')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

    env = gym.make("MountainCar-v0")
    env.reset()

    done = False
    while not done:
        action = 2  # always go right!
        env.step(action)
        env.render()