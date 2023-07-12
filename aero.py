import tkinter as tk

root = tk.Tk()

root.title("hello")

root.mainloop()

# import os
# import subprocess 
# import time
# import requests
# import pymysql

# authHeader = {"Authorization" : None}
# parentFolder = 'tests'

# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'

#     def disable(self):
#         self.HEADER = ''
#         self.OKBLUE = ''
#         self.OKGREEN = ''
#         self.WARNING = ''
#         self.FAIL = ''
#         self.ENDC = ''
	
# def printw(str):
# 	print(bcolors.WARNING + str + bcolors.ENDC)

# def printe(str):
# 	print(bcolors.FAIL + str + bcolors.ENDC)

# def prints(str):
# 	print(bcolors.OKGREEN + str + bcolors.ENDC)

# def auth():
# 	r = requests.post('https://apiv2.shiprocket.in/v1/external/auth/login', json = {
# 		"email" : "sg49@illinois.edu",
# 		"password" : "Sg1253**"
# 	})
# 	return r.json()

# def print_file(file = None):
# 	if os.path.exists(file):
# 		try:
# 			os.startfile(file, "print")
# 		except Exception as e:
# 			print(e)
# 	else:
# 		print('-- file does not exist!')
		
# def print_file_wrapper(file = None):
# 	print_file(file)
# 	time.sleep(2)
# 	subprocess.call("TASKKILL /F /IM Acrobat.exe", shell = True)

# def getShipmentId(orderId):
# 	r = requests.get('https://apiv2.shiprocket.in/v1/external/orders?search=' + orderId, headers = authHeader)
# 	return r.json()['data']

# def getAWB(shipmentId):
# 	r = requests.post('https://apiv2.shiprocket.in/v1/external/courier/assign/awb', headers = authHeader, json = {
# 		"shipment_id" : shipmentId
# 	})
# 	return r.json()

# def getLabel(shipmentId):
# 	r = requests.post('https://apiv2.shiprocket.in/v1/external/courier/generate/label', headers = authHeader, json = {
# 		"shipment_id" : [shipmentId]
# 	})
# 	return r.json()

# def downloadLabel(labelUrl, orderId, parentFolder):
# 	r = requests.get(labelUrl, allow_redirects = True)
# 	open(parentFolder + '/' + orderId + '.pdf', 'wb').write(r.content)

# def pushToDB(orderId, total_items, scanned_items):
# 	con = pymysql.connect(host='172.106.0.55', port=10176, user='Shubham', passwd='Sg1253**', database='aero')
# 	with con.cursor() as cur:
# 		cur.execute("INSERT IGNORE INTO `labels` (`order_number`, `total_items`, `scanned_items`) VALUES ('" + orderId + "', " + str(total_items) + ", " + str(scanned_items) + ")")
# 	con.commit()
# 	con.close()

# def incrementInDB(orderId):
# 	con = pymysql.connect(host='172.106.0.55', port=10176, user='Shubham', passwd='Sg1253**', database='aero')
# 	with con.cursor() as cur:
# 		cur.execute("UPDATE `labels` SET `scanned_items` = `scanned_items` + 1 WHERE `order_number` = '" + orderId + "'")
# 	con.commit()
# 	con.close()

# def checkForCompleteDB(orderId):
# 	con = pymysql.connect(host='172.106.0.55', port=10176, user='Shubham', passwd='Sg1253**', database='aero')
# 	with con.cursor() as cur:
# 		cur.execute("SELECT * FROM `labels` WHERE `order_number` = '" + orderId + "'")
# 		data = cur.fetchone()
# 		if int(data[1]) <= int(data[2]):
# 			con.close()
# 			return True
# 	con.close()
# 	return False	

# def existsInDB(orderId):
# 	con = pymysql.connect(host='172.106.0.55', port=10176, user='Shubham', passwd='Sg1253**', database='aero')
# 	with con.cursor() as cur:
# 		cur.execute("SELECT * FROM `labels` WHERE `order_number` = '" + orderId + "'")
# 		data = cur.fetchone()
# 		if data != None:
# 			con.close()
# 			return True
# 	con.close()
# 	return False

# def mainn():

# 	# auth for shiprocket
# 	tokenData = auth()
# 	authHeader['Authorization'] = 'Bearer ' + tokenData['token']

# 	printw("-" * 40 + " STARTING " + "-" * 40)
	
# 	while (1):
# 		os.system('cls')
# 		print("x" * 80)
# 		# scan order number
# 		orderNumber = input("scan the barcode...")
# 		if orderNumber == "x":
# 			break
# 		print("1. Read order number as " + orderNumber)
# 		orderSplit = orderNumber.split("-")
# 		orderId = orderSplit[0]

# 		if len(orderSplit) > 1:
# 			if existsInDB(orderId) == False:
# 				fraction = orderSplit[1].split("/")
# 				pushToDB(orderId, int(fraction[1].replace("O", "")), 1)
# 				prints("...recorded, scan next...")
# 				continue
# 			incrementInDB(orderId)
# 			if checkForCompleteDB(orderId) == False:
# 				prints("...recorded, scan next...")
# 				continue

# 		# get shipment ID
# 		shipmentData = getShipmentId(orderId)
# 		shipmentId = None
# 		if shipmentData:
# 			shipmentId = shipmentData[0]['shipments'][0]['id']
# 		else:
# 			printe("-- invalid order number (ShipmentId error) --")
# 			continue
# 		print("2. Shipment ID is " + str(shipmentId))

# 		# get AWB of shipment ID
# 		awbData = getAWB(shipmentId)
# 		awb = None
# 		if 'status_code' in awbData:
# 			printe("-- invalid order number (AWB error) --")
# 			printe(awbData['message'])
# 			continue
# 		if awbData['awb_assign_status'] == 0:
# 			printe("-- 3. (AWB error) --")
# 			printe("-- " + awbData['response']['data']['awb_assign_error'])
# 		else:
# 			awb = awbData['response']['data']['awb_code']
# 			print("3. AWB assigned is " + str(awb))

# 		# get label url
# 		labelData = getLabel(shipmentId)
# 		labelUrl = None
# 		if labelData['label_created'] == 1:
# 			labelUrl = labelData['label_url']
# 		else:
# 			printe("-- invalid order number (Label error) --")
# 			continue
# 		print("4. Label url is " + labelUrl)

# 		# download label
# 		downloadLabel(labelUrl, orderId, parentFolder)
# 		if os.path.exists(parentFolder + '/' + str(orderId) + '.pdf'):
# 			prints("5. Label is downloaded!")
# 		else:
# 			continue

# 		# print the file
# 		print_file_wrapper(parentFolder + '/' + str(orderId) + '.pdf')
# 		prints("check for printed file...!")

# # start program
# mainn()
