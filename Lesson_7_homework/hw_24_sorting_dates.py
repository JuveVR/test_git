# Sort list of dates ascending.
#
# Dates are presented as string in format DD-MMM, DD - day of month (1, 2, ..., 31), MMM - 3 first letters of month ('Jan', 'Feb'. ..., 'Dec')
#
# I assume lambda function will help you.
#
# Don't use libs to work with dates


my_dates = ['14-Dec', '12-Apr', '13-Apr', '31-Dec', '1-Jan', '12-Jan', '1-Jun', '1-May', '30-Feb']

month_mapping = {'Jan': 1, 'Feb': 2, 'Mar': 3,
               'Apr': 4, 'May': 5, 'Jun': 6,
               'Jul': 7, 'Aug': 8, 'Sep': 9,
               'Oct': 10, 'Nov': 11, 'Dec': 12}

sorted_dates = sorted(my_dates, key=lambda x: (month_mapping[x.split('-')[1]], int(x.split('-')[0])))
print(sorted_dates)
