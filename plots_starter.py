import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data_full_large = pd.read_csv('csv_files/full_large.csv')
data_modern_large = pd.read_csv('csv_files/modern_large.csv')
data_old_large = pd.read_csv('csv_files/old_large.csv')

#################################################################################
# CORRELATION BETWEEN YEAR AND WAR
x = data_full_large['YEAR']
y = data_full_large['WAR']

plt.scatter(x, y, s=8)

plt.xlabel('Year')
plt.ylabel('WAR')
plt.title('War over time')

plt.show()
#################################################################################


#################################################################################
# YEARS WHERE WAR LEADER = MVP LEADER
mvp_rank_1 = data_modern_large[data_modern_large["MVP_RANK"] == 1]

both_rank_1 = mvp_rank_1[mvp_rank_1["WAR_RANK"] == 1]

top5 = mvp_rank_1[mvp_rank_1["WAR_RANK"] <= 5]

percentage = (len(both_rank_1) / len(mvp_rank_1)) * 100
p2 = (len(top5) / len(mvp_rank_1)) * 100

print(f"Modern percentage: {percentage:.2f}%")
print(f"Modern percentage top 5: {p2:.2f}%")

mvp_rank_1 = data_old_large[data_old_large["MVP_RANK"] == 1]

both_rank_1 = mvp_rank_1[mvp_rank_1["WAR_RANK"] == 1]

top5 = mvp_rank_1[mvp_rank_1["WAR_RANK"] <= 5]

percentage = (len(both_rank_1) / len(mvp_rank_1)) * 100
p2 = (len(top5) / len(mvp_rank_1)) * 100

print(f"Old percentage: {percentage:.2f}%")
print(f"Old percentage top 5: {p2:.2f}%")

full_mvp_rank_1 = data_full_large[data_full_large["MVP_RANK"] == 1]

full_both_rank_1 = full_mvp_rank_1[full_mvp_rank_1["WAR_RANK"] == 1]

full_top5 = full_mvp_rank_1[full_mvp_rank_1["WAR_RANK"] <= 5]

full_percentage = (len(full_both_rank_1) / len(full_mvp_rank_1)) * 100
full_p2 = (len(full_top5) / len(full_mvp_rank_1)) * 100

print(f"Full percentage: {full_percentage:.2f}%")
print(f"Full percentage top 5: {full_p2:.2f}%")
#################################################################################

#################################################################################
# Calculate the correlation between WAR_RANKING and MVP
correlation = data_modern_large['WAR_RANK'].corr(data_modern_large['MVP_RANK'])

print(f"The modern correlation between WAR_RANK and MVP_RANK is: {correlation:.3f}")

full_correlation = data_full_large['WAR_RANK'].corr(data_full_large['MVP_RANK'])

print(f"The full correlation between WAR_RANK and MVP_RANK is: {full_correlation:.3f}")

old_correlation = data_old_large['WAR_RANK'].corr(data_old_large['MVP_RANK'])

print(f"The old correlation between WAR_RANK and MVP_RANK is: {full_correlation:.3f}")

correlation_by_year = data_full_large.groupby('YEAR').apply(
    lambda group: group['WAR_RANK'].corr(group['MVP_RANK'])
)

# Plot correlation over time
plt.figure(figsize=(10, 6))
correlation_by_year.plot(kind='line', marker='o')
plt.title('Correlation Between WAR_RANKING and MVP Over Time')
plt.xlabel('Year')
plt.ylabel('Correlation')
plt.grid()
plt.show()

# Now by decade
data_full_large = data_full_large[data_full_large['YEAR'] != 1949]

# Add a 'DECADE' column
data_full_large['DECADE'] = (data_full_large['YEAR'] // 10) * 10

# Group data by decade and calculate correlation
correlation_by_decade = data_full_large.groupby('DECADE').apply(
    lambda group: group['WAR_RANK'].corr(group['MVP_RANK'])
)

# Plot correlation by decade
plt.figure(figsize=(10, 6))
correlation_by_decade.plot(kind='line', marker='o')
plt.title('Correlation Between WAR_RANK and MVP_RANK by Decade')
plt.xlabel('Decade')
plt.ylabel('Correlation')
plt.grid(axis='y')
plt.ylim(0, 1)
plt.show()
#################################################################################


