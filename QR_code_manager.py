from tkinter import filedialog, messagebox
import os
from pathlib import Path
from window_dialog import *
import sys
import qrcode
from io import BytesIO

path = str(Path(__file__).parent.absolute())

class Dialog(QMainWindow, Ui_Dialog):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        self.setFixedSize(342, 435)
        self.qr_code_field.setPixmap(QPixmap(self.resource_path("ExampleQR.png")))
        
        self.generate_qr_btn.clicked.connect(lambda: self.generate_qr_code())
        self.download_qr_btn.clicked.connect(lambda: self.download_qr_code())
        self.qr_img = ""
    
    def generate_qr_code(self):
        
        data = self.qr_contents_field.text()
        qr = qrcode.QRCode( version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4, ) 
        qr.add_data(data) 
        qr.make(fit=True) 
        self.qr_img = qr.make_image(fill_color="black", back_color="white")
        
        byte_img = BytesIO()
        self.qr_img.save(byte_img,format="PNG")
        qt_image = QImage.fromData(byte_img.getvalue())
        pix = QPixmap.fromImage(qt_image)
        
        self.qr_code_field.setPixmap(pix)
    
    def download_qr_code(self):
        if self.qr_img == "":
            self.show_error_message("ERROR", "QR CODE NOT GENERATED")
        else:
            self.qr_img.save(path + "\\Generated QR CODE.png")
            self.show_info_message("QR CODE GENERATOR", "QR CODE DOWNLOADED")
            
    def show_error_message(self, title, message):
        messagebox.showerror(title,message)
    
    def show_info_message(self,title,message):
        messagebox.showinfo(title,message)
        
    def resource_path(self,relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Dialog()
    main_window.show()
    sys.exit(app.exec_())