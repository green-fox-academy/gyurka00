ag= 'kuty'

def text_plus_a(text):
    return text+'a'

ag= text_plus_a(ag)
print(ag)

ag2= ['rep','macsk','cic','alm','Ann','kacs']

for i in range(len(ag2)):
    ag2[i] = text_plus_a(ag2[i])

print(ag2)
