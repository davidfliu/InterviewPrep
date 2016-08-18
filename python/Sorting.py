# Sorting algorithms implemented in python.

"""
Insertion Sort:
	- Takes elements from an unsorted list and inserting them at the right place in a new sorted list.
	- Sorted list is empty from the start.
	- Total # of elements is the same in new and old list.
Complexity:
	- Best O(n)
	- Average O(n^2)
	- Worst O(n^2)
"""

def insertionSort(aList):

	for i in range(1, len(aList)):
		val = aList[i]
		j = i
		while (j > 0) and (val < aList[j - 1]):
			aList[j] = aList[j - 1]
			j = j - 1
		aList[j] = val

"""
Merge sort:
	- Subdivides list into two sub-lists, sorting them recursively and then merging them back together.
	- Recursive calls subdivide lists down to size 1 (which is already sorted).
Complexity:
	- Best O(n log(n))
	- Average O(n log(n))
	- Worst O(n^2)
"""

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

"""
Quick Sort:
	- Selects a pivot value from list. 
	- Creates two list, one with elements less than pivot and greater than.
	- Sorts two lists and joins them with pivot.
Complexity:
	- Best O(n log(n))
	- Average O(n log(n))
	- Worst O(n^2)
"""
def quickSort(aList):
	if len(aList) > 1:
		pivot_index = len(aList)/2
		smaller_list = []
		bigger_list = []

		for i, val in enumerate(aList):
			if i != pivot_index:
				if val < aList[pivot_index]:
					smaller_list.append(val)
				else:
					bigger_list.append(val)

		quickSort(smaller_list)
		quickSort(bigger_list)
		aList[:] = smaller_list + [aList[pivot_index]] + bigger_list


def main():
	items = [3, 2, 1, 6, 5]
	print "Before sort: ", items
	quickSort(items)
	print "After sort:  ", items



main()
