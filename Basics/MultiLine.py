"""
This is a doc string or multi-line comment
Provides description about the script
Some notes about the script function
"""

# implicit continuation for (), {}, []
# Using a backslash character for line continuation is unnecessary
myList = ["Item-1",
          "Item-2",
          "Item-3",
          "Item-4"]
# Number of items
print(len(myList))

myMultiLineStr = """
This is line-1
This is line-2
This is line-3
"""
print(myMultiLineStr)

myWebSite = "Google"
myWebSiteLoginUser = "guest"
myWebSiteLoginUserPwd = "guest"
# backslash character to breakdown expression in multiple lines
myWebSiteStr = myWebSite + \
               myWebSiteLoginUser + \
               myWebSiteLoginUserPwd
print(myWebSiteStr)

# string formatting
print("I visited %s with username:%s and pwd:%s" % (myWebSite, myWebSiteLoginUser, myWebSiteLoginUserPwd))
