import pandas as pd
import matplotlib.pyplot as plt

# Creates a dataframe
pars = pd.read_csv("dec_2022_ccs_data_converted\CA_DEC_2022 (TMAS).csv")

# export = pars[pars["station"] = num]

# Creates a smaller data set with certain condition stationid = 011060
station = pars[pars["Station_Id"] == 11060]

# Creates a dictionary with hour averages
hour_average = dict.fromkeys(range(0,24),0)
# Records how many days so it can take the average
days = 31

for index, row, in station.iterrows():
    hour_average[row["Hour_Record"]] += row["Hour_Volume"]

for key in hour_average:
    hour_average[key] = round(hour_average[key] / days)

print(hour_average)



fig, ax = plt.subplots()

ax.bar(hour_average.keys(), hour_average.values(), )
ax.set_xlim(-.5,23.5)
ax.set_xlabel('Hour')
ax.set_ylabel('Car Count')
ax.set_title('Average Hourly Traffic Sensor Data')

plt.show()

#print(noon_time_data)

# grabs just the column data
#hour_volume = noon_time_data["Hour_Volume"]


#hour_volume.plot.bar(x = "Day",y = "Volume")

#TODO compare the station different directions 1 or 5 using side by side bar graph
#TODO create a cool graph trend