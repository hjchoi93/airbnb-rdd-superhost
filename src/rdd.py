import statsmodels.api as sm
import numpy as np
import pandas as pd

def cutoff_filter(df: pd.DataFrame, running_var: str, c: float, h: float):
    
    """

    Pick cutoff and test multiple bandwidths 

      * Cutoff (c): review scores rating = 4.8
      * Bandwidth (h): ratings within 0.10, 0.05, 0.2
      
    df: filtered observations with sufficient calendar coverage
    
    running_var: review score rating 
    
    c: cutoff
    
    h: bandwidth 
    
    y_col: occupancy_next_30d
    
    covariates: optionally some covariates for later checks

    """
    # Filter observations around the cutoff
    # Create a regression formula that has the following variables:
    # x = running variable centered at cutoff
    # D = binary variable on whether the rating is above the cutoff 
    # xD = interaction term so the slope can differ on the right side 
    df_local = df.loc[df[running_var].between(c - h, c + h)].copy()
    df_local["x"] = df_local[running_var] - c
    df_local["D"] = (df_local[running_var] >= c).astype(int)
    df_local["xD"] = df_local["x"] * df_local["D"]

    return df_local 
    

def fit_rdd(df: pd.DataFrame, running_var: str, c: float, h: float, y_col: str, covariates=None):
    
    """
    Run Regression and fit on two lines (one below and one above the cutoff)

    df: filtered dataframe with listings that have enough calendar coverage
    """
    
    df_calendar = cutoff_filter(df, running_var, c, h)

    # Fit the OLS regression with robust standard errors
    X = sm.add_constant(df_calendar[["x", "D", "xD"]], has_constant="add")
    m = sm.OLS(df_calendar[y_col], X).fit(cov_type="HC1")

    # Confidence Intervals 
    tau = m.params["D"]
    se = m.bse["D"]
    ci_low, ci_high = tau - 1.96*se, tau + 1.96*se

    # Return model and its corresponding metrics 
    return {"model": m, "tau": tau, "ci": (ci_low, ci_high), "n": len(df_calendar)}



