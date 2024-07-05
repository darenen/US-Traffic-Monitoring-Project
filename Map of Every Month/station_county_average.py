import pandas as pd
import os
import math
import gc



def find_county(row):
    row['County'] = county_dict.get(row['Station_Id'], '')
    return row

def add_county_to_csv(data_folder):
    
    global county_dict
    for filename in os.listdir(data_folder):
        #f is the file now
        print(filename)
        
        f = os.path.join(data_folder,filename)
        if os.path.isfile(f):
            #creates dataframe of the state volume data
            cur_state = pd.read_csv(f,dtype = {'State_Code' : int, 'Station_Id' : str, 'Record_Type' : str, 'F_System' : str,
                                               'Travel_Dir' : str, 'Travel_Lane' : str,'Year_Record' : str,'Month_Record' : str,'Day_Record' : str,'Day_of_Week' : str,'Restrictions' : str,'Hour_Record' : str})
            print('length ' + str(cur_state.shape[0]))
            #adds county column to it
            #cur_state['County'] = ''
            
            #creates a smaller dictionary with station id and counties only from that state 
            
            if(not(cur_state.empty)):
                try: 
                 
                    cur_state_code = cur_state.at[2,'State_Code']
                    split_up_key = key[key['State_Code'] == cur_state_code]
                    county_dict = dict(zip(split_up_key['Station_Id'], split_up_key['County']))

                    #adds the counties and saves it into a new file
                    new_state_df = cur_state.apply(find_county, axis = 1)
                    new_state_df.to_csv(f'{data_folder}/{filename}',index = False)

                    del cur_state
                    del split_up_key

                    gc.collect()
                    
                except (KeyError):
                    print(cur_state)
            



def calculate_station_average(row) -> dict:
    row['Average'] = math.floor(row['Volume']/row['Count'])
    return row

def station_averages(directory):
    if os.path.exists('temp.csv'):
        os.remove("temp.csv")

    for filename in os.listdir(directory):
        f = os.path.join(directory,filename)
        if os.path.isfile(f):
            cur_state = pd.read_csv(f,dtype = {'State_Code' : int, 'Station_Id' : str, 'Hour_Volume' : str })
            
            #cur_state['County'] = ''
            cur_dict = {}
            
            for index,row in cur_state.iterrows():
                try:
                    cur_id = row['Station_Id']
                    #if its in the dictionary add to the volume and total count
                    if cur_id and cur_id.strip():

                        if cur_id in cur_dict:
                            data = cur_dict[cur_id]  # data is a dictionary
                            data['Count'] += 1
                            data['Volume'] += int(row['Hour_Volume'])
                            
                        else:
                            cur_dict[cur_id] = {'County': row['County'], 'Volume': int(row['Hour_Volume']), 'Count': 1, 'State_Code': row['State_Code']}
                except ValueError:
                    print(row['Hour_Volume'])        

            df = pd.DataFrame.from_dict(cur_dict, orient='index')
            df.index.names = ['Station_Id']
            newdf = df.apply(calculate_station_average,axis = 1)
            newdf.to_csv('temp.csv', header = False, mode = 'a')

            del df
            del newdf
            del cur_dict
            gc.collect()
    
            
def county_averages(directory):
    station_average = pd.read_csv('temp.csv',names = ['Station_Id', 'County', 'Volume', 'Count', 'State_Code', 'Average'],dtype = {'Station_Id':str,'County':str,'Volume':int,'Count':int,'State_Code':str,'Average':int})
    county_dict = {}

    for index,row in station_average.iterrows():
        if(len(row['State_Code']) == 1):
            county_key = f"0{row['State_Code']}{row['County']}"
        else:
            county_key = f"{row['State_Code']}{row['County']}"

        #if its in county dict just add to the count and volume
        if county_key in county_dict:
            
            data = county_dict[county_key]
            data['Count'] += row['Count']
            data['Volume'] += row['Volume']

        else:
            county_dict[county_key] = {'Volume' : row['Volume'], 'Count' : row['Count'],'State_Code' : row['State_Code'],'Average' : 0}

    for key in county_dict:
        county_dict[key]['Average'] = math.floor(county_dict[key]['Volume']/county_dict[key]['Count'])

    df = pd.DataFrame.from_dict(county_dict,orient = 'index')
    df.index.names = ['County_Key']
    print(directory)
    result = directory.split('\\')[1][:3]
    df.to_csv(f"{result} averages.csv")
    print(f"Saved to: {result} averages.csv" )
    print('lines: ' + str(count))

    del station_average
    del df
    gc.collect()

def find_averages(directory):
    add_county_to_csv(directory)
    station_averages(directory)
    county_averages(directory)

county_dict = {}
count = 0
root_dir = 'zipped data folder'
key = pd.read_csv('station_county_key.csv',dtype = {'Station_Id' : str ,'Latitude' : float,'Longitude' : float ,'State_Code' : int, 'County' : str})

for foldername in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, foldername)

    if os.path.isdir(folder_path):
        print(folder_path)
        find_averages(folder_path)
        

print('total lines: ' + str(count))