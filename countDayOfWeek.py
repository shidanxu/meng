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
import datetime



if __name__ == '__main__':

	currentPath = os.getcwd()
	oldpath = "../../alllogs/"

	files = utilities.get_all_files(oldpath)

	current_path = os.path.join(currentPath, oldpath)
	DOW_list = []
	total_time = 0
	daycount = 14

	for afile in files:
		if daycount == 0:
			break
		daycount -= 1
		print afile
		for individual_files in os.listdir(os.path.join(current_path, afile)):
			# print individual_files
			dates = re.findall('\d{8}', current_path)
			if len(dates) != 1:
				print dates, "\n\n"
			else:
				print dates

		date_object = datetime.strptime(dates[0], '%H%M%S')
		dayOfWeek = date_object.weekday()

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
						DOW_list.append(dayOfWeek)
						
						

	# print count_list
	# print sum(count_list) / len(count_list)
	# print max(count_list), min(count_list)

	print DOW_list

	
	pickle.dump(DOW_list, open("dayOfWeek.p", "wb"))
