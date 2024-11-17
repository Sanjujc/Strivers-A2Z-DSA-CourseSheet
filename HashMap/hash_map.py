a = [2,4,5,6,7]
target = 9
lower =  0
upper =len(a)-1
while lower < upper:
	mid =  (lower+upper) //2
	if target == a[mid]:
		print('Element found at position',mid)
		break
	elif target > a[mid]:
		lower = mid + 1  # Move the lower bound up since the target is greater than mid element
	else:
		upper = mid - 1
else:
	print('Element not found')

