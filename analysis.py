# analysis.py
# A tiny descriptive-stats script used to practise Git.
import statistics

values = [4, 8, 15, 16, 23, 42]

mean_value = sum(values) / len(values)
median_value = statistics.median(values)
max_value = max(values)
min_value = min(values)
range_value = [min_value, max_value]
dev = statistics.stdev(values)

print(f"Average: {mean_value:.2f}")
print(f"Median: {median_value: .2f}")

print(f"Standard deviation: {dev}")
print(f"Max:  {max_value}")
print(f"Min: {min_value}")
print(f"Range: {range_value}")