import requests, json
import ast  
from pyzbar.pyzbar import decode
from PIL import Image
from requests.exceptions import HTTPError
ledPin11 = 11     # GPIO 17
ledPin15 = 15    # GPIO 17
ledPin19 = 19    # GPIO 17
 
delay = 2   # 1s
loopCnt = 100

 
def mainout(product):
    # for i in range(10):
    #     GPIO.output(ledPin, GPIO.HIGH)  # output 3.3 V from GPIO pin
    #     time.sleep(delay)   # delay for 1s
    #     GPIO.output(ledPin , GPIO.LOW)  # output 0 V from GPIO pin
    #     time.sleep(delay)   # delay for 1s
    if product[Snickers]>0:
        n=product[Snickers]
        for i in range(n):
            GPIO.output(ledPin11, GPIO.HIGH)  # output 3.3 V from GPIO pin
            time.sleep(delay)   # delay for 1s
            GPIO.output(ledPin11 , GPIO.LOW)  # output 0 V from GPIO pin
            time.sleep(delay)   # delay for 1s
    if product['Coca-Cola']>0:
        n=product['Coca-Cola']
        for i in range(n):
            GPIO.output(ledPin11, GPIO.HIGH)  # output 3.3 V from GPIO pin
            time.sleep(delay)   # delay for 1s
            GPIO.output(ledPin11 , GPIO.LOW)  # output 0 V from GPIO pin
            time.sleep(delay)   # delay for 1s
    if product['Red Bull']>0:
        n=product['Red Bull']
        for i in range(n):
            GPIO.output(ledPin11, GPIO.HIGH)  # output 3.3 V from GPIO pin
            time.sleep(delay)   # delay for 1s
            GPIO.output(ledPin11 , GPIO.LOW)  # output 0 V from GPIO pin
            time.sleep(delay)   # delay for 1s



 
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin11, GPIO.OUT)    # initialize GPIO pin as OUTPUT pin
    GPIO.output(ledPin11, GPIO.LOW)
    GPIO.setup(ledPin15, GPIO.OUT)    # initialize GPIO pin as OUTPUT pin
    GPIO.output(ledPin15, GPIO.LOW)
    GPIO.setup(ledPin19, GPIO.OUT)    # initialize GPIO pin as OUTPUT pin
    GPIO.output(ledPin19, GPIO.LOW)

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
    print(serverIterm)
    return valid 


#Qrcode reading 

d = decode(Image.open('qrcode-kumar-1621968554.296135.png'))
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
except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6

 
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
    print(qrData)
    print(serverData)
    Valid =validate(qrData,serverData)
    print(Valid)
     


except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6

if Valid and (float(qrData['amountTopay'])==float(qrData["paid_amount"])) :

    print('hey !!',serverData["customer"],'Your Order is Approved')
    print('You can Get :',qrData['orderProductes'])
    update={}
    update['status']='Delivered'
    setup()
    mainout(qrData['orderProductes']))
    GPIO.cleanup()  # free up the resources used
    try:
        response = requests.put(url,headers=header ,data =update)
        response.raise_for_status()
        #print(response.text)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6


else:
    '''update={}
    update['status']='Pending'
    update['complete']=True
    response = requests.put(url,headers=header ,data =update)
    print(response.text)'''
    print('Sorry your code is Invalid')

