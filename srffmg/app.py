
import streamlit as st
import numpy as np
import cv2 
import matplotlib.pyplot as plt
from PIL import Image 
import time
import copy
import imutils
from scipy.spatial import distance as dist



# neural_net = cv2.dnn.readNet("yolov4-tiny-obj_final.weights", "yolov4-tiny-obj.cfg")


# classes = ["without_mask", "with_mask"]   #Initialize an array to store output labels 
# names_of_layer = neural_net.getLayerNames() 
# #Store the names of model’s layers obtained using getLayerNames() of OpenCV
# output_layers = [names_of_layer[i-1] for i in neural_net.getUnconnectedOutLayers()]
    

    
def sr(my_img):
 
    img = cv2.resize(my_img, None, fx=0.4, fy=0.4)
    height,width,channels = img.shape  
    

    # blob = cv2.dnn.blobFromImage(img, 0.00392, (618, 618), (0, 0, 0), True, crop=False)
    # neural_net.setInput(blob)
    # outs = neural_net.forward(output_layers)

    return img

def main():    
    st.title("Welcome to Streamlit Image SuperResolution app") #Title displayed in UI using streamlit.title()
    #Display some text on UI using streamlit.write()
    st.write("Select one of the following options to proceed:")
    choice = st.radio("", ("See an illustration", "Choose an image of your choice"))
     #streamlit.radio() inserts a radio button widget 

    #If user selects 2nd option:
    if choice == "Choose an image ":
        image_file = st.file_uploader("Upload", type=['jpg','png','jpeg'])

        if image_file is not None:
            my_img = Image.open(image_file)
            # img=obj_detection(my_img)
            img=my_img
            st.set_option('deprecation.showPyplotGlobalUse', False)
            column1, column2 = st.columns(2)
            #Display subheading on top of input image 
            column1.subheader("Input image") #streamlit.subheader()
            st.text("") #streamlit.text() writes preformatted and fixed-width text
            #Display the input image using matplotlib
            plt.figure(figsize = (16,16)) 
            plt.imshow(my_img)
            column1.pyplot(use_column_width=True)
            st.text("") #preformatted and fixed-width text
            column2.subheader("Output image") #Title on top of the output image
            st.text("")
            #Plot the output image with detected objects using matplotlib
            plt.figure(figsize = (15,15))
            plt.imshow(img) #show the figure
            column2.pyplot(use_column_width=True) #actual plotting

        elif choice == "See an illustration":
            #display the example image
            my_img = Image.open("sample.jpg")
            #perform object detection on the example image 
            # img=obj_detection(my_img)
            img=my_img

            st.set_option('deprecation.showPyplotGlobalUse', False)
            column1, column2 = st.columns(2)
            #Display subheading on top of input image 
            column1.subheader("Input image") #streamlit.subheader()
            st.text("") #streamlit.text() writes preformatted and fixed-width text
            #Display the input image using matplotlib
            plt.figure(figsize = (16,16)) 
            plt.imshow(my_img)
            column1.pyplot(use_column_width=True)
            st.text("") #preformatted and fixed-width text
            column2.subheader("Output image") #Title on top of the output image
            st.text("")
            #Plot the output image with detected objects using matplotlib
            plt.figure(figsize = (15,15))
            img = cv2.resize(img,(height,width))
            plt.imshow(img) #show the figure
            column2.pyplot(use_column_width=True) #actual plotting
        

if __name__ == '__main__':
    main()