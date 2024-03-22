s=input().split()
l=[]
for i in s:
    if i not in l:
        l.append(i)
l=sorted(l)
r=' '.join(l)
print(r)