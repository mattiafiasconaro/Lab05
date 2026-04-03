import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24,text_align="center")
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self.corsoSelezionato= ft.Dropdown(width=200,
                                           label="Selezionare un corso",
                                            expand=True)
        self._controller.addCorsi()
        self.btnSearchI=ft.ElevatedButton(content=ft.Text("cerca iscritti"),
                                          on_click=self._controller.cercaIscritti,
                                          width=200)




        row1=ft.Row(controls=[self.corsoSelezionato,self.btnSearchI])


        self.txtMatricola=ft.TextField(label="Matricola",expand=True)
        self.txtNome=ft.TextField(label="Nome",expand=True)
        self.txtCognome=ft.TextField(label="Cognome",expand=True)
        row2=ft.Row(controls=[self.txtMatricola,self.txtNome,self.txtCognome])

        self.btnCercaStudente=ft.ElevatedButton(content=ft.Text("Cerca Studente"),
                                                width=200,
                                                on_click=self._controller.searchStudent)
        self.btnCercaCorsi = ft.ElevatedButton(content=ft.Text("Cerca Corsi"),
                                                  width=200,
                                                  on_click=self._controller.searchCourses)
        self.btnIscrivi = ft.ElevatedButton(content=ft.Text("Iscrivi"),
                                                  width=200,
                                                  on_click=self._controller.signUp,
                                            )

        row3=ft.Row(controls=[self.btnCercaStudente,self.btnCercaCorsi,self.btnIscrivi])








        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

        self._page.add(row1, row2, row3,self.txt_result)

        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
