import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'dataexport_20200618T072434.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Temperatures reading form file
    dates, temperatures, winds = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y%m%dT%H%M%S")
        dates.append(current_date)
        temp = float(row[1])
        temperatures.append(temp)
        wind = float(row[3])
        winds.append(wind)

# Drawing figure
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.subplots_adjust(wspace=0, hspace=1)

# Diagram formatting
plt.title("Daily temperatures in Odessa, June 11-19th, 2020", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (C)", fontsize=16)
plt.plot(dates, temperatures, c='red')

plt.subplot(2, 1, 2)
plt.title("Daily winds in Odessa, June 11-19th, 2020", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Wind Speed [10 m]", fontsize=16)
plt.plot(dates, winds, c='green')

plt.show()
