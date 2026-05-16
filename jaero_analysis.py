# importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# creating dataframes
jaero_logs = pd.read_csv("data/jaero_logs.csv")
print(jaero_logs.head())

# divide logs into logs with message and logs without
