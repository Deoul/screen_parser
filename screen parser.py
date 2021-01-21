import requests
from random import shuffle
from bs4 import BeautifulSoup
from sys import argv
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 10.0; Win64, x64) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.89 Safari/532.5',
}
URL = 'https://prnt.sc/'
try:
    script, quantify = argv
    quantify = int(quantify)
except:
    quantify = 25
letters = 'qwertyuiopasdfghjklzxcvbnm1234567890'
letters_list = list(letters)
while quantify > 0:
    try:
        shuffle(letters_list)
        first_six_letters = ''.join(letters_list[0:6])
        tmp_url = URL + first_six_letters
        responce = requests.get(tmp_url, headers=headers).text
        image_url = BeautifulSoup(responce, 'lxml').find('img', class_='no-click screenshot-image')
        image_bytes = requests.get(image_url['src'], headers=headers).content
        with open(f'{first_six_letters}.png', 'wb') as file:
            file.write(image_bytes)
        quantify -= 1
        print(f'{first_six_letters}.png', 'Valid')
    except:
        continue

print('Ready')

