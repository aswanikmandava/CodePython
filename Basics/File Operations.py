# With Open statement performs auto-cleanup of file handle.
# Python closes the file automatically after the block is executed
try:
    with open("test.py", "rU") as fh:
        # file_content = fh.read()  # reads entire file as string
        # print "File content: ", file_content
        # file_line_1 = fh.readline()  # reads first line from a file
        # file_line_3 = fh.readline(3)  # reads 3rd line from a file
        # print "file_line_1:", file_line_1
        # print "file_line_3:", file_line_3
        lines = fh.readlines()  # reads entire file and store as a list of strings
        print("lines:", lines)
        count = 0
        for line in lines:
            count += 1
            print("Line-", count, " ", line)
            words = line.split()  # split the line into a list of words
            print("Words:", words)

except IOError as e:
    print("Exception occurred:", e)
