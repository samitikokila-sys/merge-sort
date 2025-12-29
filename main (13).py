def mergetwosortedarray(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    l=r=0
    out=[]
    while l<n1 and r<n2:
        if arr1[l]<=arr2[r]:
            out.append(arr1[l])
            l+=1
        else:
            out.append(arr2[r])
            r+=1
    while l<n1:
        out.append(arr1[l])
        l+=1
    while r<n2:
        out.append(arr2[r])
        r+=1
    return out
arr1=[1,7,9,15,26]
arr2=[16,19,24,27,45]
print(mergetwosortedarray(arr1,arr2))

    