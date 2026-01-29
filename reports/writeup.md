# Regression Discontinuity Analysis 

The goal was to test multiple rating-bandwidth combinations along with testing a covariate to ensure there is no potential bias of the treatment variable (occupancy rate). 

## Here are the RDD plots for all combinations:

![Rating - 4.8](figures/rdd_outcome_bandwidths_4.8.png)

![Rating - 4.75](figures/rdd_outcome_bandwidths_4.75.png)

![Rating - 4.85](figures/rdd_outcome_bandwidths_4.85.png)

![Minimum Nights - Covariate](figures/rdd_outcome_bandwidths_min_nights.png)


# Approach
Regression Discontinuity Design:
* Method to estimate a cause-and-effect relationship when a decision is made by a hard cutoff (host rating)
* The method is credible because it's a near-random experiment right at the boundary.
* The two groups below and above the cutoff are comparable - like treatment vs control

We calculate the occupancy rate of listings that have enough calendar coverage (listed for the next 30 days) and utilize that as the outcome variable

## Key result: RDD estimate around 4.8 cutoff

![RDD plot](reports/figures/rdd_outcome_bandwidths_4.8.png)

# Robustness & Validity Checks
We test three bandwidths (0.1, 0.05, 0.02) and also produce the corresponding confidence intervals. 
We also tested multiple cutoff ratings (4.75 & 4.85) with the same bandwidths. Finally, we used a different covariate from the data called minimum_nights. This variable conveys the minimum number of nights a listing is available. This test was done to ensure other listing characteristics do not change abruptly at cutoff. In a good RDD, only the treatment assignment changes sharply at the cutoff; everything else should look smooth.
The confidence intervals for every bandwidth-rating combination included zero. This means we don't have strong enough statistical evidence to rule out no jump/discontinuity. 

# Limitations
One of the bandwidth-rating combinations with the covariate included a zero, which means there is evidence of discontinuity. If one of the covariates has a discontinuity, the estimated treatment effect for the actual outcome (occupancy rate) may be biased. 

# How to run
1. Clone repo
2. Download listings.csv and calendar.csv from this [site](https://insideairbnb.com/get-the-data/)
3. Add both csv files to the data/raw directory.
4. Run the 01_analysis.pynb in the notebooks directory

# File Guide
Utilize this [data dictionary](https://docs.google.com/spreadsheets/d/1iWCNJcSutYqpULSQHlNyGInUvHg2BoUGoNRIGa6Szc4/edit?gid=1322284596#gid=1322284596) for detailed attributes on the raw data
