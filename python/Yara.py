import yara

rules = yara.compile(filepath='./rules.yara')
a = "This is my malicious string hash"

matches = rules.match(data = a)

print(matches)