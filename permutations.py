from itertools import permutations


def main():

	string = 'ABCDEFGHIJK'
	length = 0
	alternateTours = {}
	limit = 6000000
	for alternateTour in permutations(string):
		alternateTours[length] = list(alternateTour)
		#print alternateTour
		length += 1
		if length == limit:
			break
	print length


if __name__ == '__main__':
	main()
