import requests
import re, sys
from datetime import datetime
import time
print ("Chat ke sini dulu @marlboro_id_bot biar notif masuk")
#Ganti chat id (cek disini @id_chatbot)
chatid = '1164362761'
#ganti kue dengan cookie akun tumbal ente
kue = '__cfduid=da45e453d0d5fff1d18869d9c0b71de6c1613015837;aldmic-key=eyJpdiI6ImhVV2U5SVQ3c2pBaUY1VnpwbDR4Nnc9PSIsInZhbHVlIjoicGlrMjdUSDhXQ3d0NFwvZ0pkQ2hQSnZvbGltWU0rY2FlNENBb1B2NSsyRWNYTWRlczhuM3AxSGhWTktVVUFldXAiLCJtYWMiOiIzYjI5YzJiMjM4ZGE3MGNhMTA4ODc2Zjk2NjY3OGJmZjk4NzJmNDU4NjdiYTA1ZWQzOTQ3ZjZmMDYzMGFiOTE1In0%3D;XSRF-TOKEN=eyJpdiI6IkluQnJka2F6Tlp2U3d2bXY2TWpQZ3c9PSIsInZhbHVlIjoiSCtPbHJyZ2VGQUtQT1Vqeld1cHJDR216UlZjVld5c01sT3lrSjlmc01JcWZIa21HYW5JNzJYdHZ2dHYyQUtLZiIsIm1hYyI6IjU2N2IyZDlmZDlhMDk0MmM0NmQ2Y2M3ZGQ4NDdlY2RiNTAxZTczMjI2ODkzM2YxYzA5YWUyNjY5NzE3YWMwNGQifQ%3D%3D;aldmic_session=eyJpdiI6ImUySUZvQ2JLWmUzQ3NWT00yOFZZVXc9PSIsInZhbHVlIjoiZDFWdEF6S3M4WXI1M3RRY3h5cVg4dVUrTlcyTk9rcjJEQUREQ3pwZ0pSOVJ1Z0VBQllPbUZSdDV3eEFQcG1vQyIsIm1hYyI6IjU1NjA3ZTIzYWM2M2JmNTY5ZTEzODI0YThjNWMxODczNzBmZTI2ZmI1MThkMTk1YzM5ZjY3YjYyMzM4MTIyYzcifQ%3D%3D;__cf_bm=355ac0facc63e7a815ee8d6aef112ee3365d45fb-1613015845-1800-AbxUrxkyACq0u+brpkHASVzr+e6g4ZyIUxVv+9v1E4gBbL/OgRJ4iWfN/tbT29R4RgKFIUx1IZe0JNnhV6BKzRbA8t430btnRhz00Ghfx8NH8escVUqdC6FgLoF6nUbM8Q==;_gat_gtag_UA_183386867_1=1;_ga=GA1.2.1013835325.1613015760;_gid=GA1.2.621136449.1613015760;_gat_UA-102334128-3=1;_hjTLDTest=1;_hjid=5d9063db-f563-4147-93d7-2008026a01c1;_hjFirstSeen=1;_hjIncludedInPageviewSample=1;_hjAbsoluteSessionInProgress=1;_hjIncludedInSessionSample=0'
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
  page = requests.get("https://loyalty.aldmic.com/catalog/11", params=None, headers=headers).text
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
