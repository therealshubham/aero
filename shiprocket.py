import requests

authHeader = {"Authorization" : None}

def auth():
	r = requests.post('https://apiv2.shiprocket.in/v1/external/auth/login', json = {
		"email" : "sg49@illinois.edu",
		"password" : "Sg1253**"
	})
	return r.json()

def getShipmentId(orderId):
	r = requests.get('https://apiv2.shiprocket.in/v1/external/orders?search=' + orderId, headers = authHeader)
	return r.json()['data']

def getAWB(shipmentId):
	r = requests.post('https://apiv2.shiprocket.in/v1/external/courier/assign/awb', headers = authHeader, json = {
		"shipment_id" : shipmentId
	})
	return r.json()

def getLabel(shipmentId):
	r = requests.post('https://apiv2.shiprocket.in/v1/external/courier/generate/label', headers = authHeader, json = {
		"shipment_id" : [shipmentId]
	})
	return r.json()