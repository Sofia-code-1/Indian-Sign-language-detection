#common functions used across files

import cv2 as vision
import json
import log_functions as log
import common_variables as cvs



def read_config_file(config_file_path):
    try:
        with open(config_file_path, 'r') as config_file:
            data = json.load(config_file)
    except FileNotFoundError:
        print(f"The file '{config_file_path}' does not exist.")
        return -1
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return -2
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return -3

    cvs.config_data['include_letters']              = data.get('alphabets',{})
    cvs.config_data['include_words']                = data.get('words',{})
    cvs.config_data['include_action_words']         = data.get('action_words',{})
    cvs.config_data['webcam']                       = data.get('webcam') 
    cvs.config_data['CapsLock']                     = data.get('CapsLock') 
    cvs.config_data['debug']                        = data.get('debug') 
    cvs.config_data['to_control_flow_for_debug']    = data.get('to_control_flow_for_debug') 
    cvs.config_data['default_option_for_debug']     = data.get('default_option_for_debug') 
    cvs.config_data['log_file_path']                = data.get('log_file_path') 
    cvs.config_data['log_file_path_for_sample_data']= data.get('log_file_path_for_sample_data') 
    cvs.config_data['log_hand_landmarks_to_file']   = data.get('log_hand_landmarks_to_file') 
    cvs.config_data['take_sample_data']             = data.get('take_sample_data') 
    cvs.config_data['take_sample_data_for_symbol']  = data.get('take_sample_data_for_symbol') 
    cvs.config_data['take_images_of_symbols']       = data.get('take_images_of_symbols') 
    cvs.config_data['include_sound']                = data.get('include_sound') 

    if cvs.config_data['webcam'] == 'yes':
       video_device = 1
    else:
       video_device = 0
    cvs.config_data['debug']           = data.get('debug') 
    return 0


def diff(x,y,val):
    if (((x-y) >=0 and (x-y) <= val) or ((y-x) >=0 and (y-x) <= val)):
        return True
    else:
        return False

def outside_diff(x,y,val):
    if (((x-y) >= val) or ((y-x) >= val)):
        return True
    else:
        return False

def x_inbetween(x,x1,x2,val=0):
    if (((x >= (x1-val)) and (x <= (x2+val))) or ((x >= (x2-val)) and (x <= (x1+val)))):
        return True
    else:
        return False

def diff_between(l_1,l_2,l_3,r_1,r_2,r_3,val):
    if (((l_2 >= (r_1-val)) and (l_2 <= (r_3+val))) or ((l_2 >= (r_3-val)) and (l_2 <= (r_1+val)))) \
        and \
       (((r_2 >= (l_1-val)) and (r_2 <= (l_3+val))) or ((r_2 >= (l_3-val)) and (r_2 <= (l_1+val)))):
        return True
    else:
        return False

def diff_in_direction(x,y,val):
    if (((x-y) >=0 and (x-y) <= val) or ((y-x) >=0 and (y-x) <= val)):
        return 0
    elif (x-y) > val:
        return 1
    elif (y-x) > val:
        return -1
    else:
        return None


