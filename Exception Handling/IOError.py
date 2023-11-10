# catch file related exceptions
try:
    # opening a non-existing file
    fh = open("nofile.txt", "r")
    # read first 10 bytes
    print fh.read(10)
    fh.close()
except IOError:
    print "Cannot read file"