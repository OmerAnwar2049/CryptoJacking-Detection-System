<<<<<<< HEAD
import yara

def yara_scan(text):
    rules = yara.compile(filepath='./rules.yara')
    matches = rules.match(data = text)
    return matches
=======
import yara

rules = yara.compile(filepath='./rules.yara')
a = "This is my malicious string hash"

matches = rules.match(data = a)

print(matches)
>>>>>>> 3b4c7917bba4e591cce0b690f41906a45a87e6cb
