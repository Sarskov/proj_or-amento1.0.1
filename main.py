import os
from datetime import datetime
from kivy.config import Config
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'resizable', False)

from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.list import OneLineListItem
from kivy.utils import platform
from kivymd.app import MDApp
from kivy.core.window import Window
Window.size = (300, 600)  # width=300, height=600

class MainApp(MDApp):

   

    def build(self):
        self.contador = {
            'intsimples':0,
            'intparalelo':0,
            'intintermed':0,
            'tmd10a':0,
            'tmd20a':0,
            'tmd220':0,
            'cego':0,
            'furado':0,
            'coax':0,
            'placa4x2p1':0,
            'placa4x2p2':0,
            'placa4x2p3':0,
            'placa4x4p2':0,
            'placa4x4p4':0,
            'placa4x4p6':0,
            


        }
        self.dialog = None
        return Builder.load_file("main.kv")
    


    def on_intsimples(self):
        self.contador['intsimples']+= 1
        print('InterruptorSimples', self.contador['intsimples'], 'x')

    def on_intparalelo(self):
        self.contador['intparalelo'] += 1
        print("InterruptorParalelo", self.contador['intparalelo'],'x')

    def on_intintermed(self):
        self.contador['intintermed'] += 1
        print("InterruptorIntermediario", self.contador['intintermed'], 'x')

    def on_tmd10a(self):
        self.contador['tmd10a'] += 1
        print("Tomada10a", self.contador['tmd10a'], 'x')

    def on_tmd20a(self):
        self.contador['tmd20a'] += 1
        print("Tomada20a", self.contador['tmd20a'], 'x')

    def on_tmd220(self):
        self.contador['tmd220'] += 1
        print("Tomada220", self.contador['tmd220'], 'x')

    def on_cego(self):
        self.contador['cego'] += 1
        print("Cego", self.contador['cego'], 'x')

    def on_furado(self):
        self.contador['furado'] += 1
        print("Furado", self.contador['furado'], 'x')

    def on_coax(self):
        self.contador['coax'] += 1
        print("Coaxial/Rj", self.contador['coax'], 'x')

    def on_placa4x2p1(self):
        self.contador['placa4x2p1'] += 1
        print("Placa4X2P/1", self.contador['placa4x2p1'], 'x')

    def on_placa4x2p2(self):
        self.contador['placa4x2p2'] += 1
        print("Placa4x2P/2", self.contador['placa4x2p2'], 'x')

    def on_placa4x2p3(self):
        self.contador['placa4x2p3'] +=1
        print("Placa4x2P/3", self.contador['placa4x2p3'], 'x')

    def on_placa4x4p2(self):
        self.contador['placa4x4p2'] += 1
        print("Placa4x4P/2", self.contador['placa4x4p2'], 'x')


    def on_placa4x4p4(self):
        self.contador['placa4x4p4'] += 1
        print("Placa4x4P/4", self.contador['placa4x4p4'], 'x')

    def on_placa4x4p6(self):
        self.contador['placa4x4p6'] += 1
        print("Placa4x4p6", self.contador['placa4x4p6'], 'x')

    def sumario_text(self):
        return '\n'.join([f'{btn}: {cnt}' for btn, cnt in self.contador.items()])

    def mostrar_sumario(self):
        self._show_dialog(title='Resumo', text=self.sumario_text())

    def _resultado_pastas(self):
        if platform == 'android':
            from android.storage import app_storage_path
            folder = app_storage_path()
        else:
            folder = os.path.join(os.path.expanduser('~'), 'Documents', 'ResultadosDoApp')
        os.makedirs(folder, exist_ok=True)
        return folder
    

    def salvar_arquivo(self):
        folder = self._resultado_pastas()
        filename = os.path.join(folder, 'resultado.txt')
        with open(filename, 'w', encoding='utf-8') as f:
            timestamp = datetime.now().strftime('%Y=%m-%d %H:%M;%s')
            f.write(f"Resumo gerado em {timestamp}\n\n")
            f.write(self.sumario_text())
            f.write('\n')
        print (f'Resumo Salvo em {filename}')



    def update_file_list(self):
        folder = self._resultado_pastas()
        lst = self.root.ids.sm.get_screen('files').ids.file_list
        lst.clear_widgets()
        for fname in sorted(os.listdir(folder)):
            path = os.path.join(folder, fname)
            if os.path.isfile(path):
                lst.add_widget(
                    OneLineListItem(text=fname, on_release=lambda x, p=path: self._show_file(p))
                )

    def _show_file(self, path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            content = f'Erro ao ler arquivo:\n{e}'
        self._show_dialog(title=os.path.basename(path), text=content)

    def _show_dialog(self, title, text):
        if self.dialog:
            self.dialog.title = title
            self.dialog.text = text
        else:
            self.dialog = MDDialog(title=title, text=text, buttons=[MDFlatButton(text='Fechar', on_release=lambda x: self.dialog.dismiss())])
        self.dialog.open()



    def on_finalizar(self):
        self.salvar_arquivo()


if __name__ == "__main__":
    MainApp().run()