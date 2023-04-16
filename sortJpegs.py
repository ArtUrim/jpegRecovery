#!/usr/bin/env python3

import csv
import warnings
import pathlib
import shutil
import os.path
import time

class JpegDesc:

    def __init__(self,props:list):
        self.name = props[0]
        self.model = props[1]
        self.date = props[2]
        self.time = props[3]
        self.shutter = props[4]
        self.md5 = props[5]
        self.__convDate()

    def __convDate(self):
        dd = self.date.split(':')
        if len(dd) >= 3:
            self.year = dd[0]
            self.day = ''.join(dd[1:3])
            self.dir = '/'.join([self.year,self.day])
        else:
            warnings.warn( "Wrong date: {}".format( self.date ) )

    def __mkNewFileName(self):
        self.newfilename = 'KIA_' + self.shutter + '.jpg'

    def mkDir(self):
        if hasattr( self, "dir" ):
            pathlib.Path(self.dir).mkdir(parents=True,exist_ok=True)
            return True
        else:
            warnings.warn( "No dir, date: {}".format( self.date ) )
            return False

    def cpyFile(self):
        if not self.mkDir():
            warnings.warn( "No dir" )
            return False
        else:
            self.__mkNewFileName()
            fullFileName = '/'.join([self.dir,self.newfilename])
            if not os.path.isfile(fullFileName):
                shutil.copy(self.name,fullFileName)
            else:
                warnings.warn( "File {} exists".format(fullFileName) )
            return True


class JpegCollection:

    def __init__( self,fname: str ):
        self.collection = {}
        self.duplicates = 0
        self.clashes = 0
        with open( fname, "rt" ) as fd:
            creader = csv.reader(fd,delimiter=',')
            for row in creader:
                jd = JpegDesc(row)
                if jd.md5 in self.collection:
                    if jd.shutter != self.collection[jd.md5].shutter:
                        warnings.warn( "Two files, same md5sum: {} and {}".format(jd.name,self.collection[jd.md5].name))
                        warnings.warn( "    shutter count: {} and {}".format(jd.shutter,self.collection[jd.md5].shutter))
                        self.clashes += 1
                    else:
                        self.duplicates += 1 #it is normal: file recovered twice
                else:
                    self.collection[jd.md5] = jd

if __name__ == "__main__":
    start = time.time()
    fname = "all.csv"
    jc = JpegCollection( fname )
    print( "clashes: {}".format(jc.clashes) )
    print( "duplicates: {}".format(jc.duplicates) )

    counter = 0
    for jj in jc.collection:
        if jc.collection[jj].cpyFile():
            counter += 1

    print( "Finished {}, {} files recovered".format(time.time()-start,counter) )

