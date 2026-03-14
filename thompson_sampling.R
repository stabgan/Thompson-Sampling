# Thompson Sampling
# Probabilistic algorithm for the multi-armed bandit problem,
# applied to ad click-through rate (CTR) optimization.

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
N_ROUNDS <- 10000
N_ADS    <- 10

# ---------------------------------------------------------------------------
# Load dataset (resolve path relative to this script, not the cwd)
# ---------------------------------------------------------------------------
script_dir <- tryCatch(
  dirname(sys.frame(1)$ofile),
  error = function(e) getwd()
)
data_path <- file.path(script_dir, "Ads_CTR_Optimisation.csv")
dataset   <- read.csv(data_path)

# ---------------------------------------------------------------------------
# Thompson Sampling
# ---------------------------------------------------------------------------
ads_selected      <- integer(0)
numbers_of_rewards_1 <- integer(N_ADS)
numbers_of_rewards_0 <- integer(N_ADS)
total_reward      <- 0

for (n in 1:N_ROUNDS) {
  ad         <- 0
  max_random <- 0

  for (i in 1:N_ADS) {
    random_beta <- rbeta(
      n      = 1,
      shape1 = numbers_of_rewards_1[i] + 1,
      shape2 = numbers_of_rewards_0[i] + 1
    )
    if (random_beta > max_random) {
      max_random <- random_beta
      ad         <- i
    }
  }

  ads_selected <- append(ads_selected, ad)
  reward       <- dataset[n, ad]

  if (reward == 1) {
    numbers_of_rewards_1[ad] <- numbers_of_rewards_1[ad] + 1
  } else {
    numbers_of_rewards_0[ad] <- numbers_of_rewards_0[ad] + 1
  }
  total_reward <- total_reward + reward
}

cat("Total reward:", total_reward, "\n")

# ---------------------------------------------------------------------------
# Visualise results
# ---------------------------------------------------------------------------
hist(
  ads_selected,
  col  = "steelblue",
  main = "Histogram of Ad Selections",
  xlab = "Ad Index",
  ylab = "Times Selected"
)
