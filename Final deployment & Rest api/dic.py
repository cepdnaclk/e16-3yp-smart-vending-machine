
import requests, json
import ast  
from pyzbar.pyzbar import decode
from PIL import Image

d = decode(Image.open('test.jpeg'))
data=json.loads(d[0].data.decode('utf-8'))
print(type(data))
print(data)
# print(type(d[0].data.decode('utf-8')))
# print(d[0].data.decode('utf-8'))