#!/usr/bin/python3

import sys
import subprocess
from datetime import datetime

"""
get weight as command line argument.  Format as Weight, Date, Time and 
store in csv file.  Note no header in csv file.
"""


def get_weight(weight):

    date = datetime.now().strftime("%Y-%m-%d")

    time = datetime.now().strftime("%H:%M")

    weight = f"{weight}, {date}, {time} \n"
    print ("Weight: ",weight)

    # write it out to csv file
    with open('weight.txt', 'a') as outfile:
        outfile.write(weight) 

    # put in reverse chronological order using linux tac
    with open('revweight.txt', 'w') as outfile:
        subprocess.run(['tac', 'weight.txt'], stdout=outfile)


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("no argument passed")
        weight = input("Enter weight: ")
        get_weight(weight)
    else:
        get_weight(sys.argv[1])
        

