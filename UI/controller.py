import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def cercaIscritti(self,e):
        self._view.txt_result.controls.clear()
        corso=self._view.corsoSelezionato.value
        if corso is None :
            self._view.create_alert("Selezionare un corso !")
            self._view.update_page()
            return






        count=0
        for i in self._model.getAllIscritti():


            if i["codins"]== corso:
                count=count+1

        self._view.txt_result.controls.append(
            ft.Text(f" il corso ha {count} iscritti")
        )
        self._view.update_page()

        for j in self._model.getAllIscritti():

            if j["codins"] == corso:
                self._view.txt_result.controls.append(
                    ft.Text(f"{j['nome']}, {j["cognome"]} ({j["matricola"]})")
                )
                self._view.update_page()





    def addCorsi(self):
        for cod in self._model.getAllCorsi():
            self._view.corsoSelezionato.options.append(
                ft.dropdown.Option(
                    key=cod["codins"],
                    text=f"{cod["nome"]} ({cod["codins"]})"



                )
            )










    def searchStudent(self,e):


        matricola=self._view.txtMatricola.value

        try:
            matricolaInt=int(matricola)
        except ValueError:
            self._view.create_alert("insertire un valore intero numerico")

            return
        trovato=None
        for j in self._model.getcercaStudente():
            if matricolaInt == j["matricola"]:
                trovato = j
                break
        if trovato is None:
            self._view.create_alert(f"matricola {matricolaInt} non esistente")

        else:

            self._view.txtNome.value = trovato["nome"]
            self._view.txtCognome.value = trovato["cognome"]

        self._view.update_page()







    def searchCourses(self,e):
        self._view.txt_result.controls.clear()
        matricola=self._view.txtMatricola.value
        try:
            matricolaInt=int(matricola)
        except ValueError:
            self._view.create_alert("insertire un valore intero numerico")


            return

        if matricolaInt == "":
            self._view.create_alert("insertire un valore numerico")


        count=0
        for i in self._model.getCercaCorsiIscritto():
            if i["matricola"]==matricolaInt:
                count = count + 1
                self._view.txtNome.value = i["nome"]
                self._view.txtCognome.value = i["cognome"]
                self._view.update_page()

        self._view.txt_result.controls.append(
            ft.Text(f"risultano {count} corsi")
        )
        self._view.update_page()


        for j in self._model.getCercaCorsiIscritto():
            if j["matricola"]==matricolaInt:

                self._view.txt_result.controls.append(
                    ft.Text(f"{j['nomeCorso']}, {j['codins']}")
                )
        self._view.update_page()












    def signUp(self,e):
        self._view.txt_result.controls.clear()
        matricola=self._view.txtMatricola.value
        corso=self._view.corsoSelezionato.value
        try:
            matricolaInt=int(matricola)
        except ValueError:
            self._view.create_alert("insertire un valore intero numerico")
            return
        if corso is None:
            self._view.create_alert("insertire un corso")
            return
        self._view.update_page()











