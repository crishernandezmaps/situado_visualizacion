#!/usr/bin/env python3

'''
Things to:
0.- Read original images from a folder outside the project (OK)
1.- Reduce the size of the images and save them on a folder inside the project (OK)
2.- Improve IPTC info or use a different library ()
3.- Improve the resultant Json (GeoJson? ShapeFile?) ()
4.- Improve visualization (Grid) ()
5.- Create an app for this (they dont know a shit about programming) ()
'''

import numpy as np
import pandas as pd
import os
from fnmatch import fnmatch
from PIL import Image, ExifTags
from iptcinfo3 import IPTCInfo
import sys
import json

def produceJson(pathToFolder):
	outing = 'img-out/'
	try:
		### Get paths to images
		root = pathToFolder
		pattern = "*.jpg"
		images = []

		for path, subdirs, files in os.walk(root):
			for name in files:
				if fnmatch(name, pattern):
					images.append(os.path.join(path, name))

		# import code; code.interact(local=dict(globals(), **locals())) # ///////////////
		colection = []
		
		for i in images:
			a = Image.open(i)
			exif = { ExifTags.TAGS[k]: v for k, v in a._getexif().items() if k in ExifTags.TAGS }

			### Getting info
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

			# Getting IPTC Keywords -- more info: https://github.com/crccheck/iptcinfo3
			info = IPTCInfo(i)
			kw = [] 

			import code; code.interact(local=dict(globals(), **locals()))
			for x in info['keywords']:
				kw.append(x.decode("utf-8") )

			o = {
			"date": dateTime,
			"text": {
			"headline": '',
			"text": '',
			"tags": kw
			},
			"location": {
			"name": i,
			"lat": lat,
			"lon": lon,
			"zoom": 19,
			"line": False
			},
			"media": {
			"url": '../' + pathToFolder + i.split('/')[-1],
			"credit":'Santiago se Mueve',
			"caption": 'Proyecto Fondecyt Situado 2018'
			}}

			colection.append(o)

			data = {
			"storymap": {
			"slides": colection
			}}
			
			import code; code.interact(local=dict(globals(), **locals()))
			# Write JSON file
			sufx = pathToFolder.split('/')[1]
			# name = ''.join([outing,sufx,'.json'])
			name = ''.join([outing,sufx,'_test','.geojson'])

			with open(name_test, 'w') as outfile:
				json.dump(data, outfile, sort_keys = True, indent = 4, ensure_ascii = False)

			print(json.dumps(data['storymap']['slides']))

	except Exception:
		pass

### Folder containing images in JPG format
## Varas Mena ##
catatroVarasMena = '..img-in/catastroVarasMena/'
terrenoVarasMena = 'img-in/terrenoVarasMena/'
## Villa La Reina ##
terrenoVillaLaReina = 'img-in/terrenoVillaLaReina/'

### Calling function
produceJson(catatroVarasMena)
produceJson(terrenoVarasMena)
produceJson(terrenoVillaLaReina)

# import code; code.interact(local=dict(globals(), **locals()))