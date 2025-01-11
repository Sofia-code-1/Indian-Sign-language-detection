import modules_imported as mi
import hand_information as hi

#import ActionWords as aws

def populate(text,function=""):
    Hand_1_LandMarks = []
    Hand_2_LandMarks = []
    hand_1 = None
    hand_2 = None
    hand_1_data = None
    hand_2_data = None
    previous_symbol = ""
    symbol = ""
    previous_word_symbol = ""
    word_symbol = ""
    hand_detector = mi.HandTrackingModule.handDetector()
    screen = mi.vision.VideoCapture(0)
    try:
        while True:
            success, display_functions_video = screen.read()
            display_functions_video = hand_detector.findHands(display_functions_video)

            Hand_1_LandMarks = hand_detector.findPosition(display_functions_video, 0, draw=False)
            if len(Hand_1_LandMarks) != 0 and hand_1 is not None:
                hand_1_data = hand_1.get_hand_information(Hand_1_LandMarks,True) 

            Hand_2_LandMarks = hand_detector.findPosition(display_functions_video, 1, draw=False)

            if len(Hand_2_LandMarks) !=0 and hand_2 is not None:
                hand_2_data = hand_2.get_hand_information(Hand_2_LandMarks,False) 

            if (hand_1_data is None and hand_2_data is None)   or \
                (len(hand_1_data) == 0 and hand_2_data is None) or \
                (hand_1_data is None and len(hand_2_data) == 0) or \
                (len(hand_1_data) == 0 and len(hand_2_data) == 0):
                    symbol = ""
            else:
                if hand_1_data is not None:
                    if len(hand_1_data['HandLandMarks']) ==0:
                        hand_1_data['HandLandMarks'] = Hand_1_LandMarks
                if hand_2_data is not None:
                    if len(hand_2_data['HandLandMarks']) ==0:
                        hand_2_data['HandLandMarks'] = Hand_2_LandMarks

            if function != "":
                if(text == "Sign Language"):
                    symbol = function()  
                    if symbol == "Backspace":
                        if len(word_symbol)>0:
                            word_symbol = word_symbol[:-1] 
                    if previous_symbol != symbol:
                        previous_symbol = symbol
                        if symbol == "Del":
                            word_symbol = "" 
                        else:
                            if symbol != "Backspace":
                                word_symbol += str(symbol)

                        if previous_word_symbol != word_symbol:
                            previous_word_symbol = word_symbol

                else:
                    symbol = function()

                if symbol == 'Exit':
                    mi.vision.imshow("Image", display_functions_video)
                    mi.vision.waitKey(1)
                    screen.release()
                    return symbol
                    #break

            mi.vision.imshow("Image", display_functions_video)
            mi.vision.waitKey(1)
        
        screen.release()
        return False
    except Exception as err:
        print(err)
        #screen.release()
        mi.vision.destroyAllWindows()   
        raise

