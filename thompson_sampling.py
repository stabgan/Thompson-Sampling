# Thompson Sampling
# Probabilistic algorithm for the multi-armed bandit problem,
# applied to ad click-through rate (CTR) optimization.

import os
import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
N_ROUNDS = 10_000  # number of simulation rounds
N_ADS = 10         # number of ads (arms)

# ---------------------------------------------------------------------------
# Load dataset (resolve path relative to this script, not the cwd)
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, "Ads_CTR_Optimisation.csv")


def run_thompson_sampling(data: pd.DataFrame, n_rounds: int, n_ads: int):
    """Run Thompson Sampling on *data* for *n_rounds* rounds across *n_ads* ads.

    Returns
    -------
    ads_selected : list[int]
        Index of the ad chosen in each round.
    total_reward : int
        Cumulative reward over all rounds.
    """
    ads_selected: list[int] = []
    rewards_1 = [0] * n_ads  # successes per ad
    rewards_0 = [0] * n_ads  # failures per ad
    total_reward = 0

    for n in range(n_rounds):
        ad = 0
        max_random = 0.0
        for i in range(n_ads):
            sample = random.betavariate(rewards_1[i] + 1, rewards_0[i] + 1)
            if sample > max_random:
                max_random = sample
                ad = i

        ads_selected.append(ad)
        reward = data.values[n, ad]

        if reward == 1:
            rewards_1[ad] += 1
        else:
            rewards_0[ad] += 1
        total_reward += reward

    return ads_selected, total_reward


def plot_results(ads_selected: list[int]) -> None:
    """Display a histogram of ad selections."""
    plt.hist(ads_selected, edgecolor="black")
    plt.title("Histogram of Ad Selections")
    plt.xlabel("Ad Index")
    plt.ylabel("Times Selected")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    dataset = pd.read_csv(DATA_PATH)
    selections, reward = run_thompson_sampling(dataset, N_ROUNDS, N_ADS)
    print(f"Total reward: {reward}")
    plot_results(selections)
