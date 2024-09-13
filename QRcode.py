import qrcode
import cv2
from PIL import Image

data = "https://www.linkedin.com/company/cognoriseinfotech/posts/?feedView=all"
img = qrcode.make(data)
img.save('QRCode.png')

def reading_qr(qr):
    img = cv2.imread(qr)
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)
    
reading_qr("QRcode.png")