def my_generator(u=7):
    for i in range(u+1):
        if i%3==0  and i%4==0 and i!=0:
            yield i
t=int(input())
for i in my_generator(t):
    print(i,end=' ')