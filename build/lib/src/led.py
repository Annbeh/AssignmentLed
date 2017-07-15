
'''
Created on 12 Jul 2017

@author: annub
'''
import urllib.request
import re
import argparse

light = [0]
N = 0


# request
def read_url(link):
    req = urllib.request.urlopen(link)
    content = req.read().decode('utf-8')
    content_lines = content.splitlines()
    return content_lines


def read_command(command, x):
    global light  # 2d list for light

    x1 = x[0]
    y1 = x[1]
    x2 = x[2] + 1
    y2 = x[3] + 1

    if command == "off":
        for i in range(x1, x2):
            for j in range(y1, y2):
                light[i][j] = 0
    elif command == "on":
        for i in range(x1, x2):
            for j in range(y1, y2):
                light[i][j] = 1
    elif command == "switch":
        for i in range(x1, x2):
            for j in range(y1, y2):
                light[i][j] = 1 - light[i][j]


def calculate_light():
    global light
    number = 0
    for i in range(N):
        for j in range(N):
            if light[i][j] == 1:
                number += 1
    return number


def check_command(num_list):
    for i in range(len(num_list)):
        if (num_list[i] < 0):
            num_list[i] = 0
        if (num_list[i] > N):
            num_list[i] = N - 1
    return num_list


def switch_light(link):
    global light
    global N
    buffer = read_url(link)
    firstLine = buffer[0]
    N = int(firstLine)
    light = [[0] * N for _ in range(N)]

    for line in buffer[1:]:  # so if i reduce the number of rows it gives the output, you see. but if i remove the
        # total number of rows, it keeps running and takes a lot of time.

        # process line
        numbers_line = re.findall("[-\d]+", line)
        numbers_line = [int(e) for e in numbers_line]
        Not_consistent = False
        if (numbers_line[0] > numbers_line[2] or numbers_line[1] > numbers_line[3]):
            Not_consistent = True
        if (len(numbers_line) != 4 or Not_consistent):
            continue
        check_command(numbers_line)
        values = line.strip().split()
        if (values[0] == 'switch'):
            values[0] = 'switch'
        elif (values[0] == 'turn' and values[1] == 'off'):
            values[0] = 'off'
        elif (values[0] == 'turn' and values[1] == 'on'):
            values[0] = 'on'
        read_command(values[0], numbers_line)
    print(link, calculate_light())
    return

'''
uri_a = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_a.txt"
uri_b = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_b.txt"
uri_c = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_c.txt"
uri_d = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_d.txt"
switch_light(uri_a)
switch_light(uri_b)
switch_light(uri_c)
switch_light(uri_d)
'''

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input')
args = parser.parse_args()

link = args.input
switch_light(link)

