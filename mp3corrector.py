import subprocess as sp
import os
import sys as sys
import __globals as gl

import check
import config
import corrector

#parse the config file
settings = config.get_vars()
path = settings.get( "PATH" )
gl.PATH_TO_FFMPEG = settings.get( "FFMPEG" )
gl.RECURCIVE = int(settings.get( "RECURCIVE" ))

#check if the pathes are wrong
check.path( path )
check.ffmpeg( gl.PATH_TO_FFMPEG )

#create Folder for mp3 files
copy_num = 0;
ok = False
while not ok:
    path_out = os.path.dirname( path ) + "/" + os.path.basename( path ) + "_corrected"

    if copy_num:
        path_out += "_" + str( copy_num )
    
    try:
        os.mkdir( path_out, 755 )
        ok = True
    except FileExistsError:
        copy_num = copy_num+1
        
    
#get file list
corrector.edit_files_in_folder( path, path_out )

    
