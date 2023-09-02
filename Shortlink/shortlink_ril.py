import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import requests
from PyQt5.QtSvg import QSvgWidget


API_KEY = '28299270c38eb346d372112bdbaefed14bc4a'
BASE_URL = 'https://cutt.ly/api/api.php'

class LinkShortener(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Link Shortener')
        
        # Buat widget untuk input link
        self.link_label = QLabel('Link:', self)
        self.link_input = QLineEdit(self)
        
        # Buat widget untuk output link yang sudah di-short
        self.short_link_label = QLabel('Link yang sudah di-short:', self)
        self.short_link_output = QLineEdit(self)
        self.short_link_output.setReadOnly(True)
        
        # Buat widget tombol short link
        self.short_button = QPushButton('Short Link', self)
        self.short_button.clicked.connect(self.shortLink)
        
        # Buat widget tombol copy to clipboard
        self.copy_button = QPushButton('Copy to Clipboard', self)
        self.copy_button.clicked.connect(self.copyToClipboard)


        # Buat widget tombol untuk ganti mode tampilan
        self.mode_button = QPushButton('Change theme',self)
        self.mode_button.setFixedSize(115, 40)

       # self.mode_button.setFixedSize(32, 32)  # Atur ukuran tombol
        self.mode_button.clicked.connect(self.changeMode)  # Tambahkan event handler untuk tombol
        
        # Buat layout horizontal untuk link input dan tombol short link
        hbox_link = QHBoxLayout()
        hbox_link.addWidget(self.link_label)
        hbox_link.addWidget(self.link_input)
        hbox_link.addWidget(self.short_button)
        
        
        # Buat layout horizontal untuk output link dan tombol copy to clipboard
        hbox_output = QHBoxLayout()
        hbox_output.addWidget(self.short_link_label)
        hbox_output.addWidget(self.short_link_output)
        hbox_output.addWidget(self.copy_button)
        
        # Buat layout horizontal untuk tombol mode tampilan
        hbox_mode = QHBoxLayout()

        # Tambahkan spacer widget ke layout horizontal
        hbox_mode.addStretch()

        # Tambahkan mode_button ke layout horizontal
        hbox_mode.addWidget(self.mode_button)


        
        # Buat layout vertical untuk semua widget
        vbox = QVBoxLayout()
        vbox.addLayout(hbox_link)
        vbox.addLayout(hbox_output)
        # Sisipkan mode_button di bagian atas tata letak
        vbox.insertLayout(0, hbox_mode)
        # Tambahkan layout horizontal ke layout vertikal
        vbox.addLayout(hbox_mode)

        # Buat widget untuk menampilkan history link
        self.history_label = QLabel('History:', self)
        self.history_list = QListWidget(self)

        # Buat tombol hapus history
        self.clear_history_button = QPushButton('Clear History', self)
        self.clear_history_button.clicked.connect(self.clearHistory)

        # Tambahkan widget history dan tombol hapus ke layout vertical
        vbox.addWidget(self.history_label)
        vbox.addWidget(self.history_list)
        vbox.addWidget(self.clear_history_button)

        # Atur layout untuk widget utama
        self.setLayout(vbox)
    
    def shorten_link(self, full_link):

        self.payload = {'key': API_KEY, 'short' : full_link, 'name' : None}
        self.request = requests.get(BASE_URL, params=self.payload)
        self.data = self.request.json()

        print(' ')

        try:
            self.title = self.data['url']['title']
            self.short_link = self.data['url']['shortLink']

            print('Title:', self.title)
            print('Link:', self.short_link)
        except:
            self.status = self.data['url']['status']
            print('Error Status :', self.status)
    
    def shortLink(self):
        # Ambil input link dari widget input link
        link = self.link_input.text()
        
        # Proses short link di sini
        self.shorten_link(link)
        
        # Tampilkan short link di widget output
        self.short_link_output.setText(self.short_link)
        
        # Tambahkan link ke history
        self.history_list.addItem(f"{link}  ->  {self.short_link}")
    
    def copyToClipboard(self):
        # Ambil text dari widget output link yang sudah di-short
        text = self.short_link_output.text()
        
        # Salin text ke clipboard
        clipboard = QApplication.clipboard()
        clipboard.setText(text)
    
    def changeMode(self):
        # Buat widget QSvgWidget
        self.svg_widget = QSvgWidget()
        path_to_svg_bulan = os.path.join('', 'Bulan_Putih.svg')
        path_to_svg_cerah = os.path.join('', 'Cerah_Putih.svg')
        # Tampilkan asset1.png jika program berada di light mode
        # Tampilkan asset2.png jika program berada di dark mode
        if self.palette().color(QPalette.Window).lightness() > 128:  # Cek jika program berada di light mode
            # Ganti ke dark mode
            self.mode_button.setText(None)
            self.setStyleSheet('background-color: #333333; color: #CCCCCC')
            self.mode_button.setIcon(QIcon(path_to_svg_bulan))
            self.mode_button.setFixedSize(40, 40)
            self.mode_button.setIconSize(QSize(35, 35))

        else:
            # Ganti ke light mode
            self.mode_button.setText(None)
            self.setStyleSheet('background-color: #FFFFFF; color: #000000')
            self.mode_button.setIcon(QIcon(path_to_svg_cerah))
            self.mode_button.setFixedSize(40, 40)
            self.mode_button.setIconSize(QSize(35, 35))
            

    
    def clearHistory(self):
        # Hapus semua item di history
        self.history_list.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LinkShortener()
    ex.show()
    sys.exit(app.exec_())

