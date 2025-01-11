import modules_imported as mi
import hand_information as hi
import single_hand_symbols as shs 
import double_hand_letters as dhs
import os
import words as wds
import ActionWords as awds

def sentences_display():
    previous_symbol = ""
    symbol = ""
    screen = mi.vision.VideoCapture(0)
    screen_width, screen_height = mi.cfs.get_screen_widht_height()
    screen.set(3, screen_width)
    screen.set(4, screen_height)

    hand_1 = hi.hand_info()
    hand_2 = hi.hand_info()
    hand_data = None
    hand_1_data = None
    hand_2_data = None
    hand_detector = mi.HandTrackingModule.handDetector()
    display_lines = {}
    display_lines[1] = ""
    line_count = 1
    word_count = 0
    while True:
        success, screen_video = screen.read()  
        if screen_video is None:
            break

        screen_video = mi.vision.flip(screen_video,1)
        mi.vision.putText(screen_video, "Sentences" , (800, 50), mi.vision.FONT_HERSHEY_COMPLEX,1, (255, 0, 0), 2)

        screen_video = hand_detector.findHands(screen_video)
        Hand_1_LandMarks = hand_detector.findPosition(screen_video, 0, draw=False)
        Hand_2_LandMarks = hand_detector.findPosition(screen_video, 1, draw=False)

        hand_1_data = hand_1.get_hand_information(Hand_1_LandMarks,True) 
        hand_2_data = hand_2.get_hand_information(Hand_2_LandMarks,False) 
        

        if hand_1_data is None and hand_2_data is None:
            NoOfHands = 0
        elif hand_1_data is not None and hand_2_data is None:
            if len(hand_1_data['HandLandMarks']) != 0:
                NoOfHands = 1
                hand_data = hand_1_data
            else:
                NoOfHands = 0
        elif hand_1_data is None and hand_2_data is not None:
            if len(hand_2_data['HandLandMarks']) != 0:
                NoOfHands = 1
                hand_data = hand_2_data
            else:
                NoOfHands = 0
        elif hand_1_data is not None and hand_2_data is not None: 
            if len(hand_1_data['HandLandMarks']) != 0 and len(hand_2_data['HandLandMarks']) != 0:
                NoOfHands = 2
            elif len(hand_1_data['HandLandMarks']) != 0 and len(hand_2_data['HandLandMarks']) == 0:
                NoOfHands = 1
                hand_data = hand_1_data
            elif len(hand_1_data['HandLandMarks']) == 0 and len(hand_2_data['HandLandMarks']) != 0:
                NoOfHands = 1
                hand_data = hand_2_data
            elif len(hand_1_data['HandLandMarks']) == 0 and len(hand_2_data['HandLandMarks']) == 0:
                NoOfHands = 0

        if  NoOfHands == 0:
            symbol = previous_symbol
        elif NoOfHands == 1:
            symbol = awds.get_single_hand_action_word(screen)
        elif NoOfHands == 2:
           #symbol = wds.get_two_hand_word(hand_1_data,hand_2_data) 
           if symbol == "":
                symbol = awds.get_two_hand_action_word(screen)
        else:
            symbol = ""

        if symbol != previous_symbol and symbol != "":
            previous_symbol = symbol
            word_count += 1
            if len(display_lines[line_count] + " " + symbol) < 30:
                display_lines[line_count] += " " + symbol
            else:
                line_count += 1
                display_lines[line_count] = symbol

        mi.vision.putText(screen_video, "Sentences", (800, 50), mi.vision.FONT_HERSHEY_COMPLEX,1, (255, 0, 0), 2)
        for i in range(1,line_count+1):
            mi.vision.putText(screen_video, display_lines[i], (20, 200+((i-1)*75)), mi.vision.FONT_HERSHEY_COMPLEX,2, (255, 0, 0), 2)
        mi.vision.imshow("Image", screen_video)
        mi.vision.waitKey(1)
    
    screen.release()


def videos_display_from_opwn_dialog():   
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
            is_log_active = False
            log.write_message("Log Ended","hand_1")
            log.write_message("Log Ended","hand_2")
            mi.vision.putText(action_word_video, "Log Ended", (20, 200), mi.vision.FONT_HERSHEY_COMPLEX,2, (255, 0, 0), 2)
            break

        action_word_video    = mi.vision.flip(action_word_video,1)
        action_word_video    = hand_detector.findHands(action_word_video)
        hand_1.HandLandMarks =  hand_detector.findPosition(action_word_video, 0, draw=False)
        hand_2.HandLandMarks =  hand_detector.findPosition(action_word_video, 1, draw=False)

        if is_log_active == False:
            mi.vision.imshow("Image", action_word_video)
            #if mi.vision.waitKey(1) & 0xFF == ord('q'):
            mi.vision.waitKey(1)
            is_log_active = True
            log.write_message("Log started","hand_1")
            log.write_message("Log started","hand_2")
            mi.vision.putText(action_word_video, "Log started", (20, 200), mi.vision.FONT_HERSHEY_COMPLEX,2, (255, 0, 0), 2)
        else:
            mi.vision.imshow("Image", action_word_video)
            mi.vision.waitKey(1)

        hand_1.data = hand_1.get_hand_information(hand_1.HandLandMarks,True) 
        hand_2.data = hand_2.get_hand_information(hand_2.HandLandMarks,False) 
        if is_log_active == True:
            if len(hand_1.HandLandMarks) != 0:
                log.write_hand_landmarks(hand_1,"hand_1")
            if len(hand_2.HandLandMarks) != 0:
                log.write_hand_landmarks(hand_2,"hand_2")
            mi.vision.putText(action_word_video, "Log started", (20, 200), mi.vision.FONT_HERSHEY_COMPLEX,2, (255, 0, 0), 2)

        mi.vision.imshow("Image", action_word_video)
        mi.vision.waitKey(1)

    return "Exit"


        