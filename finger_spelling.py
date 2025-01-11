import modules_imported as mi
import hand_information as hi
import single_hand_symbols as shs 
import double_hand_letters as dhs
import os

def finger_spelling_display():   #hand_1_data,hand_2_data):
    hand_data = None
    previous_symbol = ""
    symbol = ""
    is_log_active = False
    selected_file = mi.cfs.open_file_dialog()
    #selected_file = "H:/8 Semester/Honors/Challenge/attack.mov"

    log = mi.log.logging()
    hand_1 = hi.hand_info()
    hand_2 = hi.hand_info()
    hand_detector = mi.HandTrackingModule.handDetector()

    if mi.cvs.config_data['log_hand_landmarks_to_file'] == "True":
        if mi.cvs.config_data['take_sample_data'] == "False":
            log.open_log_file(mi.cvs.config_data['take_sample_data_for_symbol'])
        else:
            log.open_log_file(mi.cvs.config_data['take_sample_data_for_symbol'])

    if selected_file == "":
        return "Exit"

    file_name, file_name_extension = os.path.splitext(selected_file)
    file_name_extension = file_name_extension.lower()
    if file_name_extension == ".mov" or file_name_extension == ".mp4":
        screen = mi.vision.VideoCapture(selected_file)  #'H:/8 Semester/Honors/Challenge/1. loud/MVI_5179.MOV')
    while True:
        if file_name_extension == ".mov" or file_name_extension == ".mp4":
            success, action_word_video = screen.read()  # mi.vision.VideoCapture('H:/8 Semester/Honors/what.mp4') #"H:/8 Semester/Honors/Challenge/1. loud/MVI_5177.MOV")        #mi.cvs.screen.read()
        elif file_name_extension == ".jpg" or file_name_extension == ".jpeg" or file_name_extension == ".png":
            action_word_video = mi.vision.imread(selected_file)
        else:
            screen = mi.vision.VideoCapture(0)
            screen_width, screen_height = mi.cfs.get_screen_widht_height()
            screen.set(3, screen_width)
            screen.set(4, screen_height)
            success, action_word_video = screen.read()
            
        if action_word_video is None:
            #selected_file = "H:/8 Semester/Honors/Challenge/animal.mov"
            #file_name, file_name_extension = os.path.splitext(selected_file)
            #file_name_extension = file_name_extension.lower()
            #if file_name_extension == ".mov" or file_name_extension == ".mp4":
            #    screen = mi.vision.VideoCapture(selected_file)  #'H:/8 Semester/Honors/Challenge/1. loud/MVI_5179.MOV')
            #continue
            if mi.cvs.config_data['log_hand_landmarks_to_file'] == "True":
                is_log_active = False
                log.write_message("Log Ended","hand_1")
                log.write_message("Log Ended","hand_2")
                mi.vision.putText(action_word_video, "Log Ended", (20, 200), mi.vision.FONT_HERSHEY_COMPLEX,2, (255, 0, 0), 2)
            break

        action_word_video    = mi.vision.flip(action_word_video,1)
        action_word_video    = hand_detector.findHands(action_word_video)
        hand_1.HandLandMarks =  hand_detector.findPosition(action_word_video, 0, draw=False)
        hand_2.HandLandMarks =  hand_detector.findPosition(action_word_video, 1, draw=False)

        mi.vision.putText(action_word_video, "Text", (20, 200), mi.vision.FONT_HERSHEY_COMPLEX,2, (255, 0, 0), 2)

        if is_log_active == False:
            mi.vision.imshow("Image", action_word_video)
            #if mi.vision.waitKey(1) & 0xFF == ord('q'):
            mi.vision.waitKey(1)
            if mi.cvs.config_data['log_hand_landmarks_to_file'] == "True":
                is_log_active = True
                log.write_message("Log started","hand_1")
                log.write_message("Log started","hand_2")
                mi.vision.putText(action_word_video, "Log started", (20, 200), mi.vision.FONT_HERSHEY_COMPLEX,2, (255, 0, 0), 2)
        else:
            mi.vision.imshow("Image", action_word_video)
            mi.vision.waitKey(1)

        hand_1.data = hand_1.get_hand_information(hand_1.HandLandMarks,True) 
        hand_2.data = hand_2.get_hand_information(hand_2.HandLandMarks,False) 
        if mi.cvs.config_data['log_hand_landmarks_to_file'] == "True":
            if is_log_active == True:
                if len(hand_1.HandLandMarks) != 0:
                    log.write_hand_landmarks(hand_1,"hand_1")
                if len(hand_2.HandLandMarks) != 0:
                    log.write_hand_landmarks(hand_2,"hand_2")
                mi.vision.putText(action_word_video, "Log started", (20, 200), mi.vision.FONT_HERSHEY_COMPLEX,2, (255, 0, 0), 2)

        mi.vision.imshow("Image", action_word_video)
        mi.vision.waitKey(1)

    return "Exit"

