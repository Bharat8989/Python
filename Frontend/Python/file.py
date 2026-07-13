file = open('sometext.txt')
print(file.read())

file= open('sometext.txt','w')

# file.write('this is the new text added to the file' )

print(file.write('this is the new text added to the file' ))
file.close()