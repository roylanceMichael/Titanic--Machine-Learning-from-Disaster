import csv as csv
import imp

utils = imp.load_source('utils', '../Utilities/utils.py')
util = utils.Utils()

csvArray = util.createArrayFromCsvFile('weka_train.csv')

