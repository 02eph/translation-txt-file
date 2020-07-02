import re
import requests

f = open('Computer Science an overview.txt', 'r', encoding='UTF8').read()
result = re.findall(r'[A-z][a-z][a-z]+', f.lower())
dict_result = list(set(result))
#dict_result.sort()
#print(dict_result, len(dict_result))

URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"
KEY = "trnsl.1.1.20200317T141945Z.3adf4b4353f01ace.a67430d22bdfb533cce3a00f2cc3d53ccef9e939"

def translate_text(dict_text):
    params = {
        "key": KEY,
        "text": dict_text,
        "lang": 'en-ru'
    }
    response = requests.get(URL, params=params)
    return response.json()

f1 = open('words.txt', 'w')

for w in dict_result[:100]:
    json = translate_text(w)
    print(w, " - ", ''.join(json["text"]))
    f1.write(w+" - "+''.join(json["text"])+'\n')
f1.close()