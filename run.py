import requests
import re, sys
from datetime import datetime
import time
print ("Chat ke sini dulu @marlboro_id_bot biar notif masuk")
#Ganti chat id (cek disini @id_chatbot)
chatid = '1468054653'
#ganti kue dengan cookie akun tumbal ente
kue = '__cfduid=da45e453d0d5fff1d18869d9c0b71de6c1613015837;_ga=GA1.2.1013835325.1613015760;_hjid=5d9063db-f563-4147-93d7-2008026a01c1;_hjTLDTest=1;_hjAbsoluteSessionInProgress=0;aldmic-key=eyJpdiI6IjBPbVlLN2VaNnJwODFpZkxzU2xNR0E9PSIsInZhbHVlIjoiN3dkREJuVVY1d2Ird3djdEFtOHlBZHV3N3k2ekU3a1lKd1NQdStUS3IyVUpZd2NsaERYRUlaTnpjcjdsekpTUiIsIm1hYyI6IjlhOTgzYTJjN2QwOWQ3NWY3ZTViMTliY2QzNTNiOWZmNzljNzI0ODcxNTEzMDdmMDZhY2ViOGZiYmRjMDE2ZWYifQ%3D%3D;__cf_bm=3d814a1d7a465740244dee743fd87df8186982d8-1613361032-1800-AbHNG+m4KNiJ+d3f53rZF7477Qv52cJAh8pzSRf1GV11YxzuvpbZ4S1+rT6jBCxIX6gNc/Ox88sSo4csH/0Zc6CLOwGEKPzdl4hj+DcFvAusboHFBDlbYAst49sAZVSDNw==;_gid=GA1.2.226113092.1613360912;_hjIncludedInSessionSample=0;XSRF-TOKEN=eyJpdiI6IlFrQ3VDdHhEXC8wWTA1TG14TndRM1pnPT0iLCJ2YWx1ZSI6IjlzODNidFNXSnFDbHZwa0JwZUNldWhoTWJxWGhCd0Jqd0J6ZEZod0o0Um9tcThiSzF6aE1sc28rQ0RHcGRZNW8iLCJtYWMiOiI1NDlhYWUyNmIyOWZjODNlYjA3NjM3N2Y3ODIzM2Q4ZDZmY2EyNTlkNzE2ZDU0NTczOTdlZjQ0NzAwZjgxZGFkIn0%3D;aldmic_session=eyJpdiI6IldNaEUxVHZBSDdVQUwzb2MzMk1XQlE9PSIsInZhbHVlIjoiZmhESkdtZmU5R0hiNnJaNzJCRmk4azc3aVBMVzM4dUU5K1NwbFQ3aVlqOFNpZWtUaTNaTHkrRzZycFFxREJnaiIsIm1hYyI6IjM4ZjAwMjEwYWNkN2IzZDRhMmZiODA5NDBkNDM3OWNkZjljZTczN2M3MjQ0MzFiNTNmODYyZTA5NjllYmU2NjAifQ%3D%3D'
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
      #waktu = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
      msg = (redeem)
      print (redeem)
  time.sleep(60*1)
