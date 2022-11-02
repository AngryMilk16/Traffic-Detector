import cv2

cap = cv2.VideoCapture("Objects/Car1.mp4") #opens the path for video

#tells what objects are moving by removing background
object_detect = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=20)

#sizing frame
def vidsize(frame, scale=1):
    width = int(frame.shape[1] *scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

#reading video and then playing video
while True:

    isTrue, frame = cap.read()
    height, width, _ = frame.shape
    #print(height, width), tells user height and width of screen
    #Reigon of interest
    roi = frame[300: 500, 400: 1000]
    
    mask = object_detect.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        
        area = cv2.contourArea(cnt)
        if area > 800:
            #cv2.drawContours(roi, [cnt], -1, (255, 0, 0), 2) #this highlights objects in blue
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(roi, (x,y), (x + w, y +h), (0, 255, 0), 2)

    frame_rescaled = vidsize(frame)

    #cv2.imshow('roi', roi), shows reigon of interest
    cv2.imshow('video resized', frame_rescaled)

    if cv2.waitKey(20) & 0xFF==ord('d'): #0xFF==ord('d') mean that if the letter 'd' is pressed on the keyboard it closes video
        break

cap.release()
cv2.destroyAllWindows()
