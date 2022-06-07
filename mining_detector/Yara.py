import yara

def yara_scan(text):
    rules = yara.compile(filepath='E:\\Malware\\CryptoJacking-Detection-System\\static_analysis\\rules.yara')
    matches = rules.match(data = text)
    return matches

# print(yara_scan("mining--nicehash"))