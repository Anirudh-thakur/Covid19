# Student Action: Run the code below.
# Storing the path of 'time_series_covid19_confirmed_global.csv'' in 'conf_csv' variable.
conf_csv =r'COVID_19_data\csse_covid_19_data\csse_covid_19_time_series\time_series_covid19_confirmed_global.csv'
# Storing the path of 'time_series_covid19_deaths_global.csv'' in 'deaths_csv' variable.
deaths_csv = r'COVID_19_data\csse_covid_19_data\csse_covid_19_time_series\time_series_covid19_deaths_global.csv'
# Storing the path of 'time_series_covid19_recovered_global.csv' in 'rec_csv' variable.
rec_csv = r'COVID_19_data\csse_covid_19_data\csse_covid_19_time_series\time_series_covid19_recovered_global.csv'
# Student Action: Run the code below.
import pandas as pd # Data processing 
import matplotlib.pyplot as plt # Data visualisation
import seaborn as sns # Data visualisation
import folium # Cartograms / maps
import datetime # Work with date and time values

# Student Action: Run the code below.
# DataFrame for the total confirmed cases.
conf_df = pd.read_csv(conf_csv)
# Total confirmed cases in India.
india_cases = conf_df[conf_df['Country/Region'] == 'India'].iloc[:, 4:].apply(sum, axis=0)
india_cases.index = pd.to_datetime(india_cases.index)
china_cases = conf_df[conf_df['Country/Region'] == 'China'].iloc[:, 4:].apply(sum, axis=0)
china_cases.index = pd.to_datetime(china_cases.index) # The datetime value is formatted in the yyyy-mm-dd format.
# Student Action: Run the code below.
# The DataFrame for the total confirmed cases in India only.
last_col = conf_df.columns[-1]
conf_india_df = conf_df[conf_df['Country/Region'] == 'India']

# Map to show the distribution of confirmed coronavirus cases in China (regular markers).
India_map = folium.Map(location=[20.5937, 78.9629], width='100%', height='90%', tiles='Stamen Toner', zoom_start=20)
for i in conf_india_df.index:
  folium.Marker(location=[conf_india_df.loc[i, 'Lat'], conf_india_df.loc[i, 'Long']],
                popup= str(conf_india_df.loc[i, 'Province/State']) + "\n" + str(conf_india_df.loc[i, last_col])).add_to(India_map)
from IPython.display import display
India_map
India_map.save("IndiaMap.html")
conf_china_df = conf_df[conf_df['Country/Region'] == 'China']

# Map to show the distribution of confirmed coronavirus cases in China (regular markers).
china_map = folium.Map(location=[30.9756, 112.2707], width='100%', height='90%', tiles='Stamen Toner', zoom_start=4.25)
for i in conf_china_df.index:
  folium.Marker(location=[conf_china_df.loc[i, 'Lat'], conf_china_df.loc[i, 'Long']],
                popup= str(conf_china_df.loc[i, 'Province/State']) + "\n" + str(conf_china_df.loc[i, last_col])).add_to(china_map)
china_map
china_map.save("ChinaMap.html")