import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('Please choose a city of interest from Chicago, New York City and Washington: ')
            city = city.title()
            cities = {'Chicago': True, 'New York City': True, 'Washington': True}
            cities[city]
            break
        except:
            print('Please enter a valid city name.')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Please choose a month from January to June OR enter "all" for no filter on month: ')
            month = month.title()
            months = {'January': True, 'February': True, 'March': True, 'April': True, 'May': True, 'June': True, 'All': True}
            months[month]
            break
        except:
            print('Please enter a valid month OR all for no filter')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Please choose a day of week OR enter "all" for no filter on day of week: ')
            day = day.title()
            days = {'Monday': True, 'Tuesday': True, 'Wednesday': True, 'Thursday': True, 'Friday': True, 'Saturday': True, 'Sunday': True,'All': True}
            days[day]
            break
        except:
            print('Please enter a valid day of week OR all for no filter.')

    print('-'*40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1 
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
   
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Common Month: ', months[popular_month-1])
    
    # TO DO: display the most common day of week
    df['dayofweek'] = df['Start Time'].dt.weekday_name
    popular_dayofweek = df['dayofweek'].mode()[0]
    print('Most Common Day of Week: ', popular_dayofweek)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Common End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['comb'] = df['Start Station'] + ' to ' + df['End Station']
    popular_comb_station = df['comb'].mode()[0]
    print('Most Common Combination of Start Station and End Station:', popular_comb_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total travel time is: {} seconds'.format(total_time))
    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Mean travel time is: {} seconds'.format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:\n', user_types)

    # TO DO: Display counts of gender
    try:
        user_gender = df['Gender'].value_counts()
        print('Counts of user gender:\n', user_gender)
    except: 
        print('No gender information')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('Earliest year of birth:', df['Birth Year'].min())
        print('Most recent year of birth:', df['Birth Year'].max())
        print('Most common year of birth:', df['Birth Year'].mode()[0])
    except:
        print('No birth year information')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    while True:
        try:
            decisions = {'yes': True, 'no': True}
            decision = input('Do you want to see raw data?').lower()
            decisions[decision]
            i = 0
            while decision == 'yes':
                print(df[(i*5):(i*5+5)])
                while True:
                    try:
                        decision = input('Do you want to see 5 more lines of raw data? Enter yes for more.').lower()
                        decisions[decision]
                        i += 1
                        break
                    except:
                        print('Please enter yes or no.')
            #if decision == 'yes':
            #    i = 1
            #    print(df.head())
            #    decision = input('Do you want to see more 5 lines of raw data? Enter yes for more.').lower()
            #    while decision == 'yes':
            #        print(df[(i*5):(i*5+5)])
            #        decision = input('Do you want to see more 5 lines of raw data? Enter yes for more.').lower()
            #        i += 1
            break
        except:
            print('Please enter yes or no.')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

