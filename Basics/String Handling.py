myStr = "  Hello, my name is Aswani Kumar Mandava   "
# replace comma with exclamation
print myStr.replace(",", "!")
# replace space with # but for 5 occurrences only
print myStr.replace(" ", "#", 5)
print myStr.lower()
# print except first 3 chars
print "***" + myStr[3:] + "***"
# print except last 3 chars
print "***" + myStr[:-3] + "***"
# print first 10 chars
print "***" + myStr[:10] + "***"
# trim leading and trailing white spaces
print myStr.strip()
myStr = myStr.strip()
# find a word in the string
word = "Mandava"
print myStr.find(word)
print "myStr:", myStr + "***"
print myStr.startswith("Hello")
print myStr.endswith("Mandava")

if word in myStr:
    print "Word %s exists" % word

if "Kumar" in myStr:
    print "Kumar exists"
    print "Checking if word %s exists in first 50 chars" % word
    print myStr.find(word,0,50)
else:
    print "Kumar DOES NOT exist"

anotherStr = "msdava-ctwsld01.abc.com:/vol1223.aggr"
fqdn = anotherStr.split(":")
print "List: %s" % fqdn
print "fqdn:", fqdn[0]

# extract short hostname
# set MaxSplit to 1
myList = anotherStr.split(".", 1)
print "myList:", myList
print "shortname:", myList[0]

#

