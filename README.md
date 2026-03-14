# Thompson Sampling

> Multi-armed bandit solver using Thompson Sampling for ad click-through rate (CTR) optimization.

## What It Does

Simulates an online ad-selection scenario where an algorithm must decide which of 10 ads to show in each round, learning from binary rewards (click / no click) to maximise total clicks over 10,000 rounds.

## Methodology

Thompson Sampling is a Bayesian approach to the exploration–exploitation trade-off:

1. **Model** — each ad's unknown CTR is modelled with a Beta distribution: `Beta(α, β)` where `α = successes + 1` and `β = failures + 1`.
2. **Sample** — draw a random value from every ad's current Beta distribution.
3. **Select** — pick the ad whose sample is highest.
4. **Update** — observe the reward and increment `α` (click) or `β` (no click).

Because the Beta distribution naturally narrows as evidence accumulates, the algorithm explores uncertain ads early on and gradually exploits the best performer.

## Dataset

`Ads_CTR_Optimisation.csv` — 10,000 rows × 10 columns. Each cell is a binary reward (1 = click, 0 = no click) from a simulated ad campaign.

## Dependencies

| Language | Packages |
|----------|----------|
| Python 3 | `matplotlib`, `pandas` |
| R        | base (no extra packages) |

## How to Run

### 🐍 Python

```bash
pip install -r requirements.txt
python thompson_sampling.py
```

### 📊 R

```r
Rscript thompson_sampling.R
# or inside an R session:
source("thompson_sampling.R")
```

Both scripts print the total reward and display a histogram showing which ad the algorithm converged on.

## Tech Stack

| | |
|---|---|
| 🐍 Python 3 | Core implementation |
| 📊 R | Alternative implementation |
| 📈 Matplotlib | Visualisation |
| 🐼 pandas | Data loading |
| 📐 Beta Distribution | Bayesian prior/posterior |

## Known Issues

- Dataset is fully simulated; real-world CTRs would require a live feedback loop.
- No command-line arguments yet — round count and ad count are constants at the top of each script.
- The R script's `sys.frame(1)$ofile` path resolution only works when the file is `source()`-d; when run with `Rscript` it falls back to `getwd()`.

## License

MIT
