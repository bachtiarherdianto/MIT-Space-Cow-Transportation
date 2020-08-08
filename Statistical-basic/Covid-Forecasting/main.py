import pandas as pd, matplotlib.pyplot as plt



confirmed = pd.read_csv('confirmed.csv')
deaths = pd.read_csv('death.csv')
recovered = pd.read_csv('recovered.csv')
# print(confirmed.head())       # display the raw data


confirmed = confirmed.drop(['Province/State', 'Lat', 'Long'], axis= 1)
deaths = deaths.drop(['Province/State', 'Lat', 'Long'], axis= 1)
recovered = recovered.drop(['Province/State', 'Lat', 'Long'], axis= 1)

confirmed = confirmed.groupby(confirmed['Country/Region']).aggregate('sum')
deaths = deaths.groupby(deaths['Country/Region']).aggregate('sum')
recovered = recovered.groupby(recovered['Country/Region']).aggregate('sum')

confirmed = confirmed.T
deaths = deaths.T
recovered = recovered.T
# print(confirmed['Indonesia'].tail())  # preview the recent data by country


new_cases = confirmed.copy()                # duplicate the data into new variable
for day in range(1, len(confirmed)):        # day = 0 is the first day
    new_cases.iloc[day] = confirmed.iloc[day] - confirmed.iloc[day-1]

grow_rate = confirmed.copy()                # duplicate the data into new variable
for day in range (1, len(confirmed)):       # day = 0 is the first day
    grow_rate.iloc[day] = (new_cases.iloc[day] / confirmed.iloc[day-1]) * 100   # to percentage

active_cases = confirmed.copy()
for day in range(0, len(confirmed)):
    active_cases.iloc[day] = confirmed.iloc[day] - (deaths.iloc[day] + recovered.iloc[day])

overall_growth_rate = confirmed.copy()
for day in range(1, len(confirmed)):
    overall_growth_rate.iloc[day] = ((active_cases.iloc[day] - active_cases.iloc[day-1]) / active_cases.iloc[day-1]) * 100  # to percentage

death_rate = confirmed.copy()
for day in range(0, len(confirmed)):
    death_rate.iloc[day] = (deaths.iloc[day] / confirmed.iloc[day]) * 100   # to percentage

hozpitalization_rate_estimate = 0.05    # rate of hospitals' capacity is 5%
hozpitalization_needed = confirmed.copy()
for day in range(0, len(confirmed)):
    hozpitalization_needed.iloc[day] = active_cases.iloc[day] * hozpitalization_rate_estimate

estimated_death_rate = 0.03     # estimation rate of death is 3%
# print(deaths['Indonesia'].tail()[4] / estimated_death_rate)

def confirmed_plot(countries_list, confirmed_data):
    ax = plt.subplot()
    ax.set_facecolor('black')
    ax.figure.set_facecolor('#121212')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.set_title('Total Confirmed Cases', color='black')
    ax.legend(loc='upper left')
    for country in countries_list:
        confirmed_data[country][0:].plot(label= country)
    plt.legend(loc= 'upper left')
    plt.show()

def overall_grow_rate_graph_by_country(countries_list, overall_grow_rate_data):
    for country in countries_list:
        ax = plt.subplot()
        ax.set_facecolor('black')
        ax.figure.set_facecolor('#121212')
        ax.tick_params(axis= 'x', colors= 'white')
        ax.tick_params(axis= 'y', colors= 'white')
        ax.set_title(f'Overall Active Growth Rate in {country}', color= 'white')
        overall_grow_rate_data[country][10:].plot.bar()
        plt.show()

def simulation_growth_rate(base_data, estimation):
    simulation_growth_rate = estimation
    dates = pd.date_range(start='4/18/2020', periods=14, freq= 'D')
    dates = pd.Series(dates)
    dates = dates.dt.strftime('%m/%d/%Y')
    simulated = base_data.copy()
    simulated = simulated.append(pd.DataFrame(index= dates))
    for day in range(len(confirmed), len(confirmed)+14):    # simulation for 14 days
        simulated.iloc[day] = simulated.iloc[day - 1] * (simulation_growth_rate + 1)
    return simulated

def simulation_graph(country_sample, simulation_data):
    sample = country_sample
    ax = simulation_data[sample][10:].plot(label= 'US')
    ax.set_axisbelow(True)
    ax.set_facecolor('black')
    ax.figure.set_facecolor('#121212')
    ax.tick_params(axis= 'x', colors= 'white')
    ax.tick_params(axis= 'y', colors= 'white')
    ax.set_title(f'Simulation {sample}', color= 'white')
    # ax.legend(loc= 'upper left')
    plt.show()


countries = ['Italy', 'US', 'China', 'Indonesia']

# confirmed_plot(countries, confirmed)
# overall_grow_rate_graph_by_country(countries, overall_growth_rate)

simulation = simulation_growth_rate(confirmed, 0.1)
print(simulation['Indonesia'].tail(20))  # preview the recent data by country
simulation_graph('Indonesia', simulation)