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
	
	for afile in files:
		print afile
		with open(os.path.join(current_path, afile), 'r') as f:
			content = f.readlines()
			count = 0
			for line in content:
				count += 1
			print count