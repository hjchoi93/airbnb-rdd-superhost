# airbnb-rdd-superhost
This analysis implements a regression discontinuity design to assess if a host rating at or above a certain number causes higher bookings

# Overview
The analysis shows whether or not hosts who possess a specific rating or higher can cause bookings to significantly increase if that threshold is met. We compare the occupancy rate below and above the cutoff to verify if a statistically significant jump occurs at the chosen rating. This can provide meaningful insights to both the business and the hosts. If a statistically significant jump is proven, the business can incentivize hosts to achieve that rating to bring in more bookings. The hosts can make improvements to their rental and their service to eventually achieve that rating; being assured that rating will lead to significantly higher bookings than they otherwise would have. 

# Data
Data is acquired from Inside Airbnb - a nonprofit dedicated to collecting comprehensive rental data across many cities worldwide. 
* listings.csv - detailed information on each listing such as host information, availability, and attributes of the residence
* calendar.csv - records the price, availability and other details from the listing's calendar for each day of the next 365 days

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
