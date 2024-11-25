from collections import defaultdict
arr = [4,1,2,3,1,2,3,4,1,4,2,4,1]
freq  = defaultdict(int)
for each in arr:
    freq[each] +=1
print(freq)

print(freq[3])