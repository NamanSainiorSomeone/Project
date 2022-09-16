def loud(text):
    return text.upper()

def quite(text):
    return text.lower()

def hello(func):
    text= func("Hello")
    print(text)

hello(loud)

def devisor(x):
    def dividet(y):
        return y/x
    return dividet


devide = devisor(2)
print (devide(20000))