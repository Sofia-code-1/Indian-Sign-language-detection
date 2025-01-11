
import modules_imported as mi
import hand_information as hi
import single_hand_symbols as shs 
import double_hand_letters as dhs

def letter_display():  #hand_1_data,hand_2_data):
    previous_symbol = ""
    symbol = ""
    mi.cvs.config_data['CapsLock'] = "True"
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
    while True:
        success, screen_video = screen.read()  
        if screen_video is None:
            break

        mi.vision.putText(screen_video, "Alphabets" , (800, 50), mi.vision.FONT_HERSHEY_COMPLEX,1, (255, 0, 0), 2)

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
           symbol = shs.single_hand_letters_display(hand_data['HandLandMarks'])
        elif NoOfHands == 2:
           symbol = dhs.double_hand_letters_display(hand_1_data,hand_2_data)
        else:
            symbol = ""

        if symbol == "Exit":
            screen.release()
            break

        if symbol != previous_symbol:
            previous_symbol = symbol

        mi.vision.putText(screen_video, str(symbol), (150, 450), mi.vision.FONT_HERSHEY_COMPLEX,10, (255, 0, 0), 10)
        mi.vision.imshow("Image", screen_video)
        mi.vision.waitKey(1)
    screen.release()
    
    return symbol

        