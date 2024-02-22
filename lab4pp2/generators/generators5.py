def my_generator(u):
    for i in range(u):
        yield i
t=int(input())
e=[]
for i in my_generator(t+1):
    e.append(i)
print(e[::-1])