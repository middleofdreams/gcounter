#
#       This file is part of GCounter application
#       
#       Copyright 2009  Kuba Wrozyna <middleofdreams.wordpress.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import gtk,gtk.glade

def assignwidgets(mainclass):
		mainclass.op1 = mainclass.wTree.get_widget("radiobutton1")
		mainclass.op2 = mainclass.wTree.get_widget("radiobutton2")
		mainclass.op3 = mainclass.wTree.get_widget("radiobutton3")
		mainclass.op4 = mainclass.wTree.get_widget("radiobutton4")		
		mainclass.ile = mainclass.wTree.get_widget("spinbutton1")
		mainclass.ileh = mainclass.wTree.get_widget("spinbutton2")

		mainclass.btn1 = mainclass.wTree.get_widget("button1")
		mainclass.btn2= mainclass.wTree.get_widget("button2")
		mainclass.bar = mainclass.wTree.get_widget("statusbar1")
		mainclass.entry1 = mainclass.wTree.get_widget("comboboxentry1").child
		mainclass.entry2 = mainclass.wTree.get_widget("comboboxentry2").child
		mainclass.check = mainclass.wTree.get_widget("checkbutton1")
		mainclass.check2 = mainclass.wTree.get_widget("checkbutton2")
		mainclass.check5 = mainclass.wTree.get_widget("checkbutton5")
		mainclass.combo1 = mainclass.wTree.get_widget("comboboxentry1")
		mainclass.about = mainclass.wTree.get_widget("aboutdialog1")
		mainclass.label1 = mainclass.wTree.get_widget("label1")
		mainclass.label2 = mainclass.wTree.get_widget("label2")
		mainclass.mitem1 = mainclass.wTree.get_widget("imagemenuitem6")
		mainclass.mitem2 = mainclass.wTree.get_widget("imagemenuitem7")
		mainclass.mitem3 = mainclass.wTree.get_widget("menuitem6")
		mainclass.mitem4 = mainclass.wTree.get_widget("menuitem7")
		mainclass.menu1 = mainclass.wTree.get_widget("menu1")
		mainclass.elementy = gtk.ListStore(str)
		mainclass.combo1.set_model(mainclass.elementy)
		mainclass.combo2 = mainclass.wTree.get_widget("comboboxentry2")
		mainclass.elementy2 = gtk.ListStore(str)
		mainclass.combo2.set_model(mainclass.elementy2)
		
		mainclass.prefwindow = mainclass.wTree.get_widget("dialog1")
		
		dic = { "on_button1_clicked" : mainclass.button1_clicked,
		"on_button2_clicked" : mainclass.button2_clicked,
		"entry_dis" : mainclass.entry_dis,
		"entry_en" : mainclass.entry_en,
		"entry2disen" : mainclass.entry2disen,
		"zamknij" : mainclass.mainquit,
		"about" : mainclass.aboutt,
		"about_close" : mainclass.aboutt_close,
		"defaults" : mainclass.defaults,
		"clear_history" : mainclass.clear_history,
		"preferences": mainclass.openprefs,
		"prefssave":	mainclass.prefssave,
		"prefscancel":	mainclass.prefscancel,
		"on_checkbutton5_toggled": mainclass.notifytoggle}
		mainclass.wTree.signal_autoconnect(dic)

def createstatusicon(mainclass,dir):	
	
		mainclass.window.set_icon_from_file(dir+"/icon.png") 
		mainclass.staticon = gtk.StatusIcon() 
		mainclass.staticon.set_from_file(dir+"/icon.png") 
		mainclass.staticon.set_blinking(False) 
		mainclass.staticon.set_tooltip("Gcounter: "+mainclass.string_ready)
		mainclass.staticon.connect("activate", mainclass.activate) 
		mainclass.staticon.connect("popup_menu", mainclass.popup, mainclass.menu1) 
		mainclass.staticon.set_visible(True)
