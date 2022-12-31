import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def check_data_entry(prompt, valid_entries):
    """
    Asks user to type some input and verify if the entry typed is valid.
    Since we have 3 inputs to ask the user in get_filters(), it is easier to write a function.
    Args:
        (str) prompt - message to display to the user
        (list) valid_entries - list of string that should be accepted
    Returns:
        (str) user_input - the user's valid input
    """
    try:
        user_input = str(input(prompt)).lower()

        while user_input not in valid_entries:
            print('Sorry... it seems like you\'re not typing a correct entry.')
            print('Let\'s try again!')
            user_input = str(input(prompt)).lower()

        print('Great! the choose entry is: {}\n'.format(user_input))
        return user_input
    except valueError:
        print('Seems like there is an issue with your input')
    pass



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hi there! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    valid_cities = CITY_DATA.keys()
    prompt_cities = 'Please choose one of the 3 cities (chicago, new york city, washington): '
    city = check_data_entry(prompt_cities, valid_cities)
    # get user input for month (all, january, february, ... , june)
    valid_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    prompt_month = 'Please choose a month (all, january, february, ... , june): '
    month = check_data_entry(prompt_month, valid_months)
    # get user input for day of week (all, monday, tuesday, ... sunday)
    valid_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    prompt_day = 'Please choose a day (all, monday, tuesday, ... sunday): '
    day = check_data_entry(prompt_day, valid_days)

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city -  name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day
    if day != 'all':
        df = df[df['day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # TO DO: display the most common day of week
    # TO DO: display the most common start hour
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

    # display the most common month
    popular_month = df['month'].mode()
    print('Most Popular Month:', popular_month)

    # display the most common day of week
    popular_day_of_week = df['day'].mode()
    print('Most Day Of Week:', popular_day_of_week)

    # display the most common start hour
    popular_common_start_hour = df['hour'].mode()

    print('Most Common Start Hour:', popular_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def stations_stats(df):
    """ the most popular stations and trip?"""
    print("\nCalculating The Most Popular Stations and Trip\n")
    start_time = time.time()
    # display most popular used start station

    most_popular_start = df[' Start Station'].mode()
    print('Start Station:', most_popular_start)

    # display most popular used end station
    most_popular_end = df['End Station'].mode()
    print('Most End Station:', most_popular_end)

    # display most combination of start station and end station trip
    popular_start_end = df(['Start Station', 'End Station']).mode()
    print('most combination of start station and end station:', popular_start_end)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration(df):
    """ The total and average trip duration?"""
    print('\nCalculating Trip Duration\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df["Trip Duration"].sum()

    print("Total Travel Time", total_travel_time)

    # display mean travel time
    mean_travel_time = df["Trip Duration"].mean()

    print("Mean Travel Time", mean_travel_time)

    print("\nThis took %s seconds" % (time.time() - start_time))
    print('-' * 40)

    # Display counts of user types


def user_type(df):
    print('\nCalculating User Stats.\n')
    start_time = time.time()

    # Display counts of user types
    print("User Type Stats:")
    print(df["User Type"].value_counts())

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
     most_common_year = df["Birth Year"].mode()
     print("Most Common Year", most_common_year)
     most_recent_year = df["Birth Year"].max()
     print("Most Recent Year", most_recent_year)
     earliest_year = df["Birth Year"].min()
     print("Earliest Year", earliest_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_data(df):

    raw_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    start_loc = 0
    while raw_data == 'yes':
        if raw_data != 'yes':
            break
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        raw_display = input("Do you wish to continue?: ").lower()
        if raw_display.lower() != 'yes':
            break
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        trip_duration(df)
        user_type(df)
        display_data(df)

        while True:
            view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
            if view_data.lower() != 'yes':
                break
            display_data(df)
            break

            restart = input('\nWould you like to restart? Enter yes or no\n')
            if restart.lower() != "yes":
                break


if __name__ == "__main__":
    main()
