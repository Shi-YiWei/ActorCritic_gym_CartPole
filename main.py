import gym
import torch
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

from ActorCritic import ActorCritic
from utils import train_on_policy_agent
from plot import plot
from arguments import get_args




args = get_args()

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

env = gym.make(args.env_name)
env.seed(0)
torch.manual_seed(0)


state_dim = env.observation_space.shape[0]
action_dim = env.action_space.n







agent = ActorCritic(state_dim, args, action_dim, device)

return_list = train_on_policy_agent(env, agent, args)


episodes_list = list(range(len(return_list)))

plot(episodes_list,return_list,args)