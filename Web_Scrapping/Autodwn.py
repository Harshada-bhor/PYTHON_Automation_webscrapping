#Automation script which download specific file and store into the
# current directory of application.

from urllib.parse import urlparse
from sys import *
import os
import requests


def is_downloadable(url):
   h= requests.head(url,allow_redirects=True)
   header= h.headers
   content_type=header.get('content-type')

   if 'text' in content_type.lower():
       return False

   if 'html' in content_type.lower():
       return True


   return True

def get_filename_from_cd(cd):
    a= urlparse(cd)
    return os.path.basename(a.path)

def MarvellousDownload(url):
    allowed = is_downloadable(url)
    if allowed:
        try:
            res = requests.get(url,allow_redirects=True)

            filename= get_filename_from_cd(url)
            fd = open(filename,"wb")

            for buffer in res.iter_content(1024):
                fd.write(buffer)

            fd.close()
            return True
        except Exception as E:
            return False

    else:
        return False

def main():
    print("___________Python Automation & Machine learning__________")
    print("Application Name:" +argv[0])

    if (len(argv) == 2):


        if (argv[1] == "-h"):
            print("This script is used to download file")
            exit()

        if (argv[1] == "-u"):
            print("Usage : Application_name ")
            exit()


    url='https://www.google.com/favicon.ico'

    result = MarvellousDownload(url)

    if result:
        print("file successfuly downloaded")

    else:
        print("file failed to downloaded")


if (__name__ == "__main__"):
    main()