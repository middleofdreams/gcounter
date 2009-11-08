#!/usr/bin/env python
# -*- coding: utf-8 -*-

#loading main libraries
import sys,pygtk,gtk,gtk.glade,time,os,pango
#trying to load python-notify
try:
	import pynotify
	notifies=True			
except:
	notifies=False
	
#import gcounter files
import data
from data import *
from data.widgets import *
from data.countdown import *
from data.preferences import *
pygtk.require("2.0")

#assign the main directory... usually /usr/share/gcounter
dir=os.path.abspath(os.path.dirname(sys.argv[0]))+"/data"


#main class - for gui etc
class gcounter:
	def __init__(self):
		# choosing glade file for gui
		self.gladefile =  dir+"/alter.glade"
		self.wTree = gtk.glade.XML(self.gladefile) 
		# getting main window
		self.window = self.wTree.get_widget("window1")
		self.window.show()
		if (self.window):
			self.window.connect("destroy",self.mainquit)
		
	

		#assign notifies var as class var
		self.notifies=notifies
		#loading widgets name:
		assignwidgets(self)
		#set language
		multilang.setlang(self)
		createstatusicon(self,dir)     		
		self.bar.push(0,self.string_ready)
		self.entry1.set_sensitive(0)
		self.entry2.set_sensitive(0)
		self.minuty = 0
		self.sekundy = 0
		
		#load preferences
		self.gcprefs=gcpreferences()
		self.gcprefs.loaduserdata(self)
		self.gcprefs.loadprefs(self)
		
		#few control vars
		self.countdown=False
		self.quit=False
		#if pynotify importet successful - init notifies.
		if notifies:pynotify.init("GCounter Notify")
		
	#handlers for gui actions:
		
	def prefscancel(self,widget):
		preferences.loadmainprefs(self)
		self.prefwindow.hide()

	def prefssave(self,widget):
		self.gcprefs.savemainprefs(self)
		self.prefwindow.hide()
	def openprefs(self,widget):
		self.gcprefs.loadmainprefs(self)			
		self.gcprefs.openwindow(self)
		
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
		os.remove(userdata)
		os.remove(userdata2)
		self.elementy.clear()
		self.elementy2.clear()
		self.gcprefs.loaduserdata(self)
		self.entry1.set_text("")
		self.entry2.set_text("")
			
	def defaults(self, widget):
		d = gdbm.open(prefs, 'c')
		d["action"]="1"
		d["minutes"]="1"
		d["hours"]="0"
		d["closeapp"]="False"
		d["runbefore"]="False"
		d["userdata1"]=""
		d["userdata2"]=""
		d.close()
		self.gcprefs.loadprefs(self)
		
		
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
		gl.gcprefs.saveprefs(self)
		self.aaa=licznik(self,notifies)
		self.btn1.set_sensitive(0)
		self.btn2.set_sensitive(1)
		self.mitem3.set_sensitive(0)
		self.mitem4.set_sensitive(1)
		gl.gcprefs.saveuserdata(self)
		gl.countdown=True
		if self.trayopt2=="True": self.window.hide()
	def button2_clicked(self, widget):
		self.aaa.running=False	
		self.btn1.set_sensitive(1)
		self.btn2.set_sensitive(0)
		gl.countdown=False
		self.mitem3.set_sensitive(1)
		self.mitem4.set_sensitive(0)
		self.window.show()
	def akcja(self):
		if self.defaction=="1":
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
				
		if self.defaction=="2":	
			if self.check2.get_active():
				os.popen(self.entry2.get_text())
			if self.check.get_active():
				self.window.hide()	
			if self.op1.get_active():
				os.popen("sudo pm-suspend")
			elif self.op2.get_active():
				os.popen("sudo shutdown")
			elif self.op3.get_active():
				os.popen("sudo reboot")

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
	gl=gcounter()
	gtk.main()
