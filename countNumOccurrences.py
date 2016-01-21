import utilities
import random_generator
import numpy as np
import os
from sklearn.preprocessing import normalize
import random
import matplotlib.pyplot as plt

if __name__ == '__main__':

	currentPath = os.getcwd()
	oldpath = "../../alllogs/"

	files = utilities.get_all_files(oldpath)

	current_path = os.path.join(currentPath, oldpath)
	count_list = []

	for afile in files:
		print afile
		for individual_files in os.listdir(os.path.join(current_path, afile)):
			# print individual_files
			with open(os.path.join(os.path.join(current_path, afile), individual_files), 'r') as f:
				content = f.readlines()
				count = len(content)
				# print count
				if count > 300:
					print content
					raw_input()
				count_list.append(count)
