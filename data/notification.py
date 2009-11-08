
	
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
