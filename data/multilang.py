# -*- coding: utf-8 -*-
import locale
def setlang(gl):
	gl.notifystr=()
	if locale.getlocale()[0]=="pl_PL":
		import lang_pl
		lang_pl.set(gl)
	
	
	else:
		gl.string_remains="Remains"
		gl.string_ready="Ready"
		gl.string_stopped="Stopped"
		gl.notifystr=("Warning","System will be suspended in: ","System will be halted in: ","System will be rebooted in: ",
		"Performing user defined acion in: ")


