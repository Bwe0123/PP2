def my_generator(u=7):
    for i in range(u):
        if i*i<=u and i!=0:
            yield i*i
e=int(input())
for i in my_generator(e):
    print(i,end=' ')