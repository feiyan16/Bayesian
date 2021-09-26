from NaiveBayes import NaiveBayes
from Test import Test
import sys

n = len(sys.argv)
if n == 1:
    print("Please enter training data and test data file along with python file")
    quit()
elif n == 2:
    print("Please enter BOTH training data and test data file")
    quit()
elif n == 3:
    training_file = sys.argv[1]
    test_file = sys.argv[2]
    bayes = NaiveBayes(training_file)
    test_1 = Test("training", training_file, bayes)
    test_1.run_test()
    test_2 = Test("test", test_file, bayes)
    test_2.run_test()
