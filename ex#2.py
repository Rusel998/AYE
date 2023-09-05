k = (input("WHAT'RE WE DOING RN? (+, -, /, *): "))

a = float(input("FIRSTNUM: "))
b = float(input("SECONDNUM: "))

if k == "+":
    c = a + b
    print("THEANSWERIS: " + str(c))
elif k == "-":
    c = a - b
    print("THEANSWERIS: " + str(c))
elif k == "/":
    c = a / b
    print("THEANSWERIS: " + str(c))
elif k == "*":
    c = a * b
    print("THEANSWERIS: " + str(c))
else:
    print("THEFUCKISWRONGWITHUMONKEY?!")
