import requests, json
import ast  
from pyzbar.pyzbar import decode
from PIL import Image
from requests.exceptions import HTTPError
import RPi.GPIO as GPIO
import time
 
ledPin = 11     # GPIO 17
 
delay = 1   # 1s
loopCnt = 100

 
def main():
    for i in range(10):
        GPIO.output(ledPin, GPIO.HIGH)  # output 3.3 V from GPIO pin
        time.sleep(delay)   # delay for 1s
        GPIO.output(ledPin , GPIO.LOW)  # output 0 V from GPIO pin
        time.sleep(delay)   # delay for 1s
 
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)    # initialize GPIO pin as OUTPUT pin
    GPIO.output(ledPin, GPIO.LOW)
     


def validate(qrData,serverData):
    valid=False
    serverIterm={}
    for iterm in serverData['OrderItems']:
        serverIterm[iterm['name']]=iterm['quantity']
    if((qrData['transactionComplete']==serverData["complete"])
    and (qrData['transactionstatus']==serverData["status"]) 
    and (float(qrData['transaction_id'])==float(serverData["transaction_id"])) 
    and (qrData['transactionstatus']==serverData["status"]) 
    and (int(qrData['amountTopay'])==int(serverData["paidAmount"])) 
    and (serverIterm==qrData['orderProductes'])
    and (qrData['customerName']==serverData["customer"])):
        
        valid=True
    return valid 


#Qrcode reading 

d = decode(Image.open('qr.jpeg'))
qrData=json.loads(d[0].data.decode('utf-8'))
# print(qrData)



#servar request
load={
    "username": "karikaran",
    "password": "Test1357"
}

try :

    response = requests.post('https://smart-happyvending.herokuapp.com/api/api/token/', json=load)
    data=ast.literal_eval(response.text) 
    print(data)

    response.raise_for_status()

except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
 

 
# print(type(response.text))
   
header={}

header['Authorization']='Bearer  '+ data['access']
# print(header)
url='https://smart-happyvending.herokuapp.com/api/orders/'+qrData['Id']+'/'

try :

    response = requests.get(url,headers=header ,)
    response.raise_for_status()

        

    # data1 = response.read()
    jsonData = json.loads(response.text)
    # print(jsonData)
    serverData=jsonData 

    Valid =validate(qrData,serverData)
     


except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6

if Valid and (float(qrData['amountTopay'])==float(qrData["paid_amount"])) :

    print('hey !!',serverData["customer"],'Your Order is Approved')
    print('You can Get :',qrData['orderProductes'])

else:
    setup()
    main()
    GPIO.cleanup()  # free up the resources used

    print('Sorry your code is Invalid')

