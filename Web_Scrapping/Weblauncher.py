#Automation script which accept file name. Extract all URL's from that file and connect
# to that URL's.

import os
import urllib3
from sys import *
import webbrowser
import re


def is_connected():
    cmd = os.system('ping google.com -w 4 > clear')
    if cmd == 0:
        return True
    else:
        return False

    

def Find(string):
    url= re.findall('https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*))+',string)
    return url

def Weblauncher(path):
    with open(path) as fp:
        for line in fp:
            print(line)
            url= Find(line)
            print(url)
            for str in url:
                webbrowser.open(str,new=2)


def main():
    print("___________Python Automation & ml learning__________")
    print("Application Name:" +argv[0])

    if (len(argv) != 2):
        print("Insufficient arguments")
        exit()

    if (argv[1] == "-h"):
        print("This script will travel the directory and display the names of all entries")
        exit()

    if (argv[1] == "-u"):
        print("Usage : Application_name Direcory_Name")
        exit()

    try:
        connected = is_connected()

        if connected:
            Weblauncher(argv[1])
        else:
            print("unable to connect internet...")

    except ValueError:
        print("Error:Invalid Datatype of input")
    except Exception as E:
        print("Error:Invalid input",E)


if (__name__ == "__main__"):
    main()