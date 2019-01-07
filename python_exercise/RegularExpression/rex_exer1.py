import re

data = """
park 800905-1049118
kim 700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******",data))

# Meta characters in Rex
# . ^ $ * + ? { } [ ] \ | ( )


p = re.compile('[a-z]+')

m = p.match("python")
print(m)

# m = p.match("3 python")
# print(m)

m.group()
print(m)


p = re.compile("^python\s\w+",re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))


p = re.compile("[a-z]+")
m = p.search("5 python")
m.start() + m.end()


p = re.compile("a[.]{3,}b")
m = p.match("a....b")
print(m)
