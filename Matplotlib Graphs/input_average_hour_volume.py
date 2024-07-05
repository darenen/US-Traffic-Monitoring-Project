import pandas as pd
import matplotlib.pyplot as plt
import random

# Creates a dataframe
print("Showing the average hourly volume of cars in a state")

#abbreviations for the state
state_abbreviations = {
    'alabama': 'AL',
    'alaska': 'AK',
    'arizona': 'AZ',
    'arkansas': 'AR',
    'california': 'CA',
    'colorado': 'CO',
    'connecticut': 'CT',
    'delaware': 'DE',
    'florida': 'FL',
    'georgia': 'GA',
    'hawaii': 'HI',
    'idaho': 'ID',
    'illinois': 'IL',
    'indiana': 'IN',
    'iowa': 'IA',
    'kansas': 'KS',
    'kentucky': 'KY',
    'louisiana': 'LA',
    'maine': 'ME',
    'maryland': 'MD',
    'massachusetts': 'MA',
    'michigan': 'MI',
    'minnesota': 'MN',
    'mississippi': 'MS',
    'missouri': 'MO',
    'montana': 'MT',
    'nebraska': 'NE',
    'nevada': 'NV',
    'new hampshire': 'NH',
    'new jersey': 'NJ',
    'new mexico': 'NM',
    'new york': 'NY',
    'north carolina': 'NC',
    'north dakota': 'ND',
    'ohio': 'OH',
    'oklahoma': 'OK',
    'oregon': 'OR',
    'pennsylvania': 'PA',
    'rhode island': 'RI',
    'south carolina': 'SC',
    'south dakota': 'SD',
    'tennessee': 'TN',
    'texas': 'TX',
    'utah': 'UT',
    'vermont': 'VT',
    'virginia': 'VA',
    'washington': 'WA',
    'west virginia': 'WV',
    'wisconsin': 'WI',
    'wyoming': 'WY'
}

# finding the state the user wants to look at and gets the abbreviation
state = input("Enter the name of the state: ")

while(not(state.lower() in state_abbreviations.keys())):
    state = input("Please enter a valid state: ")

abbrevation = state_abbreviations[state.lower()]

#gets the dataset
pars = pd.read_csv(f"dec_2022_ccs_data_converted/{abbrevation}_DEC_2022 (TMAS).csv", dtype = { 'Record_Type': int, 'State_Code' : int, 'F_System' : str, 'Station_Id' : str, 'Travel_Dir' : int, 'Year_Record' : int,
                                                                                                       'Month_Record': int,'Day_Record' : int,'Day_of_Week' : int,'Hour_Record' : int ,'Hour_Volume' : int ,'Restrictions' : int})
# dtype = { 'column name': type }
# Record_Type,State_Code,F_System,Station_Id,Travel_Dir,Travel_Lane,Year_Record,Month_Record,Day_Record,Day_of_Week,Hour_Record,Hour_Volume,Restrictions

#gets the station ID, only doing random right now
station_id_input = input("Next, enter the station you want to find (type R for a random one): ")
if(station_id_input.lower() == 'r'): 
    # sample() gets a random row
    station_id = pars.sample()['Station_Id'].values[0]
else:
    #TODO: make sure the inpt is correct
    station_id = station_id_input


print(f'using station: {station_id}')



# Creates a smaller data set with certain condition stationid = 011060
station = pars[pars["Station_Id"] == station_id]

# Creates a dictionary with hour averages
hour_average = dict.fromkeys(range(0,24),0)
# Records how many days so it can take the average
days = 31

#iterates through rows
for index, row, in station.iterrows():
    hour_average[row["Hour_Record"]] += row["Hour_Volume"]

# finds the average
for key in hour_average:
    hour_average[key] = round(hour_average[key] / days)



# Plots it
fig, ax = plt.subplots()

ax.bar(hour_average.keys(), hour_average.values(), )
ax.set_xlim(-.5,23.5)
ax.set_xlabel('Hour')
ax.set_ylabel('Car Count')
ax.set_title('Average Hourly Traffic of Station ' + str(station_id))
plt.show()

