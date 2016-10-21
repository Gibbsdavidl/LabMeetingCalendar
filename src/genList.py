# Lab meeting calendar generator v1.0 #
# Oct 21 2016
# dgibbs@systemsbiology.org

# This will generate the calendar list speakers. #
# The output is in rows Month,Day,Name,Email

import sys
import numpy as np
import calendar

cal = calendar.Calendar()

# Email List #
emails = open("/Users/davidgibbs/Data/emailsysdir/emailList.txt",'r').read().strip().split("\n")
en = len(emails) # number of speakers
idx = 0          # speaker index mod en

holidays = [(1,1), (1,18), (2,15), (5,30), (7,4), (8,5), (11,24), (11,25), (12,25), (12,26)]

# The permutation #
np.random.seed()
for i in xrange(1,1733):
    emailPerm = np.random.permutation(en)

# for the rest of 2016 and 2017
for yi in [2016,2017]:
    # for each month
    for mi in [11,12,1,2,3,4,5,6,7,8,9,10,11,12]:
        for di in cal.itermonthdays2(2016, mi): # iterate over days, Sunday == 0, Thursday == 4
            if di[1] == 3 and di[0] != 0 and di not in holidays:
                p = emails[emailPerm[idx % en]].split(',')
                print("\t".join([str(mi), str(di[0]), p[2], p[1]]))
                idx +=1 
