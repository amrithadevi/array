  um=int(input())
  l=[int(x) for x in input().split()[:num]]
  nlj=[]
  for i in range(0,int(len(l))):
     if(i==l[i]):
         nlj.append(i)
  if(int(len(nlj)))!=0:
        for u in nlj:
            print(u,end=" ")
  else:
      print(-1)
