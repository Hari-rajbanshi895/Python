
f = open('file.txt', 'r')
f.seek(10)
f.tell()
print(f.readline())

with open('file2.txt', 'w') as f:
    f.write("How are you?")

# 
