import modules_imported as mi
import display_functions as dfs
import single_hand_symbols as shs
import digits as dgs
import alphabets as abc
import finger_spelling as fsg
import keyboard as kbd
import words as wds
import ActionWords as aws
import sentences as ssd
import display_videos as dvs

print("Its okay")

background_image    = mi.vision.imread('Images/HomeScreen2.png')

if mi.cfs.read_config_file(mi.cvs.config_data['config_file_path']) !=0:
    print ('Error in config file reading') 
    exit(-1)

def detect_signs():
    mi.cvs.video_device = mi.cfs.get_video_device()
    screen_width, screen_height = mi.cfs.get_screen_widht_height()

    #mi.cvs.screen = mi.vision.VideoCapture('H:/8 Semester/Honors/Challenge/1. loud/MVI_5177.MOV')  #mi.cvs.video_device)
    screen = mi.vision.VideoCapture(mi.cvs.video_device)
    screen.set(3, screen_width)
    screen.set(4, screen_height)
    #hand_detector = HandTrackingModule.handDetector(detectionCon=0.75)
    hand_detector = mi.HandTrackingModule.handDetector()

    hand_0_previous_symbol = -1
    hand_0_symbol = -1

    hand_1_symbol = -1

    selected_option = mi.ccs.no_selection
    prev_capslock_status = None

    HandLandMarks             = []
    NoOfHands = 0

    sentence = ''
    ret = None
    while True:
        success_menu, menu_image = screen.read()
        if menu_image is None:
            break
        menu_image = hand_detector.findHands(menu_image)

        mi.cfs.include_image(mi.vision,menu_image,background_image,0 ,15 ,1272,670)     #1366,768   #1092,614

        mi.vision.imshow("Image", menu_image)
        mi.vision.waitKey(1)

        ################################### Home screen is displayed ##################################################
        HandLandMarks             = []
        NoOfHands = 0

        HandLandMarks = hand_detector.findPosition(menu_image, draw=False)
        prev_capslock_status = mi.cvs.config_data['CapsLock']    # storing CapsLock status
        mi.cvs.config_data['CapsLock'] = "False"
        if len(HandLandMarks) != 0:
            selected_option = shs.digit_display(HandLandMarks)
            if  selected_option == 99:
                if shs.thumbs_down(HandLandMarks) == True:
                    pass
                else:
                    selected_option = mi.ccs.no_selection

        if mi.cvs.config_data['to_control_flow_for_debug'] == "True":  # this is for hard-coding target option/letter/symbol
            selected_option = int(mi.cvs.config_data['default_option_for_debug'])

        display_position = (20,200)
        if selected_option == mi.ccs.digits_selected:
            ret = dfs.populate("digits", dgs.digit_display)
        elif selected_option == mi.ccs.letters_selected:
            ret = dfs.populate("Alphabets", abc.letter_display)
        elif selected_option == mi.ccs.fingerspelling_selected:
            ret = dfs.populate("Finger spelling",fsg.finger_spelling_display)
        elif selected_option == mi.ccs.keyboard_selected:
            ret = dfs.populate("Keyboard", kbd.keyboard_symbol_display)
        elif selected_option == mi.ccs.words_selected:
            ret = dfs.populate("Words",wds.words_display)
        elif selected_option == mi.ccs.action_words_selected:
            ret = dfs.populate("Action Words",aws.action_words_display)
        elif selected_option == mi.ccs.sentences_selected:
            ret = dfs.populate("Sentences",ssd.sentences_display)
        elif selected_option == mi.ccs.sign_language_selected:
            ret = dfs.populate("Sign Language",dvs.video_symbol_display)
        else:
            if mi.cvs.config_data['take_sample_data'] == "True":
                if int(mi.cvs.config_data['default_option_for_debug']) == mi.ccs.digits_selected:
                    ret = dfs.populate("digits", dgs.digit_display)
                elif int(mi.cvs.config_data['default_option_for_debug']) == mi.ccs.letters_selected:
                    ret = dfs.populate("Alphabets", abc.letter_display)
                elif int(mi.cvs.config_data['default_option_for_debug']) == mi.ccs.fingerspelling_selected:
                    ret = dfs.populate("Finger spelling",fsg.finger_spelling_display)
                elif int(mi.cvs.config_data['default_option_for_debug']) == mi.ccs.keyboard_selected:
                    ret = dfs.populate("Keyboard", kbd.keyboard_symbol_display)
                elif int(mi.cvs.config_data['default_option_for_debug']) == mi.ccs.words_selected:
                    ret = dfs.populate("Words",wds.words_display)
                elif int(mi.cvs.config_data['default_option_for_debug']) == mi.ccs.action_words_selected:
                    ret = dfs.populate("Action Words",aws.action_words_display)
                elif int(mi.cvs.config_data['default_option_for_debug']) == mi.ccs.sentences_selected:
                    ret = dfs.populate("Sentences",ssd.sentences_display)
                elif int(mi.cvs.config_data['default_option_for_debug']) == mi.ccs.sign_language_selected:
                    ret = dfs.populate("Sign Language",dvs.video_symbol_display)

        if ret == "Exit":
            selected_option = mi.ccs.no_selection
            mi.vision.imshow("Image", menu_image)
            mi.vision.waitKey(1)
            #screen.release()
            continue

        mi.cvs.config_data['CapsLock'] = prev_capslock_status  # re-storing CapsLock status
        mi.vision.imshow("Image", menu_image)
        mi.vision.waitKey(1)
                
    #screen.release()
    #mi.vision.destroyAllWindows()   

detect_signs()