import re
pattern = 'a...s$'
#test_string = 'abyss'
#test_string = 'byss'
test_string = 'abacus'
result = re.match (pattern, test_string)
if result:
    print("Search Successful.")
else:
    print("Search Unsuccessful.")

#Search Unsuccessful.

import re
pat='b|h+a|i|u+t'
txt=input("enter any text")
result=re.match(pat,txt)
if result:
    print("yes")
else:
    print("no")

'''
enter any textbut
yes
'''

import re
pat='[A-Za-z-]+[A-Za-z-]+'
txt=input("enter any text")
result=re.match(pat,txt)
if result:
    print("yes")
else:
    print("no")

'''
enter any text
Kanishk Singhania
yes
'''