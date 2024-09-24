#python3 sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km s_km e_km z_km
# sez_to_ecef.py
#
# Usage: sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km s_km e_km z_km
#  Text explaining script usage
# Parameters:
#  o_lat_deg latitude in degrees
#  o_lon_deg longitude in degrees
#  o_hae_km height above 
#
# Output:
#  A description of the script output
# ecef_x_km
# ecef_y_km
# ecef_z_km 
# ecef vector in km
# Written by Chatham Campbell

# import Python modules
import math
import sys # argv

# initialize script arguments
o_lat_deg = float('nan')
o_lon_deg = float('nan') 
o_hae_km = float('nan') 
s_km = float('nan') 
e_km = float('nan') 
z_km = float('nan') 

# parse script arguments
if len(sys.argv)==7:
  o_lat_deg = float(sys.argv[1])
  o_lon_deg = float(sys.argv[2]) 
  o_hae_km = float(sys.argv[3])
  s_km = float(sys.argv[4]) 
  e_km = float(sys.argv[5]) 
  z_km = float(sys.argv[6]) 
else:
  print(\
   'Usage: '\
   'python3 sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km s_km e_km z_km'\
  )
  exit()
# write script below this line
Ry = [
    [sin(o_lon_deg), 0, cos(o_lon_deg)],
    [0, 1, 0],
    [-cos(o_lon_deg), 0, sin(o_lon_deg)]  
  ]
rSEZ = [s_km, e_km, z_km]
firstRotation = Ry * rSEZ
Rz = [
  [cos(o_lat_deg), -sin(o_lat_deg), 0],
  [sin(o_lat_deg), cos(o_lat_deg), 0],
  [0, 0, 1]
]
rECEF = Rz*firstRotation
ecef_x_km = rECEF[0]
ecef_y_km = rECEF[1]
ecef_z_km = rECEF[2]
print(ecef_x_km)
print(ecef_y_km)
print(ecef_z_km)
#sez_to_ecef.py 37.207 -80.419 0.63 -.5 0 .15