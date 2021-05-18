import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    valid_city_input=["c","w","nyc"]
    city = ""
    while True:
        city=input("\nplease enter desired city: 'c' for chicago, 'w' for washington and 'nyc' for new york city = ").lower()
        if city in valid_city_input:
            break
        else:
            print("Please make sure you enter either 'c','w' or 'nyc'")

    if city=="c":
        city = "chicago"
    elif city=="w":
        city = "washington"
    elif city =="nyc":
        city = "new york city"

    # get user input for month (all, january, february, ... , june)
    valid_month_input=["all", "january", "february", "march","april" ,"may", "june"]
    month = ""
    while True:
        month=input("\nplease enter desired month: ('january', 'february', ... , 'june') OR 'all' to not apply any filter = ").lower()
        if month in valid_month_input:
            break
        else:
            print("Please make sure you enter full valid month name corretly")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    valid_day_input=["all", "monday", "tuesday", "wednesday","thursday" ,"friday", "saturday","sunday"]
    day = ""
    while True:
        day=input("\nplease enter desired day of week: ('monday', 'tuesday', ... 'sunday') OR 'all' to not apply any filter = ").lower()
        if day in valid_day_input:
            break
        else:
            print("Please make sure you enter full valid day of week name corretly")

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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != all:
        df = df[df['month'] == month.title()]
    if day != all:
        df = df[df['day_of_week'] == day.title()]

    if len(df.index) ==0:
        print("\n Your choices resulted in an empty data set \n Please try another combination \n")   
        city, month, day = get_filters()

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('-'*40)
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['hour'] = df['Start Time'].dt.hour

    # display the most common month
    print("Most common month is: {}\n".format(df['month'].mode()[0]))
    
    # display the most common day of week
    print("Most common day of week is: {}\n".format(df['day_of_week'].mode()[0]))

    # display the most common start hour
    print("Most common hour is: {}:00".format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    print("Most common used start station is: {}\n".format(df['Start Station'].mode()[0]))


    # display most commonly used end station
    print("Most common used end station is: {}\n".format(df['End Station'].mode()[0]))


    # display most frequent combination of start station and end station trip
    print("Most most frequent combination of start station and end station trip is: {}".format((df['Start Station'] + df['End Station']).mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time is: {} seconds\n".format(df['Trip Duration'].sum()))

    # display mean travel time
    print("Mean travel time is: {} seconds".format(df['Trip Duration'].mean()))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of user types are:\n {}\n".format(df['User Type'].value_counts()))

    try:
        # Display counts of gender
        print("Counts of gender are:\n {}\n".format(df['Gender'].value_counts()))

        # Display earliest, most recent, and most common year of birth
        print("Earliest year of birth is : {}".format(df['Birth Year'].min()))
        print("Most recent year of birth is : {}".format(df['Birth Year'].max()))
        print("Nost common year of birth is : {}".format(df['Birth Year'].mode()[0]))
    except Exception as e:
        print("Sorry looks like the city you chose have no records of Gender or Birth Year")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays five rows of data."""
    index = 0
    while True:
        user_choice = input("enter 'yes' to see next five rows of data or 'no' to break \n").lower()
        if (user_choice=="yes"):
            start_time = time.time()
            try:
                print('\nshowing data...\n')
                print(index)
                for i in range(index,index+5):
                    print(df.iloc[ index , :],"\n")
                    index=index +1

            except Exception as e:
                print("Sorry looks like you saw all the data rows\n")

            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)
        elif (user_choice=="no") :
            break
        else:
            print("Invalid input\n")
            continue

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print('\n',df)


        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
