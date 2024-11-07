a = [10,20,30,40,50]
b=[]
for saran in a:
    x=saran*4
    b.append(x)
print(b)

#list comprehension
b=[saran*4 for saran in a]
print(b)
#list comprehension
b=[saran*4 for saran in a if saran >= 30]
print(b)
