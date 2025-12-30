import qrcode
import barcode
from barcode.writer import ImageWriter
from IPython.display import display
from PIL import Image

def QrCodeCreate():
      link = input("Enter anuthing to generate QRcode:")
      qr = qrcode.QRCode(version=2, box_size=10, border=4)
      qr.add_data(link)
      qr.make(fit=True)
      fill = input("Select color to fill(black, white):")
      backColor = input("Select color to back color(black, white):")
      image = qr.make_image(fill=fill, back_color=backColor)
      image.save("QRCode.png")
      Image.open("QRCode.png")
def BarCodeCreate():
      barcodeNumber = input("Write barcode number(EAN must have 12 digits):")
      
      barcode_format = barcode.get_barcode_class("ean13")
      barcode_number = barcodeNumber
      barcode_image = barcode_format(barcode_number, writer=ImageWriter())
      barcode_filename = "barcode_image"
      barcode_image.save(barcode_filename)
      display(Image=f"{barcode_filename}.png")
def menu():
    while True:
        print("""
  ___  ____               _                    
 / _ \|  _ \ ___ ___   __| | ___               
| | | | |_) / __/ _ \ / _` |/ _ \              
| |_| |  _ < (_| (_) | (_| |  __/              
 \__\_\_| \_\___\___/ \__,_|\___|_             
  __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| (_| |  __/ | | |  __/ | | (_| | || (_) | |   
 \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|   
 |___/                                          
by: pyps231
          """)

        print("===MENU===\n1.CreateQrCode\n2.CreateBarCode\n3.Exit")
        select = int(input("Select(1,2,3):"))

        if select == 1:
          QrCodeCreate()
        if select == 2:
          BarCodeCreate()
        if select == 3:
          print("EXIT...")
          break
    
menu()