import RPi.GPIO as GPIO
import time
import sys
import requests, json
import ast
from requests.exceptions import HTTPError
from time import sleep
from goto import *
import var
import pio
import resource

#assign GPIO pins for motor
LCD_RS = 32
LCD_E  = 36
LCD_D4 = 15
LCD_D5 = 16
LCD_D6 = 18
LCD_D7 = 22


temp_channel  = 0
'''
define pin for lcd
'''
# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005




GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#for defining more than 1 GPIO channel as input/output use
DC_Motor_Pin1 = 11
DC_Motor_Pin2 = 13
GPIO.setup(DC_Motor_Pin1, GPIO.OUT)
GPIO.setup(DC_Motor_Pin2, GPIO.OUT)
GPIO.setup(7, GPIO.IN) 
GPIO.setup(10, GPIO.IN)          #Read output from PIR motion sensor
GPIO.setup(12, GPIO.OUT)         #LED output pin
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(38, GPIO.OUT)                    ## set output.
GPIO.setup(37, GPIO.OUT) 
GPIO.setup(40, GPIO.OUT) 
GPIO.setup(LCD_E, GPIO.OUT)  # E
GPIO.setup(LCD_RS, GPIO.OUT) # RS
GPIO.setup(LCD_D4, GPIO.OUT) # DB4
GPIO.setup(LCD_D5, GPIO.OUT) # DB5
GPIO.setup(LCD_D6, GPIO.OUT) # DB6
GPIO.setup(LCD_D7, GPIO.OUT) # DB7

LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

pwm1=GPIO.PWM(38,50)                        ## PWM Frequency
pwm2=GPIO.PWM(37,50)
pwm3=GPIO.PWM(40,50)
pwm1.start(0)
pwm2.start(0)
pwm3.start(0)

delay = 1   # 1s
loopCnt = 100

def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command
 
  GPIO.output(LCD_RS, mode) # RS
 
  # High bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
  lcd_toggle_enable()
 
  # Low bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
  lcd_toggle_enable()
'''
Function Name : lcd_toggle_enable()
Function Description:basically this is used to toggle Enable pin
'''
def lcd_toggle_enable():
  # Toggle enable
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)
'''
Function Name :lcd_string(message,line)
Function  Description :print the data on lcd 
'''
def lcd_string(message,line):
  # Send string to display
 
  message = message.ljust(LCD_WIDTH," ")
 
  lcd_byte(line, LCD_CMD)
 
  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)



 
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

 
# Function to calculate temperature from
# TMP36 data, rounded to specified
# number of decimal places.
def ConvertTemp(data,places):
 
  # ADC Value
  # (approx)  Temp  Volts
  #    0      -50    0.00
  #   78      -25    0.25
  #  155        0    0.50
  #  233       25    0.75
  #  310       50    1.00
  #  465      100    1.50
  #  775      200    2.50
  # 1023      280    3.30
 
  temp = ((data * 330)/float(1023))
  temp = round(temp,places)
  return temp
 
  
def validate(qrData,serverData):
    valid= 0
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
        
        valid=1
    return valid 

def mainout(product):
    # for i in range(10):
    #     GPIO.output(ledPin, GPIO.HIGH)  # output 3.3 V from GPIO pin
    #     time.sleep(delay)   # delay for 1s
    #     GPIO.output(ledPin , GPIO.LOW)  # output 0 V from GPIO pin
    #     time.sleep(delay)   # delay for 1s
    if product['Snickers']>0:
        n=product['Snickers']
        Nu = str(n)
        lcd_string(Nu + ' Snickers.',LCD_LINE_1)
        time.sleep(1)
        lcd_string('',LCD_LINE_1)
        for i in range(n):
              Num = str(i+1)
              lcd_string('Snickers - ' + Num,LCD_LINE_1)
              time.sleep(1)
              Step_motor1()
              time.sleep(delay)   # delay for 1s
              lcd_string('',LCD_LINE_1)
    if product['Coca-Cola']>0:
        n=product['Coca-Cola']
        Nu = str(n)
        lcd_string(Nu + ' Coca Cola.',LCD_LINE_1)
        time.sleep(1)
        lcd_string('',LCD_LINE_1)
        for i in range(n):
              Num = str(i+1)
              lcd_string('Coca Cola - ' + Num,LCD_LINE_1)
              time.sleep(1)
              Step_motor2()
              time.sleep(delay)   # delay for 1s
              lcd_string('',LCD_LINE_1)
    if product['Red Bull']>0:
        n=product['Red Bull']
        Nu = str(n)
        lcd_string(Nu + ' Red Bull.',LCD_LINE_1)
        time.sleep(1)
        lcd_string('',LCD_LINE_1)
        for i in range(n):
              Num = str(i+1)
              lcd_string('Red Bull - ' + Num,LCD_LINE_1)
              time.sleep(1)
              Step_motor3()
              time.sleep(delay)   # delay for 1s
              lcd_string('',LCD_LINE_1)

