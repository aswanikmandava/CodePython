import os


# modContent = dir(os)
#
# for item in modContent:
#     print item


# rename dummy.txt to dummyfile.txt
os.rename("dummyfile.txt", "dummy.txt")

# remove file
os.remove("dummy.txt")