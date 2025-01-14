import sys      

n,m = map(int,input().split())

arr = list(map(int,sys.stdin.readline().rstrip().split()))

start = 0 
end = max(arr)          # arr의 최대값

result = 0

while (start <= end):
    total = 0
    mid = int((start + end)/2)

    for x in arr:
        if x > mid:
            total += x - mid
            
        print(total)
        if total < m:
            end = mid -1
        else:
            result = mid
            start = mid + 1
            
print(result)
        