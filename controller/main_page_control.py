from view.main_window import Ui_MainWindow
from PyQt6.QtWidgets import QFileDialog, QMessageBox

class Main_page_control():
    def __init__(self, view:Ui_MainWindow):
        self.view = view
        self.view.btn_open_file_main.clicked.connect(self._select_song_file)
        
    
    """_summary_
    This function creates a QFileDialog to get the name of a song
    """    
    def _select_song_file(self):
        file_name, filter = QFileDialog.getOpenFileName(parent=None, caption='Seleccione un archivo', directory='', filter='MP3 Files (*.mp3)' )
        
        if not file_name:
            QMessageBox.information(None, 'Error de selección de archivo', 'No se seleccionó ningún archivo')