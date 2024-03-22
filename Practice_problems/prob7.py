start=1000
end=3000
result=[]
for i in range(start,end+1):
    even = True
    for digit in str(i):
        if int(digit) % 2 != 0:
            even = False
            break
    if even:
        result.append(str(i))

print(','.join(result))