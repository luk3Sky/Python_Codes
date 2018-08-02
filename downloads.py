import random
import urllib.request
import urllib
from urllib3 import request


def download_image(url):
    file_name = str(random.randrange(1, 1000)) + '.jpeg'
    urllib.request.urlretrieve(url, file_name)


# download_image("https://a.pololu-files.com/picture/0J5068.600x480.jpg?177f3d11af1e7340760d9e83fab61489")

def download_csv_files(csv_url):
    print("in the f^n")
    # csv = request.urlopen(csv_url).read()
    response = urllib.request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines_list = csv_str.split('\\n')
    # file writing and handling
    write_file = open((random.randrange(1, 1000) + '.csv'), 'w')
    for line in lines_list:
        print("damn")
        write_file.write(line + '\n')
    write_file.close()
