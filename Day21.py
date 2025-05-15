# Files IO in python:

# f = open("myfile.txt",'w') #Write method
# f.write("Hello World!")
# f.close()

# with open("myfile.txt",'a') as f: #Append method
#     f.write("Good Morning!")
    
# with open("myfile.txt",'r') as f: #Read method
#     text = f.read()
#     print(text)

#Readline method

# f = open('myfile.txt', 'r')
# i = 0
# while True:  
#     line = f.readline()
#     if not line:
#         break
#     i = i + 1
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1].strip()
#     m3 = line.split(",")[2].strip()
#     print(f"Marks of student {i} in math is: {m1}")
#     print(f"Marks of student {i} in english is:  {m2}")
#     print(f"Marks of student {i} in nepali is: {m3}")
#     print(line)
    
# writeline method
f = open('myfile1.txt','w')

lines = ['line1\n','line2\n','line3\n','line4\n']
f.writelines(lines)
f.close()