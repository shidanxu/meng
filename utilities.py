# 1. Parse a file to get a list of states [0, 1, 2, 2, 2, 1, ... ,0]

# 2. Parse all files to generate the markov matrix transition probabilities

# 3. Generate data from the Markov matrix

# 4. Compare and contrast results
import random_generator
import numpy as np
import os
from sklearn.preprocessing import normalize

def statesToPeriod(states, timePeriod = 15):
	lengthPeriods = 24*60 / timePeriod
	# print lengthPeriods
	periods = [1]*lengthPeriods
	


	for eachTuple in states:
		time, state, ip = eachTuple
		periods[timeToIndex(time)] = state
	
	# print periods
	return periods

def timeToIndex(datetimeObj, timePeriod = 15):
	assert 60 / timePeriod
	return datetimeObj.hour * 60 / timePeriod + datetimeObj.minute / timePeriod

def computeTransitionMatrix(periods, states = 3):
	transitionMatrix = []
	for jj in range(states):
		transitionMatrix.append([0]*states)
	# print transitionMatrix

	for i in range(len(periods) - 1):
		begin = periods[i] - 1
		end = periods[i+1] - 1
		# print begin, end

		transitionMatrix[begin][end] += 1

		# print transitionMatrix
	assert sum([sum(item) for item in transitionMatrix]) == len(periods) - 1

	# print np.matrix(transitionMatrix)
	return np.matrix(transitionMatrix)

def computeProbabilityMatrix(transitionMatrix):
	normed_matrix = normalize(transitionMatrix.astype(float), axis=1, norm='l1')
	# print normed_matrix
	return normed_matrix

def generateDataFromMarkovMatrix(markovMatrix):
	return

if __name__ == '__main__':
	totalTransitionMatrix = np.matrix([[0,0,0], [0,0,0], [0,0,0]])
	# for files in os.listdir("fakeData"):

	basepath = '../../alllogs/'
	for files in os.listdir(basepath):
		path = os.path.join(basepath, files)
		if os.path.isdir(path):
			for logFile in os.listdir(path):
				states = random_generator.parseEntry(path, logFile)
				# print states

				periods = statesToPeriod(states)
				transitionMatrix = computeTransitionMatrix(periods)

				totalTransitionMatrix = totalTransitionMatrix + transitionMatrix
				print totalTransitionMatrix
				
	print totalTransitionMatrix
	normed_matrix = computeProbabilityMatrix(totalTransitionMatrix)
	print normed_matrix