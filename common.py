import sys
from math import sqrt

def euclideanDistance(coordinateTuple1, coordinateTuple2):
	try:
		xDiff = coordinateTuple1[0] - coordinateTuple2[0]
		yDiff = coordinateTuple1[1] - coordinateTuple2[1]
		return int(sqrt((xDiff * xDiff) + (yDiff * yDiff)))

	except IndexError as err:
		print 'ERROR in euclideanDistance'
		print sys.exc_info()
