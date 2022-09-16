def add(*args):
    sum= 0
    for i in args:
        sum += i
    return sum
print(add(1,2,3,4,5,6,7,8,9,0))

def hello(**kwargs):
    print("Heello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")


hello(first= "Naman", middle="the grate",last="saini")