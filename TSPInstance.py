import sys
from common import euclideanDistance


class TSPInstance:
	def __init__(self):
		self.cities = []
		self.tour = []
		self.tourCost = [] # tourCost[i] is the cost of edge from city i to city i+1
		self.coordinates = []
		self.totalTourCost = 0
		self.distance = {}


	def addCity(self, city, posx, posy):
		self.cities.append(city)
		self.coordinates.append([int(posx), int(posy)])


	def printTour(self):
		try:
			#print 'Basic tour cost is ' + str(self.totalTourCost)
			print "Basic tour is " + str(self.tour) + " and its cost is " + str(self.totalTourCost)
		except IndexError as err:
			print 'ERROR in TSPInstance.printTour()'
			print sys.exc_info()


	def printDistanceMatrix(self):
		print self.distance


	def computeDistances(self):
		try:
			length = len(self.cities)
			for i in range(0, length-1):
				startCity = self.cities[i]
				copy = self.cities[:]
				copy.remove(startCity)
				for endCity in copy:
					edge = startCity + endCity
					cost = euclideanDistance(self.coordinates[i], self.coordinates[i+1])
					self.distance[edge] = cost
			#for
			#self.printDistanceMatrix()

		except IndexError as err:
			print 'ERROR in TSPInstance.computeDistances()'
			print sys.exc_info()


	def basicSolver(self):
		try:
			# basicSolver constructs a tour by visiting adjacent(alphabetically) cities
			length = len(self.cities)
			for i in range(0, length):
				self.tour.append(self.cities[i])
				if i == length - 1:
					key = self.cities[0] + self.cities[i]
				else:
					key = self.cities[i] +  self.cities[i+1]
				distance = self.distance[key]
				self.tourCost.append(distance)
				self.totalTourCost += distance
			#for
			self.tour.append(self.cities[0])

		except IndexError as err:
			print 'ERROR in TSPInstance.basicSolver()'
			print sys.exc_info()
