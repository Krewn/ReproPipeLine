import GeneFeilds as gf


def prDict2(sdmB):					# This is usful for printing csv files.######################
	op=''
	First=True
	for k in sdmB:
		if First:
			First= False
		else:
			if(op[len(op)-1]==','):op=op[0:len(op)-1]+'\n'
		for k2 in sdmB[k]:
			try:
				op += str(sdmB[k][k2])
			except(TypeError):
				op+=str(k2)
			op += ','
	if(op[len(op)-1]==','):op=op[0:len(op)-1]+'\n'
	op+='\n'
	return(op)
def prDictAlt(Dists):
	#print Dists.keys()
	#for k in Dists.keys():
		#print (len(Dists[k]))
	tail=""						#Here we will us it to construct a predetermined input for R##
	#n=0						#With a columns 'Time',gene1,gene2,gene3...###################
	for k in Dists:					#################val###val###val###val########################
		#print k		
		for k2 in Dists[k]:			#################val...val...val...val########################
			#print k2			
			tail+=str(k2)+','		##############################################################
			#n2+=1
		tail=tail[0:len(tail)-1]
		tail+="\n"
	tail=tail[0:len(tail)-1]
	#Head+="\n"
	return(tail)

def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

def getColNames(data):
	try:
		names=[""]*(len(data[0]))
		for k in range(0,len(data[0]),1):
			names[k]=data[0][k]
		return(names)
	except(KeyError):
		ky = data.keys()
		names=[""]*(len(data[ky[0]]))
		for k in range(0,len(data[k2]),1):
			names[k]=data[k2][k]
		return(names)

def getRowNames(data):
	try:
		names=[""]*(len(data))
		for k in range(0,len(data),1):
			names[k]=data[k][0]
		return(names)
	except(KeyError):
		names=[""]*(len(data))
		n=0
		for k in data:
			names[n]=data[k][1]
			n+=1
		return(names)

def getTypes(samples):
	Type=['']*len(samples)
	for k in range(0,len(samples),1):
		for k2 in range(0,len(samples[k]),1):
			if samples[k][k2]=='B' and samples[k][k2+1]=='J':
				Type[k]='Fib'
			if samples[k][k2]=='H' and (samples[k][k2+1]=='1' or samples[k][k2+1]=='9'):
				Type[k]='hESC'
			if samples[k][k2]=='S' and samples[k][k2+5]=='-' and samples[k][k2+14]=='-':
				Type[k]='--'
			if samples[k][k2]=='S' and samples[k][k2+5]=='+' and samples[k][k2+14]=='-':
				Type[k]='+-'
			if samples[k][k2]=='S' and samples[k][k2+5]=='+' and samples[k][k2+14]=='+':
				Type[k]='++'
	return (Type)

def ltd(l):
		n=0
		d={}
		for k in l:
			d[n]=k
			n+=1
		return(d)

def getST(samples):			
	S=['']*len(samples)
	T=['']*len(samples)
	hesc=['']*len(samples)
	fib = ['']*len(samples)
	for k in range(0,len(samples),1):
		for k2 in range(0,len(samples[k]),1):
			if samples[k][k2]=='B' and samples[k][k2+1]=='J':
				fib[k]='+'
			if samples[k][k2]=='H' and (samples[k][k2+1]=='1' or samples[k][k2+1]=='9'):
				hesc[k]='+'
			if samples[k][k2]=='S' and samples[k][k2+5]=='-' and samples[k][k2+14]=='-':
				S[k]='-'
				T[k]='-'
			if samples[k][k2]=='S' and samples[k][k2+5]=='+' and samples[k][k2+14]=='-':
				S[k]='+'
				T[k]='-'
			if samples[k][k2]=='S' and samples[k][k2+5]=='+' and samples[k][k2+14]=='+':
				S[k]='+'
				T[k]='+'
	#print S, T, hesc, fib
	a = {'SEA4':ltd(S),'TRA160':ltd(T),'hesc':ltd(hesc),'fib':ltd(fib)}
	return (a)

def getTypesMP(samples):
	Type=getTypes(samples)
	TypeMP= ['']*len(samples)
	for k in range(0,len(samples),1):
		for k2 in range(0,len(samples[k]),1):
			if samples[k][k2]=='M' and samples[k][k2+1]=='O' and samples[k][k2+2]=='N' and samples[k][k2+3]=='O':
				TypeMP[k]='mono'
	for k in range(0,len(samples)):
		if TypeMP[k] != 'mono':
			Type[k] = ''
	#print len(Type)
	#print len(TypeMP)
	for k in range(0,len(samples)):
			try:
				if TypeMP[k] != 'mono' and Type[k] != 'Fib' and Type[k] != 'hESC':
					TypeMP[k]='poly'
			except(IndexError):
				TypeMP[k]='poly'
	days=getdays(samples)
	stats=getST(samples)
	return ({'ID':Type,'MvP':TypeMP,'day':days,'SEA4':stats['SEA4'],'TRA160':stats['TRA160'],'hESC':stats['hesc'],'Fib':stats['fib']})

