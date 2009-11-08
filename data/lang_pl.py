# -*- coding: utf-8 -*-

def set(gl):
	gl.label1.set_label("Wybierz akcję:")
	gl.label2.set_label("W następującym czasie")
	gl.op1.set_label("Uśpij komputer")
	gl.op2.set_label("Wyłącz komputer")
	gl.op3.set_label("Uruchom ponownie komputer")
	gl.op4.set_label("Akcja użytkownika")
	gl.check2.set_label("Wykonaj akcję przed:")
	gl.check.set_label("Zamknij program po wykonaniu")
	gl.about.set_comments("Gcounter to aplikacja napisana w języku python z wkorzystaniem biblioteki pyGTK.\nPozwala ona na wyłączenie, ponowne uruchomienie bądź uśpienie komputera o podanym czasie. Posiada wsparcie dla DBus i LibNotify")
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
