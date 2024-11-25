from collections import defaultdict

nums = [1, 2, 4,2]
k = 5
freq = defaultdict(int)
for each in nums:
    freq[each] +=1
max_val = 0
min_val = 0
print(freq)
max_val_fe = {}
for key, value in freq.items():
    max_val =  max(max_val,value)
    min_val =  min(min_val,value)
print(min_val)
print(max_val)
