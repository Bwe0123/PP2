def my_generator(u,t):
    for i in range(u,t+1):
        yield i*i
t=int(input())
y=int(input())
for i in my_generator(t,y):
    print(i,end=' ')