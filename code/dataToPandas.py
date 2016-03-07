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

def main(testSampleSize = 10000000000):
	totalTransitionMatrix = np.matrix([[0,0,0], [0,0,0], [0,0,0]])

	limit = testSampleSize
	finished = False
	parse = True
	basepath = '../../alllogs/'
	dataFile = []
	dailyTotalData = pd.DataFrame()

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
				dailyTotalData = pd.DataFrame()
				print "Date is: ", date
				if date.startswith("201312"):
					continue

				for logFile in os.listdir(path):
					if limit == 0:
						finished = True
						break

					actualFilePath = os.path.join(path, logFile)
					dataFile = pd.read_csv(actualFilePath, sep = ";", names = ["timeStart", "timeEnd", "ip", "device", "id"], header=None)
					
					dateTimeDate = time.strptime(date, "%Y%m%d")
					# print dateTimeDate
					dataFile["date"] = date
					weekday = computeWeekday(date)
					dataFile["weekday"] = weekday

					dailyTotalData = pd.concat([dailyTotalData, dataFile])

					limit -= 1
				print dailyTotalData.head()
				dailyTotalData.to_pickle("pickleData/data" + str(date) + ".pickle")
					# print limit
					# print totalTransitionMatrix

if __name__ == '__main__':
	main()

# What are the entries I want
# Date, Day of week, 