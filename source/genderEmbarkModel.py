import createModelBase
import numpy as np

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

		#I need to fill in the gaps of the data and make it complete.
		#So where there is no price, I will assume price on median of that class
		#Where there is no age I will give median of all ages

		#All the ages with no data make the median of the data
		train_array[train_array[0::,5] == '',5] = np.median(train_array[train_array[0::,5]\
		                                           != '',5].astype(np.float))
		
		#All missing ebmbarks just make them embark from most common place
		train_array[train_array[0::,11] == '',11] = np.round(np.mean(train_array[train_array[0::,11]\
		                                                   != '',11].astype(np.float)))

		return np.delete(train_array,[0,3,8,10],1) #remove the name data, cabin and ticket

	def createTestModel(self, test_array):
		#I need to convert all strings to integer classifiers:
		#Male = 1, female = 0:
		test_array[test_array[0::,3]=='male',3] = 1
		test_array[test_array[0::,3]=='female',3] = 0
		#ebark c=0, s=1, q=2
		test_array[test_array[0::,10] =='C',10] = 0 #Note this is not ideal, in more complex 3 is not 3 tmes better than 1 than 2 is 2 times better than 1
		test_array[test_array[0::,10] =='S',10] = 1
		test_array[test_array[0::,10] =='Q',10] = 2

		#All the ages with no data make the median of the data
		test_array[test_array[0::,4] == '',4] = np.median(test_array[test_array[0::,4]\
		                                           != '',4].astype(np.float))
		#All missing ebmbarks just make them embark from most common place
		test_array[test_array[0::,10] == '',10] = np.round(np.mean(test_array[test_array[0::,10]\
		                                                   != '',10].astype(np.float)))

		for i in xrange(np.size(test_array[0::,0])):
		    if test_array[i,7] == '':
		    	test_data[i,7] = np.median(test_data[(test_data[0::,7] != '') &\
                                             (test_data[0::,0] == test_data[i,0])\
            ,7].astype(np.float))

		return np.delete(test_array,[2,7,9],1) #remove the name data, cabin and ticket