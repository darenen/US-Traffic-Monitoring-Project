import pandas as pd
import matplotlib.pyplot as plt

# Creates a dataframe
pars = pd.read_csv("data folders/dec_2022_ccs_data_converted/CA_DEC_2022 (TMAS).csv")




# export = pars[pars["station"] = num]

# Creates a smaller data set with certain condition stationid = 011060
station1 = pars[pars["Station_Id"] == 11060]

# data at 12 am from direction = 1
noon_time_data_dir1 = station1[(station1["Hour_Record"] == 12) & (station1["Travel_Dir"] == 1)]
noon_time_data_dir5 = station1[(station1["Hour_Record"] == 12) & (station1["Travel_Dir"] == 5)]

#sets the index of these to day record, 
# inplace = true means whether to modify or create new one  
noon_time_data_dir1.set_index('Day_Record', inplace=True)
noon_time_data_dir5.set_index('Day_Record', inplace=True)

bar_graph = pd.DataFrame({
    'direction1': noon_time_data_dir1["Hour_Volume"],
    'direction5': noon_time_data_dir5["Hour_Volume"]})
print(bar_graph)

ax = bar_graph.plot.bar(stacked = True)
#ax = bar_graph.plot.bar()

ax.set_ylabel("Volume")
ax.set_title('12 PM Hour Volume by Direction on Different Days')

plt.show()

'''
speed = [0.1, 17.5, 40, 48, 52, 69, 88]
lifespan = [2, 8, 70, 1.5, 25, 12, 28]
index = ['snail', 'pig', 'elephant',
         'rabbit', 'giraffe', 'coyote', 'horse']
df = pd.DataFrame({'speed': speed,
                   'lifespan': lifespan}, index=index)
ax = df.plot.bar(rot=0)
'''