#! /usr/bin/python3
# encoding=utf8

import time

class sortMethod(object):
	"""docstring for sortMethod"""
	def __init__(self):
		super(sortMethod, self).__init__()


	def bubbleSort(self, string):
		"""
		docstring for bubble.
		:param string: a list.
		:return: a sorted list.
		"""

		length = len(string)

		if (length <= 1):
			return string

		for i in range(length):
			for j in range(length-i-1):
				if (string[j] > string[j+1]):
					string[j], string[j+1] = string[j+1], string[j]
				else:
					pass

		return string

	def selectSort(self, string):
		"""
		docstring for select.
		:param string: a list.
		:return: a sorted list.
		"""

		length = len(string)

		if (length <= 1):
			return string

		for i in range(length):
			temp = i
			for j in range(length)[i+1: ]:
				if string[j] < string[temp]:
					temp = j

			if temp == i:
				pass
			else:
				string[i], string[temp] = string[temp], string[i]

		return string

	def insertSort(self, string):
		"""
		docstring for select.
		:param string: a list.
		:return: a sorted list.
		"""

		length = len(string)

		if (length <= 1):
			return string

	def shellSort(self, string):
		"""
		docstring for select.
		:param string: a list.
		:return: a sorted list.
		"""

		length = len(string)

		if (length <= 1):
			return string

	def mergeSort(self, string):
		"""
		docstring for select.
		:param string: a list.
		:return: a sorted list.
		"""

		length = len(string)

		if (length <= 1):
			return string

	def quickSort(self, string):
		"""
		docstring for select.
		:param string: a list.
		:return: a sorted list.
		"""
		def quick(string, start, end):
			if start < end:
				i = start
				j = end
				base = string[i]

				while(i < j):
					while (i < j) and (string[j] >= base):
						j -= 1
					string[i] = string[j]

					while (i < j) and (string[i] <= base):
						i += 1
					string[j] = string[i]

				string[i] = base

				quick(string, start, i - 1)
				quick(string, j + 1, end)

			return string

		quick(string, 0, len(string) - 1)

	def heapSort(self, string):
		"""
		docstring for select.
		:param string: a list.
		:return: a sorted list.
		"""

		length = len(string)

		if (length <= 1):
			return string

	def countingSort(self, string):
		"""
		docstring for select.
		:param string: a list.
		:return: a sorted list.
		"""

		length = len(string)

		if (length <= 1):
			return string

	def bucketSort(self, string):
		"""
		docstring for select.
		:param string: a list.
		:return: a sorted list.
		"""

		length = len(string)

		if (length <= 1):
			return string

	def radixSort(self, string):
		"""
		docstring for select.
		:param string: a list.
		:return: a sorted list.
		"""

		length = len(string)

		if (length <= 1):
			return string


def main():
	sortMethodInstance = sortMethod()

	a = [1, 4, 6, 7, 6, 6, 7, 6, 8, 6]

	# Bubble
	print(a)
	startTime = time.time()
	print(sortMethodInstance.bubbleSort(a))
	endTime = time.time()
	print(endTime - startTime)

	a = [1, 4, 6, 7, 6, 6, 7, 6, 8, 6]

	# Select
	print(a)
	startTime = time.time()
	print(sortMethodInstance.selectSort(a))
	endTime = time.time()
	print(endTime - startTime)

	a = [1, 4, 6, 7, 6, 6, 7, 6, 8, 6]

	# Quick
	print(a)
	startTime = time.time()
	sortMethodInstance.quickSort(a)
	print(a)
	endTime = time.time()
	print(endTime - startTime)


if __name__ == '__main__':
	main()
