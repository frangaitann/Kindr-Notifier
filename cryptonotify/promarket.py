#NOTIFIER

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
import requests
import os

token= 'BOT-TOKEN'
telegram_id= 'CHAT-ID'

def notif_sender(msg):
     url= f'https://api.telegram.org/bot{token}/sendMessage'
     data= {'chat_id': telegram_id, 'text': msg}
     response= requests.post(url, data=data)
     return response.json




def notifier():

    os.system('clear')

    timestamp = datetime.datetime.now()

    timestamp_final = timestamp.strftime("%d %H:%M:%S")

    options= Options()
    options.add_argument("-headless")
    print("Headless web established (000)")

#Opening Firefox, Ripio & DolarHoy website
    driver=webdriver.Firefox(options=options)
    driver.get("https://www.ripio.com/ar/criptomonedas/cotizacion/")
    
    print("Connected to Coinbase (001)")
    


    while True:
        # driver.refresh()
        
        driver=webdriver.Firefox(options=options)
        driver.get("https://www.ripio.com/ar/criptomonedas/cotizacion/")
        

        buyprice = driver.find_element("xpath", "/html/body/section[4]/div[2]/div[1]/div[2]") 

        sellprice = driver.find_element("xpath", "/html/body/section[4]/div[2]/div[1]/div[3]")
        
        
        
        driver=webdriver.Firefox(options=options)
        driver.get("https://www.dolarhoy.com/cotizacion-dolar-blue")
        


        buyprice_blue = driver.find_element(By.CSS_SELECTOR, ".is-8 > div:nth-child(1) > div:nth-child(2)")
        
        sellprice_blue = driver.find_element(By.CSS_SELECTOR, ".is-8 > div:nth-child(2) > div:nth-child(2)")

        pre_buy_blue = buyprice_blue.text
        
        pre_sell_blue = sellprice_blue.text
        
        buy_blue = pre_buy_blue.replace("$", "")
        
        sell_blue = pre_sell_blue.replace("$", "")
        
        buy_blue_def = float(buy_blue)
        
        sell_blue_def = float(sell_blue)
       
       
       

        timestamp = datetime.datetime.now()

        timestamp_final = timestamp.strftime("%d %H:%M:%S")
        
        pre_buy = buyprice.text

        pre_sell = sellprice.text

        buy = pre_buy.replace("$", "")
        
        
        

        buy = float(buy)

        sell = pre_sell.replace("$", " ")

        sell = float(sell)


        current= time.localtime()

        current_hour= current.tm_hour

        if 9 <= current_hour <= 16:

                print(f"""[{timestamp_final}] UXD |     BUY:{pre_buy}     SELL:{pre_sell}
            BLU |   BUY:{buy_blue_def}  SELL:{sell_blue_def}
""")
                notif_sender(f'''🔴 UXD (Cryptodollar) |    ⬇️ COMPRA {buy}    ⬆️ VENTA {sell}
BLU (Dolar Blue)    ⬇️ COMPRA {buy_blue_def}    ⬆️ VENTA {sell_blue_def}
.''')
                
        else:
             print(f'COTIZACION CERRADA HASTA LAS 10:00 A.M | ULTIMO PRECIO REGISTRADO: UXD {buy}  BLU {buy_blue_def}')

        prev_buyprice = buy

        time.sleep(3600)

notifier()
