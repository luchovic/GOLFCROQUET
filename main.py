"""
Tarjeta de Control Personal - Golf Croquet
App simple para marcar, por equipo, en qué vuelta (1 a 10) se pasó
cada uno de los 6 aros (A.I a A.VI), y calcular el TOTAL (suma de vueltas).
En golf croquet: menos vueltas = mejor puntaje.
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp

AROS = ["A.I", "A.II", "A.III", "A.IV", "A.V", "A.VI"]
VUELTAS = list(range(1, 11))


class FilaAro(BoxLayout):
    """Una fila de la tarjeta: nombre del aro + botones 1-10 (selección única)."""

    def __init__(self, nombre_aro, on_change, **kwargs):
        super().__init__(orientation="horizontal", spacing=dp(4),
                          size_hint_y=None, height=dp(48), **kwargs)
        self.nombre_aro = nombre_aro
        self.on_change = on_change
        self.valor = None
        self.botones = {}

        lbl = Label(text=nombre_aro, size_hint_x=None, width=dp(60), bold=True)
        self.add_widget(lbl)

        for v in VUELTAS:
            btn = ToggleButton(text=str(v), group=nombre_aro,
                                size_hint_x=None, width=dp(40))
            btn.bind(on_press=self._make_handler(v))
            self.botones[v] = btn
            self.add_widget(btn)

    def _make_handler(self, valor):
        def handler(instance):
            # Si se vuelve a tocar el mismo botón ya activo, Kivy lo mantiene
            # presionado dentro del grupo (no permite deseleccionar solo);
            # replicamos "deseleccionar" tocando el mismo valor otra vez.
            if self.valor == valor and instance.state == "down":
                # permitir deselección manual
                pass
            if instance.state == "down":
                self.valor = valor
            else:
                if self.valor == valor:
                    self.valor = None
            self.on_change()
        return handler

    def reset(self):
        self.valor = None
        for btn in self.botones.values():
            btn.state = "normal"


class TarjetaControl(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", spacing=dp(6),
                          padding=dp(10), **kwargs)

        titulo = Label(text="TARJETA DE CONTROL PERSONAL",
                        font_size=dp(20), bold=True,
                        size_hint_y=None, height=dp(40))
        self.add_widget(titulo)

        fila_equipo = BoxLayout(orientation="horizontal", size_hint_y=None,
                                 height=dp(40), spacing=dp(6))
        fila_equipo.add_widget(Label(text="EQUIPO:", size_hint_x=None,
                                      width=dp(80), bold=True))
        self.equipo_input = TextInput(text="1", multiline=False,
                                       input_filter=None)
        fila_equipo.add_widget(self.equipo_input)
        self.add_widget(fila_equipo)

        scroll = ScrollView(size_hint=(1, 1))
        filas_container = GridLayout(cols=1, size_hint_y=None, spacing=dp(4))
        filas_container.bind(minimum_height=filas_container.setter("height"))

        self.filas = []
        for aro in AROS:
            fila = FilaAro(aro, self.actualizar_total)
            self.filas.append(fila)
            filas_container.add_widget(fila)

        scroll.add_widget(filas_container)
        self.add_widget(scroll)

        fila_total = BoxLayout(orientation="horizontal", size_hint_y=None,
                                height=dp(50), spacing=dp(6))
        fila_total.add_widget(Label(text="TOTAL:", font_size=dp(18),
                                     bold=True, size_hint_x=None, width=dp(100)))
        self.total_label = Label(text="-", font_size=dp(22), bold=True)
        fila_total.add_widget(self.total_label)
        self.add_widget(fila_total)

        botonera = BoxLayout(orientation="horizontal", size_hint_y=None,
                              height=dp(48), spacing=dp(6))
        btn_reset = Button(text="Nueva tarjeta")
        btn_reset.bind(on_press=self.reset_tarjeta)
        botonera.add_widget(btn_reset)
        self.add_widget(botonera)

    def actualizar_total(self):
        valores = [f.valor for f in self.filas]
        if all(v is not None for v in valores):
            self.total_label.text = str(sum(valores))
        else:
            completados = sum(1 for v in valores if v is not None)
            self.total_label.text = f"({completados}/6 aros)"

    def reset_tarjeta(self, instance=None):
        for fila in self.filas:
            fila.reset()
        self.equipo_input.text = ""
        self.total_label.text = "-"


class CroquetApp(App):
    def build(self):
        self.title = "Tarjeta de Control Personal"
        return TarjetaControl()


if __name__ == "__main__":
    CroquetApp().run()
