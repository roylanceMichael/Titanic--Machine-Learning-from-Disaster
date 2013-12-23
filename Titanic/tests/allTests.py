import imp
import unittest
util = imp.load_source('util', 'source/util.py')


class UtilsTest(unittest.TestCase):
	def test_returnArrayFromCsvFile(self):
		# arrange
		train_csv_file = "tests/csvTestFile.csv"
		utils = util.Util()

		# act
		array = utils.createArrayFromCsvFile(train_csv_file)
		
		# assert
		self.assertTrue(len(array) == 2, len(array))

def main():
	unittest.main()

if __name__ == '__main__':
	main()