import utilities
import random_generator
import numpy as np
import os
from sklearn.preprocessing import normalize
import random
import matplotlib.pyplot as plt
import pickle
import features
import re
from datetime import datetime



if __name__ == '__main__':

	currentPath = os.getcwd()
	oldpath = "../../alllogs/"

	files = utilities.get_all_files(oldpath)

	current_path = os.path.join(currentPath, oldpath)
	DOW_list = [0,0,0,0,0,0,0]
	TOD_weekend_list = []
	TOD_weekday_list = []
	total_time = 0
	# daycount = 50

	for afile in files:
		# if daycount == 0:
		# 	break
		# daycount -= 1
		print afile
		dates = re.findall('\d{8}', afile)
		if len(dates) != 1:
			print dates, "\n\n"
		else:
			print dates
		date_object = datetime.strptime(dates[0], '%Y%m%d')
		dayOfWeek = date_object.weekday()
		print dayOfWeek

		for individual_files in os.listdir(os.path.join(current_path, afile)):
			# print individual_files
					
			with open(os.path.join(os.path.join(current_path, afile), individual_files), 'r') as f:
				content = f.readlines()
				count = len(content)

				# print count
				# if count > 300:
					# print count, content
					# print "\n\n\n"
					# raw_input()
				

				for line in content:
					if line.strip() != None:				
						val = features.timeOfDay(line)
					if val != None:
						if dayOfWeek == 5 or dayOfWeek == 6:
							DOW_list[dayOfWeek] += 1
							TOD_weekend_list.append(val)
						else:
							DOW_list[dayOfWeek] += 1
							TOD_weekday_list.append(val)

						

	# print count_list
	# print sum(count_list) / len(count_list)
	# print max(count_list), min(count_list)

	print DOW_list

	
	pickle.dump(TOD_weekday_list, open("weekdayTimeStart.p", "wb"))
	pickle.dump(TOD_weekend_list, open("weekendTimeStart.p", "wb"))
