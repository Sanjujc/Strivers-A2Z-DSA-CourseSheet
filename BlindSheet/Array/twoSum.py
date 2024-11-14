a = [2,6,8,5,11]
target = 14

hash_map  = {

}

for each in range(0,len(a)):
    diff = target - a[each]
    print(diff)
    if diff not in hash_map:
        hash_map[a[each]] = each
    else:
        print(hash_map[diff],each)
        print(hash_map)
        break

sorted(a)
i = 0
j = len(a) -1
while i < j:
    if a[i] + a[j] == target:
        print('Yes')
        break
    elif a[i] + a[j] > target:
        j -= 1  # Move the right pointer left
    else:
        i += 1  # Move the left pointer right
else:
    print('No')