from datetime import datetime
import csv
import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

# 0 STATION
# 1 NAME
# 2 DATE
# 3 PRCP
# 4 TMAX
# 5 TMIN
# 6 TOBS

    # Get dates, high and low temperatures from this file
    dates, highs, lows = [], [], []
    for line, row in enumerate(reader):

        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print("Missing Data: Line: ", line, " Date: ", row[2], " High: ", row[4], " Low: ", row[5])
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the high and low temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
ax.set_title("Daily high and low temperatures - 2018\nDeath Valley, CA", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (°F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()