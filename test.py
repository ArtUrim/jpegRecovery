#!/home/orangepi/Test/pyexif/bin/python3

import shutil
import os
from exif import Image
from pathlib import Path
import io

def traverse_recov(dname,type='.jpg'):
    resflist = []
    if os.path.exists(dname) and os.path.isdir(dname):
        with os.scandir(dname) as files:
            for ff in files:
                if ff.is_file() and ff.name.casefold().endswith('.jpg'):
                    resflist.append( dname + '/' + ff.name)
                    print( "File {}".format(ff.name) )
    return resflist

def isJpegType(fd,tags : dict):
    if isinstance(fd,str):
        try:
          fdesc = open(fd,'rb')
        except FileNotFoundError:
            return False
        fd = fdesc
    if isinstance(fd,io.IOBase):
        fd = Image(fd)
    if not isinstance(fd,Image):
        return False

    if not fd.has_exif:
        return False

    for tt in tags:
        if tt in fd.list_all():
            if not fd[tt].startswith(tags[tt]):
               return False
    return True
            

def addDir(updir,date):
    p = Path(updir)
    try:
        p.mkdir()
    except FileExistsError as exc:
        pass

    p = Path(updir + '/' + date )
    try:
        p.mkdir()
    except FileExistsError as exc:
        pass
    return p

if __name__ == "__main__":
    dd = traverse_recov("jpg")
    addDir( 'result', '0312' )
    addDir( 'result', '0317' )
    addDir( 'result', '0312' )
    for ff in dd:
        if isJpegType(ff,{'Model': 'PENTAX K-5 II s'}):
            print( " file {} is ok".format(ff) )
        else:
            print( " file {} not match".format(ff) )
