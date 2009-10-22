import os,sys
dir=os.path.abspath(os.path.dirname(sys.argv[0]))+"/data"
workpath=os.environ['HOME']+"/.gcounter"
userdata=workpath+"/userdata.opt"
userdata2=workpath+"/userdata2.opt"
prefs=workpath+"/prefs.opt"

def tryfiles():
	try:
		f = open (userdata,"r")
	except IOError:
		if not os.path.isdir(workpath):
			d = os.makedirs(workpath)
		f=open (userdata,"w")
	f.close()
	try:
		f = open (userdata2,"r")
	except IOError:
		if not os.path.isdir(workpath):
			d = os.makedirs(workpath)
		f=open (userdata2,"w")
	f.close()
	try:
		f = open (prefs,"r")
		ppp=True
	except IOError:
		ppp=False
		if not os.path.isdir(workpath):
			d = os.makedirs(workpath)
		f=open (prefs,"w")
		f.write("1\n")
		f.write("1\n")
		f.write("False\n")
		f.write("False\n")
		f.write("\n")
		f.write("\n")
	if ppp:
		if f.readline()=="":
			f.close()		
			f=open (prefs,"w")
			f.write("1\n")
			f.write("1\n")
			f.write("False\n")
			f.write("False\n")
			f.write("\n")
			f.write("\n")
	f.close()	
			
	

		


def loaduserdata(gl):		
	f=open(userdata, 'r')
	if f.readline()=="":
		gl.elementy.append(["notify-send ALARM!"])
	f.close()
	
	f = open (userdata,"r")
	for line in f.read().split('\n'):
		if line!="":
			gl.elementy.prepend([line])
	
	f.close()
	
	f = open (userdata2,"r")
	if f.readline()=="":
		gl.elementy2.append(["mpc pause"])
	f.close()
	
	f = open (userdata2,"r")
	for line in f.read().split('\n'):
		if line!="":
			gl.elementy2.prepend([line])
		
	f.close()
		
def saveuserdata(gl):
	iter=gl.elementy.get_iter(0)
	i=False
	if gl.combo1.child.get_text()!="":
		while iter:
			if gl.combo1.child.get_text()!= gl.elementy.get_value(iter,0):
				 i=True
			else:
				i=False
				break;
			
			iter=gl.elementy.iter_next(iter)
		if i:
			fa = open(userdata,"a")
			fa.write(gl.combo1.child.get_text()+"\n")
			fa.close()
	i=False
	iter=gl.elementy2.get_iter(0)
	if gl.combo2.child.get_text()!="":
		while iter:
			if gl.combo2.child.get_text()!= gl.elementy2.get_value(iter,0):
				 i=True
			else:
				i=False
				break;
			
			iter=gl.elementy2.iter_next(iter)
		if i:
			fa = open(userdata2,"a")
			fa.write(gl.combo2.child.get_text()+"\n")
			fa.close()
				
def loadprefs(gl):
	f = open (prefs,"r")
	action=f.readline()
	time=f.readline()
	closeapp=f.readline().rstrip("\n")
	runbefore=f.readline().rstrip("\n")
	puserdata=f.readline()
	puserdata2=f.readline()
	f.close()
	action= int(action)
	if action==1:
		gl.op1.set_active(1)
		gl.entry1.set_text("")
	elif action==2:
		gl.op2.set_active(1)
		gl.entry1.set_text("")
	elif action==3:
		gl.op3.set_active(1)
		gl.entry1.set_text("")
	elif action==4:
		gl.op4.set_active(1)
		gl.entry1.set_sensitive(1)
		gl.entry1.set_text(puserdata.rstrip("\n"))
	gl.ile.set_value(float(str(time)))	
	if closeapp=="True":
		gl.check.set_active(1)
	else:
		gl.check.set_active(0)
	if runbefore=="True":
		gl.check2.set_active(1)
		gl.entry2.set_sensitive(1)
		gl.entry2.set_text(puserdata2.rstrip("\n"))
	else:
		gl.check2.set_active(0)
		gl.entry2.set_sensitive(0)	
		gl.entry2.set_text("")

def saveprefs(gl):
	time=gl.ile.get_value_as_int()			
	if gl.check2.get_active():
		runbefore="True"
	else:
		runbefore="False"
	if gl.check.get_active():
		closeapp="True"
	else:
		closeapp="False"
	if gl.op1.get_active():
		action=1
	elif gl.op2.get_active():
		action=2
	elif gl.op3.get_active():
		action=3
	else:
		action=4
	puserdata=gl.entry1.get_text()
	puserdata2=gl.entry2.get_text()			
	
		
	f = open (prefs,"w")
	f.write(str(action)+"\n")
	f.write(str(time)+"\n")
	f.write(str(closeapp)+"\n")
	f.write(str(runbefore)+"\n")
	f.write(str(puserdata)+"\n")
	f.write(str(puserdata2)+"\n")
	f.close()	
			

