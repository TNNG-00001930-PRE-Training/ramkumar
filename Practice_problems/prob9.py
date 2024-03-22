import re

passwords = input().split(',')
result = []
for password in passwords:
	if(len(password) >= 6 and len(password) <= 12):
		if re.search("[a-z]", password) and re.search("[A-Z]", password) and re.search("[0-9]", password) and re.search("[$#@]", password):
			result.append(password)

print(','.join(result))
