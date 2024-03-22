str = input()
upper=0
lower=0
for i in str:
    if i.isalpha():
        if i.isupper():
            upper+=1
        else:
            lower+=1
print("UPPER CASE : ",upper)
print("LOWER CASE : ",lower)