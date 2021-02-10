
name = 'MOM'
print(name)
print(len(name))
index = (len(name))
reverse_string = ""
while ( index <= 0):
   # print(name[index])
    reverse_string = reverse_string + name[index]
    index = index - 1
print(reverse_string)

if(name == reverse_string):
    print("this is a pallendrom")