def print_hand_landmarks(RightHandLandMarks,LeftHandLandMarks,vision,image,symbol,left=100,top=20,gap=25,color=(0,200,0)): 

    if len(RightHandLandMarks) !=0:
        vision.putText(image,"First Hand:",(left, top+0*gap), vision.FONT_HERSHEY_COMPLEX,1, color, 2)
        vision.putText(image,str(RightHandLandMarks[0]),(left, top+1*gap), vision.FONT_HERSHEY_COMPLEX,1, color, 2)
        vision.putText(image,str(RightHandLandMarks[1]),(left, top+2*gap), vision.FONT_HERSHEY_COMPLEX,1, color, 2)
        vision.putText(image,str(RightHandLandMarks[2]),(left, top+3*gap), vision.FONT_HERSHEY_COMPLEX,1, color, 2)
        vision.putText(image,str(RightHandLandMarks[3]),(left, top+4*gap), vision.FONT_HERSHEY_COMPLEX,1, color, 2)
        vision.putText(image,str(RightHandLandMarks[4]),(left, top+5*gap), vision.FONT_HERSHEY_COMPLEX,1, color, 2)

    if len(LeftHandLandMarks) !=0:
        vision.putText(image,"Second Hand:",(left, top+6*gap), vision.FONT_HERSHEY_COMPLEX,1, (0,255, 0), 2)
        vision.putText(image,str(LeftHandLandMarks[0]),(left, top+7*gap), vision.FONT_HERSHEY_COMPLEX,1, color, 2)
        vision.putText(image,str(LeftHandLandMarks[1]),(left, top+8*gap), vision.FONT_HERSHEY_COMPLEX,1, color, 2)
        vision.putText(image,str(LeftHandLandMarks[2]),(left, top+9*gap), vision.FONT_HERSHEY_COMPLEX,1, color, 2)
        vision.putText(image,str(LeftHandLandMarks[3]),(left, top+10*gap), vision.FONT_HERSHEY_COMPLEX,1, color, 2)
        vision.putText(image,str(LeftHandLandMarks[4]),(left, top+11*gap), vision.FONT_HERSHEY_COMPLEX,1, color, 2)
    
    if len(RightHandLandMarks) !=0:
        print("First Hand: " + str(RightHandLandMarks[0]))
        print(str(RightHandLandMarks[1])+","+str(RightHandLandMarks[2])+","+str(RightHandLandMarks[3])+","+str(RightHandLandMarks[4]))
        print(str(RightHandLandMarks[5])+","+str(RightHandLandMarks[6])+","+str(RightHandLandMarks[7])+","+str(RightHandLandMarks[8]))
        print(str(RightHandLandMarks[9])+","+str(RightHandLandMarks[10])+","+str(RightHandLandMarks[11])+","+str(RightHandLandMarks[12]))
        print(str(RightHandLandMarks[13])+","+str(RightHandLandMarks[14])+","+str(RightHandLandMarks[15])+","+str(RightHandLandMarks[16]))
        print(str(RightHandLandMarks[17])+","+str(RightHandLandMarks[18])+","+str(RightHandLandMarks[19])+","+str(RightHandLandMarks[20]))
    if len(LeftHandLandMarks) !=0:
        print("Second Hand: " + str(LeftHandLandMarks[0]))
        print(str(LeftHandLandMarks[1])+","+str(LeftHandLandMarks[2])+","+str(LeftHandLandMarks[3])+","+str(LeftHandLandMarks[4]))
        print(str(LeftHandLandMarks[5])+","+str(LeftHandLandMarks[6])+","+str(LeftHandLandMarks[7])+","+str(LeftHandLandMarks[8]))
        print(str(LeftHandLandMarks[9])+","+str(LeftHandLandMarks[10])+","+str(LeftHandLandMarks[11])+","+str(LeftHandLandMarks[12]))
        print(str(LeftHandLandMarks[13])+","+str(LeftHandLandMarks[14])+","+str(LeftHandLandMarks[15])+","+str(LeftHandLandMarks[16]))
        print(str(LeftHandLandMarks[17])+","+str(LeftHandLandMarks[18])+","+str(LeftHandLandMarks[19])+","+str(LeftHandLandMarks[20]))

    print(symbol + " and " + str(cvs.config_data['CapsLock']))

from tkinter import *
def get_screen_widht_height():
    screen_width, screen_height = 0,0
    #Import the required libraries
    #Create an instance of tkinter frame
    win= Tk()
    #Get the current screen width and height
    screen_width, screen_height =  win.winfo_screenwidth(), win.winfo_screenheight()

    win.destroy()
    return screen_width, screen_height

import tkinter as tk
from tkinter import filedialog
def open_file_dialog():
    root = tk.Tk()
    #root.withdraw()  # Hide the main window
    #root.lower()
    root.iconify()

    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=(("Video files", "*.mov;*.mp4"),("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*"))
    )

    if file_path:
        # my_selected_file = file_path
        #print(f"Selected file: {file_path}")
        # You can handle the selected file path as needed (e.g., read the file, process it, etc.)
        return file_path
    else:
        return ""

def get_video_device():
    return cvs.video_device

def include_image(vision,main_image,image,x,y,width,height):
    image_resized = vision.resize(image, (width, height))

    # Create a region of interest (ROI) on the main image where the icon will be placed
    roi   = main_image[y:y+image_resized.shape[0], x:x+image_resized.shape[1]]

    # Check if the ROI dimensions are valid
    if roi.shape[0] == 0 or roi.shape[1] == 0:
        print("Error: Invalid ROI dimensions.")
        exit()

    # Create a mask for the icon
    mask = vision.cvtColor(image_resized, vision.COLOR_BGR2GRAY)
    ret, mask = vision.threshold(mask, 10, 255, vision.THRESH_BINARY)

    # Invert the mask
    mask_inv = vision.bitwise_not(mask)

    # Use the mask to place the icon on the ROI
    main_image_bg = vision.bitwise_and(roi, roi, mask=mask_inv)
    image_fg      = vision.bitwise_and(image_resized, image_resized, mask=mask)
    combined = vision.addWeighted(main_image_bg, 1, image_fg, 1, 0)

    # Place the combined image back onto the main image
    main_image[y:y+image_resized.shape[0], x:x+image_resized.shape[1]] = combined


def initialize_commaon_variables():
    cvs.config_data = {'config_file_path':'configuration.json','include_letters':{},'include_words':{},
               'webcam':'',
               'CapsLock':None,'debug':None,'to_control_flow_for_debug':None,
               'log_file_path':'','log_file_path_for_sample_data':'','log_hand_landmarks_to_file':None,
               'take_sample_data':None,'take_sample_data_for_symbol':'',
               'take_images_of_symbols':None,
               'include_sound':None
               }
    cvs.video_device          = 0
    cvs.screen                = None
    cvs.hand_detector         = None
    cvs.hand_1                = None
    cvs.hand_2                = None
    cvs.Hand_1_LandMarks      = []
    cvs.Hand_2_LandMarks      = []

    cvs.previous_symbol = ''
    cvs.symbol          = ''
    cvs.symbol_mached   = False

    cvs.previous_word_symbol = ''
    cvs.word_symbol          = ''

