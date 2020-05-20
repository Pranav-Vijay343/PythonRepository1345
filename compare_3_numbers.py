while True:
    a = int(input("Enter a number."))
    b = int(input("Enter a second number."))
    c = int(input("Enter a third number."))
    var1 = "This is the largest number:"
    if a>b>c or a>c>b:
        print(var1)
        print(a)
    elif b>c>a or b>a>c:
        print(var1)
        print(b)
    elif c>b>a or c>a>b:
        print(var1)
        print(c)
