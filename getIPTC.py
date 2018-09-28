#!/usr/bin/python
import numpy as np
import pandas as pd
import os
from fnmatch import fnmatch
from PIL import Image, ExifTags
# from iptcinfo3 import IPTCInfo
from iptcinfo import IPTCInfo
import sys
import json


def produceJson(pathToFolder):
	try:

		### Get paths to images
		root = pathToFolder
		pattern = "*.jpg"
		images = []

		for path, subdirs, files in os.walk(root):
			for name in files:
				if fnmatch(name, pattern):
					images.append(os.path.join(path, name))

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

			for x in info['keywords']:
				kw.append(x.decode("utf-8") )

			o = {
			"date": dateTime,
			"text": {
			"headline": 'Catastro',
			"text": ",".join(kw),
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
			"url": 'https://raw.githubusercontent.com/crishernandezmaps/imagenes/master/' + i.split('/')[-1],
			"credit":'Santiago se Mueve',
			"caption": 'Proyecto Fondecyt Situado 2018'
			}}

			colection.append(o)

			data = {
			"storymap": {
			"slides": colection
			}}

			# Write JSON file
			# with open(''.join([root,'/',pathToFolder.split('/')[-1],'.json']), 'w') as outfile:
			with open('data/x.json', 'w') as outfile:
				json.dump(data, outfile, sort_keys = True, indent = 4, ensure_ascii = False)

			print json.dumps(data['storymap']['slides'])


	except Exception:
		pass

# Folder containing images in JPG format
produceJson('imagenes') 
# produceJson(r'../../imagenes/varas_mena/terreno')



