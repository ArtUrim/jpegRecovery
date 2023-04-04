#!/usr/bin/env python3

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

def prepFile(fd):
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
    return fd

def isJpegType(fd,tags : dict):

    fd = prepFile(fd)

    if not fd.has_exif:
        return False

    for tt in tags:
        if tt in fd.list_all():
            if tags[tt] is None:
                continue
            elif isinstance(fd[tt],str):
               if not fd[tt].startswith(tags[tt]):
                   return False
            elif isinstance(fd[tt],int):
               if fd[tt] != tags[tt]:
                   return False
            else:
               return False
        else:
            return False
    return True

def onlyAdapted( jfiles: list, tags: dict ):
    pass
            
def getTimes(fd):
    fd = prepFile(fd)
    if False == fd:
        return {}

    retVal = {}

    if not fd.has_exif:
        return {}

    for tt in fd.list_all():
        if tt.startswith('datetime'):
            retVal[tt] = fd[tt]

    return retVal

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

def convertTime(orgVal:str):
    stl = orgVal.split( ' ' )
    if len(stl) < 2:
        return {}

    date = stl[0].split( ':' )
    if len(date) < 3:
        return {}

    minutes = stl[1].split( ':' )
    if len(minutes) < 3:
        return {}

    
    midnight = 3600*int(minutes[0]) + 60* int(minutes[1]) + int(minutes[2])

    return {
            'date': stl[0],
            'year': int(date[0]),
            'month': int(date[1]),
            'day': int(date[2]),
            'time': stl[1],
            'hour': int(minutes[0]),
            'min': int(minutes[1]),
            'sec': int(minutes[2]),
            'midnight': midnight
            }

def testSamopt():
    fg = convertTime('2015:07:19 12:08:40')
    dd = traverse_recov("jpg")
    addDir( 'result', '0312' )
    addDir( 'result', '0317' )
    addDir( 'result', '0312' )
    for ff in dd:
        if isJpegType(ff,{'model': 'PENTAX K-5 II s'}):
            print( " file {} is ok".format(ff) )
        else:
            print( " file {} not match".format(ff) )

    rr = getTimes('jpg/43745280.jpg')
    print( "{}".format(rr['datetime']) )
    print( "{}".format(len(rr)) )

if __name__ == "__main__":
    images = traverse_recov( "images" )
