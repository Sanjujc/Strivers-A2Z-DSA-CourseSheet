
a = [0,0,1,1,1,2,2,3,3,4]
largest = a[0]
second_large = -1
for each in range(1,len(a)):
    if each > largest:
        second_large = largest
        largest = a[each]
    elif each == largest and largest>second_large:
        second_large = a[each]
print(second_large)