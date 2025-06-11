import cv2 as cv
import qrcode
def g(data, filename="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    img_cv = cv.imread(filename)
    cv.imshow("QR Code", img_cv)
    cv.waitKey(0)
    cv.destroyAllWindows()
if __name__ == "__main__":
    user_input = input("Please enter your data :")
    g(user_input)