def getdays(samples):								#Parsing based on predetermined naming convention.
	day=[0]*len(samples)							#
	for k in range(1,len(samples)-1,1):
		for k2 in range(0,len(samples[k])):
			if samples[k][k2]=='D':
				#print samples[k]
				if is_number(samples[k][k2+1]+samples[k][k2+2]):			
					day[k]=float(samples[k][k2+1]+samples[k][k2+2])
				elif is_number(samples[k][k2+1]):
					day[k]=flaot(samples[k][1])
	#print '##'	
	#print (day)	
	return(day)

def EUC (BData,Type):
	#print Type
	#print BData
	fibAvg   =[0]*len(BData[0])
#	for k in BData:
#		if (len(BData[k])!= len(BData[0])):
#			print 'the fuck mang' 
#		else: print k
	fibCount =0
	hESCAvg  =[0]*len(BData[0])
	hESCCount=0
	#BData[1][len(BData[1])-1]
	#ke = BData.keys()
#	print ke
#	print len (BData)
#	print len (BData[ke[0]])
	for k in range(0,len(BData),1):						#Establish FIB and hESC average
		if(Type[k]=="Fib"):
			#print 'fib'
			fibCount+=1
			for k2 in range(0,len(BData[1])-1,1):
				if(is_number(BData[k][k2])):			
					fibAvg[k2]+=float(BData[k][k2])		
		if(Type[k]=="hESC"):
			#print 'hesc'
			hESCCount+=1
			for k2 in range(0,len(BData[k])-1,1):
				if(is_number(BData[k][k2])):
					hESCAvg[k2]+=float(BData[k][k2])
	#print fibCount
	#print hESCCount
	for k in range(0,len(fibAvg),1):					#fibAvg & hESCAvg have the same length
		fibAvg[k]=fibAvg[k]/fibCount
		hESCAvg[k]=hESCAvg[k]/hESCCount


	eucDistFib=[0]*len(BData)
	eucDisthESC=[0]*len(BData)
	fd=0
	hd=0

	for k in range(0,len(BData),1):
		fd=0
		hd=0
		for k2 in range(0,len(BData[k]),1):
			if(is_number(BData[k][k2])):
				fd+=(BData[k][k2]-fibAvg[k2])*(BData[k][k2]-fibAvg[k2])
				hd+=(BData[k][k2]-hESCAvg[k2])*(BData[k][k2]-hESCAvg[k2])
		eucDistFib[k]=fd**0.5
		eucDisthESC[k]=hd**0.5
	return(eucDistFib,eucDisthESC)

def GetTimes(eucDistFib,eucDisthESC,BData):
	FibFib=0								#Fibroblas center on Fibdist
	FibEsc=0								#Fibroblas center on HescDist
	EscFib=0								#Hesc center on Fib
	EscEsc=0								#Hesc senter on Hesc

	fibCount =0
	hESCCount=0
	Type = getTypes(getRowNames(BData))

	for k in range (0,len(BData),1):
		if Type[k]=="Fib" :
			fibCount+=1
			FibFib+=eucDistFib[k]
			FibEsc+=eucDisthESC[k]	
		if Type[k]=="hESC":
			hESCCount+=1
			EscFib+=eucDistFib[k]
			EscEsc+=eucDisthESC[k]

	EscFib/=hESCCount
	EscEsc/=hESCCount
	FibFib/=fibCount
	FibEsc/=fibCount
	#print EscFib
	#print EscEsc
	#print FibFib
	#print FibEsc
	FibD=EscFib-FibFib							#component on fibroblast axis of vector T in Euc space
	EscD=EscEsc-FibEsc							#component on Hesc axis of vector T in Euc space
	magT=(FibD**2 + EscD**2)**0.5

	times=[]
	for k in range(0,len(eucDistFib)):
		if is_number(eucDistFib[k]):
			times.append((eucDistFib[k]*FibD+eucDisthESC[k]*EscD)/magT)
		else:
			print "mmk"
	return(times)

