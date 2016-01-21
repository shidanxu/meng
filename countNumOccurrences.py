import utilities
import random_generator
import numpy as np
import os
from sklearn.preprocessing import normalize
import random
import matplotlib.pyplot as plt
import features

if __name__ == '__main__':

	currentPath = os.getcwd() + "../../"
	oldpath = "../../alllogs"

	files = get_all_files(oldpath)
	
	for afile in files:
		print afile
		with open(os.path.join(current_path, afile), 'r') as f:
			content = f.readlines()
			count = 0
			for line in content:
				count += 1
			print count