n=int(input("enter the number"))
for i in range(2,n+1):
    if i>1:
        for j in range(2,i):
           if i%j==0:
               break
        else:
            if n%i==0:
                print(i)