import subprocess as sp
import os
import sys as sys
import __globals as gl

import check
import config

#parse the config file
settings = config.get_vars()
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

