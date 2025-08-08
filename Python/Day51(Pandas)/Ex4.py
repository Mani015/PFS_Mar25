

import numpy as np
import pandas as pd


s4 = pd.Series([11,22,33,44,np.nan,55,66,77])
# print(s4)
# 0    11.0
# 1    22.0
# 2    33.0
# 3    44.0
# 4     NaN
# 5    55.0
# 6    66.0
# 7    77.0
# dtype: float64

#
# Return True if there are any NaNs.
# print(s4.hasnans)  True

