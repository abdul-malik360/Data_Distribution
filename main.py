# import to calculate mean and median
import numpy
# import to calculate mode
import scipy
from scipy import stats
marks_of_students = [90, 72, 82, 90, 69, 19, 23, 30, 45, 5]
my_mean = numpy.mean(marks_of_students)
my_median = numpy.median(marks_of_students)
my_mode = stats.mode(marks_of_students)
my_range = numpy.ptp(marks_of_students)
my_quartile_range = numpy.percentile(marks_of_students, 25)
my_variance = numpy.var(marks_of_students)


print("The mean of the student's marks is:", my_mean)
print("The median of the student's marks is:", my_median)
print("The mode of the student's marks is:", my_mode)
print("The range of the student's marks is:", my_range)
print("The variance of the student's marks is:", my_variance)
