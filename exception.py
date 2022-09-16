
try:
    numerator =int(input("no. 1 "))
    denominator = int(input("no.2 "))
    print(numerator/denominator)

except ZeroDivisionError:
    print("no no no")

except ValueError:
    print("only no.")

except Exception:
    print("something went wrong ")

else:
    print("atleat you are smart")

finally:
    print("this will always execute")