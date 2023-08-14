import numpy as np
import cv2
from sface import SFace

def main():
    cap = cv2.VideoCapture(0)
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    while(True):
        _, frame = cap.read()
        fps = cap.get(cv2.CAP_PROP_FPS)
        cv2.putText(frame, "{}".format(fps), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), thickness=2)
        lists = cascade.detectMultiScale(frame, minSize=(100, 100))
        if len(lists):
            for (x,y,w,h) in lists:
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), thickness=2)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
