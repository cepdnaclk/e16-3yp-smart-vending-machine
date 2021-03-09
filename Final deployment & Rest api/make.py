import pyqrcode 
import png 
from pyqrcode import QRCode 
  
  
# String which represents the QR code 
s = "http://ec2-54-87-72-111.compute-1.amazonaws.com   https://smart-happyvending.herokuapp.com/"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the svg file naming "myqr.svg" 
url.svg("myqr1.svg", scale = 8) 
  
# Create and save the png file naming "myqr.png" 
url.png('myqr1.png', scale = 6) 