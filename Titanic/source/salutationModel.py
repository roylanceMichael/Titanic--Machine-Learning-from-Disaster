import createModelBase
import numpy as np
import re

class CreateModel(createModelBase.CreateModelBase):

	def createTrainModel(self, train_array):
		#I need to convert all strings to integer classifiers:
		#Male = 1, female = 0:
		train_array[train_array[0::,4]=='male',4] = 1
		train_array[train_array[0::,4]=='female',4] = 0
		#embark c=0, s=1, q=2
		train_array[train_array[0::,11] =='C',11] = 0
		train_array[train_array[0::,11] =='S',11] = 1
		train_array[train_array[0::,11] =='Q',11] = 2

		for row in train_array:
			nameCell = row[3].lower()

			# Mr. Master. defaulting to 0
			# Miss. Mrs. defaulting to 1
			if re.match('mr\.', nameCell) and row[2] == 1: 
				row[3] = 0
			elif re.match('master', nameCell) and row[2] == 1:
				row[3] = 1
			elif re.match('miss', nameCell) and row[2] == 1:
				row[3] = 2
			elif re.match('mrs\.', nameCell) and row[2] == 1:
				row[3] = 3
			if re.match('mr\.', nameCell) and row[2] == 2: 
				row[3] = 4
			elif re.match('master', nameCell) and row[2] == 2:
				row[3] = 5
			elif re.match('miss', nameCell) and row[2] == 2:
				row[3] = 6
			elif re.match('mrs\.', nameCell) and row[2] == 2:
				row[3] = 7
			if re.match('mr\.', nameCell) and row[2] == 3: 
				row[3] = 8
			elif re.match('master', nameCell) and row[2] == 3:
				row[3] = 9
			elif re.match('miss', nameCell) and row[2] == 3:
				row[3] = 10
			elif re.match('mrs\.', nameCell) and row[2] == 3:
				row[3] = 11
			else:
				row[3] = 12


		#I need to fill in the gaps of the data and make it complete.
		#So where there is no price, I will assume price on median of that class
		#Where there is no age I will give median of all ages

		#All the ages with no data make the median of the data
		train_array[train_array[0::,5] == '',5] = np.median(train_array[train_array[0::,5]\
		                                           != '',5].astype(np.float))
		
		#All missing ebmbarks just make them embark from most common place
		train_array[train_array[0::,11] == '',11] = np.round(np.mean(train_array[train_array[0::,11]\
		                                                   != '',11].astype(np.float)))

		return np.delete(train_array,[0,8,10],1) #remove the name data, cabin and ticket

	def createTestModel(self, test_array):
		#I need to convert all strings to integer classifiers:
		#Male = 1, female = 0:
		test_array[test_array[0::,3]=='male',3] = 1
		test_array[test_array[0::,3]=='female',3] = 0
		#ebark c=0, s=1, q=2
		test_array[test_array[0::,10] =='C',10] = 0 #Note this is not ideal, in more complex 3 is not 3 tmes better than 1 than 2 is 2 times better than 1
		test_array[test_array[0::,10] =='S',10] = 1
		test_array[test_array[0::,10] =='Q',10] = 2

		for row in test_array:
			nameCell = row[3].lower()
			#row[2] = int(row[2])
			# Mr. Master. defaulting to 0
			# Miss. Mrs. defaulting to 1

			if re.match('mr\.', nameCell) and row[1] == 1: 
				row[2] = 0
			elif re.match('master', nameCell) and row[1] == 1:
				row[2] = 1
			elif re.match('miss', nameCell) and row[1] == 1:
				row[2] = 2
			elif re.match('mrs\.', nameCell) and row[1] == 1:
				row[2] = 3
			if re.match('mr\.', nameCell) and row[1] == 2: 
				row[2] = 4
			elif re.match('master', nameCell) and row[1] == 2:
				row[2] = 5
			elif re.match('miss', nameCell) and row[1] == 2:
				row[2] = 6
			elif re.match('mrs\.', nameCell) and row[1] == 2:
				row[2] = 7
			if re.match('mr\.', nameCell) and row[1] == 3: 
				row[2] = 8
			elif re.match('master', nameCell) and row[1] == 3:
				row[2] = 9
			elif re.match('miss', nameCell) and row[1] == 3:
				row[2] = 10
			elif re.match('mrs\.', nameCell) and row[1] == 3:
				row[2] = 11
			else:
				row[2] = 12

		#All the ages with no data make the median of the data
		test_array[test_array[0::,4] == '',4] = np.median(test_array[test_array[0::,4]\
		                                           != '',4].astype(np.float))
		#All missing embarks just make them embark from most common place
		test_array[test_array[0::,10] == '',10] = np.round(np.mean(test_array[test_array[0::,10]\
		                                                   != '',10].astype(np.float)))

		for i in xrange(np.size(test_array[0::,0])):
		    if test_array[i,8] == '':
		    	test_array[i,8] = 0

		return np.delete(test_array,[7,9],1) #remove the name data, cabin and ticket