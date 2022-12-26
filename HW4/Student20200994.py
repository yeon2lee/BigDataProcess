import sys
import os
import numpy as np
import operator 

def create_data_set(training_dir):
	labels = []
	file_list = os.listdir(training_dir)
	data = []
	index = 0
	for file_name in file_list:
		file = training_dir + "/" + file_name 
		data_label_id = file_name.split('_')
		labels.append(int(data_label_id[0]))
		with open(file) as fp:
			tmp_data = []
			for line in fp:
				for word in line:
					if word != '\n':
						tmp_data.append(int(word))
			data.append(tmp_data)

	group = np.array(data)

	return group, labels
 	


def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis = 1)
	distances = sqDistances ** 0.5
	sortedDistIndicies = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
	sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
	return sortedClassCount[0][0]


if __name__ == "__main__":
	training_dir = sys.argv[1]
	test_dir = sys.argv[2]

	dataSet, labels = create_data_set(training_dir)

	file_list = os.listdir(test_dir)
	total_count = len(file_list)

	for i in range(1, 21):
		count = 0

		for file_name in file_list:
			file = test_dir + "/" + file_name
			data_label_id = file_name.split('_')	
			correct = int(data_label_id[0])
		
			tmp_data = []
			with open(file) as fp:
				for line in fp:
					for word in line:
						if word != '\n':
							tmp_data.append(int(word))	

				inX = np.array(tmp_data)
				answer = classify0(inX, dataSet, labels, i)
				if answer != correct:
					count += 1

		error = round(count / total_count * 100)
		print(error)

