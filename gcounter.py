#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,pygtk,gtk,gtk.glade,time,threading,gobject,os,locale,dbus
import data
pygtk.require("2.0")
global dir,userdata, userdata2
dir=os.path.abspath(os.path.dirname(sys.argv[0]))+"/data"
userdata=dir+"/userdata.opt"
userdata2=dir+"/userdata2.opt"



# klasa licznika - watki
class licznik(threading.Thread):
	
	 
	 def __init__ (self):
		threading.Thread.__init__(self)
		gl.countdown= True
		threading.Thread(target=self.odliczanie,args=()).start()
		
			
	 def odliczanie(self):	
		self.minuty=gl.ile.get_value_as_int()
		self.sekundy=0
		for i in range(self.minuty*60, 0, -1):
			if gl.countdown==False:
				break
			else:
				if self.sekundy==0:
					self.sekundy=59	
					self.minuty=self.minuty-1
					gl.bar.push(0,gl.string_remains+": "+str(self.minuty)+" min "+str(self.sekundy)+" s")
					gl.staticon.set_tooltip(gl.string_remains+": "+str(self.minuty)+" min "+str(self.sekundy)+" s")

				else:
					self.sekundy=self.sekundy-1
					gl.bar.push(0,gl.string_remains+": "+str(self.minuty)+" min "+str(self.sekundy)+" s")
					gl.staticon.set_tooltip(gl.string_remains+": "+str(self.minuty)+" min "+str(self.sekundy)+" s")
				time.sleep(1)
				gl.staticon.set_blinking(True) 
			
			if gl.countdown:
				if self.minuty==0:
					if self.sekundy==0:
						gl.bar.push(0,gl.string_ready)
						gl.btn1.set_sensitive(1)
						gl.btn2.set_sensitive(0)
						gl.staticon.set_blinking(False)
						gl.akcja()
			else:
				if gl.quit==False:
					gl.bar.push(0, gl.string_stopped)
					time.sleep(1)
					gl.bar.push(0,gl.string_ready)
					gl.staticon.set_blinking(False)
