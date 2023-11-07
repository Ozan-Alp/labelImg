import cv2 

def get_contrast(img):
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img_grey.std()
# define a video capture object 
vid = cv2.VideoCapture(r"c:\Users\ozan\Downloads\DJI_0010.MP4") 
i=0
max_cont=0
framecount=30
for k in range(100): 
      
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 
    i+=1
    if ret:
        if (cur_val:=get_contrast(frame)) > max_cont:
            best_img=frame
            max_cont=cur_val
            best_idx=i
        if i%30==0:
            cv2.imwrite(r"C:\\Users\\ozan\Desktop\\lol\\"+str(best_idx)+".jpeg", frame)
            max_cont=0
        # Display the resulting frame 
        cv2.imshow('frame', frame) 
        
        # the 'q' button is set as the 
        # quitting button you may use any 
        # desired button of your choice 
        if cv2.waitKey(1) & 0xFF == ord('q') or i==67: 
            break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 