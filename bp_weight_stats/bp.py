#! /usr/bin/python3

import sys
import subprocess
from datetime import datetime




def get_bp(sys,dias,hr):

    date = datetime.now().strftime("%Y-%m-%d")

    time = datetime.now().strftime("%H:%M")

    bp = f"{sys}, {dias}, {hr}, {date}, {time} \n"
    print (bp)


    # write it out to csv file
    with open('bp.txt', 'a') as outfile:
        outfile.write(bp) 
        
    # put in reverse chronological order using linux tac
    with open('revbp.txt', 'w') as outfile:
        subprocess.run(['tac', 'bp.txt'], stdout=outfile)

if __name__ == "__main__":

    if len(sys.argv) < 4:
        print("Requires three arguments: Systolic Diastolic HeartRate.  Improper number of arguments passed")
        sys = input("Enter systolic: ")
        dias = input("Enter diastolic: ")
        hr = input("Enter heartRate: ")
        get_bp(sys, dias, hr)
        
    else:
        get_bp(sys.argv[1], sys.argv[2], sys.argv[3] )