class glowna:
	def __init__(self):
		# wybieramy plik *glade
		self.gladefile =  dir+"/alter.glade"
		self.wTree = gtk.glade.XML(self.gladefile) 
		# pobieramy główne okno
		self.window = self.wTree.get_widget("window1")
		self.window.show()
		if (self.window):
			self.window.connect("destroy",self.mainquit)
		
		self.op1 = self.wTree.get_widget("radiobutton1")
		self.op2 = self.wTree.get_widget("radiobutton2")
		self.op3 = self.wTree.get_widget("radiobutton3")
		self.op4 = self.wTree.get_widget("radiobutton4")		
		self.ile = self.wTree.get_widget("spinbutton1")
		self.btn1 = self.wTree.get_widget("button1")
		self.btn2= self.wTree.get_widget("button2")
		self.bar = self.wTree.get_widget("statusbar1")
		self.entry1 = self.wTree.get_widget("comboboxentry1").child
		self.entry2 = self.wTree.get_widget("comboboxentry2").child
		self.check = self.wTree.get_widget("checkbutton1")
		self.check2 = self.wTree.get_widget("checkbutton2")
		self.combo1 = self.wTree.get_widget("comboboxentry1")
		self.about = self.wTree.get_widget("aboutdialog1")
		self.label1 = self.wTree.get_widget("label1")
		self.label2 = self.wTree.get_widget("label2")
		self.mitem1 = self.wTree.get_widget("imagemenuitem6")
		self.mitem2 = self.wTree.get_widget("imagemenuitem7")
		self.mitem3 = self.wTree.get_widget("menuitem6")
		self.mitem4 = self.wTree.get_widget("menuitem7")
		self.menu1 = self.wTree.get_widget("menu1")
		self.elementy = gtk.ListStore(str)
		self.combo1.set_model(self.elementy)
		self.combo2 = self.wTree.get_widget("comboboxentry2")
		self.elementy2 = gtk.ListStore(str)
		self.combo2.set_model(self.elementy2)
		self.string_remains="Remains"
		self.string_ready="Ready"
		self.string_stopped="Stopped"
		data.multilang.setlang(self)
			
		dic = { "on_button1_clicked" : self.button1_clicked,
		"on_button2_clicked" : self.button2_clicked,
		"entry_dis" : self.entry_dis,
		"entry_en" : self.entry_en,
		"entry2disen" : self.entry2disen,
		"zamknij" : self.mainquit,
		"about" : self.aboutt,
		"about_close" : self.aboutt_close,
		"defaults" : self.defaults,
		"clear_history" : self.clear_history}
		self.wTree.signal_autoconnect(dic)
	
		self.window.set_icon_from_file(dir+"/icon.png") 
		self.staticon = gtk.StatusIcon() 
		self.staticon.set_from_file(dir+"/icon.png") 
		self.staticon.set_blinking(False) 
		self.staticon.set_tooltip("Gcounter: "+self.string_ready)
		self.staticon.connect("activate", self.activate) 
		self.staticon.connect("popup_menu", self.popup, self.menu1) 
		self.staticon.set_visible(True)
        
        		
		self.bar.push(0,self.string_ready)
		self.entry1.set_sensitive(0)
		self.entry2.set_sensitive(0)
		self.minuty = 0
		self.sekundy = 0
		data.preferences.tryfiles()
		data.preferences.loaduserdata(self)
		data.preferences.loadprefs(self)
		self.countdown=False
		self.quit=False
	def activate(self,widget):
		if self.window.is_active():
			self.window.hide()
		else:
			self.window.show()
	def popup(self,widget, button, time, test = None):
		if button == 3:
			if test:
				test.show_all()
				test.popup(None, None, None, 3, time)
	def zamknij(self, widget):
		gtk.main_quit()	
	def aboutt(self, widget):
		self.response = self.wTree.get_widget("aboutdialog1").run() 
		if self.response == gtk.RESPONSE_DELETE_EVENT or self.response == gtk.RESPONSE_CANCEL:
			self.wTree.get_widget("aboutdialog1").hide()
	def aboutt_close(self, widget):
		self.about.hide()

	def clear_history(self, widget):
		f = open(userdata,"w")
		f.write("")
		f.close()
		f = open(userdata2,"w")
		f.write("")
		f.close()
		self.elementy.clear()
		self.elementy2.clear()
		data.preferences.loaduserdata(self)
		self.entry1.set_text("")
		self.entry2.set_text("")
			
	def defaults(self, widget):
		f = open (dir+"/prefs.opt","w")
		f.write("1\n")
		f.write("1\n")
		f.write("False\n")
		f.write("False\n")
		f.write("\n")
		f.write("\n")
		f.close()	
		data.preferences.loadprefs(self)
	def entry2disen(self, widget):
		if self.check2.get_active():
			self.entry2.set_sensitive(1)
		else:
			self.entry2.set_sensitive(0)	
		
	def entry_dis(self, widget):
		self.entry1.set_sensitive(0)
		
	def entry_en(self, widget):
		self.entry1.set_sensitive(1)
		
	def button1_clicked(self, widget):
		data.preferences.saveprefs(gl)
		self.aaa=licznik()
		self.btn1.set_sensitive(0)
		self.btn2.set_sensitive(1)
		self.mitem3.set_sensitive(0)
		self.mitem4.set_sensitive(1)
		data.preferences.saveuserdata(self)
		gl.countdown=True
		self.window.hide()
	def button2_clicked(self, widget):
		self.aaa.running=False	
		self.btn1.set_sensitive(1)
		self.btn2.set_sensitive(0)
		gl.countdown=False
		self.mitem3.set_sensitive(1)
		self.mitem4.set_sensitive(0)
		self.window.show()
	def akcja(self):
		if self.check2.get_active():
			os.popen(self.entry2.get_text())
		if self.check.get_active():
			self.window.hide()	
		if self.op1.get_active():
			os.popen("dbus-send --system --dest=org.freedesktop.Hal --type=method_call --print-reply /org/freedesktop/Hal/devices/computer  org.freedesktop.Hal.Device.SystemPowerManagement.Suspend int32:0")
		elif self.op2.get_active():
			os.popen("dbus-send --system --dest=org.freedesktop.Hal --type=method_call --print-reply /org/freedesktop/Hal/devices/computer  org.freedesktop.Hal.Device.SystemPowerManagement.Shutdown")
		elif self.op3.get_active():
			os.popen("dbus-send --system --dest=org.freedesktop.Hal --type=method_call --print-reply /org/freedesktop/Hal/devices/computer  org.freedesktop.Hal.Device.SystemPowerManagement.Reboot")

		else:
			os.popen(self.entry1.get_text())
		if self.check.get_active():
			gtk.main_quit()
	
	def mainquit(self, widget):
		if self.countdown:
			self.countdown=False
		self.quit=True
		gtk.main_quit()
		
	
			
# wywołanie aplikacji
if __name__ == "__main__":
	gtk.gdk.threads_init()
	gl=glowna()
	gtk.main()
