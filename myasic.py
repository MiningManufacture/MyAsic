############################################ =@GliderTeam 2020=#########################################################
#Monitoring of Bitmain miners S9,S17,L3+################################################################################
import  socket
import threading
import time
import  queue
import os
import json
import telepot
import bitmain_api
import requests
from requests.auth import HTTPDigestAuth
from aio_api_ros import create_rosapi_connection

#user settings##########################################################################################################
ip_gateway = '192.168.11.1'
SetProxy = telepot.api.set_proxy("http://157.245.124.217:3128")
bot = telepot.Bot('921075076:AAH3omROOvV8emtDLcWiZEWAVmwT4-sQ900')
miner_login = 'root'
miner_passw = 'root'
license_key = 'gfdfg76845jhfdg78435hjkgfdy734875u43hg7fguu435y7t3htgjdfng837453ytyrehjgiu'
#end of user settings###################################################################################################

#API####################################################################################################################
def convert(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    return "%dh:%02dm:%02ds" % (hour, min, sec)

# def getasicinfo(ferma,ipp, chats, bot):
def getasicinfo_ghh(ipp):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        sock.connect((ipp, 4028))
        sock.send(bytes(json.dumps({'command': 'stats'}), encoding='utf-8'))
        info = sock.recv(4096)
        info = info+sock.recv(4096)
        info = info + sock.recv(4096)
        info = info.decode()
        info = json.loads(info[:-1].replace('}{', '},{'))
        model = str(info['STATS'][0]['Type'])
        ghh = int(info['STATS'][1]['GHS 5s'].split('.')[0])
        # print(model)
        # print(ghh)
        # if model.find('S9')>0:
        #     minertype = 'S9'
        # if model.find('S17')>0:
        #     minertype = 'S17'
        # if model.find('L3')>0:
        #     minertype = 'L3+'
        # else:
        #     minertype = 'Unknown'
        # print(minertype)
        sock.close()
        return ipp, model, ghh

    except Exception as e:
        sock.close()
        # print(e)
        pass

##############################################END OF API################################################################

#MAIN###################################################################################################################
print('start')
list=[]
ippp=ip_gateway.split('.')
for vv in range(135,139):
   ip=str(ippp[0]+'.'+ippp[1]+'.'+ippp[2]+'.'+str(vv))
   # print(ip)
   info = getasicinfo_ghh(ip)
   if info != None:
       list.append(info)

total = 0
for vv in list:
    total += int(vv[2])

list.append(total)

print(list)

print('end')

