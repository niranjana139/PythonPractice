ch='y'
while ch=='y':
    number=int(input("Enter the number: "))
    if number<0:
        ch='n'
else:
    print("Entered value is negative")

sentence1=input("Say something: ")
words= sentence1.split()
print("Split the sentence into words: ",words)

for word in words:
    print(word)
