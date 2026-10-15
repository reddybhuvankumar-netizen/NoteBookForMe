%%writefile /content/NoteBookForMe/main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class NoteBookForMeApp(App):
    def build(self):
        root = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        root.add_widget(Label(
            text="NOTE BOOK FOR ME",
            font_size="26sp",
            bold=True
        ))

        root.add_widget(Label(
            text="Customer Transactions",
            font_size="18sp"
        ))

        root.add_widget(Button(
            text="+ Add Customer",
            size_hint_y=None,
            height="55dp"
        ))

        return root

NoteBookForMeApp().run()