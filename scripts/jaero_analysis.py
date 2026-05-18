# importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# creating dataframe + wrangling
jaero_logs = pd.read_csv("data/jaero_logs.csv")
jaero_logs = jaero_logs.drop(jaero_logs[jaero_logs["aes_id"] == "06A125"].index) # no interpretable information from what I can see - can reintegrate later if needed
print(jaero_logs.head())

# divide logs into logs with message and logs without
no_message_log_count = len(jaero_logs[jaero_logs["has_message_or_logged"] == "0"])
print(no_message_log_count)
with_message_log_count = len(jaero_logs[jaero_logs["has_message_or_logged"] == "1"])
print(with_message_log_count)

# registered countries with highest message counts - this could be something to look deeper into!
message_counts_by_country = (jaero_logs.groupby('registration_country')['message_count'].sum().sort_values(ascending=False).reset_index())
print(message_counts_by_country)

# visualizations
message_counts_by_country.head(15).plot(kind='barh', x='registration_country', y='message_count', legend=False)
plt.xlabel('Total Messages')
plt.title('Top 15 Countries by Message Count')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('outputs/top_message_countries.png', dpi=150)
plt.show()