
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import boxcox, yeojohnson

def skew_calc(df):
    """
    Diagnoses skewness for every numeric column in a DataFrame and recommends a transformation based on the column's skewness and
    minimum value. Binary, encoded, and ID columns are excluded, since skewness isn't a meaningful for them.
    It returns a DataFrame with the following columns:
    Feature, Skewness, Degree, Direction, Recommended Transformation
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    results = []

    for col in numeric_cols:
        # Skip columns containing 'id' or binary/encoded variables
        if 'id' in str(col).lower() or df[col].nunique() <= 2:
            continue

        series = df[col].dropna()
        if series.empty:
            continue

        skew = series.skew()
        abs_skew = abs(skew)
        min_val = series.min()

        # Determine Degree and Direction
        if abs_skew < 0.5:
            degree = "Approximately Normal"
            direction = "Symmetric"
            recommendation = "No transformation needed"
        else:
            if skew > 0:
                direction = "Right (Positive)"
            else:
                direction = "Left (Negative)"

            if 0.5 <= abs_skew <= 1.0:
                degree = "Moderately Skewed"
            else:
                degree = "Highly Skewed"

            # Recommendations
            if skew > 0 and abs_skew > 1.0:
                if min_val > 0:
                    recommendation = "Box-Cox or Yeo-Johnson"
                elif min_val == 0:
                    recommendation = "log(x+1) or Yeo-Johnson"
                else:
                    recommendation = "Yeo-Johnson"

            elif skew > 0 and 0.5 <= abs_skew <= 1.0:
                if min_val > 0:
                    recommendation = "log(x+1) or Yeo-Johnson"
                elif min_val == 0:
                    recommendation = "log(x+1) or Yeo-Johnson"
                else:
                    recommendation = "Yeo-Johnson"

            else:
                if min_val > 0:
                    recommendation = "Box-Cox or Yeo-Johnson"
                else:
                    recommendation = "Yeo-Johnson"

        results.append({
            'Feature': col,
            'Skewness': round(skew, 4),
            'Degree': degree,
            'Direction': direction,
            'Recommended Transformation': recommendation
        })

    return pd.DataFrame(results)
