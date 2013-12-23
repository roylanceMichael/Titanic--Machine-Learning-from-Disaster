from abc import ABCMeta, abstractmethod

class CreateModelBase(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def createTrainModel(self, train_array):
		pass

	@abstractmethod
	def createTestModel(self, test_array):
		pass