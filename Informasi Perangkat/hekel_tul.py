import sys
import requests
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Buat request ke API IP Geolocation untuk mendapatkan alamat IP publik
        api_key = "5fd6fb2e39ef40ff867ccf0fc55233cc"
        api_url = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}"
        response = requests.get(api_url)

        # Cek status kode HTTP dari response
        if response.status_code == 200:
            # Dapatkan informasi geolokasi dari response API jika request berhasil
            data = response.json()
            self.public_ip_user = data["ip"]
            self.country_user = data["country_name"]
            self.city_user = data["city"]
            self.country_code_user = data["country_code2"]
            self.latitude_user = data["latitude"]
            self.longitude_user = data["longitude"]
            self.currency_user = data["currency"]
            self.isp_user = data["isp"]

        else:
            # Tampilkan pesan error jika request gagal
            print("Terjadi kesalahan saat memproses request. Silakan coba lagi.")

        # Buat label untuk menampilkan alamat IP publik
        self.ip_label = QLabel(f"Alamat IP: {self.public_ip_user}")
        self.country_user_label = QLabel(f"Negara Anda: {self.country_user}")
        self.city_user_label = QLabel(f"Kota Anda: {self.city_user}")
        self.country_code_label = QLabel(f"Kode Negara: {self.country_code_user}")
        self.latitude_user_label = QLabel(f"lat: { self.latitude_user}")
        self.longitude_user_label = QLabel(f"long: {self.longitude_user}")
        self.currency_user_label = QLabel(f"Mata Uang: {self.currency_user}")
        self.isp_user_label = QLabel(f"ISP: {self.isp_user}")
        
        # Buat input untuk alamat IP yang akan dicari informasinya
        self.ip_input = QLineEdit()
        self.ip_input.setPlaceholderText("Masukkan alamat IP yang ingin dicari informasinya")

        # Buat tombol untuk mengirim request ke API IP Geolocation
        self.submit_button = QPushButton("Cari informasi")
        self.submit_button.clicked.connect(self.on_submit)

        # Buat label untuk menampilkan hasil informasi geolokasi
        self.result_label = QLabel()

        # Buat layout vertikal
        layout = QVBoxLayout()

        # Tambahkan widget ke dalam layout
        layout.addWidget(self.ip_label)
        layout.addWidget(self.country_user_label)
        layout.addWidget(self.city_user_label)
        layout.addWidget(self.country_code_label)
        layout.addWidget(self.latitude_user_label)
        layout.addWidget(self.longitude_user_label)
        layout.addWidget(self.currency_user_label)
        layout.addWidget(self.isp_user_label)
        layout.addWidget(self.ip_input)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.result_label)

        # Tambahkan layout ke window
        self.setLayout(layout)

    def on_submit(self):
      # Dapatkan alamat IP yang dimasukkan oleh pengguna
      ip_address = self.ip_input.text()

      # Buat request ke API IP Geolocation menggunakan alamat IP yang didapat
      api_key = "5fd6fb2e39ef40ff867ccf0fc55233cc"
      api_url = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip_address}"
      response = requests.get(api_url)

      # Cek status kode HTTP dari response
      if response.status_code == 200:
          # Dapatkan informasi geolokasi dari response API jika request berhasil
          data = response.json()
          country = data["country_name"]
          city = data["city"]
          country_code = data["country_code2"]
          latitude = data["latitude"]
          longitude = data["longitude"]
          currency = data["currency"]
          isp = data["isp"]

          # Tampilkan informasi di label hasil
          result_text = f"Negara: {country}\nKota: {city}\nKode Negara: {country_code}\nLatitude: {latitude}\nLongitude: {longitude}\nMata Uang: {currency}\nISP: {isp}"
          self.result_label.setText(result_text)
      else:
          # Tampilkan pesan error jika request gagal
          self.result_label.setText("Terjadi kesalahan saat memproses request. Silakan coba lagi.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
