import os,sys
import gdbm


dir=os.path.abspath(os.path.dirname(sys.argv[0]))+"/data"
workpath=os.environ['HOME']+"/.gcounter"
userdata=workpath+"/userdata.opt"
userdata2=workpath+"/userdata2.opt"
prefs=workpath+"/prefs.db"

def tryfiles():
	if not os.path.isdir(workpath):
		os.makedirs(workpath)
	d = gdbm.open(prefs, 'c')
	if d.firstkey()==None:
		d["action"]="1"
		d["minutes"]="1"
		d["hours"]="0"
		d["closeapp"]="False"
		d["runbefore"]="False"
		d["userdata1"]=""
		d["userdata2"]=""
	d.close()

def loaduserdata(gl):		
	d = gdbm.open(userdata, 'c')
	if d.firstkey()==None:
		gl.elementy.append(["notify-send ALARM!"])
	else:
		k = d.firstkey()
		while k != None:
			gl.elementy.prepend([d[k]])
			k = d.nextkey(k)
	d.close()

	d = gdbm.open(userdata2, 'c')
	if d.firstkey()==None:
		gl.elementy2.append(["mpc pause"])
	else:
		k = d.firstkey()
		while k != None:
			gl.elementy.prepend([d[k]])
			k = d.nextkey(k)
	d.close()			
	
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
			d = gdbm.open(userdata, 'c')
			l=len(d.keys())
			d[str(l)]=str(gl.combo1.child.get_text())
			d.close()
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
			d = gdbm.open(userdata2, 'c')
			l=len(d.keys())
			d[str(l)]=str(gl.combo2.child.get_text())
			d.close()
				
def loadprefs(gl):
	d = gdbm.open(prefs, 'r')
	action=d["action"]
	time=d["minutes"]
	timeh=d["hours"]
	closeapp=d["closeapp"]
	runbefore=d["runbefore"]
	puserdata=d["userdata1"]
	puserdata2=d["userdata2"]
	d.close()
	action=int(action)
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
	gl.ileh.set_value(float(str(timeh)))
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
	timeh=gl.ileh.get_value_as_int()			
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
	
	d = gdbm.open(prefs, 'c')
	d["action"]=str(action)
	d["minutes"]=str(time)
	d["hours"]=str(timeh)
	d["closeapp"]=str(closeapp)
	d["runbefore"]=str(runbefore)
	d["userdata1"]=str(puserdata)
	d["userdata2"]=str(puserdata2)
	d.close()	
			

