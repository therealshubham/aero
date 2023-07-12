import os
import subprocess 
import time
import requests

def print_file(file = None):
	if os.path.exists(file):
		try:
			os.startfile(file, "print")
		except Exception as e:
			print(e)
	else:
		print('-- file does not exist!')
		
def print_file_wrapper(file = None):
	print_file(file)
	time.sleep(2)
	subprocess.call("TASKKILL /F /IM Acrobat.exe", shell = True)

def downloadLabel(labelUrl, orderId, parentFolder):
	r = requests.get(labelUrl, allow_redirects = True)
	open(parentFolder + '/' + orderId + '.pdf', 'wb').write(r.content)