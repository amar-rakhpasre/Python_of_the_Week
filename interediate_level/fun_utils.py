# *** this is use in 

import os
import datetime

def check_cmd(cmd):
	return os.system(cmd)

#check_cmd("date")
#check_cmd("df -h")
#check_cmd("free")

def show_date():
	 return datetime.datetime.today()

today = show_date()

print(today)
