from urllib import request
from requests import get
import time
from os import mkdir

try:
    mkdir("avas")
except:
    pass
def get_random_avatar_from_web():
        r = get('https://thispersondoesnotexist.com/image')
        # print(r.content)
        # print(b64encode(r.content))
        return(r.content)

i = input("Сколько ав генерировать")
for i in range(1, i+1):
    with open(f"avas/image{i}.png", "wb") as f:
        f.write(get_random_avatar_from_web())
    time.sleep(1)
