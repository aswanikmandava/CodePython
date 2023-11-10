# search(pattern, string, flag)
# pattern - regex
# string - match string
# flag - re.DOTALL, re.IGNORECASE, re.MULTILINE

# To syntax check - compile a python script
# python -m py_compile examples.py

import re

# match_str = 'Typed on HP Spectre laptop'
# result = re.search(r'\s\w+\s', match_str)
# if result:
#     print 'Found:-', result.group()
# else:
#     print 'No match found'
#
# # search() returns first match string using regex
# # findall() returns all matching strings using regex
#
# results = re.findall(r'\s\w+\s', match_str)
# for m_str in results:
#     print 'MATCHED:-', m_str

# match_section = '''Google News is a news aggregator and app developed by Google.
# It presents a continuous, customizable flow of articles organized from thousands of publishers and magazines.
# Google News is available on Android, iOS, and the web.
# A beta version was launched in September 2002, and released officially in January 2006'''
#
# # dot character matches all characters except new line - To match new line, use DOTALL flag
# # space character matches white space, tab, new line
# result = re.search(r'.*', match_section)
# print 'Found:-', result.group()
#
# # regex is case-sensitive - To ignore case, use IGNORECASE flag
# result = re.search(r'\snews\s', match_section)
# print 'Found:-', result.group()
# result = re.search(r'\snews\s', match_section, re.IGNORECASE)
# print 'Found:-', result.group()
#
# result = re.findall(r'^Google', match_section, re.MULTILINE)
# for line in result:
#     print 'Found:-', line

# \w matches a word character that includes a-z, A-Z, 0-9 and underscore
# \W matches a non-word character
line = 'my email is aswani.k.mandava@gmail.com and my mobile no is (856) 229-6536'
my_email = re.search(r'([\w.?]+)@([\w.]+)', line)
my_mobile = re.search(r'\([0-9]{3}\)\s[0-9]{3}\-[0-9]{4}', line)
if my_email:
    print 'Email:', my_email.group()
    print 'Email user:', my_email.group(1)
    print 'Email domain:', my_email.group(2)
else:
    print 'Cannot extract email'
if my_mobile:
    print 'Mobile:', my_mobile.group()
else:
    print 'Cannot extract mobile no'



