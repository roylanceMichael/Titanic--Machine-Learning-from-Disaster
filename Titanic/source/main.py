import sys
import imp
import classify

def main():
	# constant strings
	train_csv_file = 'data/train.csv'
	test_csv_file = 'data/test.csv'

	modelClassName = sys.argv[1]

	# instanced classes we'll need
	utils = imp.load_source('utils', '../Utilities/utils.py')
	util = utils.Utils()
	classifier = classify.Classify()

	# load in the model file, which has a class with createXModel(X_array)
	createModel = imp.load_source('createModel', 'source/' + modelClassName + '.py')
	createModelInst = createModel.CreateModel()

	# create the arrays from the file
	train_array = util.createArrayFromCsvFile(train_csv_file)
	test_array = util.createArrayFromCsvFile(test_csv_file)

	# create the models from our input
	train_model = createModelInst.createTrainModel(train_array)
	test_model = createModelInst.createTestModel(test_array)

	# print models to view
	util.createCsvFileFromArray(train_model, 'models/train_' + modelClassName + '.csv')
	util.createCsvFileFromArray(test_model, 'models/test_' + modelClassName + '.csv')

	# train the classifier
	classifier.train(train_model)

	# predict the test model
	results = classifier.predict(test_model)

	# util out results to view
	util.createCsvFileFromArray(results, 'results/' + modelClassName + '.csv')

if __name__ == '__main__':
	main()