import numpy as np # use numpy library as np for array object
import cv2 # opencv-python

# segment the pool table used color information
def table_selection(image):
    boundary = [ ([60, 60, 0], [190, 150, 55])] # color boundary for the pool table

    # create NumPy arrays from the boundary
    for (lower, upper) in boundary:
    	lower = np.array(lower, dtype = "uint8")
    	upper = np.array(upper, dtype = "uint8")
     
    	mask = cv2.inRange(image, lower, upper) # create the mask for the selected region
    	result = cv2.bitwise_and(image, image, mask = mask) # remain only the pool table
        
    return result # return table selection

# Canny Edge Detection
def edge_detection(image):
    gray = cv2.cvtColor(table_img, cv2.COLOR_BGR2GRAY) # convert image in to grayscale
    gray = cv2.GaussianBlur(gray,(3, 3),0) # use gaussian blur
    edged = cv2.Canny(gray,50,150,apertureSize = 3) # Canny Edge Detection
    return edged # return edge image


# Hough Lines Detection (with "cv2.HoughLinesP")
def hough_line_P(image, edge_img):
    # Call function "cv2.HoughLinesP" and adjust the parameter for the function 
    lines = cv2.HoughLinesP(edge_img,rho=1,theta=np.pi/180, threshold=158,lines=np.array([]), 
                            minLineLength=508,maxLineGap=192)
    
    line_selection = [1, 2, 6, 7] # line selection for the pool table
    # draw four line for the pool table
    for i in range(4):
        cv2.line(image, (lines[line_selection[i]][0][0], lines[line_selection[i]][0][1]), 
                 (lines[line_selection[i]][0][2], lines[line_selection[i]][0][3]), 
                 (0, 0, 255), 3, cv2.LINE_AA)
   
    return image # return image with four lines for the pool table    

# Hough Lines Detection (with "cv2.HoughLines")
def hough_line(image, edge_img):
    # Call function "cv2.HoughLines" and adjust the parameter for the function
    line = cv2.HoughLines(edge_img,rho=3,theta=np.pi/180, threshold=450)

    # calsulate the line point use "theta" and "rho" value
    
    # Parameters ---------------------------------------------#
    # rho – Distance resolution of the accumulator in pixels. #
    # theta – Angle resolution of the accumulator in radians. #
    #---------------------------------------------------------#
    
    for i in range(1, 5): # calculate points for each line and draw the four lines
        for rho,theta in line[i]:
            a, b = np.cos(theta), np.sin(theta)              # calculate slop scale
            x, y = a*rho, b*rho                            # calculate one point (x0, y0) on the line
            x1, y1 = int(x + 600*(-b)), int(y + 600*(a))   # calculate two end points of the line
            x2, y2 = int(x - 1500*(-b)), int(y - 1500*(a)) # calculate two end points of the line

            cv2.line(image,(x1,y1),(x2,y2),(0,255,255),1) # draw line on the image 
            
    return image # return image with four lines for the pool table

Hough_Line_function = input('(1) cv2.HoughLines (2) cv2.HoughLinesP: ')
           
#--------------------------------------------#
image = cv2.imread('pool.jpg')              # read image
table_img = table_selection(image)           # segment the pool table used color information
edge_img = edge_detection(table_img)         # Canny Edge Detection
if (Hough_Line_function == 1):               #
    line_img = hough_line(image, edge_img)   # Hough Lines Detection
if (Hough_Line_function == 2):               #
    line_img = hough_line_P(image, edge_img) # Hough Lines Detection
#--------------------------------------------#

#cv2.imwrite("1_a-1_function_2.jpg", line_img) # output result image name 1_a.jpg
cv2.imshow("images", line_img) # show result image
cv2.waitKey(0) # system pause