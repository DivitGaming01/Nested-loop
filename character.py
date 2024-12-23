m=str(input("Enter a Word"))
c=str(input("Enter a Character"))
i=0
count=0
while(i<len(m)):
    if m[i]==c:
        count=count+1
    i=i+1
print(c,count)