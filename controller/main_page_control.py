from view.main_window import Ui_MainWindow
from PyQt6.QtWidgets import QFileDialog, QMessageBox
from model.model import Mp3Player

class Main_page_control():
    def __init__(self, view:Ui_MainWindow):
        self._view = view
        self._view.btn_open_file_main.clicked.connect(self._select_song_file)
        self._model_player = Mp3Player()
    
    def _select_song_file(self):
        """This function open a QFileDialog to select a MP3 file to play.

        Returns:
            str: The song's name if QFileDialog works well. Empty string if no file is selected.
        """
        file_name, filter = QFileDialog.getOpenFileName(parent=None, caption='Seleccione un archivo', directory='', filter='MP3 Files (*.mp3)' )
        
        if file_name:
            self._play_song(file_name)
        else:
            QMessageBox.information(None, 'Error de selección de archivo', 'No se seleccionó ningún archivo')
            self._play_song(None)
    
    def _play_song(self, file_name):
        play_song = self._model_player.play_song(file_name)
        if play_song[0]:
            QMessageBox.information(None, 'Error de reproducción', play_song[0])