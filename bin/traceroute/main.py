import sys
import socket
from bin.traceroute.plot import *
from bin.traceroute.getloc import *
from bin.traceroute.trace import *

def Traceroute(dest):
  sender_location = getMyLoc()
  destination_ip = socket.gethostbyname(dest)
  destination_location = getTargetLoc(destination_ip)
  ip_list = traceroute(dest)
  
  route_location_list = getLoc(ip_list)
  route_location_list.insert(0, sender_location)
  route_location_list.append(destination_ip)
  
  # initialize map
  figure = go.Figure()
  mapsInit(figure)
  
  route_location_longitute = []
  route_location_latitute = []
  
  longitute = 0
  latitute = 0
  
  for x in route_location_longitute:
    if x[1][0] - longitute == 0 or x[1][1] - latitute == 0:
      continue
    route_location_longitute.append(x[1][0])
    route_location_latitute.append(x[1][1])
    
    longitute = x[1][0]
    latitute = x[1][1]
    
  # creating the route
  for i in range(len(route_location_longitute)-1):
      for x in route_location_list:
          if (route_location_longitute[i],route_location_latitute[i]) in x:
              route_city = x[2]
              route_ip = x[0]
      print(route_ip,'---',route_city)
      addRoute(figure,f'route{i}',((route_location_longitute[i:i+2],route_location_latitute[i:i+2]),route_city))
  print(destination_ip[0],'---',destination_location[2])
  
  # marking the source IP and destination IP
  mark(figure,f'My IP - {sender_location[2]}', sender_location[1])
  mark(figure,f'{dest} - {destination_location[2]}',destination_location[1],name=dest)
  
  figure.show()