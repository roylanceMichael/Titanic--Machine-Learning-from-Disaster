import numpy as np
import csv as csv
import re
import os

class Utils:
	def createArrayFromCsvFile(self, csvFile):
		csv_file_object = csv.reader(open(csvFile, 'rb'))

		header = csv_file_object.next()

		list_data =[]

		for row in csv_file_object: 
		    list_data.append(row[0:]) 

		return np.array(list_data)

	def createCsvFileFromArray(self, array, fileName):
		open_file_object = csv.writer(open(fileName, "wb"))

		for row in array:
			open_file_object.writerow(row)