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