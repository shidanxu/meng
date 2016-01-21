import utilities
import random_generator
import numpy as np
import os
from sklearn.preprocessing import normalize
import random
import matplotlib.pyplot as plt
import pickle
import features



if __name__ == '__main__':

	currentPath = os.getcwd()
	oldpath = "../../alllogs/"

	files = utilities.get_all_files(oldpath)

	current_path = os.path.join(currentPath, oldpath)
	count_list = []
	time_count_list = np.array([0]*17)
	total_time = 0
	daycount = 14

	for afile in files:
		if daycount == 0:
			break
		daycount -= 1
		print afile
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
				count_list.append(count)

				for line in content:
					val = features.timeStartFeature(line)
					if val != None:
						ip = np.array(val)
						# print ip
						time_count_list = np.add(time_count_list, ip)
						total_time += 1
						

	# print count_list
	# print sum(count_list) / len(count_list)
	# print max(count_list), min(count_list)

	print time_count_list
	print time_count_list, total_time
	total_time =float(total_time)

	frequencyTime = time_count_list/total_time

	pickle.dump(frequencyTime, open("TimeBinaryFrequency.p", "wb"))
