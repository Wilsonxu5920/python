rainfall = []
for _ in range(12):
    rainfall.append(float(input("Enter rainfall for a month: ")))

total_rainfall = sum(rainfall)
average_rainfall = total_rainfall / 12
max_rainfall = max(rainfall)
min_rainfall = min(rainfall)

print(f"Total Rainfall: {total_rainfall}")
print(f"Average Monthly Rainfall: {average_rainfall}")
print(f"Month(s) with the highest rainfall: {', '.join(str(i+1) for i, val in enumerate(rainfall) if val == max_rainfall)}")
print(f"Month(s) with the lowest rainfall: {', '.join(str(i+1) for i, val in enumerate(rainfall) if val == min_rainfall)}")