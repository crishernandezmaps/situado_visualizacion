#!/usr/bin/env python3
import os, glob
import sys
import shutil
import datetime
from PIL import Image, ExifTags
from iptcinfo3 import IPTCInfo
from geojson import Point, Feature, FeatureCollection, dump

route2folderWithImages = sys.argv[1]

pwd2root = os.getcwd()

d = str(datetime.datetime.now())
timeStamp = d.split(' ')[0].strip()

def getFileWithExt(extension,path2Folder):
    cd = os.chdir(path2Folder)
    filesEXT = []
    ext = ''.join(['*.',extension])
    for f in glob.glob(ext):
        filesEXT.append(f)
    return filesEXT

def downSize():

    lisOfBigImages = getFileWithExt('jpg',route2folderWithImages)
    for i in lisOfBigImages:   
        try:
            foo = Image.open(i)
            foo = foo.resize((160,300),Image.ANTIALIAS)
            foo.save(''.join([toSaveImages,'/',i]),optimize=True,quality=95) # From 1.9GB to 8.8MB ... nice!
            print(i + ' is done!')
        except:
            print(i + '... is already done!!!')
            pass   

    ### creating a folder to save our final data ###
    smallImagestoday = ''.join(['smallImages_',timeStamp])
    if(os.path.isdir(smallImagestoday)):
        pass
    else:
        os.mkdir(smallImagestoday)

    ### extracting Exif and IPTC info from big images - originals ###
    lisOfBigImages = getFileWithExt('jpg',route2folderWithImages)
    collection = []
    print('getting EXIF and IPTC info ...')
    for i in lisOfBigImages:   
        try:
            openSmall = Image.open(i)
            exif = { ExifTags.TAGS[k]: v for k, v in openSmall._getexif().items() if k in ExifTags.TAGS }
            dateTime = exif['DateTime'][0:10].replace(':','-').strip()
            lat = [float(x)/float(y) for x, y in exif['GPSInfo'][2]]
            lon = [float(x)/float(y) for x, y in exif['GPSInfo'][4]]
            latref = exif['GPSInfo'][1]
            lonref = exif['GPSInfo'][3]
            lat = lat[0] + lat[1]/60 + lat[2]/3600
            lon = lon[0] + lon[1]/60 + lon[2]/3600
            if latref == 'S':
                lat = -lat
            if lonref == 'W':
                lon = -lon
            
            info = IPTCInfo(i,force=True)
            kw = []
            for x in info['keywords']:
                kw.append(x.decode("utf-8") )                                        
            
            o = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [lon,lat]
                },
                "properties": {
                    "name": i,
                    "date": dateTime,
                    "tags": kw,
                    "image": ''.join(['https://github.com/crishernandezmaps/situado_visualizacion/blob/gh-pages/',smallImagestoday,'/',i,'?raw=true']),
                    "author": "Made by Cris Hernandez for FONDECYT Nº 1171554, INVI - U. of Chile, 2018/9"
                }
            } 
            
            collection.append(o)   
        except:
            pass

    data = {
        "type": "FeatureCollection",
        "features": collection
    }

    ### Saving GeoJson ###
    name = ''.join([pwd2root,'/',smallImagestoday,'/',route2folderWithImages.split('/')[-1],'_',timeStamp,'.geojson'])
    with open(name, 'w') as f:
        dump(data, f)        
    
    print(data)
    print('All Done :)...')


if __name__ == "__main__":
    downSize()
    pass


'''
https://github.com/crishernandezmaps/situado_visualizacion/blob/gh-pages/smallImages_2019-06-20/IMG_20180319_162715.jpg 
'''