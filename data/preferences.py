import os,sys
import gdbm,gtk


dir=os.path.abspath(os.path.dirname(sys.argv[0]))+"/data"
workpath=os.environ['HOME']+"/.gcounter"
userdata=workpath+"/userdata.db"
userdata2=workpath+"/userdata2.db"
prefs=workpath+"/prefs.db"


class gcpreferences():
	def __init__(self):
		self.tryfiles()
			
	def openwindow(self,mainclass):
		if not mainclass.notifies:
			mainclass.wTree.get_widget("label9").set_sensitive(False)
			mainclass.wTree.get_widget("vbox8").set_sensitive(False)
			mainclass.wTree.get_widget("label11").set_text("Install python-notify \nto get this work!")
			mainclass.wTree.get_widget("label11").modify_font(pango.FontDescription("sans 17")) 
		response = mainclass.prefwindow.run() 	
		if response == gtk.RESPONSE_DELETE_EVENT or response == gtk.RESPONSE_CANCEL:
			mainclass.prefwindow.hide()




	def tryfiles(self):
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
			d["p_defaction"]="1"
			d["p_trayopt1"]="True"
			d["p_trayopt2"]="True"
			d["p_notif"]="True"
		d.close()

	def loaduserdata(self,mainclass):		
		d = gdbm.open(userdata, 'c')
		if d.firstkey()==None:
			mainclass.elementy.append(["notify-send ALARM!"])
		else:
			k = d.firstkey()
			while k != None:
				mainclass.elementy.prepend([d[k]])
				k = d.nextkey(k)
		d.close()

		d = gdbm.open(userdata2, 'c')
		if d.firstkey()==None:
			mainclass.elementy2.append(["mpc pause"])
		else:
			k = d.firstkey()
			while k != None:
				mainclass.elementy2.prepend([d[k]])
				k = d.nextkey(k)
		d.close()			
		
	def saveuserdata(self,mainclass):
		iter=mainclass.elementy.get_iter(0)
		i=False
		
		
		if mainclass.combo1.child.get_text()!="":
			while iter:
				if mainclass.combo1.child.get_text()!= mainclass.elementy.get_value(iter,0):
					 i=True
				else:
					i=False
					break;
				
				iter=mainclass.elementy.iter_next(iter)
			if i:
				d = gdbm.open(userdata, 'c')
				l=len(d.keys())
				d[str(l)]=str(mainclass.combo1.child.get_text())
				d.close()
		i=False
		iter=mainclass.elementy2.get_iter(0)
		if mainclass.combo2.child.get_text()!="":
			while iter:
				if mainclass.combo2.child.get_text()!= mainclass.elementy2.get_value(iter,0):
					 i=True
				else:
					i=False
					break;
				
				iter=mainclass.elementy2.iter_next(iter)
			if i:
				d = gdbm.open(userdata2, 'c')
				l=len(d.keys())
				d[str(l)]=str(mainclass.combo2.child.get_text())
				d.close()
					
	def loadprefs(self,mainclass):
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
			mainclass.op1.set_active(1)
			mainclass.entry1.set_text("")
		elif action==2:
			mainclass.op2.set_active(1)
			mainclass.entry1.set_text("")
		elif action==3:
			mainclass.op3.set_active(1)
			mainclass.entry1.set_text("")
		elif action==4:
			mainclass.op4.set_active(1)
			mainclass.entry1.set_sensitive(1)
			mainclass.entry1.set_text(puserdata.rstrip("\n"))
		mainclass.ile.set_value(float(str(time)))	
		mainclass.ileh.set_value(float(str(timeh)))
		if closeapp=="True":
			mainclass.check.set_active(1)
		else:
			mainclass.check.set_active(0)
		if runbefore=="True":
			mainclass.check2.set_active(1)
			mainclass.entry2.set_sensitive(1)
			mainclass.entry2.set_text(puserdata2.rstrip("\n"))
		else:
			mainclass.check2.set_active(0)
			mainclass.entry2.set_sensitive(0)	
			mainclass.entry2.set_text("")
		self.loadmainprefs(mainclass)
		
	def saveprefs(self,mainclass):
		time=mainclass.ile.get_value_as_int()	
		timeh=mainclass.ileh.get_value_as_int()			
		if mainclass.check2.get_active():
			runbefore="True"
		else:
			runbefore="False"
		if mainclass.check.get_active():
			closeapp="True"
		else:
			closeapp="False"
		if mainclass.op1.get_active():
			action=1
		elif mainclass.op2.get_active():
			action=2
		elif mainclass.op3.get_active():
			action=3
		else:
			action=4
		puserdata=mainclass.entry1.get_text()
		puserdata2=mainclass.entry2.get_text()			
		
		d = gdbm.open(prefs, 'c')
		d["action"]=str(action)
		d["minutes"]=str(time)
		d["hours"]=str(timeh)
		d["closeapp"]=str(closeapp)
		d["runbefore"]=str(runbefore)
		d["userdata1"]=str(puserdata)
		d["userdata2"]=str(puserdata2)
		d.close()	
				
	def loadmainprefs(self,mainclass):
		try:
			d = gdbm.open(prefs, 'r')
			mainclass.defaction=d["p_defaction"]
			mainclass.trayopt1=d["p_trayopt1"]
			mainclass.trayopt2=d["p_trayopt2"]
			mainclass.notif=d["p_notif"]
		except:
			d.close()
			d = gdbm.open(prefs, 'c')
			d["p_defaction"]="1"
			d["p_trayopt1"]="True"
			d["p_trayopt2"]="True"
			d["p_notif"]="True"
			mainclass.defaction=d["p_defaction"]
			mainclass.trayopt1=d["p_trayopt1"]
			mainclass.trayopt2=d["p_trayopt2"]
			mainclass.notif=d["p_notif"]
		d.close()
		
		if mainclass.defaction=="2": mainclass.wTree.get_widget("radiobutton6").set_active(True)
		else: mainclass.wTree.get_widget("radiobutton5").set_active(True)
		
		if mainclass.trayopt1=="True": mainclass.wTree.get_widget("checkbutton3").set_active(True)
			
		if mainclass.trayopt2=="True": mainclass.wTree.get_widget("checkbutton4").set_active(True)
		if mainclass.notif=="True": mainclass.wTree.get_widget("checkbutton5").set_active(True)

	def savemainprefs(self,mainclass):
		
		
		if mainclass.wTree.get_widget("radiobutton6").get_active():
			mainclass.defaction="2"
		else: mainclass.defaction="1"
		if mainclass.wTree.get_widget("checkbutton3").get_active(): mainclass.trayopt1="True"
		else: mainclass.trayopt1="False"
		if mainclass.wTree.get_widget("checkbutton4").get_active(): mainclass.trayopt2="True"
		else: mainclass.trayopt2="False"
		if mainclass.wTree.get_widget("checkbutton5").get_active(): mainclass.notif="True"
		else: mainclass.notif="False"
		d = gdbm.open(prefs, 'c')
		d["p_defaction"]=mainclass.defaction
		d["p_trayopt1"]=mainclass.trayopt1
		d["p_trayopt2"]=mainclass.trayopt2
		d["p_notif"]=mainclass.notif
		d.close()
