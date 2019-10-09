import subprocess as sp
import os
import sys as sys
import __globals as gl


#function to correct id3 tags in the file
#gets just full path
def edit_file( path, filename, path_out ):
    
    #get the real name of the song and artist
    #you can refactor this part of code. Now, it's a bit shitty 
    try:
        parts = os.path.splitext(filename)[0].split( " - " )
        artist = parts[0]
        title = parts[1]
        if len( parts ) > 2:  #extra ' - ' symbol
            parts.pop(0)
            title = " - ".join( parts )
    except:
        print( "File '" + filename + "' has non-formalized name" )
        return;

    #if folder hasn't been created - create it!
    if not( os.path.exists(path_out) and os.path.isdir(path_out) ):
        os.mkdir( path_out, 755 )

    #names and pathes
    fullname = path + '/' + filename
    fullname_out = path_out + '/' + filename
    prog = gl.PATH_TO_FFMPEG

    #fill args list
    args = [ prog, "-i", '"' + fullname + '"', "-id3v2_version", "3" ]

    def add_tag( tag, value ):
        args.append( "-metadata" )
        args.append( '"' + tag + "=" + value + '"' )

    add_tag( "title", title )
    add_tag( "artist", artist )
    args.append( '"' + fullname_out + '"' )

    #convert to command
    cmd = " ".join( args )  #fuck off this subprocess (it doesn't work with args[])  

    #execute
    process = sp.Popen( cmd,
                         shell=False,
                         stdout=sp.PIPE,
                         stderr=sp.STDOUT)
    out, err = process.communicate()
    errcode = process.returncode
    
    '''
    print( "_________________________________________" )
    print( cmd )
    print( "_________________________________________" )
    '''
    
    print( "File " + filename + " has been corrected" )
    #print( out )




#funtion to call 'edit_file()' for every mp3 in the folder
#gets just full path
def edit_files_in_folder( path, path_out ):
    for root, dirs, files in os.walk(path):
        for f in files:
            file_path_out = path_out + "/" + os.path.basename(root)
            if root == path:    #crutch
                file_path_out = path_out
            edit_file( os.path.normpath(root), f, file_path_out )
