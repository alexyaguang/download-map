#readertwo
def intofiles(inputfile,filenode,fileway,filerelation):
	a=open(inputfile,"r")
	line=a.readline()
	count=0
	nodecoll=""
	relationcoll=""
	waycoll=""
	res=""
	switch =0
	while line:
		if  line.startswith("  <node"):
			switch=1
		elif line.startswith("  <way"):
			switch=2
		elif line.startswith("  <relation"):
			switch=3
		elif line.startswith("</osm>") or line.startswith("<osm"):
			switch=0

		if switch==1:
			nodecoll+=line
		if switch ==2:
			waycoll+=line
		if switch ==3:
			relationcoll+=line
		line=a.readline()

	res_node=open(filenode,"a")
	res_node.write(nodecoll)
	res_node.close()
	res_way=open(fileway,"a")
	res_way.write(waycoll)
	res_way.close()
	res_relation=open(filerelation,"a")
	res_relation.write(relationcoll)
	res_relation.close()

def into_one_file(nodefile,wayfile,relationfile,finalfile):
	prefix="<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<osm version=\"0.6\" generator=\"Overpass API 0.7.56.3 eb200aeb\">\n"
	aftfix="</osm>"
	res=open(finalfile,"w")
	node_content=open(nodefile,"r")
	way_content=open(wayfile,"r")
	relation_content=open(relationfile,"r")
	res.write(prefix)
	res.write(node_content.read())
	res.write(way_content.read())
	res.write(relation_content.read())
	res.write(aftfix)
	node_content.close()
	way_content.close()
	relation_content.close()
	res.close()
