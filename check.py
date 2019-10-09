#check pathes

import subprocess as sp
import os
import sys
import __globals as gl


#function to check if the path to th folder with music is wrong or not
#gets path to the folder
def path( path ):
    if not path:
        print( "Path to the music folder hasn't been defined in the config file" )
        print( "Please, define it here: " + gl.PATH_TO_CONFIG )
        sys.exit(0)

    #check if the path is wrong
    try:
        music_list = os.listdir( path )
    except:
        print( "No such folder!" )
        print( "Please, change path to the folder in " + gl.PATH_TO_CONFIG )
        sys.exit(0)

    #here the folder is being read  
    print( "Folder is found! Ok!" )
    print( "You can change it here: " + gl.PATH_TO_CONFIG )




#function to check if the path to the ffmpeg is wrong
#gets path to ffmpeg
def ffmpeg( ffmpeg ):
    if not ffmpeg:
        print( "Path to the music ffmpeg hasn't been defined" )
        print( "Please, define it here: " + gl.PATH_TO_CONFIG )
        sys.exit(0)

    #check if the path is wrong
    args = [ ffmpeg, "-version" ]    
    process = sp.Popen(args,
                    stdout=sp.PIPE,
                    stderr=sp.STDOUT)   
    out, err = process.communicate()
    errcode = process.returncode
    if err:
        print( "Error is occured with ffmpeg! Check path in " + gl.PATH_TO_CONFIG )
        sys.exit(0)
    if not out:
        print( "ffmpeg returned empty result! Check path in " + gl.PATH_TO_CONFIG )
        sys.exit(0)

