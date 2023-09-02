# Import required modules
import sys
from PyQt5.QtWidgets import *

class IMTApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set the size of the window
        self.setFixedWidth(296)
        # Create labels and input fields for height and weight
        tinggi_label = QLabel("Tinggi Badan (cm):", self)
        self.tinggi_input = QLineEdit(self)

        berat_label = QLabel("Berat Badan (kg):", self)
        self.berat_input = QLineEdit(self)

        # Create label and combo box for gender
        jenis_kelamin_label = QLabel("Jenis Kelamin:", self)
        self.jenis_kelamin_combo = QComboBox(self)
        self.jenis_kelamin_combo.addItems(["Pria", "Wanita"])

        # Create calculate button
        self.hitung_button = QPushButton("Hitung IMT", self)
        self.hitung_button.clicked.connect(self.hitungIMT)


        # Create label to display calculation result
        self.hasil_label = QLabel("", self)

        # Create table to display BMI values
        self.tabel_bmr = QTableWidget(self)
        self.tabel_bmr.setColumnCount(2)
        self.tabel_bmr.setHorizontalHeaderLabels(["Kategori", "IMT"])
        self.tabel_bmr.setVisible(False)
        # Set layout
        layout = QVBoxLayout(self)
        layout.addWidget(tinggi_label)
        layout.addWidget(self.tinggi_input)
        layout.addWidget(berat_label)
        layout.addWidget(self.berat_input)
        layout.addWidget(jenis_kelamin_label)
        layout.addWidget(self.jenis_kelamin_combo)
        layout.addWidget(self.hitung_button)

        layout.addWidget(self.hasil_label)
        layout.addWidget(self.tabel_bmr)

        self.setLayout(layout)
        self.setWindowTitle("Indeks Massa Tubuh")
        self.show()

    def hitungIMT(self):
        self.hasil_label.setText(" ")
        self.setFixedHeight(264)
        if self.tinggi_input.text().isdigit() and self.tinggi_input.text().isdigit():

            # Get height and weight from input fields
            tinggi = float(self.tinggi_input.text()) / 100
            berat = float(self.berat_input.text())

            # Calculate BMI
            imt = berat / (tinggi ** 2)

            # Get gender from combo box
            jenis_kelamin = self.jenis_kelamin_combo.currentText()

            # Determine ideal weight status based on BMI and gender
            if jenis_kelamin == "Pria":
                if imt < 18.5 :
                    status = "Berat badan kurang"
                elif imt >= 18.5 and imt < 24.9:
                    status = "Berat badan ideal"
                elif imt >= 25 and imt < 29.9:
                    status = "Berat badan berlebih"
                elif imt >= 30 and imt < 34.9:
                    status = "Obesitas tingkat 1"
                elif imt >= 35 and imt < 39.9:
                    status = "Obesitas tingkat 2"
                else:
                    status = "Obesitas tingkat 3"

            elif jenis_kelamin == "Wanita":
                if imt < 18.5 :
                    status = "Berat badan kurang"
                elif imt >= 18.5 and imt < 24.9:
                    status = "Berat badan ideal"
                elif imt >= 25 and imt < 29.9:
                    status = "Berat badan berlebih"
                elif imt >= 30 and imt < 34.9:
                    status = "Obesitas tingkat 1"
                elif imt >= 35 and imt < 39.9:
                    status = "Obesitas tingkat 2"
                else:
                    status = "Obesitas tingkat 3"

            # Display calculation result in label
            self.hasil_label.setText(f"IMT: {imt:.2f} ({status})")
        else:
            choice = QMessageBox.warning(self, 'Warning', 'Masukkan angka dengan benar!', QMessageBox.Ok)


# Run the application
if __name__ == "__main__":
  app = QApplication(sys.argv)
  imt_app = IMTApp()
  sys.exit(app.exec_())
