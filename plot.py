

import matplotlib.pyplot as plt

from utils import moving_average


def plot(episodes_list,return_list,args):
	plt.plot(episodes_list, return_list)
	plt.xlabel('Episodes')
	plt.ylabel('Returns')
	plt.title('Actor-Critic on {}'.format(args.env_name))
	plt.show()

	mv_return = moving_average(return_list, 9)
	plt.plot(episodes_list, mv_return)
	plt.xlabel('Episodes')
	plt.ylabel('Returns')
	plt.title('Actor-Critic on {}'.format(args.env_name))
	plt.show()