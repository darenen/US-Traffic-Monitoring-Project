# US Traffic Monitoring

### Getting the Traffic Data
To get the data of the traffic sensors, go to https://www.fhwa.dot.gov/policyinformation/tables/tmasdata/ and download the desired folder
Then open up the 'Converting the raw data,' open the script and run it. Enter the name of the zipped folder. 
It will convert all the data from .TOL to .csv and unzip the folder so it can be used. 
You can copy and paste the data folder into different folders in the repository

### Finding the Averages in Each County in a Given Month
Open up the folder 'Finding County Averages'
Run the program and input the folder of csvs to it.
The program will first find the entire volume and number of observations of each station.
Then it will lookup the county to find the averages of traffic volume per hour in each county
The averages will be saved into '(month) averages'

### Finding the County of Each Station
To download the data for each station, go to https://www.fhwa.dot.gov/policyinformation/tables/tmasdata/ and download the station data
run that through the script in 'Converting the raw data'. The headers are not aligned to the actual values. You will need the station id, state code, latitude and longitude columns
The program will use Nomatim GeoPy to find the county using reverse address lookup from latitude and longitude of each station
Because there is a limit to number of API references before it will stop working. You will need to go to the last cell and run it multiple times until all 7000 stations' county have been found
There will be missing gaps because the library wont be able to find the county. 
You can manually enter the counties in which will take a lot of time. I have added the finished 'station_county_key.csv' to save you the hard work

### December 2015 Traffic Map
Creates a map to visualize the traffic of a single month using folium GeoJson
Shows charts of the data using matplotlib

### Map of Every Month
Creates a single map with multiple overlays of the traffic volume heatmap from each month
Has rvd.py and station_county_average.py which proccesses all the data into a new folder with the averages
'county_volume_map' will show the map

### Matplotlib Graphs
Displays patterns in the traffic volume of a month
Run each program to see cool graphs
