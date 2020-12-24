from bs4 import *
import requests as rq
import os
from urllib.request import Request, urlopen

def start():
  os.system('cls' if os.name == 'nt' else 'clear')


  filename = str(input("Please Enter a folder name : "))
  input01 = input("Enter WEBPAGE : ")
  sa = int(input("How Many sources(Max5) : "))

  req = Request(input01,headers={'User-Agent': 'Mozilla/5.0'})
  webpage = urlopen(req).read()
  print(webpage)
  r2 = (rq).get(input01)
  soup2 = BeautifulSoup(r2.text, "html.parser")
  links = []
  amount = 0

  #------------------------------------------------------------------1 SOURCE
  if sa == 1:
    source = input("Paste The Source : ")
    fa = "img[src^="+'"'+source+'"'+"]"
    
    x01 = soup2.select(fa)
    for img in x01:
      links.append(img['src'])
      amount += 1
  #------------------------------------------------------------------2 SOURCE
  elif sa == 2:
    source1 = input("Paste The Source : ")
    fa1 = "img[src^="+'"'+source1+'"'+"]"
    source2 = input("Paste The Source : ")
    fa2 = "img[src^="+'"'+source2+'"'+"]"
    
    x01 = soup2.select(fa1)
    for img in x01:
      links.append(img['src'])
      amount += 1
    x02 = soup2.select(fa2)
    for img in x02:
      links.append(img['src'])
      amount += 1
  #------------------------------------------------------------------3 SOURCE
  elif sa == 3:
    source1 = input("Paste The Source : ")
    fa1 = "img[src^="+'"'+source1+'"'+"]"
    source2 = input("Paste The Source : ")
    fa2 = "img[src^="+'"'+source2+'"'+"]"
    source3 = input("Paste The Source : ")
    fa3 = "img[src^="+'"'+source3+'"'+"]"
    
    x01 = soup2.select(fa1)
    for img in x01:
      links.append(img['src'])
      amount += 1
    x02 = soup2.select(fa2)
    for img in x02:
      links.append(img['src'])
      amount += 1
    x03 = soup2.select(fa3)
    for img in x03:
      links.append(img['src'])
      amount += 1
  #------------------------------------------------------------------4 SOURCE
  elif sa == 4:
    source1 = input("Paste The Source : ")
    fa1 = "img[src^="+'"'+source1+'"'+"]"
    source2 = input("Paste The Source : ")
    fa2 = "img[src^="+'"'+source2+'"'+"]"
    source3 = input("Paste The Source : ")
    fa3 = "img[src^="+'"'+source3+'"'+"]"
    source4 = input("Paste The Source : ")
    fa4 = "img[src^="+'"'+source4+'"'+"]"
    
    x01 = soup2.select(fa1)
    for img in x01:
      links.append(img['src'])
      amount += 1
    x02 = soup2.select(fa2)
    for img in x02:
      links.append(img['src'])
      amount += 1
    x03 = soup2.select(fa3)
    for img in x03:
      links.append(img['src'])
      amount += 1
    x04 = soup2.select(fa4)
    for img in x04:
      links.append(img['src'])
      amount += 1
  #------------------------------------------------------------------5 SOURCE
  elif sa == 5:
    source1 = input("Paste The Source : ")
    fa1 = "img[src^="+'"'+source1+'"'+"]"
    source2 = input("Paste The Source : ")
    fa2 = "img[src^="+'"'+source2+'"'+"]"
    source3 = input("Paste The Source : ")
    fa3 = "img[src^="+'"'+source3+'"'+"]"
    source4 = input("Paste The Source : ")
    fa4 = "img[src^="+'"'+source4+'"'+"]"
    source5 = input("Paste The Source : ")
    fa5 = "img[src^="+'"'+source5+'"'+"]"
    
    x01 = soup2.select(fa1)
    for img in x01:
      links.append(img['src'])
      amount += 1
    x02 = soup2.select(fa2)
    for img in x02:
      links.append(img['src'])
      amount += 1
    x03 = soup2.select(fa3)
    for img in x03:
      links.append(img['src'])
      amount += 1
    x04 = soup2.select(fa4)
    for img in x04:
      links.append(img['src'])
      amount += 1
    x05 = soup2.select(fa5)
    for img in x05:
      links.append(img['src'])
      amount += 1
  #------------------------------------------------------------------ELSE
  else:
    print("Invalid Sorry")
    os.system('cls' if os.name == 'nt' else 'clear')
  #------------------------------------------------------------------Downloader/Save

  saved = 0

  for l in links:
    print(l)

  print(amount)

  os.mkdir(filename)
  i = 1

  for index, img_link in enumerate(links):
    if i <=5000:
      img_data = rq.get(img_link).content
      with open(filename+"\\"+str(index+1)+'.jpg', 'wb+') as f:
        f.write(img_data)
      i += 1
      saved += 1
      print(amount, "/", saved)
    else:
      f.close()
      break
  start()


  #------------------------------------------------------------------SCRIPT start
start()

    



