import time
from datetime import datetime as dt
host_temp="H:\hamza#1\PYTHON\hosts"
host_path=r"C:\Windows\System32\drivers\etc"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","fb.com"]
while True:
	if dt(dt.now().year,dt.now().month,dt.now().day,9,58) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
		print("Working Hours...")
		with open(host_temp,'r+') as file:
			content=file.read()
			for website in website_list:
				if website in content:
					pass
				else:
					file.write(redirect +" "+ website+"\n")
	else:
		with open(host_temp,'r+') as file:
			content=file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate()
		print("FUN HOURS.....")
	time.sleep(5)
