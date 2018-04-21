# regex: Regular expression library
import re

# Replacing all the upper case letters with ''
string = "'I AM NOT YELLING', she said. Though we knew it to not be true."
new = re.sub('[A-Z]', '', string)
print(new)  # '   ', she said. hough we knew it to not be true.

# Replacing all the lower case letters with ''
new = re.sub('[a-z]', '', string)
print(new)  # 'I AM NOT YELLING',  . T       .

# Replacing .,\' (punctuations) with ''
new = re.sub('[.,\']', '', string)
print(new)  # I AM NOT YELLING she said Though we knew it to not be true

# Replacing all the lower case letters and punctuations with ''
new = re.sub('[.,\'a-z]', '', string)
print(new)  # I AM NOT YELLING   T

# Replacing all lower case letters,punctuations and whitespace with ''
new = re.sub('[.,\'a-z+" "]', '', string)
print(new)  # IAMNOTYELLINGT

# Replacing all the characters except digits 0-9 with ''
string = string + "132324"
new = re.sub('[^0-9]', '', string)
print(new)  # 132324