months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

def get_rainfall():
    for month in months:
    
        month =float(input(f"Enter rainfall for {month}: ")) 
    

    
    return month
def display_results(rainfall):
    total_rainfall = sum(rain[1] for rain in rainfall)
    avg_rainfall = total_rainfall / len(rainfall)
    max_rainfall = max(rainfall, key=lambda x: x[1])
    min_rainfall = min(rainfall, key=lambda x: x[1])
    
    print(f"\nTotal Rainfall: {total_rainfall}")
    print(f"Average Monthly Rainfall: {avg_rainfall}")
    print(f"Highest Rainfall: {max_rainfall[1]} in {max_rainfall[0]}")
    print(f"Lowest Rainfall: {min_rainfall[1]} in {min_rainfall[0]}")