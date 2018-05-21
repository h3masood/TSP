import sys
from copy import deepcopy
from TSPInstance import TSPInstance
from TSPAnnealer import TSPAnnealer

def main():
	problemDir = "./randTSP/11/"
	instance36 = "./randTSP/problem36"
	j = 0
	schedules = [0.80]
	#schedules = [0.90, 0.85, 0.80]
	findings = {}
	for i in range(1, 2):
		src = "instance_" + str(i)
		findings[src] = []
		problemFile = problemDir +  src + ".txt"
		problemInstance = open(instance36, 'r')
		tspInstance = TSPInstance()
		for line in problemInstance:
			tokens = line.split()
			if len(tokens) == 1:
				continue # ignore input size
			tspInstance.addCity(tokens[0], tokens[1], tokens[2])
		tspInstance.computeDistances()
		tspInstance.basicSolver()
		basicTourCost = tspInstance.totalTourCost
		for schedule in schedules:
			print "Schedule used = " + str(schedule)
			instanceCopy = deepcopy(tspInstance)
			tspAnnealer = TSPAnnealer(instanceCopy)
			tspAnnealer.anneal(schedule)
			annealedCost = tspAnnealer.tspInstance.totalTourCost
			tour = tspAnnealer.tspInstance.tour
			data = [schedule, basicTourCost, annealedCost, tour]
			findings[src].append(data)
		#for
	#for
	print findings
	'''
	for i in range(1,2):
		instance = "problem36" +  str(i)
		dataList = findings[instance]
		for data in dataList:
			print("problem36" + " | " + str(data[0]) + " | " + str(data[1]) + " | " + str(data[2]))
	'''

if __name__ == "__main__":
	main()
