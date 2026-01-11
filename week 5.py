#ทั้วไป
a = 1
b = 4
sum = a+b
minus = a-b
multiply = a*b
divide = a/b


#oop

def SUM(a, b,c):
    sum = int(a)+int(b)+int(c)
    return sum

def MINUS(a, b):
    sum = int(a)-int(b)
    return sum

def MULTIPLY(a, b):
    sum = int(a)*int(b)
    return sum

def DIVIDE(a, b):
    minus = int(a)/int(b)
    return minus

operate = input("1=SUM, 2=MINUS, 3=MULTIPLY, 4=DIVIDE : ")
if(operate == "1"):

    inp1 = input("a : ")
    inp2 = input("b : ")
    inp3 = input("c : ")
    print("SUM =", SUM(int(inp1), int(inp2), int(inp3)))
elif(operate == "2"):
    inp1 = input("a : ")
    inp2 = input("b : ")
    print("MINUS =", MINUS(int(inp1), int(inp2)))
elif(operate == "3"):
    inp1 = input("a : ")
    inp2 = input("b : ")
    print("MULTIPLY =", MULTIPLY(int(inp1), int(inp2)))
elif(operate == "4"):
    inp1 = input("a : ")
    inp2 = input("b : ")
    print("DIVIDE =", DIVIDE(int(inp1), int(inp2)))
else:
    print("not Found")


#print("SUM =", SUM(inp1, inp2, inp3))





#print("SUM =", SUM(int(inp1), int(inp2), int(inp3)))
#print("MINUS =", MINUS(int(inp1), int(inp2)))
#print("MULTIPLY =", MULTIPLY(int(inp1), int(inp2)))
#print("DIVIDE =", DIVIDE(int(inp1), int(inp2)))