
import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if "AM" in s:
        s = s.strip("AM")
        hr, min, sec = s.split(":")
        if hr == "12":
            hr = "00"
    else:
        s = s.strip("PM")
        hr, min, sec = s.split(":")
        if hr != "12":
            hr = (12 + int(hr)).__str__()
        
    return hr + ":" + min + ":" + sec
        

if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)

    # f.write(result + '\n')

    # f.close()
