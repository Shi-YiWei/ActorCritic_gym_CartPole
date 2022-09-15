import argparse


def get_args():
    parse = argparse.ArgumentParser()


    parse.add_argument('--gamma', type=float, default=0.99, help='the discount factor of RL')
    parse.add_argument('--env-name', type=str, default='CartPole-v0', help='the environment name')
    parse.add_argument('--actor_lr', type=float, default=1e-3, help='learning rate of the algorithm')
    parse.add_argument('--critic_lr', type=float, default=1e-2, help='learning rate of the algorithm')
    parse.add_argument('--num-episodes', type=int, default=1000, help='the number of episodes')
    parse.add_argument('--hidden-dim', type=int, default=128, help='the hidden dim')

    args = parse.parse_args()





    return args