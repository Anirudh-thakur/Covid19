Execution Screenshots in Outputs folder 
git clone https://github.com/CSSEGISandData/COVID-19.git by using git bash in the current directory
pip install pandas
pip install matplotlib
pip install seaborn 
pip install folium 
pip install datetime
pip install Ipython (To display map image)
pip install conda 


c:\Users\Anirudh\.vscode\extensions\ms-python.python-2020.6.91350\pythonFiles\pyvsc-run-isolated.py pip install -U pylint
to install pylint 

Copy full paths instead of relative paths 

https://towardsdatascience.com/covid-19-data-processing-58aaa3663f6


add r to relative path : conf_csv =conf_csv =r'COVID_19_data\csse_covid_19_data\csse_covid_19_time_series\time_series_covid19_confirmed_global.csv'

Initial Setup code 

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
# Display the first five rows of the 'conf_df' DataFrame.
print(conf_df.head())


Plot graph(Global)
conf_df = pd.read_csv(conf_csv)
global_cases = conf_df.iloc[:, 4:].apply(sum, axis=0)
# Converting the indices to datetime values.
global_cases.index = pd.to_datetime(global_cases.index) # The datetime value is formatted in the yyyy-mm-dd format.
global_cases
conf_df = pd.read_csv(conf_csv)
plt.style.use('dark_background')
plt.figure(figsize=(20, 6))
plt.title('Total Coronavirus Cases Reported Across the Globe')
plt.plot(global_cases.index, global_cases, c='red', linewidth=7, marker='*', markersize=10)
plt.xticks(rotation=90)
plt.ylabel('in millions')
plt.grid(True, 'major', linestyle='--', c='grey')
plt.show()

PlotGraph(India)
conf_df = pd.read_csv(conf_csv)
# Total confirmed cases in India.
india_cases = conf_df[conf_df['Country/Region'] == 'India'].iloc[:, 4:].apply(sum, axis=0)
india_cases.index = pd.to_datetime(india_cases.index)
# Student Action: Run the code below.
# Line plot for the total number of coronavirus confirmed cases reported in India.
plt.figure(figsize=(20, 6))
plt.title('Total Coronavirus Cases Reported in India')
plt.plot(india_cases.index, india_cases, c='r', linewidth=2, marker='o', markersize=7)
plt.xticks(rotation=45)
plt.grid(True, 'major', linestyle='--', c='grey')
plt.show()

To show cases on Map 

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