def Step_motor1():
    pwm1.ChangeDutyCycle(5)
    time.sleep(0.8)
    pwm1.ChangeDutyCycle(7.5)
    time.sleep(0.8)
    lcd_string('Delivered',LCD_LINE_2)
    time.sleep(1)
    lcd_string('',LCD_LINE_2)
    print("SM1.")
    pwm1.ChangeDutyCycle(5)
    time.sleep(0.8)
    

def Step_motor2():
    pwm2.ChangeDutyCycle(5)
    time.sleep(0.8)
    pwm2.ChangeDutyCycle(7.5)
    time.sleep(0.8)
    lcd_string('Delivered',LCD_LINE_2)
    time.sleep(1)
    lcd_string('',LCD_LINE_2)
    print("SM2.")
    pwm2.ChangeDutyCycle(5)
    time.sleep(0.8)
 
def Step_motor3():
    pwm3.ChangeDutyCycle(5)
    time.sleep(0.8)
    pwm3.ChangeDutyCycle(7.5)
    lcd_string('Delivered',LCD_LINE_2)
    time.sleep(0.8)
    lcd_string('',LCD_LINE_2)
    print("SM3.")
    time.sleep(1)
    pwm3.ChangeDutyCycle(5)
    time.sleep(0.8) 



def apicall():
    qrData={"orderDate": "2021-01-31 09:01:54.743494+00:00", "transactionComplete": True, "transactionstatus": "Pending", "customerName": "giri", "customerEmail": "giri@gmail.com", "orderProductes": {"Snickers": 3, "Coca-Cola": 2, "Red Bull": 3}, "amountTopay": 109.0, "paid_amount": 109.0, "transaction_id": 1621976701.054469, "Id": "106"}
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

    if (qrData['transactionComplete']==serverData["complete"]) and (qrData['transactionstatus']==serverData["status"])  and (float(qrData['amountTopay'])==float(qrData["paid_amount"])) :

        print('hey !!',serverData["customer"],'Your Order is Approved')
        lcd_string('hey !! ' + serverData["customer"],LCD_LINE_1)
        time.sleep(2)
        lcd_string('Order is Done',LCD_LINE_2)
        time.sleep(2)
        lcd_string('',LCD_LINE_1)
        lcd_string('',LCD_LINE_2)
        print('You can Get :',qrData['orderProductes'])
        lcd_string('You can Get :',LCD_LINE_1)
        time.sleep(2)
        lcd_string('',LCD_LINE_1)
        update={}
        update['status']='Delivered'
        mainout(qrData['orderProductes'])
        lcd_string('Thank You',LCD_LINE_1)
        time.sleep(1)
        lcd_string('For purchasing',LCD_LINE_2)
        time.sleep(2)
        lcd_string('',LCD_LINE_1)
        lcd_string('',LCD_LINE_2)
        lcd_string('PIR Sensor OFF',LCD_LINE_1)
        time.sleep(3)
        lcd_string('',LCD_LINE_1)
        try:
            response = requests.put(url,headers=header ,data =update)
            response.raise_for_status()
            #print(response.text)
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6

    else:
          update={}
          update['status']='Pending'
          update['complete']=True
          response = requests.put(url,headers=header ,data =update)
          print(response.text)
          print('Sorry your code is Invalid')
          lcd_string('Code is Invalid',LCD_LINE_1)
          time.sleep(2)
          lcd_string('',LCD_LINE_1)
          lcd_string('Try Next Time',LCD_LINE_1)
          time.sleep(3)
          lcd_string('',LCD_LINE_1)
          lcd_string('PIR Sensor OFF',LCD_LINE_1)
          time.sleep(3)
          lcd_string('',LCD_LINE_1)
    
      

#motor_direction = input('select motor direction a=anticlockwise, c=clockwise: ')
while (True):
    i=GPIO.input(7) 
    print("Welcome hiii")  
    if i==1:                 #When output from motion sensor is LOW
      GPIO.output(12, 1)  #Turn ON LED
      GPIO.output(8, GPIO.HIGH) # Turn on the light
      lcd_init()
      lcd_string("Welcome ",LCD_LINE_1)
      time.sleep(2)
      lcd_string("Show your code ",LCD_LINE_1)
      time.sleep(3)
      lcd_string("Scanning.....",LCD_LINE_1)
      time.sleep(2)
       
      j=1
      if(j==1):
          apicall()
          print("Your Orders are Delivered.")
          print("See you Next Time.Thank you")
          GPIO.output(8, GPIO.LOW) # Turn of the light
          GPIO.output(12, 0)  #Turn OFF LED
          time.sleep(0.1)

        
    elif i==0:               #When output from motion sensor is HIGH
      print("Bye")
      GPIO.output(12, 0)  #Turn OFF LED
      time.sleep(0.1)
  

        