#!/usr/bin/env python3
import requests
import socket
import time

httpUrl = 'https://google.com'
dnsDomain = 'google.com'


def test_http():
  try:
    response = requests.get(httpUrl)
    if response.status_code == 200:
      return True
    else:
      print(f'error in http load, error code: {response.status_code}')
      return False
  except Exception as e:
    print(f'error in http load: {e}')
    return False


def test_dns():
  try:
    result = socket.gethostbyname(dnsDomain)
    if not result:
      return False
    else:
      return True
  except Exception as e:
    print(f'error in dns test: {e}')
    return False


while True:
  http_status = test_http()
  if http_status is True:
    print('HTTP OK')
  else:
    print('HTTP Fail')

  dns_status = test_dns()
  if dns_status is True:
    print('DNS OK')
  else:
    print('DNS Fail')

  time.sleep(5)
