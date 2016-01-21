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
	ip_count_list = np.array([0]*32)
	total_ip = 0
	daycount = 30

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
					ip = np.array(features.ipFeature(line))
					print ip
					ip_count_list = np.sum(ip_count_list, ip)
					total_ip += 1
					

	# print count_list
	# print sum(count_list) / len(count_list)
	# print max(count_list), min(count_list)

	print ip_count_list
	print ip_count_list/total_ip

	frequencyIP = ip_count_list/total_ip

	pickle.dump(frequencyIP, open("ipBinaryFrequency.p", "wb"))
