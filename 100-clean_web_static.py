#/usr/bin/python3
"""Module to execute functions"""

from fabric.api import *

env.host = ['35.231.167.55', '34.236.146.248']

def do_clean(number=0):
    """Function that deletes out-of-date archives"""
    if number == 0 or number == 1:
        
    if number == 2:
        