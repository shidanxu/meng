import numpy as np
import os
import random
import matplotlib.pyplot as plt
import pandas as pd
import re
import pickle
from datetime import datetime
import time

def combine(entry):
	pass

def computeDate(filename):
	p = re.compile(r'(\d{8})')
	results = re.search(p, filename)
	print "filename is: ", filename, type(filename)
	print "results is: ", results.group(0)
	return results.group(0)

def computeWeekday(stringDate):
	dateTimeDate = time.strptime(stringDate, "%Y%m%d")
	dt = datetime.fromtimestamp(time.mktime(dateTimeDate))
	return dt.weekday()

def dump(filename, obj):
	pickle.dump(obj, filename)

def pdCombine(file, df):
	df = df.concat(file)
	return df

def main(testSampleSize = 1000):
	totalTransitionMatrix = np.matrix([[0,0,0], [0,0,0], [0,0,0]])

	limit = testSampleSize
	finished = False
	parse = True
	basepath = '../../alllogs/'

	try:
		os.listdir(basepath)
	except Exception, e:
		print e
		parse = False


	if parse:
		for files in os.listdir(basepath):
			if finished == True:
				break
			path = os.path.join(basepath, files)
			if os.path.isdir(path):
				date = computeDate(path)
				print "Date is: ", date

				for logFile in os.listdir(path):
					if limit == 0:
						finished = True
						break

					actualFilePath = os.path.join(path, logFile)
					dataFile = pd.read_csv(actualFilePath, sep = ";", names = ["id", "timeStart", "timeEnd", "ip", "device"], header=None)
					
					dateTimeDate = time.strptime(date, "%Y%m%d")
					# print dateTimeDate
					dataFile["date"] = date
					weekday = computeWeekday(date)
					dataFile["weekday"] = weekday
					print dataFile.head()

					limit -= 1
					# print limit
					# print totalTransitionMatrix

if __name__ == '__main__':
	main(10)

# What are the entries I want
# Date, Day of week, 