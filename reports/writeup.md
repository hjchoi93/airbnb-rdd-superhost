# Regression Discontinuity Analysis 

The goal was to test multiple rating-bandwidth combinations along with testing a covariate to ensure there is no potential bias of the treatment variable (occupancy rate). 

## Here are the RDD plots for all combinations:

![Rating - 4.8](figures/rdd_outcome_bandwidths_4.8.png)

![Rating - 4.75](figures/rdd_outcome_bandwidths_4.75.png)

![Rating - 4.85](figures/rdd_outcome_bandwidths_4.85.png)

![Minimum Nights - Covariate](figures/rdd_outcome_bandwidths_min_nights.png)

While there does seem to be notable jumps at the cutoff threshold for many of these combinations, the confidence intervals for ALL rating-bandwidth combinations for the outcome variable (occupancy rate) includes zero. Therefore, we cannot conclude there is a statistically signiifcant jump at the cutoff that would cause a significant increase in bookings at that rating. 

For the minimum nights covariate analysis, the bandwidth at 0.2 does not include zero and only includes negative numbers. This implies there is a negative discontinuity at the cutoff rating of 4.8 and could potentially bias the treatment results. So if a covariate like minimum_nights shows a discontinuity at the cutoff, it implies:
* sorting/manipulation (different types of listings end up just above), or
* sample selection/filtering that changes the composition right at the cutoff, or
* the running variable is heaped/discrete in a way that breaks the “local randomization” intuition.

