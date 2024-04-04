import pandas as pd
data = {'value': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# 1. Moving Average (using rolling mean)
window_size = 2
df['moving_average'] = df['value'].rolling(window=window_size).mean()

# 2. Cumulative Sum
df['cumulative_sum'] = df['value'].cumsum()

# 3. Ranking (ascending order)
df['rank'] = df['value'].rank(ascending=True)

# 4. Percentile (50th percentile is the median)
df['median'] = df['value'].rolling(window=1).quantile(0.5)  # Consider window size for percentiles

# Print the DataFrame with added columns
print(df)
