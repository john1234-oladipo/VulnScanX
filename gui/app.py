from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton

class VulnScanGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VulnScanX GUI")
        self.setGeometry(100, 100, 400, 300)
        
        layout = QVBoxLayout()
        self.scan_btn = QPushButton("Run Scan")
        self.scan_btn.clicked.connect(self.run_scan)
        layout.addWidget(self.scan_btn)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def run_scan(self):
        print("Scan initiated...")  # Replace with actual scan logic

app = QApplication([])
window = VulnScanGUI()
window.show()
app.exec_()
