# Sorting algorithms implemented in python.

"""
Insertion Sort:
	- Takes elements from an unsorted list and inserting them at the right place in a new sorted list.
	- Sorted list is empty from the start.
	- Total # of elements is the same in new and old list.
"""

def insertion_sort(aList):

	for i in range(1, len(aList)):
		val = aList[i]
		j = i
		whilge (j > 0) and (val < aList[j - 1]):
			aList[j] = aList[j - 1]
			j = j - 1
		aList[j] = val	


def main():
	items = [3, 2, 1, 6, 5]
	print "Before sorting: ", items
	insertion_sort(items)
	print "After sorting:  ", items

main()
