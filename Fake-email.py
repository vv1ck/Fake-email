import requests,secrets,json,time
Coke = secrets.token_hex(8)*2
from user_agent import generate_user_agent
r = requests.session()
print("""
      __      _ 
     / _|    | |    By JOKER @vv1ck
    | |_ __ _| | _____
    |  _/ _` | |/ / _ \ ┌─┐┌┬┐┌─┐┬┬
    | || (_| |   <  __/ ├┤ │││├─┤││
    |_| \__,_|_|\_\___| └─┘┴ ┴┴ ┴┴┴─
          Create fake email""")
def CODE():
  global sisn , tim
  while True:
    ERR = 0
    urlCOD = 'https://10minutemail.net/address.api.php?sessionid='+sisn+'&_='+tim
    try:
      time.sleep(4)
      send2 = r.get(urlCOD)
      msg = send2.json()['mail_list'][ERR]['subject']
      if msg.find('Hi, Welcome to 10 Minute Mail')>=0:
        print(f'[!] No messages yet ')
        print(' ━━━━━━━━━━━━━━━━━━━━━')
      elif '"from"'in send2.text:
        eml = send2.json()['mail_list'][ERR]['from']
        TM = send2.json()['mail_list'][ERR]['datetime']
        print('From email: '+eml)
        print('data time: '+TM)
        print('New messages : '+msg)
        print(' ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
      elif '"datetime"'in send2:
        TM = send2.json()['mail_list'][ERR]['datetime']
        print('data time: '+TM)
        print('New messages : '+msg)
        print(' ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
      else:
        print('[*] Email expired ..')
        input(' ')
        exit()
    except TypeError:
      print('[*] Email expired ..')
      input(' ')
      exit()
    except AttributeError:
      print('sorry')
      exit()#by @vv1ck
def EmAIl():
  global sisn , tim
  vv1ck = 'https://10minutemail.net/address.api.php?'
  headers = {
  'Host':'10minutemail.net',
  'Cookie':Coke,
  'User-Agent':generate_user_agent(),
  'Accept':'application/json,',
  'Accept-Language':'en-US,en;q=0.5',
  'Accept-Encoding':'gzip,',
  'X-Requested-With':'XMLHttpRequest',
  'Referer':'https://10minutemail.net/m/?lang=ar',
  'Te':'trailers',
  'Connection':'close'}
  send = r.get(vv1ck,headers=headers)
  email = str(send.json()['mail_get_mail'])
  sisn = str(send.json()['session_id'])
  tim = str(send.json()['mail_get_time'])
  print('  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
  print('   [$] Email: '+email+'')
  print('  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
  time.sleep(1)
  CODE()
EmAIl()
