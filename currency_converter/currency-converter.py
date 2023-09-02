import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

class CurrencyConverter(QWidget):
    def __init__(self):
        super().__init__()

        # Inisialisasi widget
        self.initUI()

    def initUI(self):
        # Buat combo box untuk memilih mata uang asal dan tujuan
        self.cb_from = QComboBox(self)
        self.cb_to = QComboBox(self)

        # Isi combo box dengan daftar mata uang yang tersedia
        self.cb_from.addItems(['USD', 'IDR', 'EUR', 'JPY', 'GBP', 'CNY'])
        self.cb_to.addItems(['USD', 'IDR', 'EUR', 'JPY', 'GBP', 'CNY'])

        # Buat label dan field teks untuk menampilkan nominal yang ingin dikonversi
        self.lbl_amount = QLabel(self)
        self.lbl_amount.setText("Nominal:")
        self.txt_amount = QLineEdit(self)

        # Tulisan dari
        self.lbl_dari = QLabel(self)
        self.lbl_dari.setText("Dari:")

        # Tulisan ke
        self.lbl_ke = QLabel(self)
        self.lbl_ke.setText("Ke:")

        # Buat label dan field teks untuk menampilkan hasil konversi
        self.lbl_result = QLabel(self)
        self.lbl_result.setText("Hasil konversi:")
        self.txt_result = QLineEdit(self)
        self.txt_result.setReadOnly(True)

        # Buat tombol Konversi
        self.btn_convert = QPushButton("Konversi", self)
        self.btn_convert.clicked.connect(self.convert)

        # Atur posisi widget di tata letak
        self.lbl_amount.move(20, 20)
        self.txt_amount.move(80, 20)
        self.lbl_dari.move(20, 53)
        self.lbl_ke.move(200, 53)
        self.cb_from.move(20, 70)
        self.cb_to.move(200, 70)
        self.lbl_result.move(20, 155)
        self.txt_result.move(20, 175)
        self.btn_convert.move(95, 110)
        

        self.setGeometry(850, 400, 290, 210)
        self.setWindowTitle('Konversi Mata Uang')
        self.show()

    def convert(self):
        # Dapatkan mata uang asal dan tujuan dari combo box
        currency_from = self.cb_from.currentText()
        currency_to = self.cb_to.currentText()

        # Dapatkan nominal yang ingin dikonversi dari field teks
        amount = self.txt_amount.text()
        amount = float(amount)  # Ubah ke tipe float

        # URL dasar untuk mengakseS API Open Exchange Rates
        base_url = "https://openexchangerates.org/api/latest.json"

        # Masukkan API key Anda di sini
        api_key = "88817a8f2ee4405f9b6720609eeb424c"

        # Buat permintaan ke API menggunakan metode GET
        response = requests.get(base_url, params={'app_id': api_key})

        # Cek apakah permintaan berhasil
        if response.status_code == 200:
            # Jika berhasil, ubah respons ke dalah format JSON
            data = response.json()
            # Dapatkan nilai tukar mata uang asal ke USD
            rate_from = data['rates'][currency_from]
            # Dapatkan nilai tukar USD ke mata uang tujuan
            rate_to = data['rates'][currency_to]

            # Hitung nilai tukar mata uang asal ke mata uang tujuan
            result = amount * rate_to / rate_from

            # Tampilkan hasil konversi di field teks
            self.txt_result.setText(str(result))
        else:
            # Jika permintaan gagal, tampilkan pesan peringatan
            QMessageBox.warning(self, "Gagal", "Gagal mendapatkan data dari server")

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = CurrencyConverter()
  sys.exit(app.exec_())
