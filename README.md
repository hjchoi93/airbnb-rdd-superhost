# airbnb-rdd-superhost
This analysis implements a regression discontinuity design to assess if a host rating at or above a certain number causes higher bookings

# Overview
The analysis shows whether or not hosts who possess a specific rating or higher can cause bookings to significantly increase if that threshold is met. We compare the occupancy rate below and above the cutoff to verify if a statistically significant jump occurs at the chosen rating. This can provide meaningful insights to both the business and the hosts. If a statistically significant jump is proven, the business can incentivize hosts to achieve that rating to bring in more bookings. The hosts can make improvements to their rental and their service to eventually achieve that rating; being assured that rating will lead to significantly higher bookings than they otherwise would have. 

# Data
Data is acquired from Inside Airbnb - a nonprofit dedicated to collecting comprehensive rental data across many cities worldwide. 
* listings.csv - detailed information on each listing such as host information, availability, and attributes of the residence
* calendar.csv - records the price, availability and other details from the listing's calendar for each day of the next 365 days			