'''
import keyboard as kbd
import alphabets as abc

previous_symbol = ''
symbol = ''
word = ''
def finger_spelling_display(hand_1_data, hand_2_data):
    global word
    global previous_symbol
    global symbol
    symbol = kbd.keyboard_symbol_display(hand_1_data,hand_2_data)
    #symbol = abc.letter_display(hand_1_data,hand_2_data)
    if previous_symbol == symbol:
        return word
    else:
        if symbol == ' ':
            return 'Exit'
        else:
            previous_symbol = symbol
            word += str(symbol)
    return word

def populate_fingerspelling(screen,hand_detector,is_capslock_set,hand_1,hand_2,take_sample_data,take_sample_data_for_symbol,include_sound,log_hand_landmarks_to_file):
    global previous_symbol
    global symbol
    global previous_word_symbol
    global word_symbol
    global vision
    global cvs
    try:
        while True:
            #letter_image = vision.imread('images/letter_A.png')
            success, word_image = screen.read()
            vision.putText(word_image, "finger spelling", (700, 50), vision.FONT_HERSHEY_PLAIN,2, (255, 0, 0), 3)
            
            if previous_symbol != symbol:
                if symbol == "CapsLock":
                    if cvs.config_data['CapsLock'] == True:
                        cvs.config_data['CapsLock'] = False
                    else:
                        cvs.config_data['CapsLock'] = True
                elif symbol == "Delete":
                    previous_word_symbol = word_symbol
                    previous_symbol = symbol
                    word_symbol = ""
                    symbol = ""
                elif symbol == "":
                    symbol = previous_symbol
                elif symbol == "BackSpace":
                    word_symbol = word_symbol[:-1]
                elif symbol == "Dummy":
                    symbol = ""
                else:
                    word_symbol = word_symbol + symbol


            previous_word_symbol = word_symbol
            previous_symbol = symbol
                
            if word_symbol != '':
                vision.putText(word_image, word_symbol, (10, 100), vision.FONT_HERSHEY_PLAIN,2, (255, 0, 0), 2)
                vision.putText(word_image, "                     ", (10, 50), vision.FONT_HERSHEY_PLAIN,2, (0, 255, 0), 3)
                #vision.putText(word_image, "Please wait ...      ", (10, 50), vision.FONT_HERSHEY_PLAIN,2, (0, 255, 0), 3)

            if previous_word_symbol != word_symbol and include_sound == True:
                text_to_speech.say(word_symbol)
                text_to_speech.runAndWait()
        
            vision.imshow("Image", word_image)
            vision.waitKey(1)
                
#            if len(Hand_1_LandMarks) !=0:
#                Hand_1_LandMarks.clear()
#            if len(Hand_2_LandMarks) !=0:
#                Hand_2_LandMarks.clear()

            vision.waitKey(200)

    except Exception as err:
        print(err)
        raise
'''