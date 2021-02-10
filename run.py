import requests
import re, sys
from datetime import datetime
import time
print ("Chat ke sini dulu @marlboro_id_bot biar notif masuk")
#Ganti chat id (cek disini @id_chatbot)
chatid = '00000000'
#ganti kue dengan cookie akun tumbal ente
kue = '__cfduid='
headers = ({
'Host': 'loyalty.aldmic.com',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi Note 5A Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
'Cookie': kue
})
while(True):
  #Ganti angka 2 dengan angka catalog yg ente pengen cek
  page = requests.get("https://loyalty.aldmic.com/catalog/2", params=None, headers=headers).text
  nama = re.findall(r'<h4>(.*?)</h4>', page)
  if nama == []:
    print("Error Cookie")
    break
  redem = re.findall(r'">(.*?)</label></a>', page)
  for i in range(len(nama)): 
    print(nama[i])
    redems = re.sub(r'[0-9]', '', redem[i])
    redeem = redems.replace('<label class="padding">', '')
    if redeem == 'redeem':
      waktu = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
      msg = (redeem+' => '+waktu)
      get = requests.get('https://api.telegram.org/bot1642391808:AAFEXkpHnBJQ2v0zzoePlnBIWwgzL9jw9Hg/sendMessage?chat_id='+chatid+'&text='+nama[i]+"%0A"+msg)
      print (msg)
    elif redeem == 'Out of Stock':
      print (redeem)
      time.sleep(60*3)
