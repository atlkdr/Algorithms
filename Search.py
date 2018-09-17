import math

#COMAPRISION BASED SEARCHING ALGORITHMS

def linear(arr,el): 
	for i in arr:
		if i==el:
			return True
	return False		

def binary(arr,el,i,j): # Given arr is sorted
	if j>=i:
		mid=i+(j-i)/2
		if arr[mid]==el:
			return True	 
		elif el>arr[mid]:
			return binary(arr,el,mid+1,j) # Continuos Loop if only mid and i==j allowed
		else:
			return binary(arr,el,i,mid-1)
	else:
		return False	

# Complexity Becomes O(root(n))

def Jump(arr,el):	# Given arr is sorted
	step=int(math.sqrt(len(arr)))
	checked_till=0
	previous_till=checked_till
	while(checked_till<(len(arr)-1)):
		if arr[checked_till]==el:
			return True
		if arr[checked_till]>el:
			break
		else:
			previous_till=checked_till
			checked_till+=step
	for i in range(previous_till,checked_till):
		if i < len(arr):
			if arr[i]==el:
				return True		
	return False	


def Exponential(arr,el): # Given arr is sorted
	if arr[0]==el:
		return True
	i=1
	previous_i=i
	while(i<len(arr) and arr[i]<=el):
		if arr[i]==el:
			return True
		previous_i=i
		i=i*2
	return binary(arr,el,previous_i,min(i,len(arr)-1))	

def Interpolationsearch(arr,el):
	low=0
	hi=len(arr)-1
	while( hi>low and x > arr[low] and x < arr[hi] ):
		pos=low+int((float(hi-low)/(arr[hi]-arr[low]))*(x-arr[low]))
		if arr[pos]==el:
			return True
		elif arr[pos]<x:
			low=pos+1
		else:
			hi=pos-1		
	return False