from utils import *
from covid import *
import pandas as pd

#3
casesdf = pd.read_csv('COVID-19-master/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')

#5
casesdf = correctDateFormat(casesdf, 'Confirmed')
#print(fixdf.head())

#7
deathsdf = pd.read_csv('COVID-19-master/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
deathsdf = correctDateFormat(deathsdf, 'Deaths')
recovereddf = pd.read_csv('COVID-19-master/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
recovereddf = correctDateFormat(recovereddf, 'Recovered')

#9
coviddf = mergeData(casesdf, deathsdf, 'Deaths')
coviddf = mergeData(casesdf, recovereddf, 'Recovered')
print(coviddf.tail())

#11
plotTimeline(coviddf, 'Date', 'Confirmed')
plotTimeline(coviddf, 'Date', 'Deaths')
plotTimeline(coviddf, 'Date', 'Recovered')

#13
#plotMultipleTimelines(coviddf, 'Date', 'Confirmed', 'Country/Region')
