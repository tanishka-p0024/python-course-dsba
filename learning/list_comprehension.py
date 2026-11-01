# comprehension = [function,loop,filter if any]

domains = ['www.google.com','localhost','WWW.AMAZON.IN','openai.com']

cleaned = [
    d.lower().replace('www.','')
    for d in domains
    if '.' in d
]
print(cleaned)