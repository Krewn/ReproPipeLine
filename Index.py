import os

class indexer:
	path = "~"
	site = "."
	proj = ""
	prod = []
	loc=[]
	
	def __init__(self,p):
		self.path=p
		self.make()
	def fprep(self,name):
		name.replace(".","")
		name.replace("\\","/")
		return(name)
	def refPrep(self):
		ref = self.site
		for qw in self.loc:
			ref+="/"+qw
		return(ref)
	def HtmlFrek(self,adir):
		self.loc.append(adir)
		os.chdir(adir)
		ret="<h2>"+adir+"</h2>"
		files = [f for f in os.listdir('.') if os.path.isfile(f) and f.split(".")[len(f.split("."))-1]=="html"]
		for t in files:
			ret+="<a href ="+self.refPrep()+"/"+self.fprep(t)+">"+self.fprep(t)+"</a><br>\n"
		images = [f for f in os.listdir('.') if os.path.isfile(f) and f.split(".")[len(f.split("."))-1]!="html"]
		for i in images:
			i = self.fprep(i)
			ref = self.refPrep()
			ret+= "<img src="+ref+"/"+i+">\n"
		folders = [f for f in os.listdir(".") if not os.path.isfile(f)]
		for k in folders:
			if(k.__contains__(".")):
				continue
			ret+="<div class='blue1'>"
			ret+=self.HtmlFrek(k)
			ret+="</div>"
		os.chdir("..")
		del self.loc[len(self.loc)-1]
		return(ret)
		
	def HtmlProd(self):
		print("start")
		ret = ""
		ret+="""<!DOCTYPE html><html>"""
		ret+="""
		<head>
			<link rel="stylesheet" type="text/css" href="index.css">
		</head>
		"""
		ret+="<body bgcolor='black'>"
		files = [f for f in os.listdir('.') if os.path.isfile(f) and f.split(".")[len(f.split("."))-1]=="html"]
		for t in files:
			ret+="<a href ="+self.refPrep()+"/"+self.fprep(t)+">"+self.fprep(t)+"</a><br>\n"
		folders = [f for f in os.listdir(".") if not os.path.isfile(f)]
		for k in folders:
			if(k.__contains__(".")):
				continue
			print k
			ret+="<div>"
			ret+=self.HtmlFrek(k)
			ret+="</div>"
		ret+="</body>"
		ret+="""</html>"""
		self.prod = ret
		return(ret)
		
	def cssProd(self):
		#insert Css within quoted area
		return("""
h2{
	color: ghostwhite;
}
a{
	color: darkkhaki;
}
img{
	max-width:636px;
	max-height:495px;
}
		""")
	
	def make(self):
		css = self.cssProd()
		html = self.HtmlProd()
		w = open("index.html","w")
		w.write(html)
		w.close()
		w = open("index.css","w")
		w.write(css)
		w.close()		 
		
i = indexer(".")

#print i.prod


