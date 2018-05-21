from math import exp, factorial
import sys
import random
from itertools import permutations
import numpy as np


# TSPAnnealer
# improves upon an existing TSP tour
class TSPAnnealer():
	def __init__(self, TSPInstance):
		self.tspInstance = TSPInstance

	def printTour(self, schedule):
		print "Annealed Tour cost is " + str(self.tspInstance.totalTourCost)
		print "Final tour is " + str(self.tspInstance.tour) + "\n"

	def anneal(self, annealingSchedule=0.90):
		try:
			finalTour = self.tspInstance.tour
			tourLength = len(finalTour) - 1
			finalTourCost = self.tspInstance.totalTourCost
			random.seed(29898) # seeding our random number generator
			temperature = 100.0
			alpha = annealingSchedule
			terminationValue = 0.0001
			#explorationAffinity = factorial(tourLength) + 1
			#explorationAffinity = min(5041, explorationAffinity)
			explorationAffinity = 10000
			# for num of cities <= 11, the following call generates all subtours
			# for all other values it randomly generates 10000 different subtours
			moveset = self.generateMoveset(finalTour)
			movesetLength = moveset[1]
			moveset = moveset[0]
			k = 0
			while temperature > terminationValue:
				if tourLength >= 11:
					moveset = self.generateMoveset(finalTour)
					movesetLength = moveset[1]
					moveset = moveset[0]
				for tries in range(0, explorationAffinity):
					select = random.randrange(0, movesetLength, 1)
					nextTour = moveset[select]
					nextTourCost = self.cost(nextTour, self.tspInstance.distance)
					delta = nextTourCost - finalTourCost
					if delta > 0:
							# found a worse tour than the current finalTour
							ap = self.acceptanceProbability(delta, temperature)
							if ap > random.random(): # probabilistically accept worse solution
								finalTour = nextTour
								finalTourCost = nextTourCost
					else: # found better tour
						finalTour = nextTour
						finalTourCost = nextTourCost
				#for
				print "(" + str(k)  + ", " + str(temperature) + ")"
				k += 1
				temperature = alpha * temperature
			#while
			self.tspInstance.tour = finalTour
			self.tspInstance.totalTourCost = finalTourCost

		except IndexError as err:
			print 'ERROR in TSPInstance.anneal()'
			print sys.exc_info()


	def acceptanceProbability(self, delta, temperature):
		try:
			value = float(delta) * -1 / temperature
			return exp(value)

		except TypeError as err:
			print 'ERROR in TSPAnnealer.acceptanceProbability()'
			print sys.exc_info()


	# generateMoveset
	# returns a list of 2-tuples where each tuple contains the edges to swap while
	# preserving the tour
	# currentTour is an ordered list of cities where for each (i,i+1), city i is the
	# and city i+1 is the end of one leg of the tour
	def generateMoveset(self, currentTour):
		try:
			subTourLength = len(currentTour) - 2
			tour = currentTour[1:subTourLength+1] # remove city 'A' from the tour
			solutionsTuple = self.generateNeighbourSet(tour, subTourLength) # reorder the sequnce in which intermediary cities are visited
			return solutionsTuple

		except IndexError as err:
			print 'ERROR in TSPAnnealer.generateMoveset()'
			print sys.exc_info()

	# generateNeighbourSet
	# input: a list of intermediary cities in a tour
	# output: a list of lists where each element is a reording of the sequence of
	# intermediary cities
	def generateNeighbourSet(self, intermediaryCities, numCities=11):
		try:
			alternateTours = {}
			length = 0
			if numCities < 11:
				# deterministic permutation generator
				for alternateTour in permutations(intermediaryCities):
					alternateTour = list(alternateTour)
					alternateTour.insert(0, 'A')
					alternateTour.append('A')
					alternateTours[length] = alternateTour
					length += 1
			else:
				# randomized permutation generator
				limit = 10000
				for i in range(0, limit + 1):
					alternateTour = np.random.permutation(intermediaryCities)
					alternateTour = list(alternateTour)
					alternateTour.insert(0, 'A')
					alternateTour.append('A')
					alternateTours[i] = alternateTour
			return [alternateTours, limit]

		except IndexError as err:
			print 'ERROR in TSPAnnealer.generateNeighbourSet()'
			print sys.exc_info()


	def cost(self, tour, distMatrix):
		try:
			tourCost = 0
			edges = distMatrix.keys()
			for i in range(0, len(tour) - 1):
				startCity = tour[i]
				endCity = tour[i+1]
				edge = startCity + endCity
				if edge not in edges:
					 edge = endCity + startCity
				tourCost += distMatrix[edge]
			#for
			return tourCost

		except IndexError as err:
			print 'ERROR in TSPAnnealer.cost()'
			print sys.exc_info()
