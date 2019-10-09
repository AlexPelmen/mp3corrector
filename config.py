import subprocess as sp
import os
import sys
import __globals as gl

gl.PATH_TO_CONFIG = os.getcwd() + "\config.txt"

#function that returns a dictionary with variables from config
def get_vars():
    f_config = open( gl.PATH_TO_CONFIG , 'r')  #config file
    settings = {};  #settings from config

    #get all variables from config 
    strings = f_config.read().split( '\n' )
    for str in strings:
        if ~str.find( "=" ):
            var, value = str.split( "=" )
            settings[ var ] = value

    return settings
