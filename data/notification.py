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

	
class gcnotify():


	def __init__(self,mainclass,secs):
		import pynotify
		self.title=mainclass.notifystr[0]
		self.body=self.getnotifybody(mainclass)
		body=self.body+str(secs)+"s"
		self.n = pynotify.Notification(self.title, body)  
		self.n.attach_to_status_icon(mainclass.staticon)
		self.n.show()
		
	def getnotifybody(self,mainclass):
		if mainclass.op1.get_active():
			body=mainclass.notifystr[1]
		elif mainclass.op2.get_active():
			body=mainclass.notifystr[2]
		elif mainclass.op3.get_active():
			body=mainclass.notifystr[3]
		else:
			body=mainclass.notifystr[4]
		return body
		
	def update(self,secs):
		body=self.body+str(secs)+"s"
		self.n.update(self.title, body)  
		self.n.show()
	def stop(self):  
		self.n.close()
