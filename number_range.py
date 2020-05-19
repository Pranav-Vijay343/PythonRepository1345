# var1 = "hello world"
# print(var1)

#a = 55
#b = a*3
#c = a + b
#print(c)

sampleRange = "Sample range: numbers 1-50"
print(sampleRange)
a = 1
print(a)
while a < 50:
    b = a + 1
    print(b)
    a += 1
sequenceFinished = "Numbers 1-50 are listed. Please enter new range."
print(sequenceFinished)
while True:
    c = int(input("Enter minimum number"))
    d = int(input("Enter maximum number"))
    print(c)
    while c < d:
        e = c + 1
        print(e)
        c += 1
