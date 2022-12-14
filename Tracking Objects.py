import cv2


## Object detectin with WebCam

cap = cv2.VideoCapture(0)

# tracker = cv2.legacy.TrackerMOSSE_create()
tracker = cv2.TrackerCSRT_create()
success,img = cap.read()
## Initializing the bounding Box
bbox = cv2.selectROI('Tracking',img,False)
## Determing the bounding box where we should draw the bounding box
tracker.init(img, bbox)

## We are fixing our bounding box with drawBox function.
def drawBox(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img, 'On tracking', (75, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (125, 255, 0), 2)



while True:
    timer = cv2.getTickCount()

    ## This gives us our frame
    success,img = cap.read()
    ## FPS formula to display it on our frame
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

    ## We are updating our tracker with 'img'
    success,bbox = tracker.update(img)
    print(bbox)
    if success:
        drawBox(img,bbox)
    else:
        cv2.putText(img, 'LOST', (75, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.putText(img,str(int(fps)),(75,50),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

    cv2.imshow('Tracking',img)


    ## If we press 'q' our program will end the program.

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