def DimensionalReduct(Data):
	prDict2(Data)
	well={}
	well['genes']=getColNames(Data)
	well['samples']=getRowNames(Data)
	well['Day']=getdays(well['samples'])
	#print (well['samples'])
	print('pcaStart')
	well['PCA']=gf.PCA(Data)
	print('pcaEnd')
	well['type']=getTypes(well['samples'])
	#print (well['type'])
	well['euc']={}
	print('EucStart')
	well['euc']=EUC(Data,well['type'])
	well['time']=GetTimes(well['euc'][0],well['euc'][1],Data)
	print('EucEnd')
	first=True
	_k=0
	water={}
	for k in Data:
		#print('-')
		bucket=[]
		if first:
			#print('--')
			first=False
			bucket=Data[k]
			for k2 in well['PCA']:
				_k3=0
				for k3 in k2:
					#print k3
					bucket.append('PCA'+str(_k3))
					_k3+=1
				break
			bucket.append('EucDFib')
			bucket.append('EucDHesc')
			bucket.append('time')
			bucket.append('type')
			bucket.append('day')
		else:
			#print k
			#print('---')
			for k2 in Data[k]:
				bucket.append(k2)
			for k3 in well['PCA'][k-1]:
				#print k3
				bucket.append(k3)
			bucket.append(well['euc'][0][_k])
			bucket.append(well['euc'][1][_k])
			bucket.append(well['time'][_k])
			bucket.append(well['type'][_k])
			bucket.append(well['Day'][_k])
		_k=_k+1
		water[k]=bucket
	return(water)

def getHescFib(File1,FileWithFib_Hesc):
	known = getTypesMP(getRowNames(File1))
	hasHESC=False
	hasfib=False
	#print known
	for k in known['hESC']:
		if known['hESC'][k] == '+':
			hasHESC=True
	for k in known['Fib']:
		if known['Fib'][k] == '+':
			hasfib=True
	#print 'hasHESC:',hasHESC
	#print 'hasfib:',hasfib
	n = 0
	#print '!!!!!!!!'
	if(hasHESC == False):
		known2 = getTypesMP(getRowNames(FileWithFib_Hesc))
		k2 = 0
		for k in FileWithFib_Hesc:
			try:
				if known2['ID'][k] == 'hESC' or known2['hESC'][k] == '+':
					File1[len(File1)]=FileWithFib_Hesc[k]
			except(TypeError):
				if known2['ID'][k2] == 'hESC' or known2['hESC'][k2] == '+':
					File1.append(k)
			k2+=1
	if(hasfib == False):
		k2 = 0
		known2 = getTypesMP(getRowNames(FileWithFib_Hesc))
		for k in FileWithFib_Hesc:
			try:
				if known2['ID'][k] == 'Fib' or known2['Fib'][k] == '+':
					File1[len(File1)]=FileWithFib_Hesc[k]
			except(TypeError):
				if known2['ID'][k2] == 'Fib' or known2['Fib'][k2] == '+':
					File1.append(k)
			k2+=1
	return(File1)

def doEverything():
	data = gf.readFiles()

	Agg={}				# Combined the 2 inputs into one table
	r=0
	c=0
	first = True
	First = True
	uids=[]
	ids=[]
	for k in data:
		uids.append(k)
		#print k
		if first:
			Agg[r]=[]
			first=False				#The first row or heading is only required in the first file
			for k2 in data[k][data[k].keys()[0]]:
				Agg[r].append(k2)
			ids.append("NULL")
			r=r+1
		First=True
		for k2 in data[k]:
			Agg[r]=[]
			if First:
				First=False
			else:	#Make an agragate table - It is important to note that this assumes Assays are alligned across input tables.
				for k3 in data[k][k2]:
					Agg[r].append(k3)
				r+=1
				ids.append(k)
	for f in data:
		if f[0]=='_':
			if f[1]=='_':
				Twep=f	
	for k in data:
		if k != Twep:
			data[k]=getHescFib(data[k],data[Twep])
	prDict2(Agg)
	a = DimensionalReduct(Agg)
	print('PrintingStart')
	op = open('outPut',"w")
	op.write(prDictAlt(a))
	op.close
	print('PrintingComplete')
	Agg[0]=Agg[0][0:len(Agg[1])]
	temp={}
	temp['Agg']=Agg
	a = gf.doEverything1(temp,ids,uids) # # GeneFields[f][g][k0][_k][_k2]
	if not gf.os.path.exists('geneFieldsOP13'):
    		gf.os.makedirs('geneFieldsOP13')
	gf.os.chdir('geneFieldsOP13')
	for k in a:
		for k2 in a[k]:
			for k3 in a[k][k2]:
				temp = open(str(k2)+str(k3)[:-4]+'.csv',"w")
				temp.write(prDict2(a[k][k2][k3]))
				temp.close()
				temp = open(str(k2)+str(k3)[:-4]+'.m',"w")
				temp.write(gf.octPrt(a[k][k2][k3],str(k2)+str(k3)[:-4]))
				temp.close()
	#gf.doEverything2(temp) #//TODO Fix
	
		
doEverything()






















