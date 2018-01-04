# Lab meeting calendar generator v1.1 #
# Jan 3, 2018
# dgibbs@systemsbiology.org

# This will generate the calendar list speakers. #
# The output is in rows Month,Day,Name,Email

import sys
import numpy as np
import calendar

cal = calendar.Calendar()

# Email List #
emails = open("dat/email_list_2018.txt",'r').read().strip().split("\n")
en = len(emails) # number of speakers
idx = 0          # speaker index mod en

holidays = [(1,1), (1,15), (2,19), (5,28), (7,4), (9,3), (11,22), (11,23), (12,25)]
holidayNames = ['New Years Day', 'MLK Day', 'Presidents Day',  'Memorial Day', 'July 4th', 'Labor Day', 'Thanksgiving pt.1', 'Thanksgiving pt.2', 'Christmas']

# The permutation #
np.random.seed()
for i in range(1,111):
    emailPerm = np.random.permutation(en)

# use previously generated ordering #
#ordering = open("dat/ordering.txt",'r').read().strip().split("\n")
ordering = np.array(emails)[emailPerm]

years  =  [2018 for i in range(0,12)]
months = [1,2,3,4,5,6,7,8,9,10,11,12]

# for 2018
for (yi,mi) in zip(years,months):
    thursCount = 0
    for di in cal.itermonthdays2(2018, mi): # iterate over days, Sunday == 0, Thursday == 4
        if (mi,di[0]) in holidays:
            print("\t".join([str(yi), str(mi), str(di[0]), 'Holiday']))
        elif (thursCount < 3) and (di[1] == 3) and (di[0] != 0) and ((mi,di[0]) not in holidays):
            thursCount += 1
            p = ordering[idx % en].split(',')
            print("\t".join([str(yi), str(mi), str(di[0]), p[1], p[2]]))
            idx +=1 
        elif di[1] == 3 and thursCount == 3:
            thursCount = 0
            print("\t".join([str(yi), str(mi), str(di[0]), 'Last Thursday Discussion']))

