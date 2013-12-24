import sys
import imp
import classify

def main():
	# constant strings
	train_csv_file = 'data/train.csv'
	test_csv_file = 'data/test.csv'

	# util
	utils = imp.load_source('utils', '../Utilities/utils.py')
	util = utils.Utils()
	classifier = classify.Classify()

	# create the arrays from the file
	train_array = util.createArrayFromCsvFile(train_csv_file)
	test_array = util.createArrayFromCsvFile(test_csv_file)

	# train the classifier
	classifier.train(train_array)

	# predict the test model
	results = classifier.predict(test_array)

	# util out results to view
	util.createCsvFileFromArray(results, 'results/digitResults.csv')

if __name__ == '__main__':
	main()