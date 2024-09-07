import shutil
import datetime
import os

def backup_files(source,destination):
	today = datetime.date.today()
	backup_file_name = os.path.join(destination,f"backup_{today}") #f means f stering for varivabal ki value ider print hojaye gi
	#backup_file_name = destination,f"backup_{today}"
	shutil.make_archive(backup_file_name,'gztar',source)

source = "/home/vagrant/python-learning"
destination = "/home/vagrant/python-learning/backup_folder"
backup_files(source,destination)
