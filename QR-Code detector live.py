import cv2
import pyperclip
import numpy as np


def detect_qr_code():
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        data, bbox, _ = detector.detectAndDecode(frame)
        if bbox is not None:
            bbox = np.int32(bbox)  # تبدیل bbox به عدد صحیح
            for i in range(len(bbox[0])):
                cv2.line(frame, tuple(bbox[0][i]), tuple(bbox[0][(i + 1) % len(bbox[0])]), (0, 255, 0), 2)

            if data and data.strip():  # بررسی مقدار معتبر داده QR
                print(f"QR Code Data: {data}")
                pyperclip.copy(data)
                cv2.putText(frame, data, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

        cv2.imshow("QR Code Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect_qr_code()