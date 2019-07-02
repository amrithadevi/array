    def gcd(a,b):
    i=1
    while(i <= a and i <= b):
        if(a % i == 0 and b % i == 0):
            gcd = i
        i = i + 1
    return(gcd)
        l=[]
        x,y=input().split()
        x=int(x)
        y=int(y)
        n=list(map(int,input().split()))
         v=[]
  for j in range(y):
    h, j = input().split()
    h = int(h)
    j = int(j)
    v.append(gcd(n[h-1],n[j-1]))
 k=len(v)
  for i in range(k):
    print(v[i])
