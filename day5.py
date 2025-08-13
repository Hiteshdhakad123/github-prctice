x=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
i=2
while(i<10):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
    i=i+1
print(even)
print(odd)