

word = input("Enter a word:   "  )
print(word)
index = 0
print(len(word))
index = (len(word))
reverse_string = ''

while (index <= 0):
    print(word[index])
    index = index - 1
    reverse_string = reverse_string + word[index]
print(reverse_string)

if(word == reverse_string):
    print("this is a pallendrom")
else:
    print("this is not a pallendrom")
