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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_selection = input('To view the available bikeshare data, kindly type:\n The letter (c) for Chicago\n The letter (n) for New York City\n The letter (w) for Washington\n  ').lower()

    while city_selection not in ["c","n","w"]:
        print("That's invalid input. ")
        city_selection = input('To view the available bikeshare data, kindly type:\n The letter (c) for\
                Chicago\n The letter (n) for New York City\n The letter (w) for Washington\n  ').lower()

    city_selections={"c":'chicago.csv',"n":'new_york_city.csv',"w":'washington.csv'}
    if city_selection in city_selections.keys():
        city=city_selections[city_selection]


    # TO DO: get user input for month (all, january, february, ... , june)
    months=['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month=input('\n\nTo filter {}\'s data by a particular month, please type the month name or all for not filtering by month:\n-January\n-February\n-March\n-April\n-May\n-June\n-All\n\n:'.format(city.title())).lower()
    while month not in months:
        print("That's invalid choice, please type a valid month name or all.")
        month = input(
            '\n\nTo filter {}\'s data by a particular month, please type the month name or all for not filtering by month:\n-January\n-February\n-March\n-April\n-May\n-June\n-All\n\n:'.format(
                city.title())).lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day=input('\n\nTo filter {}\'s data by a particular day, please type the day name or all for not filtering by day:\n-Monday\n-Tuesday\n-Wednesday\n-Thursday\n-Friday\n-Saturday\n-Sunday\n-All\n\n:'.format(
                city.title())).lower()
    while day not in days:
        print("That's invalid choice, please type a valid day name or all.")
        day = input(
            '\n\nTo filter {}\'s data by a particular day, please type the day name or all for not filtering by day:\n-Monday\n-Tuesday\n-Wednesday\n-Thursday\n-Friday\n-Saturday\n-Sunday\n-All\n\n:'.format(
                city.title())).lower()



    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    # load data file into a dataframe
    df=pd.read_csv(city)
    # convert the Start Time column to datetime
    df["Start Time"]=pd.to_datetime(df["Start Time"])

    # extract month and day of week from Start Time to create new columns
    df["Month"]=df["Start Time"].dt.month
    df["Day"]=df["Start Time"].dt.day_name()

    # filtering by month
    if month != "all":
        # use the index of the months list to get the corresponding int
        months=['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df=df[df["Month"] == month]


    # filtering by day of week
    if day != "all":
        # filter by day of week to create the new dataframe
        df=df[df["Day"] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['Month'].mode()[0]
    print("The most common month : ", popular_month)



    # TO DO: display the most common day of week
    popular_day = df['Day'].mode()[0]
    print("The most common day of week : ",popular_day)

    # TO DO: display the most common start hour
    df["Hour"]=df["Start Time"].dt.hour
    popular_hour = df['Hour'].mode()[0]
    print("The most common start hour : ",popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_startstation = df["Start Station"].mode()[0]
    print("The most commonly used start station : ",popular_startstation)



    # TO DO: display most commonly used end station
    popular_endstation = df["End Station"].mode()[0]
    print("The most commonly used end station : ", popular_endstation)


    # TO DO: display most frequent combination of start station and end station trip
    df["rout"] = df["Start Station"] + "-" + df["End Station"]
    popular_combination=df["rout"].mode()[0]
    print("The most frequent combination of start station and end station trip : ",popular_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_traveltime=df["Trip Duration"].sum()
    print("The total travel time : ",total_traveltime)


    # TO DO: display mean travel time
    mean_traveltime=df["Trip Duration"].mean()
    print("The mean travel time : ",mean_traveltime)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df["User Type"].value_counts()
    print("\nThe counts of user types : \n",user_types)

    # TO DO: Display counts of gender
    # I can fix this issue also by using Try & except blocks.
    if city == 'washington.csv':
        print("This data is not available for Washington.")
    else:
        gender_types=df["Gender"].value_counts()
        print("\nThe counts of gender : \n",gender_types)

    # TO DO: Display earliest, most recent, and most common year of birth
    # I can fix this issue also by using Try & except blocks.
    if city == 'washington.csv':
        print("This data is not available for Washington.")
    else:
        earliest=df["Birth Year"].min()
        most_recent=df["Birth Year"].max()
        most_common=df["Birth Year"].mode()
        print("\nThe earliest year of birth : {}\n The most recent year of birth : {} \n The most common year of birth : {}".format(earliest,most_recent,most_common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def display_raw_data(city):
    print('\n Raw data is available to check... \n')
    display_raw=input("\n Would you like to see the raw data? Enter yes or no.\n")
    while display_raw == "yes":
        try:
            for chunk in pd.read_csv(city,chunksize=5):
                print(chunk)
                display_raw = input("\n May you want to have a look on more raw data? Type yes or no\n")
                if display_raw != "yes" :
                    print("Thank you so much.")
                    break
            break
        except KeyboardInterrupt:
            print("Thank you so much.")















def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
