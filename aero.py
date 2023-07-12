import os
import tkinter as tk

from bcolors import *
from db import *
from shiprocket import *
from utils import *
from config import *

# root = tk.Tk()
# root.title("hello")
# root.mainloop()

def mainn():
    # auth for shiprocket
    tokenData = auth()
    authHeader['Authorization'] = 'Bearer ' + tokenData['token']

    printw("-" * 40 + " STARTING " + "-" * 40)

    while 1:
        os.system('cls')
        print("x" * 80)
        # scan order number
        orderNumber = input("scan the barcode...")
        if orderNumber == "x":
            break
        print("1. Read order number as " + orderNumber)
        orderSplit = orderNumber.split("-")
        orderId = orderSplit[0]

        if len(orderSplit) > 1:
            if existsInDB(orderId) == False:
                fraction = orderSplit[1].split("/")
                pushToDB(orderId, int(fraction[1].replace("O", "")), 1)
                prints("...recorded, scan next...")
                continue
            incrementInDB(orderId)
            if checkForCompleteDB(orderId) == False:
                prints("...recorded, scan next...")
                continue

        # get shipment ID
        shipmentData = getShipmentId(orderId)
        shipmentId = None
        if shipmentData:
            shipmentId = shipmentData[0]['shipments'][0]['id']
        else:
            printe("-- invalid order number (ShipmentId error) --")
            continue
        print("2. Shipment ID is " + str(shipmentId))

        # get AWB of shipment ID
        awbData = getAWB(shipmentId)
        awb = None
        if 'status_code' in awbData:
            printe("-- invalid order number (AWB error) --")
            printe(awbData['message'])
            continue
        if awbData['awb_assign_status'] == 0:
            printe("-- 3. (AWB error) --")
            printe("-- " + awbData['response']['data']['awb_assign_error'])
        else:
            awb = awbData['response']['data']['awb_code']
            print("3. AWB assigned is " + str(awb))

        # get label url
        labelData = getLabel(shipmentId)
        labelUrl = None
        if labelData['label_created'] == 1:
            labelUrl = labelData['label_url']
        else:
            printe("-- invalid order number (Label error) --")
            continue
        print("4. Label url is " + labelUrl)

        # download label
        downloadLabel(labelUrl, orderId, parentFolder)
        if os.path.exists(parentFolder + '/' + str(orderId) + '.pdf'):
            prints("5. Label is downloaded!")
        else:
            continue

        # print the file
        print_file_wrapper(parentFolder + '/' + str(orderId) + '.pdf')
        prints("check for printed file...!")

# start program
mainn()
