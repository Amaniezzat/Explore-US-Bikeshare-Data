import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

cities = ["chicago", "new york city", "washington"]
months = ["january", "february", "march", "april", "may", "june", "all"]
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_selection = input('To view the available bikeshare data, type:\n (c) for Chicago\n (n) for New York City\n (w) for Washington\n  ').lower()

    while city_selection not in {'c','n','w'}:
        print('That\'s invalid input.')
        city_selection = input('To view the available bikeshare data, type:\n (c) for Chicago\n (n) for New York City\n (w) for Washington\n  ').lower()

    cities = {'c' : "chicago", 'n': "new york city", 'w': "washington"}
    if city_selection in cities.keys():
        city = cities[city_selection]


    time_frame = input("\nWould you like to filter your data by month, day, both, or not at all?\n")
    while time_frame not in {"none", "both", "month", "day"}:
        time_frame = input("\nInvalid input! Please re-enter the time frame you would like to filter by; month, day, both, or not at all?\n")
    while True:
        try:
            if time_frame in {"none", "both", "month", "day"}:
                break
        except KeyboardInterrupt:
            print("That's not a valid input")


    # get user input for month (all, january, february, ... , june)
    month_selection = input('\n\nIn order to filter data by a specific month, please type:\n (j) for January\n (b) for February\n (m) for March\n (a) for April\n (ma) for May\n (ju) for June\n (al) for All\n ').lower()

    while month_selection not in {'j', 'f', 'm', 'a', 'ma', 'ju', 'al'}:
        print('That\'s invalid input.')
        month_selection = input('That is an invalid input, please type:\n (j) for January\n (b) for February\n (m) for March\n (a) for April\n (ma) for May\n (ju) for June\n (al) for All\n ').lower()

    months = {'j' : "january", 'b': "february", 'm': "march", 'a' : "april", 'ma': "may", 'ju': "june", 'al' : "all"}
    if month_selection in months.keys():
        month = months[month_selection]


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = {"0" : "monday", "1": "tuesday", "2": "wednesday", "3": "thursday", "4": "friday", "5": "saturday", "6": "sunday", "7": "all"}

    day_selection = input('\n\nIn order to filter data by a specific day, please type:\n (0) for Monday\n (1) for Tuesday\n (2) for Wednesday\n (3) for Thursday\n (4) for Friday\n (5) for Saturday\n (6) for Sunday\n (7) for All\n ').lower()

    while day_selection not in {"0", "1", "2", "3", "4", "5", "6", "7"}:
        print('That\'s invalid input.')
        day_selection = input('That is an invalid input, please type:\n (0) for Monday\n (1) for Tuesday\n (2) for Wednesday\n (3) for Thursday\n (4) for Friday\n (5) for Saturday\n (6) for Sunday\n (7) for All\n ').lower()


    days = {"0" : "monday", "1": "tuesday", "2": "wednesday", "3": "thursday", "4": "friday", "5": "saturday", "6": "sunday", "7": "all"}

    if day_selection in days.keys():
        day = days[day_selection]


    if time_frame == 'none':
        print('\nFiltering for {} for the 6 months period\n\n'.format(city.title()))
        month = "all"
        day = "all"


   # now try to return the city
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # extract month and day of week from Start Time to create new columns
    df["month"] = df["Start Time"].dt.month

    df["day_of_week"] = df["Start Time"].dt.weekday_name
    
    # extract hour from Start Time to create new columns
    df["hour"] = df["Start Time"].dt.hour
    
    # filter by month if applicable
    if month != "All":
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1


        # filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week
    if day != "all":
        # filter by day of week to create the new dataframe
        df = df[df["day_of_week"] == day.title()]

    return df

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df["month"].mode()[0]
    print("The most common month: ", most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df["day_of_week"].mode()[0]
    print("The most common day: ", most_common_day)

    # TO DO: display the most common start 
    most_common_hour = df["hour"].mode()[0]
    print("The most common hour: ", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df["Start Station"].mode()[0]
    print("The most commonly used start station: ", popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df["End Station"].mode()[0]
    print("The most commonly used end station: ", popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    total_trip = df["Start Station"] + " _ " + df["End Station"]
    most_frequent_stations = total_trip.mode()[0]
    print("The most frequent combination of start station and end station trip: ", most_frequent_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("The total travel time: ", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("The average travel time: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_types_count = df["User Type"].value_counts()
        print("The count of user types: ", user_types_count)
    except KeyError:
        print("This data is not available for Washington")

    # TO DO: Display counts of gender
    try:
        gender_count = df["Gender"].value_counts()
        print("The count of user gender types: ", gender_count)
    except KeyError:
        print("This data is not available for Washington")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_brith_year = df["Birth Year"].min()
        print("The earliest year of birth: ", earliest_brith_year)
    except KeyError:
        print("This data is not available for Washington")

    try:
        most_recent_year_birth = df["Birth Year"].max()
        print("The most recent year of birth: ", most_recent_year_birth)
    except KeyError:
        print("This data is not available for Washington")

    try:
        most_common_year_birth = df["Birth Year"].mode()
        print("The most common year of birth: ", most_common_year_birth)
    except KeyError:
        print("This data is not available for Washington")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(city):
    print('\nRaw data is available to check... \n')
    display_raw = input('To View the availbale raw data in chuncks of 5 rows type: Yes or No if you don\'t want \n').lower()
    while display_raw not in ('yes', 'no'):
        print('That\'s invalid input, please enter your selection again')
        display_raw = input('To View the availbale raw data in chuncks of 5 rows type: Yes or No if you don\'t want \n').lower()
   # The second while loop is on the same level and doesn't belong to the first.
    while display_raw == 'yes':
        try:
            for chunk in pd.read_csv(CITY_DATA[city], index_col = 0 ,chunksize=5):
                print(chunk)
                display_raw = input('To View the availbale raw in chuncks of 5 rows type: Yes\n').lower()
                if display_raw != 'yes':
                    print("Thank You!")
                    break
            break
        except KeyboardInterrupt:
            print('Thank you.')  
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("Thank You!")
            break

if __name__ == "__main__":
    main()
