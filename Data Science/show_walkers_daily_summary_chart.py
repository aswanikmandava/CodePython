import numpy
from matplotlib import pyplot

def get_data_dict(filename):
    """
    Takes a csv filename and returns a dictionary with key as walker and 
    value as a list of hourly steps done by walker
    for the last week
    """
    # load hourly data from csv
    csv_data = numpy.loadtxt(filename, delimiter=",", skiprows=1, dtype=str)

    # store in dict
    hourly_steps = dict()
    for data in csv_data:
        walker = data[0]    # first cell
        walker_hourly_steps =  numpy.array(data[1:], dtype=int) # remaining all cells except first cell
        hourly_steps[walker] = walker_hourly_steps
    return hourly_steps

def normalize_data_hourly_to_daily(data):
    """
    This takes a list of metrics hour wise and generates an total daily sample
    Returns the daily metric list
    """
    daily_data = list()
    for index in range(0, len(data), 24):
        day_hourly_data = data[index:index+24]
        day_avg_metric = sum(day_hourly_data)
        daily_data.append(day_avg_metric)
    return daily_data

def get_daily_from_hourly(data):
    """
    This takes data dictionary of walkers with hourly data and convert them to a daily data
    Return the dict
    """
    daily_data = dict()
    for key, value in data.items():
        daily_data[key] = normalize_data_hourly_to_daily(value)
    return daily_data

def reduce_daily_to_weekly(data):
    """
    This takes data dictionary of walkers with daily data and convert them to a weekly data
    Return the dict
    """
    weekly_data = dict()
    for key, value in data.items():
        weekly_data[key] = sum(value)   # compute the sum of steps for the entire week
    return weekly_data

def get_lists_for_walkers_steps(data):
    """
    Breaks down weekly dictionary into 2 separate lists
        Walkers
        Steps
    """
    walkers_list = list()
    steps_list = list()
    for key, value in data.items():
        walkers_list.append(key)
        steps_list.append(value)
    return walkers_list, steps_list

def get_list_min_elememt_index(input_list):
    """
    Returns the minimum element in a given list of integers
    """
    min_index = 0
    for idx in range(len(input_list)):
        if input_list[idx] < input_list[min_index]:
            min_index = idx
    return min_index

def sort_walkers_steps_list(walkers_list, steps_list):
    sorted_walkers = list()
    sorted_steps = list()
    for idx in range(len(steps_list)):
        min_index = get_list_min_elememt_index(steps_list)
        sorted_walkers.append(walkers_list[min_index])
        sorted_steps.append(steps_list[min_index])
        # set the value to infinity so that next minimum value can be found in next iteration
        steps_list[min_index] = float("inf")
    return sorted_walkers, sorted_steps

def plot_walkers_by_steps(walkers, steps):
    pyplot.bar(walkers, steps)

def main():
    csv_filename = "walk_steps.csv"
    hourly_data = get_data_dict(csv_filename)
    daily_data = get_daily_from_hourly(hourly_data)
    weekly_data = reduce_daily_to_weekly(daily_data)
    walkers, steps = get_lists_for_walkers_steps(weekly_data)
    s_walkers, s_steps = sort_walkers_steps_list(walkers, steps)
    plot_walkers_by_steps(s_walkers, s_steps)

main()
