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
    dates, temperatures = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y%m%dT%H%M%S")
        dates.append(current_date)
        temp = float(row[1])
        temperatures.append(temp)

# Drawing figure
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, temperatures, c='red')

# Diagram formatting
plt.title("Daily temperatures in Odessa, June 2020", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

