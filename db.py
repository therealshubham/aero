import pymysql

def pushToDB(orderId, total_items, scanned_items):
	con = pymysql.connect(host='172.106.0.55', port=10176, user='Shubham', passwd='Sg1253**', database='aero')
	with con.cursor() as cur:
		cur.execute("INSERT IGNORE INTO `labels` (`order_number`, `total_items`, `scanned_items`) VALUES ('" + orderId + "', " + str(total_items) + ", " + str(scanned_items) + ")")
	con.commit()
	con.close()

def incrementInDB(orderId):
	con = pymysql.connect(host='172.106.0.55', port=10176, user='Shubham', passwd='Sg1253**', database='aero')
	with con.cursor() as cur:
		cur.execute("UPDATE `labels` SET `scanned_items` = `scanned_items` + 1 WHERE `order_number` = '" + orderId + "'")
	con.commit()
	con.close()

def checkForCompleteDB(orderId):
	con = pymysql.connect(host='172.106.0.55', port=10176, user='Shubham', passwd='Sg1253**', database='aero')
	with con.cursor() as cur:
		cur.execute("SELECT * FROM `labels` WHERE `order_number` = '" + orderId + "'")
		data = cur.fetchone()
		if int(data[1]) <= int(data[2]):
			con.close()
			return True
	con.close()
	return False	

def existsInDB(orderId):
	con = pymysql.connect(host='172.106.0.55', port=10176, user='Shubham', passwd='Sg1253**', database='aero')
	with con.cursor() as cur:
		cur.execute("SELECT * FROM `labels` WHERE `order_number` = '" + orderId + "'")
		data = cur.fetchone()
		if data != None:
			con.close()
			return True
	con.close()
	return False