import cv2

def main() : 
    path = "girls.jpg"
    img = cv2.imread(path)
    cv2.putText(img, "Hello", (240, 50), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow("test_image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()