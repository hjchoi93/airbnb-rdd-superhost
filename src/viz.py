import statsmodels.api as sm
import numpy as np
import pandas as pd
import rdd
import matplotlib.pyplot as plt

def RDD_plot(df: pd.DataFrame, running_var: str, c: float, h: float, y_col: str, ax=None, title="RDD"):

    """
    df: filtered observations with sufficient calendar coverage
    """

    df_local = rdd.cutoff_filter(df, running_var, c, h)
    m = rdd.fit_rdd(df_local, running_var, c, h, y_col, covariates=None)
    
    # Binning - put all observations into bins that are grouped by the average rating and average occupancy rate 
    bin_width = 0.1
    df_local["bin"] = np.floor(df_local["x"] / bin_width) * bin_width
    binned = (df_local.groupby("bin", as_index=False)
              .agg(x_mean=("x", "mean"),
                   y_mean=(y_col, "mean"),
                   n=(y_col, "size")))

    # Fitted lines
    x_grid = np.linspace(-h, h, 200)
    pred_left  = m["model"].predict(sm.add_constant(pd.DataFrame({"x": x_grid, "D": 0, "xD": 0}),
                                           has_constant="add"))
    pred_right = m["model"].predict(sm.add_constant(pd.DataFrame({"x": x_grid, "D": 1, "xD": x_grid}),
                                           has_constant="add"))

    # ---- Plot ON THE PROVIDED AXIS ----
    
    if ax is None:
        ax = plt.gca()
        
    ax.scatter(binned["x_mean"], binned["y_mean"])
    ax.plot(x_grid[x_grid < 0],  pred_left[x_grid < 0])
    ax.plot(x_grid[x_grid >= 0], pred_right[x_grid >= 0])
    ax.axvline(0)

    ax.set_title(title)
    ax.set_xlabel("x = rating - cutoff")
    ax.set_ylabel(y_col)

    plt.tight_layout()

    return m