ls=[4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
k=2
for i in range(len(ls)):
    for j in range(len(ls)):
        if(ls[i]<0 or ls[j]<0):
            continue
        if(i==j and j==i):
            continue
        if(ls[i]+ls[j]==k):
            ls[i]=-1
            ls[j]=-1

m=ls.count(-1)
print(int(m/2))
