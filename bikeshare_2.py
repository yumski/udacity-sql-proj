import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        city = input('Choose a city: Chicago, New York City or Washington:\n').lower()

        if city in cities:

            while True:
                month = input('Choose a month: January, February, March, April, May, June or All: \n').lower()
                if month in months:
                    while True:
                        day = input('Choose a day of week: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All: \n').lower()
                        if day not in days:
                            print('Not a valid day')
                        else:
                            return city, month, day
                else:
                    print('Not a valid month')
        else:
            print('Not a valid city')

    print('-'*40)


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
    filename = pd.read_csv(CITY_DATA[city])
    df = pd.DataFrame(filename)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    if month != 'all':
        month = months.index(month) + 1
        df['month'] = df[df['month'] == month]

    if day != 'all':
        df['day_of_week'] = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month is: ", df['month'].mode()[0])


    # display the most common day of week
    print("The most common day of week is: ", df['day_of_week'].mode()[0])

    # display the most common start hour
    print("The most common start hour is: ", df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most common used start station: ", df['Start Station'].mode()[0])


    # display most commonly used end station
    print("The most common used end station: ", df['Start Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print(df.groupby(['Start Station', 'End Station']).size().reset_index().rename(columns={0:'count'}))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time: ", df['Trip Duration'].sum())

    # display mean travel time
    print("Average travel time: ", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Total users {} subscirbers and {} customers.".format(df['User Type'].value_counts()[0], df['User Type'].value_counts()[1]))

    # Display counts of gender
    print("Total of {} males and {} females renters".format(df['Gender'].value_counts()[0], df['Gender'].value_counts()[1]))

    # Display earliest, most recent, and most common year of birth
    print("{}, {} and {} are the earliest, most recent and most common birth year".format(df['Birth Year'].min(), df['Birth Year'].max(), df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
