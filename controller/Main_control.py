from view.main_window import Ui_MainWindow
from .main_page_control import Main_page_control
from .source_folder_control import Source_folder_control
from .library_control import Library_control
from .queue_control import Queue_control
from .playlists_control import Playlists_control

class Main_control():
    def __init__(self, view:Ui_MainWindow):
        self._view = view
        self._main_page_control =  Main_page_control(self._view)
        self._source_folder_ctrl =  Source_folder_control()
        self._library_control =  Library_control()
        self._queue_control =  Queue_control()
        self._playlists_control =  Playlists_control()
        #---------------------------EVENTS-------------------------
        self._view.btn_main_page.clicked.connect(lambda:self._view.stk_main.setCurrentWidget(self._view.pg_main))
        
        self._view.btn_select_folder.clicked.connect(lambda:self._view.stk_main.setCurrentWidget(self._view.pg_select_folder))
        self._view.btn_music_library.clicked.connect(lambda:self._view.stk_main.setCurrentWidget(self._view.pg_music_library))
        self._view.btn_queue.clicked.connect(lambda:self._view.stk_main.setCurrentWidget(self._view.pg_queue))
        self._view.btn_playists.clicked.connect(lambda:self._view.stk_main.setCurrentWidget(self._view.pg_playlists))

    