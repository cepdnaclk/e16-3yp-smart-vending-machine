# Smart Vending Machine

**Hello everyone!! Welcome to our project.**  

 ![top](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/Milestone%203.png)

[**Click here to check our website!!**](https://cepdnaclk.github.io/e16-3yp-smart-vending-machine/index.html)


## Group Members
   > [S Bragadeeshan](https://github.com/Bragadeeshan)   :: E/16/055 :: e16055@eng.pdn.ac.lk
   
   > [V Harikaran](https://github.com/Karikaranvetti)     :: E/16/172 :: e16172@eng.pdn.ac.lk
   
   > [S Girishikan](https://github.com/girish4848)   :: E/16/115 :: e16115@eng.pdn.ac.lk
   
   
   ## Table of contents

1. >[Problems](https://github.com/cepdnaclk//e16-3yp-smart-vending-machine#problems)
2. >[Overview](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine#overview)
3. >[Solutions](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine#solutions)
4. >[Technologies](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine#technologies)
4. >[User Interface](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine#Interface)
4. >[Hardware Components](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine#Components)
4. >[Hardware Design](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine#Design)
5. >[Testing](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine#testing)
6. >[Detailed budget](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine#budget)
7. >[Links](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine#Links)

 
 ## PROBLEMS
   Lack of 24 hrs Open Shops.MRP products sold for higher prices.Having a big space for a shop.Having to pay for the products with cash most of the time.Easy to hack Traditional vending machine.Prices and Expiry dates are not checked by the  Traditional vending machine.
    ![problems](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/COMPARISON-FA-01.jpg)


 ## OVERVIEW
  In Smart vending machine we are addresiing the problems faced by the companies and the Consumers in communication and 
  transaction. We hope to give a real time analysis of the market for each and every product available in the vending machine.
  ![overview](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/show2.png)


  The software architecture works like the above mentioned picture First user accesses the web application and he chooses the products and the interface was made by the Python Django and the details are updated in to the database which is made by MongoDB And it is al so in the server which is The Amazon EC3 instance All the communications are done through https. There is an API in the machine which connects the sever to get the Validation requests.Finally the Machine dispences the item chose by the user
  
  
 ## SOLUTIONS
  Problems in having a traditional vending machine are - Having to pay for the products with cash most of the time.Easy to hack Traditional vending machine.Prices and Expiry dates are not checked by the Traditional vending machine.

the solution to all the problem is a Smart vending machine which has the (Gender ,Age ,generation wise) analysis , 24 hours Distribution and vending services , Transaction Datbase services. Which can be used to check the performance of a product in a specific market.Prices and expiry dates are real time because it is connected to the cloud.
 ![overview](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/show1.png)

  
 ## TECHNOLOGIES
  ### Cashless payments																
   * Using mobil e payment methods and  Card Transaction .
  ### Smartphone interaction																
   * Using smart phones to selection of the products , using the money transfer systems		
     like the help of google wallet.
  ### Energy-Saving Vending															
   * Making sure the vending machine only works when a customers there. 
     Minor changes can be made to ensure energy saving.

## INTERFACE
  ![interface](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/ui1.jpeg)
  The Website gets you to this Home page which Can be used to directly buy items or you can sign in and buy things If you sign in the company can give you discounts or other options.And also from the Homepage you can go to the cart which has the items you selected and the total amount.Other than that you can also go to the tab pending orders and use the QR codes to get the paid items to dispense. 

  ![interface](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/ui2.jpeg)
  This Page is the page you get if you want to Login.You can type in your login credentials and get into the account where you can see your previous orders and etcs. Or If you don't have an account you can go to the Signup option and Sign up for a new account.There is an option to help you reset your password as well if you forget. 

  ![interface](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/signup.jpeg)
  This is the SignUp page where you can Sign up for a new Account.The creditentials can be created here and there is a email checker and the email should be legitimate to sign in 
  
  ![interface](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/ui2.jpeg)
  After Signing in you will have a page similar to the home page but you can see your account and you can make changes to your account when you click on your profile picture.And also you will have an Profile Button on your webpage where you can go and change your account settings. 
  ![interface](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/cartview.jpeg)
  After you added the items your Cart the cart looks like this and you can edit the items that you are going to add here also.If you click check out it will take to a page where your can pay for the Items.You can use continue shopping to go back and add more items to the cart.
  ![interface](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/payment.jpeg)
  When you go to the checkout page you can see that it will ask for a name and an email. It is just for the invoice so you can use it for refunds and other proceeds. 
  ![interface](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/payways.jpeg)
  After giving the Email and the name You can choose the way to pay (Paypal / Debit Card /Credit card).After choosing the payment method you will be redirected to a dialog box which is going popup and you can give your details there and pay for the items and you will receive the items. 

  ![interface](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/paypal.jpeg)
    pop up will redirect you to Paypal

  ![interface](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/admindata.jpeg)
  If you Login with the admin Credentials you can see all the transactions that have happened with the vending machine over the time. And you can check who has bought the items and their characteristics according to their accounts.And also you can check the pending transactions. 
  ![interface](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/productadd.jpeg)
  If you Login as an Admin You can also change the number of products in the vending machine.If you see any miscalculations. And also you can search for items according to their places and the prices and also the names. 
  ![interface](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/OrderQR.jpeg)
  The other page you can check are the QR codes of the customers who are going to buy the items. 

## COMPONENTS
 ### Raspberry Pi 3 
* Broadcom BCM2837 64bit ARMv7 Quad Core Processor powered Single Board Computer running at 1.2GHz 1GB RAM

* BCM43143 WiFi on board Bluetooth Low Energy (BLE) on board

* 40pin extended GPIO , 4 x USB 2 ports 4 pole

* Stereo output and Composite video port Full size HDMI

* CSI camera port for connecting the Raspberry Pi camera

* Upgraded switched Micro USB power source (now supports up to 2.4 Amps) Expected to have the same form factor has the Pi 2 Model B, however the LEDs will change position

### Stepper Motor
* Motor Type: Bipolar Stepper

* Step Angle: 1.8 deg.

* Holding Torque: 40N.cm (56oz.in)

* Rated Current/phase: 1.7A

* Phase Resistance: 1.5Ohm±10%

* Insulation Resistance: 100MΩ¸ Min, 500VDC

* Insulation Strength: 500VAC for one minute  

### Stepper motor driver
stepper motor provides a constant holding torque without the need for the motor to be powered.Steppers provide precise positioning and repeatability of movement since good stepper motors have an accuracy of 3 – 5% of a step and this error is non-cumulative from one step to the next.

* Driver Model: L298N 2A

* Driver Chip: Double H Bridge L298N

* Motor Supply Voltage (Maximum): 46V

* Motor Supply Current (Maximum): 2A

* Logic Voltage: 5V

* Driver Voltage: 5-35V

* Driver Current:2A

* Logical Current:0-36mA

* Maximum Power (W): 25W

* Current Sense for each motor

* Heatsink for better performance

### Camera Module V2 for Raspberry Pi
* 5 megapixel native resolution sensor-capable of 2592 x 1944 pixel static images.

* Supports 1080p30, 720p60 and 640x480p60/90 video.

* Camera is supported in the latest version of Raspbian, Raspberry Pi's preferred operating system.

### Relay Module
* High-sensitivity (250 mW) and High-capacity (16 A) versions

* Rated voltage 12 V DC

* Rated current 20.8 mA

* Coil resistance 576 Ω

* Must operate voltage 75% max. of the rated voltage

* Must release voltage 10% min. of the rated voltage

* Max. voltage 180% of rated voltage (at 23°C)

* Power consumption Approx. 250 mW

### Weight Sensor
* Differential input voltage: ±40mV (Full-scale differential input voltage is ± 40mV)

* Data accuracy: 24 bit (24 bit A / D converter chip.)

* Refresh frequency: 10/80 Hz.

* Operating Voltage: 2.7V to 5V DC.

* Operating current: < 10 mA.

* Size: 24x16mm.
### PIR sensor
* Input voltage: DC 4.5~20V

* Static current: 50uA

* Output signal: 0,3V (Output high when motion detected)

* Sentry angle: 110 degree

* Sentry distance: max 7 m

* 120 degree detection angle

* Low power consumption in idle mode only 50uA and 65mA in fully active mode. 

## Design

![testing](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/hardware.png)
![testing](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/machine.png)
For the Convenience of the user the design was made to demonstrate which has all the attributes and more of a vending machine In the picture you can see a screen which is used to communicate with the user and there is a proximity sensor to make sure the vending machine only works when someone is present 
 ## TESTING
 
  ### URL unit Testing
   * This test was done in order to check whether the end to end data transaction is happening or not.   
   
   ![testing](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/test1.png)
  
  ### POST/GET Request unit Testing
   * This test to check the post and get requests
   
   ![testing](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/test2.png)
   ![testing](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/test3.png)
  
  ### Form Validation Testing
   * This test to check the Forms
   
   ![testing](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/test4.png)
   
 
 ## BUDGET
  ![budget](https://github.com/cepdnaclk/e16-3yp-smart-vending-machine/blob/main/docs/show4.png)
  
    
 ## Advising Lecturers

 -  Dr Isuru Nawinna
 -  Dr Ziyan Marikkar

##  [Department of Computer Engineering](http://www.ce.pdn.ac.lk/)

**![](https://lh4.googleusercontent.com/OkyvOJUe006Wr5Lo9PwBC-Hpn_D0aJPld-L4eLR88TKwNoe-TL_5-v8fKesJv8BZtq941FLgSWlmBOTRlVkPIXewBg4uSsAHPtr6gkLhlhrKQAhI8Qa4DXn5Gzp1eRZYiYV_o9NYT6I)**

##  [Faculty of Engineering](http://eng.pdn.ac.lk/)

**![](https://lh3.googleusercontent.com/RrwqSr9g2uPiF0l-R_y3NtjNwugTP0g-D3Yhj_IR91-zBHGAjbVJiR4Y9rHrmM1eH3h5Zdmelr6jfYEjeT9_ETOWNGSgTYuOC4Kzmrolu8hz3jDnfU1yV1R-p22OJ2iv4p6OllEGsjM)**

##  [University of Peradeniya](https://www.pdn.ac.lk/)

![enter image description here](https://upload.wikimedia.org/wikipedia/en/c/cc/University_of_Peradeniya_crest.png)
