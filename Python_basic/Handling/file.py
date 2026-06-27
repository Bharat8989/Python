# r mode (read)- existing file read karto
file =open("student.txt", "r")
data =file.read()
print(data)
# print(file)
# file.close()
#w mode (write) - navin file create karto
file=open("student.txt","w")
file.write("hello python")
# file.close()

#a mode (append ) - existing file madhye navin data add karto
file=open("student.txt","a")
file.write("\nNew student")
file.close()

# x mode (cerate)- only new file create karto

try:
    file=open("newfile.txt","x")
    print("file created successfully")
except Exception as err:
    print(f"file already existing {err}")
finally:
    if 'file' in locals():
        file.close()
        print("file closed")


file.close()