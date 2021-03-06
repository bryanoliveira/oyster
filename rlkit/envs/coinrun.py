import gym
from . import register_env


@register_env("coinrun")
class CoinRunEnv:
    def __init__(self, n_tasks=60, n_train_tasks=50, n_test_tasks=10, seed=0, **kwargs):
        self._seed = seed
        self.n_tasks = n_tasks
        self.n_train_tasks = n_train_tasks
        self.n_test_tasks = n_test_tasks
        self.tasks = []
        self._sample_tasks()  # fill up self.tasks
        self.env = self.tasks[0]  # this env will change depending on the idx
        self.observation_space = self.env.observation_space
        self.action_space = self.env.action_space

    def step(self, action):
        return self.env.step(action)

    def reset(self):
        return self.env.reset()

    def seed(self, _seed):
        self._seed = _seed
        self._sample_tasks()

    def _sample_tasks(self):
        self.tasks = [
            gym.make("procgen:procgen-coinrun-v0", start_level=idx, num_levels=1)
            for idx in range(self._seed, self._seed + self.n_tasks)
        ]

    def get_all_task_idx(self):
        return range(len(self.tasks))

    def reset_task(self, idx):
        self.env = self.tasks[idx]
        self.reset()

    def render(self):
        self.env.render()

