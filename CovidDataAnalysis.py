import pandas as pd 

import matplotlib.pyplot as plt
import numpy as np
import random
#preprocessing
inspecting_column = ["iso_code", "continent", "location", "date", 
"new_cases", "new_deaths", "new_cases_per_million", 
"new_deaths_per_million", "new_tests", "new_tests_per_thousand", "tests_per_case", 
"positive_rate", "stringency_index", "population", "population_density", "median_age", 
"aged_65_older", "aged_70_older", "gdp_per_capita", "hospital_beds_per_thousand", 
"life_expectancy", "human_development_index"]

df = pd.read_csv('owid-covid-data.csv')
df = df[inspecting_column]
df = df.dropna()

def mean_calculation(collecting_mean, group, df):
	return df.groupby(group, as_index=False)[collecting_mean].mean()

def sum_calculation(collecting_mean, group, df):
	return df.groupby(group, as_index=False)[collecting_mean].sum()

def mean_export(collecting_mean, group, df, filename):
	mean_calculation(collecting_mean,group, df).to_csv(filename, float_format='%.4f')

#calculate mean
collecting_mean = ["new_cases", "new_deaths", "new_cases_per_million", 
"new_deaths_per_million", "new_tests", "new_tests_per_thousand", "tests_per_case", "stringency_index"]
mean_export(collecting_mean, "continent", df, "continent_cases_mean.csv")
mean_export(collecting_mean, "location", df, "country_cases_mean.csv")

#calculate country demographic
collecting_sum = ["population", "population_density", "median_age", 
"positive_rate","aged_65_older", "aged_70_older", "gdp_per_capita", "hospital_beds_per_thousand", 
"life_expectancy", "human_development_index"]
mean_export(collecting_sum, "location", df, "country_demographics.csv")









#calculate daily information

#preprocessing
inspecting_column = ["iso_code", "continent", "location", "date", 
"new_cases", "new_deaths", "new_cases_per_million", 
"new_deaths_per_million"]

df = pd.read_csv('owid-covid-data.csv')
df = df[inspecting_column]
df = df.dropna()
#preprocessing
inspecting_column = ["iso_code", "continent", "location", "date", "total_cases",
"new_cases", "new_deaths", "new_cases_per_million", 
"new_deaths_per_million", "stringency_index", "population", "population_density", "median_age", 
"aged_65_older", "aged_70_older", "gdp_per_capita", "hospital_beds_per_thousand", 
"life_expectancy", "human_development_index"]

df = pd.read_csv('owid-covid-data.csv')
df = df[inspecting_column]
df = df.dropna()

country_list = ["China", "Vietnam", "United States", "India", "South Korea", "New Zealand"]

df['total_cases'] = np.log2(df['total_cases'])
df['total_cases'] = df['total_cases'].shift(periods=-3, fill_value = 0)

fig, ax = plt.subplots()
for country in country_list:
	tmp_df = df[df['location']==country].sort_values('total_cases').plot(kind = 'line', 
		x='total_cases', y='stringency_index', 
    	ax=ax, title = "Government reaction (Stringency Index / Total cases)", 
    	#color=[[random.uniform(0, 1),random.uniform(0, 1), random.uniform(0, 1)]]
    	)

ax.legend(country_list);
plt.show()
