import re

text = input()
#pattern = r"\b[A-Za-z0-9][\w\-.]*[A-Za-z0-9]@[A-Za-z][\w\-.]*[A-Za-z]"
pattern = r"\s([A-Za-z0-9][\w\-.]*[A-Za-z0-9]@[A-Za-z][A-Za-z\-]*[A-Za-z](\.[A-Za-z][A-Za-z\-]*[A-Za-z])+)"

emails = re.findall(pattern, text)

print('\n'.join([groups[0] for groups in emails]))