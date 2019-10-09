import subprocess as sp
import os
import sys as sys
import __globals as gl

import check

#parse the config file
f_config = open('config.txt', 'r')  #config file
settings = {};  #settings from config
need_to_update_config = False

#set global var with path to the music foler
gl.PATH_TO_CONFIG = os.getcwd() + "\config.txt"

#get all variables from config 
strings = f_config.read().split( '\n' )
for str in strings:
    if ~str.find( "=" ):
        var, value = str.split( "=" )
        settings[ var ] = value


path = settings.get( "PATH" )
ffmpeg = settings.get( "FFMPEG" )

check.path( path )
check.ffmpeg( ffmpeg )

'''


fullname = path + '/' + filename
prog = "E:/Games/ffmpeg/bin/ffmpeg.exe"


args = [ prog, "-i", fullname, "-id3v2_version", "3" ]

def add_tag( tag, value ):
    args.append( "-metadata" )
    args.append( '"' + tag + "=" + value + '"' )

add_tag( "title", "TEST" )

args.append( "out.mp3" )
print( " ".join( args ) )
process = sp.Popen(args,
                     stdout=sp.PIPE,
                     stderr=sp.STDOUT)

out, err = process.communicate()
errcode = process.returncode

print( out )

'''

'''
process = sp.Popen(args,
                     stdout=sp.PIPE,
                     stderr=sp.STDOUT)

out, err = process.communicate()
errcode = process.returncode

'''

