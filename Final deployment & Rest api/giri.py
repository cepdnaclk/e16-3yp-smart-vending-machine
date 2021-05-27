import RPi.GPIO as GPIO
import time
import sys
import requests, json
import ast
from requests.exceptions import HTTPError


#assign GPIO pins for motor


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#for defining more than 1 GPIO channel as input/output use
DC_Motor_Pin1 = 11
DC_Motor_Pin2 = 13
GPIO.setup(DC_Motor_Pin1, GPIO.OUT)
GPIO.setup(DC_Motor_Pin2, GPIO.OUT)
GPIO.setup(7, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(12, GPIO.OUT)         #LED output pin
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
ledPin11 = 11     # GPIO 17
ledPin15 = 15    # GPIO 17
ledPin19 = 19    # GPIO 17
 
delay = 2   # 1s
loopCnt = 100
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

def Stepper_Motor():
      print("Motor clockwise")
      GPIO.output(DC_Motor_Pin1, GPIO.HIGH)
      GPIO.output(DC_Motor_Pin2, GPIO.LOW)
      time.sleep(10)
      print("Motor Anticlockwise")
      GPIO.output(DC_Motor_Pin1, GPIO.LOW)
      GPIO.output(DC_Motor_Pin2, GPIO.HIGH)
      time.sleep(10)

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


def apicall():
    qrData={"orderDate": "2021-01-31 09:01:54.743494+00:00", "transactionComplete": True, "transactionstatus": "Pending", "customerName": "giri", "customerEmail": "giri@gmail.com", "orderProductes": {"Snickers": 3, "Coca-Cola": 1, "Red Bull": 1}, "amountTopay": 52.0, "paid_amount": 52.0, "transaction_id": 1615295639.67432, "Id": "106"}
    load={
        "username": "karikaran",
        "password": "Test1357"
    }

    try :

        response = requests.post('https://smart-happyvending.herokuapp.com/api/api/token/', json=load)
        data=ast.literal_eval(response.text) 

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

        Valid =validate(qrData,serverData)
        


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
    
      

#motor_direction = input('select motor direction a=anticlockwise, c=clockwise: ')
while (True):
   i=GPIO.input(7)
   j=GPIO.input(8) # scan qr input
   if (i==1):                 #When output from motion sensor is LOW
        GPIO.output(8, GPIO.HIGH) # Turn on the light
        print("Welcome",i)
        GPIO.output(12, 1)  #Turn ON LED
        if(j==1):
            apicall()
        
   elif i==0:               #When output from motion sensor is HIGH
        GPIO.output(12, 0)  #Turn OFF LED
        time.sleep(0.1)