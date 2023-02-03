class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n=int(len(changed)/2)
        ls=changed[:n]
        ls2=changed[n:]
        flag=True
        ls3=[]
        for i in range(len(ls)):
            if(2*ls[i]==ls2[i]):
                continue
            else:
                flag=False
        if(flag==True):
            return ls
        else:
            return ls3

        