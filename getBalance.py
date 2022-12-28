import json
import time
import schedule
import requests
from datetime import datetime

def telegram_bot_sendtext(bot_message):
    
    bot_token = '5739700031:AAFIUXWmMefYCetmd-Zr4zVCySHCiW_i1LE'
    bot_chatID = '469086017'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

def report():
    #this below api will give the balance prod
    my_balance = json.loads(requests.get('https://api.blockcypher.com/v1/btc/main/addrs/3R2N4SdCmhprXNMN4sedL7wEaaH7jdU9Wm/balance').text)
    #testing 
    #my_balance = json.loads(requests.get('https://api.blockcypher.com/v1/btc/main/addrs/1DEP8i3QJCsomS4BSMY2RpU1upv62aGvhD/balance').text)
    val = int(my_balance["balance"])
    print(val)
    if val > 0.0:
        my_message = 'Current balance is: {}'.format(val / float(100000000))
        #time = 'Current Time =', datetime.now().strftime("%H:%M:%S")
        telegram_bot_sendtext(my_message)
 
schedule.every(5).minutes.do(report)

while True:
    schedule.run_pending()
    time.sleep(1)
