def findOriginalArray(changed):
    n=int(len(changed)/2)
    ls=changed[:n]
    ls2=changed[n:]
    ls3=[]
    for i in range(len(ls)):
        if(ls[i]==2*ls2[i]):
            print(ls[i],end="")
        
print(findOriginalArray([1,3,4,2,6,8]))
