# Thompson Sampling

Thompson Sampling implementation for the multi-armed bandit problem, applied to ad click-through rate (CTR) optimization. Implementations in both Python and R.

## How It Works

Thompson Sampling is a probabilistic reinforcement learning algorithm that balances exploration and exploitation using Bayesian inference:

1. Model each ad's CTR as a Beta distribution: `Beta(successes + 1, failures + 1)`
2. Sample a random value from each ad's distribution
3. Select the ad with the highest sampled value
4. Update the distribution based on the observed reward (click or no click)

Unlike Upper Confidence Bound (UCB), Thompson Sampling is **probabilistic** — it naturally explores uncertain options while exploiting known good ones.

## Dataset

`Ads_CTR_Optimisation.csv` — 10,000 rounds × 10 ads. Each cell is a binary reward (1 = click, 0 = no click) from a simulated ad campaign.

## Usage

### Python

```bash
pip install numpy matplotlib pandas
python thompson_sampling.py
```

### R

```r
source("thompson_sampling.R")
```

Both scripts output a histogram showing which ad was selected most frequently (the algorithm converges on the best-performing ad).

## Known Issues

- Hardcoded file path — expects `Ads_CTR_Optimisation.csv` in the working directory
- No train/test split — runs on the full dataset sequentially (appropriate for online learning)
- `import random` is inside the loop section rather than at the top of the file (Python style issue)

## License

MIT
