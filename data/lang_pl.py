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

def set(gl):
	strings=["Wybierz akcję:","Gdy minie czas:","O konkretnym czasie:",\
	"Uśpij komputer","Wyłącz komputer","Uruchom ponownie komputer","Akcja użytkownika",\
	"Wykonaj akcję przed"]
	gl.label1.set_label("Wybierz akcję:")
	gl.label2.set_label("Gdy minie czas:")
	gl.wTree.get_widget("radiobutton8").set_label("O konkretnym czasie:")

	gl.op1.set_label("Uśpij komputer")
	gl.op2.set_label("Wyłącz komputer")
	gl.op3.set_label("Uruchom ponownie komputer")
	gl.op4.set_label("Akcja użytkownika")
	gl.check2.set_label("Wykonaj akcję przed:")
	gl.check.set_label("Zamknij program po wykonaniu")
	gl.about.set_comments("Gcounter to aplikacja napisana w języku python z wkorzystaniem biblioteki pyGTK.\nPozwala ona na wyłączenie, ponowne uruchomienie bądź uśpienie komputera o podanym czasie. Posiada wsparcie dla DBus i LibNotify\n\nJeśli masz jakiekolwiek pytania, znalazłeź błąd, bądź masz pomysł co można zmienić - proszę napisz do mnie.")
	gl.string_remains="Pozostało"
	gl.string_ready="Gotowy"
	gl.string_stopped="Zatrzymano"
	gl.mitem1.get_children()[0].set_label("Ustawienia domyślnie")
	gl.mitem2.get_children()[0].set_label("Wyczyść historię poleceń") 
	gl.wTree.get_widget("menuitem4").get_children()[0].set_label("Pomoc")
	gl.wTree.get_widget("menuitem1").get_children()[0].set_label("Plik")
	gl.wTree.get_widget("menuitem2").get_children()[0].set_label("Edycja")
	gl.notifystr=("Uwaga","System zostanie uśpiony za: ","System zostanie wyłączony za: ","System zostanie uruchomiony ponownie za: ",
		"Zostanie wykonana akcja użytkownika za: ")
