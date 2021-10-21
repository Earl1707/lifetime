import os
import argparse
import datetime
import time
from dateutil import relativedelta

__app__ = "lifetime"
__version__ = "0.0.1"
__author__ = "GR"
__mail__ = "rgaffu@gmail.com"

class Lifetime():
    '''life time'''

    def __init__(self, birthday, refreshTime):
        self.birthday = birthday
        self.refreshTime = refreshTime

    def lifepass(self):
        today = self.birthday.today()
        time_diff = (today - self.birthday)
        print('You are alive from {}'.format(time_diff))

        one_second = datetime.timedelta(seconds=1)
        seconds, r = divmod(time_diff, one_second)
        print('                   {:d} seconds'.format(seconds))
        one_minute = datetime.timedelta(minutes=1)
        minutes, r = divmod(time_diff, one_minute)
        print('                   {:d} minutes'.format(minutes))
        one_hour = datetime.timedelta(hours=1)
        hours, r = divmod(time_diff, one_hour)
        print('                   {:d} hours'.format(hours))
        one_day = datetime.timedelta(days=1)
        days, r = divmod(time_diff, one_day)
        print('                   {:d} days'.format(days))
        r = relativedelta.relativedelta(today, self.birthday)
        print('                   {:d} months'.format(r.years*12+r.months))
        print('                   {:d} years'.format(r.years))

    def lifemagic(self):
        #TODO calcolare i magic number con formula di approssimazione
        print('')
        diff_seconds = datetime.timedelta(seconds=2000000000)
        print('2000000000 seconds will be {}'.format(self.birthday+diff_seconds))
        diff_minutes = datetime.timedelta(minutes=30000000)
        print('30000000 minutes will be {}'.format(self.birthday+diff_minutes))
        diff_hours = datetime.timedelta(hours=500000)
        print('500000 hours will be {}'.format(self.birthday + diff_hours))
        diff_days = datetime.timedelta(days=20000)
        print('20000 days will be {}'.format(self.birthday + diff_days))
        #print('missing {} days'.format(20000-days))

    def refresh(self):
        if (self.refreshTime):
            try:
                while True:
                    time.sleep(self.refreshTime)
                    os.system('cls')
                    self.lifepass()
            except KeyboardInterrupt:
                print(' ')

def get_arguments():
    '''This function parses and return arguments passed in'''
    # Assign description to the help doc
    parser = argparse.ArgumentParser(
        description='Lifetime',
        epilog='... and good luck')
    # Add arguments
    parser.add_argument(
        '-d', '--date', type=str, help='date (dd-mm-yyyy)', nargs='+', required=True)
    parser.add_argument(
        '-t', '--time', type=str, help='time (hh:mm)', nargs='+', default=['00:00'])
    parser.add_argument(
        '-r', '--refreshtime', type=int, help='Time to refresh (s)', required=False)
    # Array for all arguments passed to script
    args = parser.parse_args()
    # Assign args to variables
    strDate = args.date[0] + " " + args.time[0]
    refresh = args.refreshtime
    try:
        aDateTime = datetime.datetime.strptime(strDate, "%d-%m-%Y %H:%M")
    except:
        parser.print_help()
        exit(2)
    # Return all variable values
    return aDateTime, refresh


if __name__ == '__main__':
    aDateTime, refreshTime = get_arguments()
    lt = Lifetime(aDateTime, refreshTime)
    lt.lifepass()
    lt.lifemagic()
    lt.refresh()
