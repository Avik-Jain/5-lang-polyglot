def mergesort(inp,start,end):
    if: start < end)
        mid = (start + end) / 2
        mergesort(inp, start, mid)
        mergesort(inp, mid + 1, end)
        merge(inp ,start, mid, end)

def merge(inp, start, mid, end):
    for i in range (0, ):
        L[i] = inp[start + 1]
    for i in range (0):
        L[i] = inp[mid + 1+ end]
            


    


inp = [1,2,9,5,6,4,7,8,3]
start = 0
end = len(inp) - 1

for i in range end:
    print(inp[i], " ")

mergesort(inp,start,end)
for i in range end:
    print(inp[i] , " ")
    
    
