#downloadmaps
import requests
from reader2 import intofiles
from reader2 import into_one_file

#a="wget -O map.osm https://overpass-api.de/api/map?bbox="
#b="-79.415686,43.777433,-79.411130,43.779762"
#os.system(a+b)
dic={}
city="Toronto"
dic["Toronto"]=(-79.407377,43.675783,0.5)#(lon, lat, radis) first two are the location of the city center the last one is the size of the city(half length of a side)
mapsx=[]
mapsy=[]
mapstotal=[]
preurl = 'https://overpass-api.de/api/map?bbox='

vecx=float(dic[city][0]-dic[city][2])
while vecx<=float(dic[city][0]+dic[city][2]):
	vecx+=0.07#limit the size of the block
	mapsx.append(format(vecx,".6f"))

vecy=float(dic[city][1]-dic[city][2])
while vecy<=float(dic[city][1]+dic[city][2]):
	vecy+=0.07#limit the size of the block
	mapsy.append(format(vecy,".6f"))
for i in mapsy:
	mapstotal.append([])
	for j in mapsx:
		mapstotal[-1].append([j,i])
for i in mapstotal:
	print(i)
count=0

for i in range(len(mapstotal)-1):
	count+=1
	for j in range(len(mapstotal[i])-1):
		print(count)
		count+=1
		vec=",".join(mapstotal[i][j]+mapstotal[i+1][j+1])
		print(preurl+vec)
		r = requests.get(preurl+vec)
		a=open("tempory","wb")#tempory file for the downloaded content
		a.write(r.content) 
		a.close()
		intofiles("tempory","filenode","fileway","filerelation")#(new download file,file of node,file of way,file of relation)
		#if count>=25:
			#break
	#if count>=25:
		#break
into_one_file("filenode","fileway","filerelation","res.osm")# the res.osm is the final result 
#line 46-49 are used for test the program, it only download 25 pieces of the maps to save time and space