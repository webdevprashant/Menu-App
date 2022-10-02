import numpy as np
def dsamenu():

	print("""
	Press 1: To Generate random array
	Press 2: To Search data using Linear Search Algorithm 
	Press 3: To Search data using Binary Search Algorithm 
	Press 4: To Sort data using Bubble Sorting Algorithm 
	Press 5: To Sort data using Selection Sorting Algorithm
	""")
def rundsamenu():
	while True:
		print()
		print("Enter Your choice : ", end='')
		userinp = int(input())
		if userinp == 1:
			arrsize = int(input("Enter Array Size : "))
			a = np.random.randint(1, 100, arrsize)
			print(a) 
		elif userinp == 2:
			arrsize = int(input("Enter Array Size : "))
			a = np.random.randint(1, 100, arrsize)
			print(a)
			searchitem = int(input("Enter Search item : "))
			for i in a:
				if i == searchitem:
					print("Found")
					break								
		elif userinp == 3:
			arrsize = int(input("Enter Array Size : "))
			a = np.random.randint(1, 100, arrsize)
			print(a)
			searchitem = int(input("Enter Search item : "))
			start = 0
			end = len(a)-1
			middle = int( (start + end) / 2 )
			while not(a[middle] == searchitem ):
				if a[middle] < searchitem:
					#print("Go Right side")
					start = middle + 1
					middle = int( (start + end ) / 2)
				elif a[middle] > searchitem:
					#print("Go Left Side")
					end = middle - 1
					middle = int ( ( start + end  ) / 2 )
				#print(start , middle , end)
				if a[middle] == searchitem:
						print("Found")
						break
		elif userinp == 4:
			arrsize = int(input("Enter Array Size : "))
			a = np.random.randint(1, 100, arrsize)
			print()
			print()
			print("Unsorted Data ........")
			print(a)
			for i in range(len(a)-1):
				for j in range(len(a) - 1- i):
				    if a[j] > a[j+1]:
				        a[j], a[j+1] = a[j+1] , a[j]
			print(a)
			print("Data Sorted Successfully .........")
			print()
			print()
		elif userinp == 5:
			myindex=0
			arrsize = int(input("Enter Array Size : "))
			a = np.random.randint(1, 100, arrsize)
			print()
			print()
			print("Unsorted Data ........")
			print(a)
			for i in range(len(a)):
				min_index = i
				for j in range(i , len(a)):
					if a[min_index] > a[j]:
						min_index = j
				a[i] , a[min_index] = a[min_index] , a[i]
			print(a)
			print("Data Sorted Successfully ........")
			print()
			print()
