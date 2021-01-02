import time
import sys

def bubble_sort(data, drawData, timeTick):
	for _ in range(len(data)-1):
		for i in range(len(data)-1):
			if data[i] > data[i+1]:
				data[i], data[i+1] = data[i+1], data[i]
				drawData(data, ['lightgreen' if x == i or x == i+1 else '#3b4249' for x in range(len(data))])
				time.sleep(timeTick)
	drawData(data, ['green' for x in range(len(data))])

def insertion_sort(data, drawData, timeTick):
	for i in range(1,len(data)):
		value = data[i]
		j = i
		while value <= data[j-1] and j != 0:
			drawData(data, ['lightgreen' if x == j else '#3b4249' for x in range(len(data))])
			data[j],data[j-1] = data[j-1],data[j]
			j -= 1
			time.sleep(timeTick)
		drawData(data, ['lightgreen' if x == j else '#3b4249' for x in range(len(data))])
		time.sleep(timeTick)
	drawData(data, ['green' for x in range(len(data))])

def selection_sort(data, drawData, timeTick):
	for i in range(len(data)-1):
		pos = i
		last = sys.maxsize
		for j in range(i+1, len(data)):
			time.sleep(timeTick)
			drawData(data, [('lightyellow' if x == j else ('lightblue' if x == i else '#3b4249')) for x in range(len(data))])
			time.sleep(timeTick)
			if data[j] < data[i] and data[j] < last:
				pos = j
				last = data[j]
				time.sleep(timeTick)
		drawData(data, [('lightgreen' if x == pos else ('lightblue' if x == i else '#3b4249')) for x in range(len(data))])
		time.sleep(timeTick)
		temp = data[i]
		data[i] = data[pos]
		data[pos] = temp
	drawData(data, ['green' for x in range(len(data))])

def merge_sort(data, drawData, timeTick):
	merge_sort_alg(data, 0, len(data)-1, drawData, timeTick)
	drawData(data, ['green' for x in range(len(data))])
	time.sleep(timeTick)

def merge_sort_alg(data, left, right, drawData, timeTick):
	if left >= right:
		return
	middle = (left + right)//2

	merge_sort_alg(data, left, middle, drawData, timeTick)
	merge_sort_alg(data, middle+1, right, drawData, timeTick)
	merge(data, left, middle, right, drawData, timeTick)

def merge(data, left, middle, right, drawData, timeTick):
	drawData(data, ['#3b4249' for x in range(len(data))])
	time.sleep(timeTick)

	leftPart = data[left:middle+1]
	rightPart = data[middle+1:right+1]
	
	leftIdx, rightIdx = 0,0

	for i in range(left, right+1):
		if leftIdx < len(leftPart) and rightIdx < len(rightPart):
			if leftPart[leftIdx] <= rightPart[rightIdx]:
				data[i] = leftPart[leftIdx]
				leftIdx += 1
			else:
				data[i] = rightPart[rightIdx]
				rightIdx += 1
		elif leftIdx < len(leftPart):
			data[i] = leftPart[leftIdx]
			leftIdx += 1
		else:
			data[i] = rightPart[rightIdx]
			rightIdx += 1
		drawData(data, ['lightblue' if x == i else '#3b4249' for x in range(len(data))])
		time.sleep(timeTick)