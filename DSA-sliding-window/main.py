arr = [5,2,-1,0,3]
k = 3
print(arr)

max_sum = 0
for i in range(k):
    max_sum += arr[i]

window_sum = max_sum
for i in range(k,len(arr)):
    window_sum += arr[i] - arr[k-i]
    max_sum = max(window_sum,max_sum)

print(max_sum,window_sum)