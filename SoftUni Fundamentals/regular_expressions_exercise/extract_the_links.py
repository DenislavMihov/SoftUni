import re
pattern = r"(www\.([A-Za-z\d\-]+)(\.[a-z]+)+)"
links = []
while True:
    line = input()

    if not line:
        break

    mathces = re.findall(pattern, line)
    links.extend([m[0] for m in mathces])

for link in links:
    print(link)