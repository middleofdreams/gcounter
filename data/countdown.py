import threading,time,notification

class licznik(threading.Thread):
	
	 
	 def __init__ (self, gl,notifies):
		threading.Thread.__init__(self)
		gl.countdown= True
		self.gl=gl
		self.notifies=notifies
		threading.Thread(target=self.odliczanie,args=()).start()
		
			
	 def odliczanie(self):	
		self.minuty=self.gl.ile.get_value_as_int()+self.gl.ileh.get_value_as_int()*60
		self.sekundy=0
		for i in range(self.minuty*60, 0, -1):
			if self.gl.countdown==False:
				break
			else:
				if self.sekundy==0:
					self.sekundy=59	
					self.minuty=self.minuty-1
					if self.minuty>59:
						self.gl.bar.push(0,self.gl.string_remains+": "+str(self.minuty/60)+" h "+str(self.minuty%60)+" min "+str(self.sekundy)+" s")
						self.gl.staticon.set_tooltip(self.gl.string_remains+": "+str(self.minuty/60)+" h "+str(self.minuty%60)+" min "+str(self.sekundy)+" s")
					else:
						self.gl.bar.push(0,self.gl.string_remains+": "+str(self.minuty)+" min "+str(self.sekundy)+" s")
						self.gl.staticon.set_tooltip(self.gl.string_remains+": "+str(self.minuty)+" min "+str(self.sekundy)+" s")

				else:
					self.sekundy=self.sekundy-1
					if self.minuty>59:						
						self.gl.bar.push(0,self.gl.string_remains+": "+str(self.minuty/60)+" h "+str(self.minuty%60)+" min "+str(self.sekundy)+" s")
						self.gl.staticon.set_tooltip(self.gl.string_remains+": "+str(self.minuty/60)+" h "+str(self.minuty%60)+" min "+str(self.sekundy)+" s")
					else:
						self.gl.bar.push(0,self.gl.string_remains+": "+str(self.minuty)+" min "+str(self.sekundy)+" s")
						self.gl.staticon.set_tooltip(self.gl.string_remains+": "+str(self.minuty)+" min "+str(self.sekundy)+" s")
						if self.notifies and self.gl.notif=="True":
							if self.minuty==0 and self.sekundy==5:
								n=notification.gcnotify(self.gl,self.sekundy)
								
							if self.minuty==0 and self.sekundy<5:
								n.update(self.sekundy)

							if self.minuty==0 and self.sekundy==0:
								n.stop()
					time.sleep(1)	
				if self.gl.trayopt1=="True": self.gl.staticon.set_blinking(True) 
			
			if self.gl.countdown:
				if self.minuty==0:
					if self.sekundy==0:
						self.gl.bar.push(0,self.gl.string_ready)
						self.gl.btn1.set_sensitive(1)
						self.gl.btn2.set_sensitive(0)
						self.gl.staticon.set_blinking(False)
						self.gl.akcja()
			else:
				if self.gl.quit==False:
					self.gl.bar.push(0, self.gl.string_stopped)
					time.sleep(1)
					self.gl.bar.push(0,self.gl.string_ready)
					self.gl.staticon.set_blinking(False)
