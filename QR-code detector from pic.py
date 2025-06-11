import cv2 as cv

img = cv.imread("qrcode.png")
detector = cv.QRCodeDetector()
data, bbox, _ = detector.detectAndDecode(img)
if bbox is not None:
    for i in range(len(bbox)):
        pt1 = (int(bbox[i][0][0]), int(bbox[i][0][1]))
        pt2 = (int(bbox[(i + 1) % len(bbox)][0][0]), int(bbox[(i + 1) % len(bbox)][0][1]))
        cv.line(img, pt1, pt2, (0, 255, 0), 2)
    if data:
        print(data)
        cv.putText(img, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10),
                   cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
cv.imshow("QR Code Detection", img)
cv.waitKey(0)
cv.destroyAllWindows()
