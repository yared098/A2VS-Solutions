
def avs(r,s):
    v=((r*(s+.16))/.067)**.5
    print(int(tound(v)))
while True:
    try:
        r,s=[float(i) for i in input().split()]
        avs(r,s)
    except EOFError:
        break
