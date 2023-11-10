fh = open("dummy.txt", "r");

# tell() provides the current position of file pointer
print "Current position of file pointer:", fh.tell()

# readlines() returns file content as a list of lines
fileContent = fh.readlines();
print "Return type of readlines():", type(fileContent)
print "file content:", fileContent
print "Current position of file pointer:", fh.tell()

# seek() takes file pointer to a specific position
# beginning of the file
fh.seek(0, 0)
print "Current position of file pointer:", fh.tell()
print "Reading the file again using read()"

# read() returns file content as a string
fileContent2 = fh.read()
print "Return type of read():", type(fileContent2)
print "file content2:", fileContent2
print "Current position of file pointer:", fh.tell()
fh.close()