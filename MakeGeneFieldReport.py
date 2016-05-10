# _  _  _____  __ __  _     ___  ___  ___   __   ___  _____  ___  ___  
#| || ||_   _||  V  || |   | _ \| __|| _,\ /__\ | _ \|_   _|| __|| _ \ 
#| >< |  | |  | \_/ || |_  | v /| _| | v_/| \/ || v /  | |  | _| | v / 
#|_||_|__|_|__|_|_|_||___| |_|_\|___||_|  _\__/_|_|_\__|_|  |___||_|_\ 
# __  / _]| __||  \| || __| | __|| || __|| |  | _\ /' _/ __            
#|__|| [/\| _| | | ' || _|  | _| | || _| | |_ | v |`._`.|__|           
#     \__/|___||_|\__||___| |_|  |_||___||___||__/ |___/      

#author : Kevin Nelson

import csv
import os
import sys

os.chdir("geneFieldsOP13")
files = [f for f in os.listdir('.') if os.path.isfile(f)]
opM=""
opHTML='<<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html smlns="http://www.w3.org/1999/xhtml">\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n<title>Genes</title>\n<style type="text/css">\n<!--\nbody {\nfont: 100% Verdana, Arial, Helvetica, sans-serif;\nbackground: #666666;\n	margin: 0; /* its good practice to zero the margin and padding of the body element to account for differing browser defaults */\npadding: 0;\ntext-align: center; /* this centers the container in IE 5* browsers. The text is then set to the left aligned default in the #container selector */\ncolor: #000000;\n}\n.oneColLiqCtr #container {\nwidth: 500px;  /* this will create a container 80% of the browser width */\nbackground: #FFFFFF;\nmargin: 0 auto; /* the auto margins (in conjunction with a width) center the page */\nborder: 1px solid #000000;\ntext-align: left; /* this overrides the text-align: center on the body element. */\n}\n.oneColLiqCtr #mainContent {\npadding: 12px 20px 0 20px; /* remember that padding is the space inside the div box and margin is the space outside the div box */\n}\n-->\n</style>\n<script src="http://lrrpublic.cli.det.nsw.edu.au/lrrSecure/Sites/LRRView/10378/applets/spry/SpryAssets/SpryCollapsiblePanel.js" type="text/javascript"></script>\n<script src="http://lrrpublic.cli.det.nsw.edu.au/lrrSecure/Sites/LRRView/10378/applets/spry/Scripts/swfobject_modified.js" type="text/javascript"></script>\n<script src="http://lrrpublic.cli.det.nsw.edu.au/lrrSecure/Sites/LRRView/10378/applets/spry/SpryAssets/SpryMenuBar.js" type="text/javascript"></script>\n<link href="http://lrrpublic.cli.det.nsw.edu.au/lrrSecure/Sites/LRRView/10378/applets/spry/CSS/Level3_3.css" rel="stylesheet" type="text/css">\n<link href="http://lrrpublic.cli.det.nsw.edu.au/lrrSecure/Sites/LRRView/10378/applets/spry/SpryAssets/SpryCollapsiblePanel.css" rel="stylesheet" type="text/css">\n<link href="http://lrrpublic.cli.det.nsw.edu.au/lrrSecure/Sites/LRRView/10378/applets/spry/SpryAssets/SpryMenuBarHorizontal_edited.css" rel="stylesheet" type="text/css">\n<style type="text/css" media="screen">#FlashID {visibility:hidden}</style></head>\n'
opHTML+='<body>'
opHTML+='<h1>All Genes</h1>'
genes={}
for k in files:
	if(k[-1:]=='m'):
		k2=0
		if(('_' in k)==True):
			while k[k2]!='_':
				k2+=1
			if((k[0:k2] in genes.keys()) == False):
				genes[k[0:k2]]=''
				genes[k[0:k2]]+='<div id="'+k[0:k2]+'" class="CollapsiblePanel CollapsiblePanelClosed">\n<div class="CollapsiblePanelTab" tabindex="0">'+k[0:k2]+'</div>\n<div class="CollapsiblePanelContent" style="display: none; visibility: visible; height: 0px;">\n'
			#print(k[0:k2] in genes.keys())
			if(k[-6:-2]=='OAC1'):
				genes[k[0:k2]]+='<img src="./geneFieldsOP13/'+k[:-6]+'_poly.jpg" width="800" height="600">\n'
				genes[k[0:k2]]+='<img src="./geneFieldsOP13/'+k[:-2]+'.jpg" width="800" height="600">\n'
			opM+=k[:-2]+'\n'+'contourf(flipud(fliplr('+k[:-2]+'\')))\ncaxis([0,1])\ncolorbar\ntitle("'+k[:-2]+'")\nxlabel("PC1")\nylabel("PC3")\nprint -djpg "'+k[:-2]+'.jpg"\n'
for k in genes:
	genes[k]+='<a href = ./G/'+k+'/'+k+'.html>'+k+'</a>'
	opHTML+=genes[k]+'</div></div>\n'
n=0
opHTML+='<script type="text/javascript">\n'
opHTML+='var CollapsiblePanel=['
for k in genes:
	opHTML+='new Spry.Widget.CollapsiblePanel("'+k+'", {contentIsOpen:false}),\n'
	n+=1
opHTML=opHTML[:-1]+'];'
opHTML+='swfobject.registerObject("FlashID");\nvar MenuBar1 = new Spry.Widget.MenuBar("MenuBar1", {imgDown:"SpryAssets/SpryMenuBarDownHover.gif", imgRight:"SpryAssets/SpryMenuBarRightHover.gif"});</script>\n'
temp = open('DrawGF.m',"w")
temp.write(opM)
temp.close
os.chdir("..")
temp = open('GeneFields13.html',"w")
temp.write(opHTML)
temp.close
	
	
