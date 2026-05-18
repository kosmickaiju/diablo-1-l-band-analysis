# importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# creating dataframe + wrangling
aviation_logs = pd.read_csv("data/l-band-aviation.csv")
print(aviation_logs.head())

# sort by protocol used (icmp, udp, etc.)
icmp_log_count = len(aviation_logs[aviation_logs["protocols"] == "null:ip:icmp:ip:udp:data"])
print(icmp_log_count)
udp_log_count = len(aviation_logs[aviation_logs["protocols"] == "null:ip:udp:data"])

'''sort by messages (particular focus on military + gov comms vs. commercial comms - means that classified information could be leaked!)
I have currently seen Air Force/McDonnell Douglas C-17A Globemaster III and UPS comms, want to filter those out'''
air_force = "United States Air Force"
globemaster = "C-17A Globemaster III"
matches_condition = aviation_logs['payload_ascii_preview'].str.contains(f"{air_force}|{globemaster}", case=False, na=False)
air_force_logs = aviation_logs[matches_condition].copy()
print(air_force_logs)


