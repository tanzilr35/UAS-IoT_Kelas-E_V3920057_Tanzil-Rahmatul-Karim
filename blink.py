import httplib2
import urllib
import random
import http.client
from time import localtime, strftime
from urllib.request import urlopen as uReq
import serial
import time
import requests as req
import json
arduino = serial.Serial('COM1,9600')

key = "QOB9NNMWOLT2BRF5" # API Key dari ThingSpeak

def ledControl(cmd):
  arduino.write(cmd.encode())

while True:
  print ("Data berhasil dikirim ke channel Blink ThingSpeak")
  time.sleep(1)
  data = random.randint(0,250)

  params = urllib.parse.urlencode({'field1':data, 'key':key})
  headers = {'Content-typeZZe' : 'application/x-www-form-urlencoded', 'Accept' : 'text/plain'}
  conn = http.client.HTTPConnection('api.thingspeak.com:80')

  rawArd = arduino.readline()
  data = rawArd[0:len(rawArd)-2].decode('utf-8')
  resp = req.get(""+data)
  dataWeb = json.loads(resp.text)
  if dataWeb['1'] == '1':
    ledControl('A')
  elif dataWeb['1'] == '0':
    ledControl('B')
  
  if dataWeb['2'] == '1':
    ledControl('C')
  elif dataWeb['2'] == '0':
    ledControl('D')

  if dataWeb['3'] == '1':
    ledControl('E')
  elif dataWeb['3'] == '0':
    ledControl('F')

  if dataWeb['4'] == '1':
    ledControl('G')
  elif dataWeb['4'] == '0':
    ledControl('H')
  
  time.sleep(1)