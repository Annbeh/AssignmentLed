'''
Created on 13 Jul 2017

@author: annub
'''

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