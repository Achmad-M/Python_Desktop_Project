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
        self.hitung_button.clicked.connect(self.tampilkanTabel)

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
            self.tinggi = float(self.tinggi_input.text()) / 100
            self.berat = float(self.berat_input.text())
            
            if self.berat < 500 and self.tinggi < 400:
                # Calculate BMI
                imt = self.berat / (self.tinggi ** 2)

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
                choiceBatas = QMessageBox.warning(self, 'Warning', 'Pastikan Anda Mengukur BMI Manusia Dewasa!', QMessageBox.Ok)
        else:
            choiceAngka = QMessageBox.warning(self, 'Warning', 'Masukkan angka dengan benar!', QMessageBox.Ok)


    def tampilkanTabel(self):
        self.tabel_bmr.setVisible(False)

        # Set row count based on number of categories
        self.tabel_bmr.setRowCount(6)
        # Get gender from combo box
        jenis_kelamin = self.jenis_kelamin_combo.currentText()

        # Set BMI values and categories in table based on gender
        if jenis_kelamin == "Pria":
            self.tabel_bmr.setItem(0, 0, QTableWidgetItem("Berat badan kurang"))
            self.tabel_bmr.setItem(0, 1, QTableWidgetItem("< 18.5"))
            self.tabel_bmr.setItem(1, 0, QTableWidgetItem("Berat badan ideal"))
            self.tabel_bmr.setItem(1, 1, QTableWidgetItem("18.5 - 24.9"))
            self.tabel_bmr.setItem(2, 0, QTableWidgetItem("Berat badan berlebih"))
            self.tabel_bmr.setItem(2, 1, QTableWidgetItem("25 - 29.9"))
            self.tabel_bmr.setItem(3, 0, QTableWidgetItem("Obesitas tingkat 1"))
            self.tabel_bmr.setItem(3, 1, QTableWidgetItem("30 - 34.9"))
            self.tabel_bmr.setItem(4, 0, QTableWidgetItem("Obesitas tingkat 2"))
            self.tabel_bmr.setItem(4, 1, QTableWidgetItem("35 - 39.9"))
            self.tabel_bmr.setItem(5, 0, QTableWidgetItem("Obesitas tingkat 3"))
            self.tabel_bmr.setItem(5, 1, QTableWidgetItem("> 40"))
        elif jenis_kelamin == "Wanita":
            self.tabel_bmr.setItem(0, 0, QTableWidgetItem("Berat badan kurang"))
            self.tabel_bmr.setItem(0, 1, QTableWidgetItem("< 18.5"))
            self.tabel_bmr.setItem(1, 0, QTableWidgetItem("Berat badan ideal"))
            self.tabel_bmr.setItem(1, 1, QTableWidgetItem("18.5 - 24.9"))
            self.tabel_bmr.setItem(2, 0, QTableWidgetItem("Berat badan berlebih"))
            self.tabel_bmr.setItem(2, 1, QTableWidgetItem("25 - 29.9"))
            self.tabel_bmr.setItem(3, 0, QTableWidgetItem("Obesitas tingkat 1"))
            self.tabel_bmr.setItem(3, 1, QTableWidgetItem("30 - 34.9"))
            self.tabel_bmr.setItem(4, 0, QTableWidgetItem("Obesitas tingkat 2"))
            self.tabel_bmr.setItem(4, 1, QTableWidgetItem("35 - 39.9"))
            self.tabel_bmr.setItem(5, 0, QTableWidgetItem("Obesitas tingkat 3"))
            self.tabel_bmr.setItem(5, 1, QTableWidgetItem("> 40"))
            
        self.tabel_bmr.setColumnWidth(0, 150)
        self.tabel_bmr.setColumnWidth(1, 88)

        # Set the height of all rows to 28 pixels
        self.tabel_bmr.verticalHeader().setDefaultSectionSize(28)
        self.tabel_bmr.setFixedSize(self.tabel_bmr.sizeHint())
        self.tabel_bmr.setEditTriggers(QTableWidget.NoEditTriggers)
        
        # Show the table
        if self.tinggi_input.text().isdigit() and self.berat_input.text().isdigit():
            if self.berat < 500 and self.tinggi < 400:
                self.setFixedHeight(600)
                self.tabel_bmr.setVisible(True)


# Run the application
if __name__ == "__main__":
  app = QApplication(sys.argv)
  imt_app = IMTApp()
  sys.exit(app.exec_())
