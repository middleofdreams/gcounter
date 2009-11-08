# -*- coding: utf-8 -*-
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


