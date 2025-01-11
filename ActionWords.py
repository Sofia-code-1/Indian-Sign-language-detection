import modules_imported as mi
import hand_information as hi
import alphabets        as abc
import pyttsx3          as tts
import numpy            as np
import words as wds

mp_holistic = mi.mp.solutions.holistic # Holistic model
mp_drawing  = mi.mp.solutions.drawing_utils # Drawing utilities


#action_word_symbol = ''
is_log_active = False

def populate_okay(HandOneLandMarksDict, HandTwoLandMarksDict, frame_difference):
    action_word_symbol = ""

    if  HandOneLandMarksDict[mi.ccs.FingerTipLandMarks[0]][1] < HandOneLandMarksDict[mi.ccs.FingerTipLandMarks[0] - 1][1] \
    and HandOneLandMarksDict[mi.ccs.FingerTipLandMarks[1]][2] > HandOneLandMarksDict[mi.ccs.FingerTipLandMarks[1] - 2][2] \
    and HandOneLandMarksDict[mi.ccs.FingerTipLandMarks[2]][2] < HandOneLandMarksDict[mi.ccs.FingerTipLandMarks[2] - 2][2] \
    and HandOneLandMarksDict[mi.ccs.FingerTipLandMarks[3]][2] < HandOneLandMarksDict[mi.ccs.FingerTipLandMarks[3] - 2][2] \
    and HandOneLandMarksDict[mi.ccs.FingerTipLandMarks[4]][2] < HandOneLandMarksDict[mi.ccs.FingerTipLandMarks[4] - 2][2]:
        action_word_symbol = "Okay"

    return action_word_symbol

def populate_book(HandOneLandMarksDict,HandTwoLandMarksDict,frame_difference):
    action_word_symbol = ""
    is_symbol_found = False

    HandOneLandMarksCount     = frame_difference
    HandOneLandMarksDiffDict  = {}
    HandOneLandMarksDiffCount = 0

    HandTwoLandMarksCount     = frame_difference
    HandTwoLandMarksDiffDict  = {}
    HandTwoLandMarksDiffCount = 0

    is_handone_moving_x_direction = 0
    is_handone_moving_y_direction = 0

    is_handtwo_moving_x_direction = 0
    is_handtwo_moving_y_direction = 0

    handone_movements_in_positive_x_direction  = 0
    handone_movements_in_negative_x_direction  = 0
    handone_movements_in_positive_y_direction  = 0
    handone_movements_in_negative_y_direction  = 0

    handtwo_movements_in_positive_x_direction  = 0
    handtwo_movements_in_negative_x_direction  = 0
    handtwo_movements_in_positive_y_direction  = 0
    handtwo_movements_in_negative_y_direction  = 0

    for i in range((len(HandOneLandMarksDict)-frame_difference)//frame_difference):
        if HandOneLandMarksCount > 0:
            HandOneLandMarksDiffDict[HandOneLandMarksDiffCount] = HandOneLandMarksDict[HandOneLandMarksCount] - HandOneLandMarksDict[HandOneLandMarksCount-frame_difference]    
            HandOneLandMarksCount += frame_difference
            HandOneLandMarksDiffCount +=1

    for i in range((len(HandTwoLandMarksDict)-frame_difference)//frame_difference):
        if HandTwoLandMarksCount > 0:
            HandTwoLandMarksDiffDict[HandTwoLandMarksDiffCount] = HandTwoLandMarksDict[HandTwoLandMarksCount] - HandTwoLandMarksDict[HandTwoLandMarksCount-frame_difference]    
            HandTwoLandMarksCount += frame_difference
            HandTwoLandMarksDiffCount +=1

    for i in range(len(HandOneLandMarksDiffDict)):
        if is_hand_stand_still(HandOneLandMarksDiffDict[i],10): 
            pass
        else:
            is_handone_moving_x_direction = hand_movement_in_direction(True,"x",HandOneLandMarksDiffDict[i],10,(500,550))
            if is_handone_moving_x_direction == 1:
                handone_movements_in_positive_x_direction +=1 
            elif is_handone_moving_x_direction == -1:
                handone_movements_in_negative_x_direction -=1 

            is_handone_moving_y_direction = hand_movement_in_direction(True,"y",HandOneLandMarksDiffDict[i],10,(500,550))
            if is_handone_moving_y_direction == 1:
                handone_movements_in_positive_y_direction +=1 
            elif is_handone_moving_y_direction == -1:
                handone_movements_in_negative_y_direction -=1 


    for i in range(len(HandTwoLandMarksDiffDict)):
        if is_hand_stand_still(HandTwoLandMarksDiffDict[i],10): 
            pass
        else:
            is_handtwo_moving_x_direction = hand_movement_in_direction(True,"x",HandTwoLandMarksDiffDict[i],10,(500,550))
            if is_handtwo_moving_x_direction == 1:
                handtwo_movements_in_positive_x_direction +=1 
            elif is_handtwo_moving_x_direction == -1:
                handtwo_movements_in_negative_x_direction -=1 

            is_handtwo_moving_y_direction = hand_movement_in_direction(True,"y",HandTwoLandMarksDiffDict[i],10,(500,550))
            if is_handtwo_moving_y_direction == 1:
                handtwo_movements_in_positive_y_direction +=1 
            elif is_handtwo_moving_y_direction == -1:
                handtwo_movements_in_negative_y_direction -=1 


            if handone_movements_in_positive_x_direction > 1 and handone_movements_in_negative_x_direction < -1 and\
               handone_movements_in_positive_y_direction > 1 and handone_movements_in_negative_y_direction < -1 and\
               handtwo_movements_in_positive_x_direction > 1 and handtwo_movements_in_negative_x_direction < -1 and\
               handtwo_movements_in_positive_y_direction > 1 and handtwo_movements_in_negative_y_direction < -1:
                is_symbol_found = True
                action_word_symbol = "Book"
                break        

    return action_word_symbol

def populate_car(HandOneLandMarksDict,HandTwoLandMarksDict,frame_difference):
    action_word_symbol = ""
    is_symbol_found = False

    HandOneLandMarksCount     = frame_difference
    HandOneLandMarksDiffDict  = {}
    HandOneLandMarksDiffCount = 0

    HandTwoLandMarksCount     = frame_difference
    HandTwoLandMarksDiffDict  = {}
    HandTwoLandMarksDiffCount = 0

    is_handone_moving_x_direction = 0
    is_handone_moving_y_direction = 0

    is_handtwo_moving_x_direction = 0
    is_handtwo_moving_y_direction = 0

    handone_movements_in_positive_x_direction  = 0
    handone_movements_in_negative_x_direction  = 0
    handone_movements_in_positive_y_direction  = 0
    handone_movements_in_negative_y_direction  = 0

    handtwo_movements_in_positive_x_direction  = 0
    handtwo_movements_in_negative_x_direction  = 0
    handtwo_movements_in_positive_y_direction  = 0
    handtwo_movements_in_negative_y_direction  = 0

    for i in range((len(HandOneLandMarksDict)-frame_difference)//frame_difference):
        if HandOneLandMarksCount > 0:
            HandOneLandMarksDiffDict[HandOneLandMarksDiffCount] = HandOneLandMarksDict[HandOneLandMarksCount] - HandOneLandMarksDict[HandOneLandMarksCount-frame_difference]    
            HandOneLandMarksCount += frame_difference
            HandOneLandMarksDiffCount +=1

    for i in range((len(HandTwoLandMarksDict)-frame_difference)//frame_difference):
        if HandTwoLandMarksCount > 0:
            HandTwoLandMarksDiffDict[HandTwoLandMarksDiffCount] = HandTwoLandMarksDict[HandTwoLandMarksCount] - HandTwoLandMarksDict[HandTwoLandMarksCount-frame_difference]    
            HandTwoLandMarksCount += frame_difference
            HandTwoLandMarksDiffCount +=1

    for i in range(len(HandOneLandMarksDiffDict)):
        if is_hand_stand_still(HandOneLandMarksDiffDict[i],10): 
            pass
        else:
            is_handone_moving_x_direction = hand_movement_in_direction(True,"x",HandOneLandMarksDiffDict[i],10,(500,550))
            if is_handone_moving_x_direction == 1:
                handone_movements_in_positive_x_direction +=1 
            elif is_handone_moving_x_direction == -1:
                handone_movements_in_negative_x_direction -=1 

            is_handone_moving_y_direction = hand_movement_in_direction(True,"y",HandOneLandMarksDiffDict[i],10,(500,550))
            if is_handone_moving_y_direction == 1:
                handone_movements_in_positive_y_direction +=1 
            elif is_handone_moving_y_direction == -1:
                handone_movements_in_negative_y_direction -=1 


    for i in range(len(HandTwoLandMarksDiffDict)):
        if is_hand_stand_still(HandTwoLandMarksDiffDict[i],10): 
            pass
        else:
            is_handtwo_moving_x_direction = hand_movement_in_direction(True,"x",HandTwoLandMarksDiffDict[i],10,(500,550))
            if is_handtwo_moving_x_direction == 1:
                handtwo_movements_in_positive_x_direction +=1 
            elif is_handtwo_moving_x_direction == -1:
                handtwo_movements_in_negative_x_direction -=1 

            is_handtwo_moving_y_direction = hand_movement_in_direction(True,"y",HandTwoLandMarksDiffDict[i],10,(500,550))
            if is_handtwo_moving_y_direction == 1:
                handtwo_movements_in_positive_y_direction +=1 
            elif is_handtwo_moving_y_direction == -1:
                handtwo_movements_in_negative_y_direction -=1 


            if handone_movements_in_positive_x_direction > 1 and handone_movements_in_negative_x_direction < -1 and\
               handone_movements_in_positive_y_direction > 1 and handone_movements_in_negative_y_direction < -1 and\
               handtwo_movements_in_positive_x_direction > 1 and handtwo_movements_in_negative_x_direction < -1 and\
               handtwo_movements_in_positive_y_direction > 1 and handtwo_movements_in_negative_y_direction < -1:
                is_symbol_found = True
                action_word_symbol = "Car"
                break        

    return action_word_symbol


def populate_alright(HandOneLandMarksDict,HandTwoLandMarksDict,frame_difference):
    return "Aright"

def populate_quiet(HandOneLandMarksDict,HandTwoLandMarksDict,frame_difference):
    action_word_symbol = ""
    HandOneLandMarksCount     = frame_difference
    HandOneLandMarksDiffCount = 0
    movements_in_x_direction = 0
    movements_in_y_direction = 0
    movements_in_z_direction = 0
    for i in range((len(HandOneLandMarksDict)-frame_difference)//frame_difference):
        if HandOneLandMarksCount > 0:
            HandOneLandMarksDiffDict[HandOneLandMarksDiffCount] = HandOneLandMarksDict[HandOneLandMarksCount] - HandOneLandMarksDict[HandOneLandMarksCount-frame_difference]    
            HandOneLandMarksCount += frame_difference
            HandOneLandMarksDiffCount +=1

    for i in range(len(HandOneLandMarksDiffDict)):
        if is_hand_stand_still(HandOneLandMarksDiffDict[i],2): 
            pass
        else:
            is_handone_moving_x_direction = hand_movement_in_direction(True,"x",HandOneLandMarksDiffDict[i],10,(500,550))
            if is_handone_moving_x_direction == 1:
                movements_in_x_direction +=1 
                if movements_in_x_direction >5:
                    break

    for i in range(len(HandOneLandMarksDiffDict)):
        if is_hand_stand_still(HandOneLandMarksDiffDict[i],2): 
            pass
        else:
            is_handone_moving_y_direction = hand_movement_in_direction(True,"y",HandOneLandMarksDiffDict[i],10,(500,550))
            if is_handone_moving_y_direction == 1:
                movements_in_y_direction +=1 
                if movements_in_y_direction >1:
                    action_words_display = 'Quiet'
                    break

    return action_words_display

def populate_loud(HandOneLandMarksDict,HandTwoLandMarksDict,frame_difference):
    action_word_symbol = ""
    HandOneLandMarksCount     = frame_difference
    HandOneLandMarksDiffCount = 0
    movements_in_x_direction = 0
    movements_in_y_direction = 0
    movements_in_z_direction = 0
    for i in range((len(HandOneLandMarksDict)-frame_difference)//frame_difference):
        if HandOneLandMarksCount > 0:
            HandOneLandMarksDiffDict[HandOneLandMarksDiffCount] = HandOneLandMarksDict[HandOneLandMarksCount] - HandOneLandMarksDict[HandOneLandMarksCount-frame_difference]    
            HandOneLandMarksCount += frame_difference
            HandOneLandMarksDiffCount +=1

    for i in range(len(HandOneLandMarksDiffDict)):
        if is_hand_stand_still(HandOneLandMarksDiffDict[i],10): 
            pass
        else:
            is_handone_moving_x_direction = hand_movement_in_direction(True,"x",HandOneLandMarksDiffDict[i],10,(500,550))
            if is_handone_moving_x_direction == 1:
                movements_in_x_direction +=1 
                if movements_in_x_direction >5:
                    #is_symbol_found = True
                    #action_word_symbol = "loud"
                    break

    for i in range(len(HandTwoLandMarksDiffDict)):
        if is_hand_stand_still(HandTwoLandMarksDiffDict[i],10): 
            pass
        else:
            is_handone_moving_x_direction = hand_movement_in_direction(False,"x",HandTwoLandMarksDiffDict[i],10,(500,550))
            if is_handone_moving_x_direction == -1:
                movements_in_x_direction -=1 
                if movements_in_x_direction <5:
                    #is_symbol_found = True
                    #action_word_symbol = "loud"
                    break

    for i in range(len(HandOneLandMarksDiffDict)):
        if is_hand_stand_still(HandOneLandMarksDiffDict[i],10): 
            pass
        else:
            is_handone_moving_y_direction = hand_movement_in_direction(True,"y",HandOneLandMarksDiffDict[i],10,(500,550))
            if is_handone_moving_y_direction == -1:
                movements_in_y_direction -=1 
                if movements_in_y_direction <5:
                    #is_symbol_found = True
                    #action_word_symbol = "loud"
                    break

    for i in range(len(HandTwoLandMarksDiffDict)):
        if is_hand_stand_still(HandTwoLandMarksDiffDict[i],10): 
            pass
        else:
            is_handone_moving_y_direction = hand_movement_in_direction(False,"y",HandTwoLandMarksDiffDict[i],10,(500,550))
            if is_handone_moving_y_direction == -1:
                movements_in_y_direction -=1 
                if movements_in_y_direction <5:
                    #is_symbol_found = True
                    #action_word_symbol = "loud"
                    break

    for i in range(len(HandOneLandMarksDiffDict)):
        if is_hand_stand_still(HandOneLandMarksDiffDict[i],10): 
            pass
        else:
            is_handone_moving_z_direction = hand_movement_in_direction(True,"z",HandOneLandMarksDiffDict[i],10,(500,550))
            if is_handone_moving_z_direction == -1:
                movements_in_z_direction -=1 
                if movements_in_z_direction <5:
                    #is_symbol_found = True
                    #action_word_symbol = "loud"
                    break

    for i in range(len(HandTwoLandMarksDiffDict)):
        if is_hand_stand_still(HandTwoLandMarksDiffDict[i],10): 
            pass
        else:
            is_handone_moving_z_direction = hand_movement_in_direction(False,"z",HandTwoLandMarksDiffDict[i],10,(500,550))
            if is_handone_moving_z_direction == -1:
                movements_in_z_direction -=1 
                if movements_in_z_direction <5:
                    is_symbol_found = True
                    action_word_symbol = "loud"
                    break

    return action_word_symbol

def populate_week(HandOneLandMarksDict,frame_difference):
    action_word_symbol = ""
    HandOneLandMarksCount     = frame_difference
    HandOneLandMarksDiffDict  = {}
    HandOneLandMarksDiffCount = 0
    movements_in_x_direction  = 0
    is_symbol_found = False
    for i in range((len(HandOneLandMarksDict)-frame_difference)//frame_difference):
        if HandOneLandMarksCount > 0:
            HandOneLandMarksDiffDict[HandOneLandMarksDiffCount] = HandOneLandMarksDict[HandOneLandMarksCount] - HandOneLandMarksDict[HandOneLandMarksCount-frame_difference]    
            HandOneLandMarksCount += frame_difference
            HandOneLandMarksDiffCount +=1

    for i in range(len(HandOneLandMarksDiffDict)):
        if is_hand_stand_still(HandOneLandMarksDiffDict[i],10): 
            pass
        else:
            is_handone_moving_x_direction = hand_movement_in_direction(True,"x",HandOneLandMarksDiffDict[i],10,(500,550))
            if is_handone_moving_x_direction == True:
                movements_in_x_direction +=1 
                if movements_in_x_direction >5:
                    is_symbol_found = True
                    action_word_symbol = "Week"
                    break

    return action_word_symbol



def populate_like(HandOneLandMarksDict,frame_difference):
    action_word_symbol = ""
    HandOneLandMarksCount     = frame_difference
    HandOneLandMarksDiffDict  = {}
    HandOneLandMarksDiffCount = 0
    movements_in_x_direction  = 0
    movements_in_positive_z_direction  = 0
    movements_in_negative_z_direction  = 0
    is_symbol_found = False
    for i in range((len(HandOneLandMarksDict)-frame_difference)//frame_difference):
        if HandOneLandMarksCount > 0:
            HandOneLandMarksDiffDict[HandOneLandMarksDiffCount] = HandOneLandMarksDict[HandOneLandMarksCount] - HandOneLandMarksDict[HandOneLandMarksCount-frame_difference]    
            HandOneLandMarksCount += frame_difference
            HandOneLandMarksDiffCount +=1

    for i in range(len(HandOneLandMarksDiffDict)):
        if is_hand_stand_still(HandOneLandMarksDiffDict[i],10): 
            pass
        else:
            is_handone_moving_z_direction = hand_movement_in_direction(True,"z",HandOneLandMarksDiffDict[i],10,(500,550))
            if is_handone_moving_z_direction == 1:
                movements_in_positive_z_direction +=1 
            elif is_handone_moving_z_direction == -1:
                movements_in_negative_z_direction -=1 

            is_handone_moving_x_direction = hand_movement_in_direction(True,"x",HandOneLandMarksDiffDict[i],10,(500,550))
            if is_handone_moving_x_direction == 0:
                movements_in_x_direction = 0 
            else:
                movements_in_x_direction  +=1 

            if movements_in_positive_z_direction >2 and movements_in_negative_z_direction < -2 and movements_in_x_direction < 10:
                #print("movements_in_positive_z_direction = " + str(movements_in_positive_z_direction) + " movements_in_negative_z_direction = " + str(movements_in_negative_z_direction) + " movements_in_x_direction= " + str(movements_in_x_direction))
                is_symbol_found = True
                action_word_symbol = "Like"
                movements_in_positive_z_direction = 0
                movements_in_negative_z_direction = 0
                movements_in_x_direction = 0
                break

    return action_word_symbol

def populate_have(HandOneLandMarksDict,HandTwoLandMarksDict,frame_difference):
    action_word_symbol = ""
    HandOneLandMarksCount     = frame_difference
    HandOneLandMarksDiffDict  = {}
    HandOneLandMarksDiffCount = 0
    movements_in_positive_y_direction  = 0
    movements_in_negative_y_direction  = 0
    is_symbol_found = False
    for i in range((len(HandOneLandMarksDict)-frame_difference)//frame_difference):
        if HandOneLandMarksCount > 0:
            HandOneLandMarksDiffDict[HandOneLandMarksDiffCount] = HandOneLandMarksDict[HandOneLandMarksCount] - HandOneLandMarksDict[HandOneLandMarksCount-frame_difference]    
            HandOneLandMarksCount += frame_difference
            HandOneLandMarksDiffCount +=1

    for i in range(len(HandOneLandMarksDiffDict)):
        if is_hand_stand_still(HandOneLandMarksDiffDict[i],10): 
            pass
        else:
            is_handone_moving_y_direction = hand_movement_in_direction(True,"y",HandOneLandMarksDiffDict[i],10,(500,550))
            if is_handone_moving_y_direction == 1:
                movements_in_positive_y_direction +=1 
            elif is_handone_moving_y_direction == -1:
                movements_in_negative_y_direction -=1 

            if movements_in_positive_y_direction >1 and movements_in_negative_y_direction < -1:
                is_symbol_found = True
                action_word_symbol = "Have"
                break

    return action_word_symbol

def populate_why(HandOneLandMarksDict,frame_difference):
    action_word_symbol = ""
    HandOneLandMarksCount     = frame_difference
    HandOneLandMarksDiffDict  = {}
    HandOneLandMarksDiffCount = 0
    movements_in_y_direction  = 0
    is_symbol_found = False
    for i in range(len(HandOneLandMarksDict)//frame_difference):
        if HandOneLandMarksCount > 0:
            HandOneLandMarksDiffDict[HandOneLandMarksDiffCount] = HandOneLandMarksDict[HandOneLandMarksCount] - HandOneLandMarksDict[HandOneLandMarksCount-frame_difference]    
            HandOneLandMarksCount += frame_difference
            HandOneLandMarksDiffCount +=1

    for i in range(len(HandOneLandMarksDiffDict)):
        if is_hand_stand_still(HandOneLandMarksDiffDict[i],10): 
            pass
        else:
            is_handone_moving_y_direction = hand_movement_in_direction(True,"y",HandOneLandMarksDiffDict[i],10,(500,550))
            if is_handone_moving_y_direction == True:
                movements_in_y_direction +=1 
                if movements_in_y_direction >5:
                    is_symbol_found = True
                    action_word_symbol = "Why"
                    break

    return action_word_symbol

def populate_your(HandOneLandMarksDict,frame_difference):
    action_word_symbol = ""
    HandOneLandMarksCount     = frame_difference
    HandOneLandMarksDiffDict  = {}
    HandOneLandMarksDiffCount = 0
    movements_in_z_direction  = 0
    is_symbol_found = False
    for i in range(len(HandOneLandMarksDict)//frame_difference):
        if HandOneLandMarksCount > 0:
            HandOneLandMarksDiffDict[HandOneLandMarksDiffCount] = HandOneLandMarksDict[HandOneLandMarksCount] - HandOneLandMarksDict[HandOneLandMarksCount-frame_difference]    
            HandOneLandMarksCount += frame_difference
            HandOneLandMarksDiffCount +=1

    for i in range(len(HandOneLandMarksDiffDict)):
        if is_hand_stand_still(HandOneLandMarksDiffDict[i],10): 
            pass
        else:
            is_handone_moving_z_direction = hand_movement_in_direction(True,"z",HandOneLandMarksDiffDict[i],10,(500,550))
            if is_handone_moving_z_direction == True:
                movements_in_z_direction +=1 
                if movements_in_z_direction >0:
                    is_symbol_found = True
                    action_word_symbol = "Your"
                    break

    return action_word_symbol

def populate_what(HandOneLandMarksDict,HandTwoLandMarksDict,frame_difference):
    action_word_symbol = ""
    HandOneLandMarksCount     = frame_difference
    HandOneLandMarksDiffDict  = {}
    HandOneLandMarksDiffCount = 0
    is_handone_moving_x_direction = 0
    movements_in_positive_x_direction = 0
    movements_in_negative_x_direction = 0
    movements_in_x_direction = 0
    is_symbol_found = False

    for i in range((len(HandOneLandMarksDict)-frame_difference)//frame_difference):
        if HandOneLandMarksCount > 0:
            HandOneLandMarksDiffDict[HandOneLandMarksDiffCount] = HandOneLandMarksDict[HandOneLandMarksCount] - HandOneLandMarksDict[HandOneLandMarksCount-frame_difference]    
            HandOneLandMarksCount += frame_difference
            HandOneLandMarksDiffCount +=1

    for i in range(len(HandOneLandMarksDiffDict)):
        if is_hand_stand_still(HandOneLandMarksDiffDict[i],10): 
            pass
        else:
            is_handone_moving_x_direction = hand_movement_in_direction(True,"x",HandOneLandMarksDiffDict[i],10,(500,550))
            if is_handone_moving_x_direction == 1:
                movements_in_positive_x_direction +=1 
            elif is_handone_moving_x_direction == -1:
                movements_in_negative_x_direction -=1 

            if movements_in_positive_x_direction > 2 and movements_in_negative_x_direction < -2:
                is_symbol_found = True
                action_word_symbol = "What"
                movements_in_positive_x_direction = 0
                movements_in_negative_x_direction = 0
                movements_in_x_direction = 0
                break


    return action_word_symbol

def get_single_hand_action_word(screen):
    global is_log_active
    HandMarksCount = 0
    action_word_symbol = ''
    HandOneLandMarksDict = {}
    Hand_1_LandMarks = []
    Hand_2_LandMarks = []
    hand_1 = hi.hand_info()
    hand_2 = hi.hand_info()
    hand_data = None
    hand_1_data = None
    hand_2_data = None

    hand_detector = mi.HandTrackingModule.handDetector()

    while True:
        success, action_word_video = screen.read()
        action_word_video = mi.vision.flip(action_word_video,1)
        action_word_video = hand_detector.findHands(action_word_video)
        HandLandMarks = hand_detector.findPosition(action_word_video, 0, draw=False)

        if mi.cvs.config_data['log_hand_landmarks_to_file'] == "True":
            if mi.cvs.config_data['take_sample_data'] == "False" and is_log_active == True:
                if len(hand_1.HandLandMarks) != 0:
                    mi.cvs.log.write_hand_landmarks(hand_1,"hand_1")
                if len(hand_2.HandLandMarks) != 0:
                    mi.cvs.log.write_hand_landmarks(hand_2,"hand_2")

        if len(HandLandMarks) == 0:
           break

        if action_word_symbol == "":
            hand_1_data = hand_1.get_hand_information(HandLandMarks,True) 
            action_word_symbol = wds.get_single_hand_word(hand_1_data) 

        if action_word_symbol == "":
            if hand_1_data['is_hand_1']               == True  and \
               hand_1_data['is_right_hand']           == True  and \
               hand_1_data['hand_orientation']        == 90    and \
               hand_1_data['is_thumb_opened']         == False and \
               hand_1_data['is_index_finger_opened']  == False and \
               hand_1_data['is_middle_finger_opened'] == True  and \
               hand_1_data['is_ring_finger_opened']   == True  and \
               hand_1_data['is_little_finger_opened'] == True :
                action_word_symbol =  "Week_starting"
            elif hand_1_data['is_hand_1']               == True  and \
                 hand_1_data['is_right_hand']           == False and \
                 hand_1_data['hand_orientation']        == 90    and \
                 hand_1_data['is_thumb_opened']         == False and \
                 hand_1_data['is_index_finger_opened']  == False and \
                 hand_1_data['is_middle_finger_opened'] == False and \
                 hand_1_data['is_ring_finger_opened']   == False and \
                 hand_1_data['is_little_finger_opened'] == False :
                  action_word_symbol =  "your_starting"
            elif hand_1_data['is_hand_1']               == True  and \
                 hand_1_data['is_right_hand']           == False and \
                 hand_1_data['hand_orientation']        == 90    and \
                 hand_1_data['is_thumb_opened']         == True  and \
                 hand_1_data['is_index_finger_opened']  == True  and \
                 hand_1_data['is_middle_finger_opened'] == True  and \
                 hand_1_data['is_ring_finger_opened']   == True  and \
                 hand_1_data['is_little_finger_opened'] == True  :
                  action_word_symbol =  "" #"why_starting"
            else:
                action_word_symbol =  ""

        else:
            if mi.cvs.config_data['take_sample_data'] == "False":
                HandOneLandMarksDict[HandMarksCount] = np.array(hand_detector.findPosition(action_word_video, 0, draw=False))
                HandMarksCount +=1
            else:
                HandOneLandMarksDict =  []

            if HandMarksCount >32:
                if action_word_symbol ==  "Week_starting":
                    action_word_symbol = populate_week(HandOneLandMarksDict,2)
                    if action_word_symbol == "":
                        action_word_symbol = populate_like(HandOneLandMarksDict,2)
                elif action_word_symbol ==  "your_starting":
                    action_word_symbol = populate_your(HandOneLandMarksDict,2)
                elif action_word_symbol ==  "why_starting":
                    action_word_symbol = populate_why(HandOneLandMarksDict,2)
                
                HandMarksCount = 0  
                

        mi.vision.putText(action_word_video, "Action Words", (800, 50), mi.vision.FONT_HERSHEY_COMPLEX,1, (255, 0, 0), 2)
        if action_word_symbol == "Week_starting":
            mi.vision.putText(action_word_video, action_word_symbol, (20, 200), mi.vision.FONT_HERSHEY_COMPLEX,1, (255, 0, 0), 1)
        else:
            mi.vision.putText(action_word_video, action_word_symbol, (20, 200), mi.vision.FONT_HERSHEY_COMPLEX,2, (255, 0, 0), 2)
        mi.vision.imshow("Image", action_word_video)
        mi.vision.waitKey(1)

    if mi.cvs.config_data['log_hand_landmarks_to_file'] == "True":
        if mi.cvs.config_data['take_sample_data'] == "False":
            #mi.cvs.log.open_log_file(mi.cvs.config_data['take_sample_data_for_symbol'])

            is_log_active = False
            mi.cvs.log.write_message("Log Ended","hand_1")
            mi.cvs.log.write_message("Log Ended","hand_2")

    

    return action_word_symbol

def get_two_hand_action_word(screen):
    global is_log_active
    action_word_symbol = ''
    HandMarksCount = 0
    hand_1 = hi.hand_info()
    hand_2 = hi.hand_info()
    hand_1_data = None
    hand_2_data = None

    HandOneMarksCount = 0
    HandOneLandMarks = []
    HandOneLandMarksDict = {}
    HandTwoMarksCount = 0
    HandTwoLandMarks = []
    HandTwoLandMarksDict = {}
    #screen = mi.vision.VideoCapture(0)
    hand_detector = mi.HandTrackingModule.handDetector()
    while True:
        success, action_word_video = screen.read()
        action_word_video = mi.vision.flip(action_word_video,1)
        action_word_video = hand_detector.findHands(action_word_video)
        if mi.cvs.config_data['take_sample_data'] == "False":
            HandOneLandMarks  = hand_detector.findPosition(action_word_video, 0, draw=False)
            HandTwoLandMarks  = hand_detector.findPosition(action_word_video, 1, draw=False)
        else:
            HandOneLandMarks  = hand_1_data['HandLandMarks']
            HandTwoLandMarks  = hand_2_data['HandLandMarks']

        if mi.cvs.config_data['log_hand_landmarks_to_file'] == "True":
            if mi.cvs.config_data['take_sample_data'] == "False" and is_log_active == True:
                if len(hand_1.HandLandMarks) != 0:
                    mi.cvs.log.write_hand_landmarks(hand_1,"hand_1")
                if len(hand_2.HandLandMarks) != 0:
                    mi.cvs.log.write_hand_landmarks(hand_2,"hand_2")

        mi.vision.putText(action_word_video, "Action Words", (800, 50), mi.vision.FONT_HERSHEY_COMPLEX,1, (255, 0, 0), 2)
        mi.vision.imshow("Image", action_word_video)
        mi.vision.waitKey(1)

        if len(HandOneLandMarks) == 0 and len(HandTwoLandMarks) == 0:
           break

        action_word_pattern_mached = False
        action_word_symbol = ""
        previous_action_word_symbol = ""

        if action_word_symbol == "":
            hand_1_data = hand_1.get_hand_information(HandOneLandMarks,True) 
            hand_2_data = hand_2.get_hand_information(HandTwoLandMarks,False) 

            if  (mi.cvs.config_data['include_action_words']['day_starting']=='i') and \
                    ( \
                    ( \
                    hand_1_data['is_hand_1']               == True  and \
                    hand_1_data['is_right_hand']           == True  and \
                    hand_1_data['hand_orientation']        == 180   and \
                    hand_1_data['is_thumb_opened']         == False and \
                    hand_1_data['is_index_finger_opened']  == True  and \
                    hand_1_data['is_middle_finger_opened'] == True  and \
                    hand_1_data['is_ring_finger_opened']   == True  and \
                    hand_1_data['is_little_finger_opened'] == True  and \
                    hand_2_data['is_hand_1']               == False and \
                    hand_2_data['is_right_hand']           == True  and \
                    hand_2_data['hand_orientation']        == 0     and \
                    hand_2_data['is_thumb_opened']         == False and \
                    hand_2_data['is_index_finger_opened']  == True  and \
                    hand_2_data['is_middle_finger_opened'] == True  and \
                    hand_2_data['is_ring_finger_opened']   == True  and \
                    hand_2_data['is_little_finger_opened'] == True     \
                    ) \
                    or \
                    ( \
                    hand_2_data['is_hand_1']               == False and \
                    hand_2_data['is_right_hand']           == True  and \
                    hand_2_data['hand_orientation']        == 180   and \
                    hand_2_data['is_thumb_opened']         == False and \
                    hand_2_data['is_index_finger_opened']  == True  and \
                    hand_2_data['is_middle_finger_opened'] == True  and \
                    hand_2_data['is_ring_finger_opened']   == True  and \
                    hand_2_data['is_little_finger_opened'] == True  and \
                    hand_1_data['is_hand_1']               == True  and \
                    hand_1_data['is_right_hand']           == True  and \
                    hand_1_data['hand_orientation']        == 0     and \
                    hand_1_data['is_thumb_opened']         == False and \
                    hand_1_data['is_index_finger_opened']  == True  and \
                    hand_1_data['is_middle_finger_opened'] == True  and \
                    hand_1_data['is_ring_finger_opened']   == True  and \
                    hand_1_data['is_little_finger_opened'] == True     \
                    ) \
                    ):
                action_word_symbol =  "Day_starting"
            elif HandOneLandMarks[4][2]     < HandOneLandMarks[3][2]  \
                and HandOneLandMarks[4][2]  < HandOneLandMarks[2][2]  \
                and HandOneLandMarks[5][2]  < HandOneLandMarks[9][2]  \
                and HandOneLandMarks[5][2]  < HandOneLandMarks[13][2] \
                and HandOneLandMarks[5][2]  < HandOneLandMarks[17][2] \
                and HandOneLandMarks[9][2]  < HandOneLandMarks[13][2] \
                and HandOneLandMarks[9][2]  < HandOneLandMarks[17][2] \
                and HandOneLandMarks[13][2] < HandOneLandMarks[17][2] \
                and HandOneLandMarks[5][1]  > HandOneLandMarks[6][1]  \
                and HandOneLandMarks[9][1]  > HandOneLandMarks[10][1] \
                and HandOneLandMarks[13][1] > HandOneLandMarks[14][1] \
                and HandOneLandMarks[17][1] > HandOneLandMarks[18][1] \
                and len(HandTwoLandMarks)==0 :
                action_word_symbol =  "Okay"
            elif HandOneLandMarks[4][2]     > HandOneLandMarks[3][2]  \
                and HandOneLandMarks[4][2]  > HandOneLandMarks[2][2]  \
                and HandOneLandMarks[5][2]  > HandOneLandMarks[9][2]  \
                and HandOneLandMarks[5][2]  > HandOneLandMarks[13][2] \
                and HandOneLandMarks[5][2]  > HandOneLandMarks[17][2] \
                and HandOneLandMarks[9][2]  > HandOneLandMarks[13][2] \
                and HandOneLandMarks[9][2]  > HandOneLandMarks[17][2] \
                and HandOneLandMarks[13][2] > HandOneLandMarks[17][2] \
                and HandOneLandMarks[5][1]  > HandOneLandMarks[6][1]  \
                and HandOneLandMarks[9][1]  > HandOneLandMarks[10][1] \
                and HandOneLandMarks[13][1] > HandOneLandMarks[14][1] \
                and HandOneLandMarks[17][1] > HandOneLandMarks[18][1] \
                and len(HandTwoLandMarks)==0 :
                action_word_symbol =  "Not Okay"
            elif HandOneLandMarks[4][2]     < HandOneLandMarks[3][2]  \
                and HandOneLandMarks[4][2]  < HandOneLandMarks[2][2]  \
                and HandOneLandMarks[5][2]  < HandOneLandMarks[9][2]  \
                and HandOneLandMarks[5][2]  < HandOneLandMarks[13][2] \
                and HandOneLandMarks[5][2]  < HandOneLandMarks[17][2] \
                and HandOneLandMarks[9][2]  < HandOneLandMarks[13][2] \
                and HandOneLandMarks[9][2]  < HandOneLandMarks[17][2] \
                and HandOneLandMarks[13][2] < HandOneLandMarks[17][2] \
                and HandOneLandMarks[5][1]  > HandOneLandMarks[6][1]  \
                and HandOneLandMarks[9][1]  > HandOneLandMarks[10][1] \
                and HandOneLandMarks[13][1] > HandOneLandMarks[14][1] \
                and HandOneLandMarks[17][1] > HandOneLandMarks[18][1] \
                and HandTwoLandMarks[4][2]  < HandTwoLandMarks[3][2]  \
                and HandTwoLandMarks[4][2]  < HandTwoLandMarks[2][2]  \
                and HandTwoLandMarks[5][2]  < HandTwoLandMarks[9][2]  \
                and HandTwoLandMarks[5][2]  < HandTwoLandMarks[13][2] \
                and HandTwoLandMarks[5][2]  < HandTwoLandMarks[17][2] \
                and HandTwoLandMarks[9][2]  < HandTwoLandMarks[13][2] \
                and HandTwoLandMarks[9][2]  < HandTwoLandMarks[17][2] \
                and HandTwoLandMarks[13][2] < HandTwoLandMarks[17][2] \
                and HandTwoLandMarks[5][1]  < HandTwoLandMarks[6][1]  \
                and HandTwoLandMarks[9][1]  < HandTwoLandMarks[10][1] \
                and HandTwoLandMarks[13][1] < HandTwoLandMarks[14][1] \
                and HandTwoLandMarks[17][1] < HandTwoLandMarks[18][1]:
                action_word_symbol =  "Alright"
            elif (( \
                hand_1_data['is_hand_1']               == True  and \
                hand_1_data['is_right_hand']           == True  and \
                #hand_1_data['hand_orientation']        == 0     and \
                hand_1_data['is_thumb_opened']         == False and \
                hand_1_data['is_index_finger_opened']  == True  and \
                hand_1_data['is_middle_finger_opened'] == False and \
                hand_1_data['is_ring_finger_opened']   == False and \
                hand_1_data['is_little_finger_opened'] == False and \
                hand_2_data['is_hand_1']               == False and \
                hand_2_data['is_right_hand']           == False and \
                #hand_2_data['hand_orientation']        == 180   and \
                hand_2_data['is_thumb_opened']         == False and \
                hand_2_data['is_index_finger_opened']  == False and \
                hand_2_data['is_middle_finger_opened'] == False and \
                hand_2_data['is_ring_finger_opened']   == False and \
                hand_2_data['is_little_finger_opened'] == False     \
               ) \
               or \
               ( \
                hand_2_data['is_hand_1']               == False and \
                hand_2_data['is_right_hand']           == True  and \
                #hand_2_data['hand_orientation']        == 0     and \
                hand_2_data['is_thumb_opened']         == False and \
                hand_2_data['is_index_finger_opened']  == True  and \
                hand_2_data['is_middle_finger_opened'] == False and \
                hand_2_data['is_ring_finger_opened']   == False and \
                hand_2_data['is_little_finger_opened'] == False and \
                hand_1_data['is_hand_1']               == True  and \
                hand_1_data['is_right_hand']           == False and \
                #hand_1_data['hand_orientation']        == 180   and \
                hand_1_data['is_thumb_opened']         == False and \
                hand_1_data['is_index_finger_opened']  == False and \
                hand_1_data['is_middle_finger_opened'] == False and \
                hand_1_data['is_ring_finger_opened']   == False and \
                hand_1_data['is_little_finger_opened'] == False     \
               ) \
               ):
                action_word_symbol =  "Time"
            elif  (mi.cvs.config_data['include_action_words']['what_starting']=='i') and \
                    ( \
                    ( \
                    hand_1_data['is_hand_1']               == True  and \
                    #hand_1_data['is_right_hand']           == True  and \
                    #hand_1_data['hand_orientation']        != 90    and \
                    hand_1_data['is_thumb_opened']         == True  and \
                    hand_1_data['is_index_finger_opened']  == True  and \
                    hand_1_data['is_middle_finger_opened'] == True  and \
                    hand_1_data['is_ring_finger_opened']   == True  and \
                    hand_1_data['is_little_finger_opened'] == True \
                    ) and \
                    hand_1_data['HandLandMarks'][4][2] > hand_1_data['HandLandMarks'][16][2] and \
                    hand_1_data['HandLandMarks'][4][2] > hand_1_data['HandLandMarks'][20][2] and \
                    hand_1_data['HandLandMarks'][8][2] > hand_1_data['HandLandMarks'][16][2] and \
                    hand_1_data['HandLandMarks'][8][2] > hand_1_data['HandLandMarks'][20][2] and \
                    hand_1_data['HandLandMarks'][12][2] > hand_1_data['HandLandMarks'][16][2] and \
                    hand_1_data['HandLandMarks'][12][2] > hand_1_data['HandLandMarks'][20][2] 
                    ):
                action_word_symbol =  "what_starting"
                if mi.cvs.config_data['take_sample_data'] == "False":
                    HandOneLandMarksDict[HandMarksCount] = np.array(hand_detector.findPosition(action_word_video, 0, draw=False))
                    HandTwoLandMarksDict[HandMarksCount] = np.array(hand_detector.findPosition(action_word_video, 1, draw=False))
                    HandMarksCount +=1
                else:
                    HandOneLandMarksDict[0]=np.array([[0, 737, 504, 0], [1, 705, 479, -32], [2, 692, 444, -46], [3, 691, 414, -59], [4, 692, 389, -72], [5, 720, 407, -5], [6, 719, 372, -36], [7, 718, 350, -66], [8, 719, 329, -88], [9, 740, 407, -12], [10, 740, 368, -37], [11, 740, 342, -64], [12, 740, 319, -84], [13, 759, 413, -27], [14, 761, 377, -53], [15, 761, 354, -70], [16, 761, 333, -82], [17, 777, 427, -46], [18, 783, 397, -69], [19, 785, 378, -78], [20, 786, 360, -83]])

                    HandTwoLandMarksDict[0]=np.array([[0, 478, 515, 0], [1, 507, 491, -37], [2, 520, 458, -55], [3, 526, 430, -72], [4, 532, 405, -90], [5, 494, 418, -28], [6, 494, 381, -63], [7, 492, 358, -93], [8, 490, 338, -114], [9, 474, 419, -35], [10, 473, 377, -63], [11, 472, 350, -89], [12, 471, 327, -109], [13, 455, 428, -48], [14, 452, 389, -75], [15, 452, 365, -95], [16, 454, 343, -109], [17, 436, 444, -65], [18, 428, 416, -92], [19, 428, 396, -102], [20, 430, 378, -109]])
                if HandMarksCount >10:
                    action_word_symbol =  populate_what(HandOneLandMarksDict,HandTwoLandMarksDict,2)
            elif  (mi.cvs.config_data['include_action_words']['book_starting']=='i') and \
                    ( \
                    ( \
                    hand_1_data['is_hand_1']               == True  and \
                    hand_1_data['is_right_hand']           == True  and \
                    hand_1_data['hand_orientation']        != 90    and \
                    hand_1_data['is_thumb_opened']         == True  and \
                    hand_1_data['is_index_finger_opened']  == True  and \
                    hand_1_data['is_middle_finger_opened'] == True  and \
                    hand_1_data['is_ring_finger_opened']   == True  and \
                    hand_1_data['is_little_finger_opened'] == True  and \
                    hand_2_data['is_hand_1']               == False and \
                    hand_2_data['is_right_hand']           == False and \
                    hand_2_data['hand_orientation']        != 90    and \
                    hand_2_data['is_thumb_opened']         == True  and \
                    hand_2_data['is_index_finger_opened']  == True  and \
                    hand_2_data['is_middle_finger_opened'] == True  and \
                    hand_2_data['is_ring_finger_opened']   == True  and \
                    hand_2_data['is_little_finger_opened'] == True     \
                    ) \
                    or \
                    ( \
                    hand_2_data['is_hand_1']               == False and \
                    hand_2_data['is_right_hand']           == True  and \
                    hand_2_data['hand_orientation']        != 90    and \
                    hand_2_data['is_thumb_opened']         == True  and \
                    hand_2_data['is_index_finger_opened']  == True  and \
                    hand_2_data['is_middle_finger_opened'] == True  and \
                    hand_2_data['is_ring_finger_opened']   == True  and \
                    hand_2_data['is_little_finger_opened'] == True  and \
                    hand_1_data['is_hand_1']               == True  and \
                    hand_1_data['is_right_hand']           == False and \
                    hand_1_data['hand_orientation']        != 90    and \
                    hand_1_data['is_thumb_opened']         == True  and \
                    hand_1_data['is_index_finger_opened']  == True  and \
                    hand_1_data['is_middle_finger_opened'] == True  and \
                    hand_1_data['is_ring_finger_opened']   == True  and \
                    hand_1_data['is_little_finger_opened'] == True     \
                    ) \
                    ):
                action_word_symbol =  "book"
                if mi.cvs.config_data['take_sample_data'] == "False":
                    HandOneLandMarksDict[HandMarksCount] = np.array(hand_detector.findPosition(action_word_video, 0, draw=False))
                    HandTwoLandMarksDict[HandMarksCount] = np.array(hand_detector.findPosition(action_word_video, 1, draw=False))
                    HandMarksCount +=1
                else:
                    HandOneLandMarksDict[0]=np.array([[0, 737, 504, 0], [1, 705, 479, -32], [2, 692, 444, -46], [3, 691, 414, -59], [4, 692, 389, -72], [5, 720, 407, -5], [6, 719, 372, -36], [7, 718, 350, -66], [8, 719, 329, -88], [9, 740, 407, -12], [10, 740, 368, -37], [11, 740, 342, -64], [12, 740, 319, -84], [13, 759, 413, -27], [14, 761, 377, -53], [15, 761, 354, -70], [16, 761, 333, -82], [17, 777, 427, -46], [18, 783, 397, -69], [19, 785, 378, -78], [20, 786, 360, -83]])

                    HandTwoLandMarksDict[0]=np.array([[0, 478, 515, 0], [1, 507, 491, -37], [2, 520, 458, -55], [3, 526, 430, -72], [4, 532, 405, -90], [5, 494, 418, -28], [6, 494, 381, -63], [7, 492, 358, -93], [8, 490, 338, -114], [9, 474, 419, -35], [10, 473, 377, -63], [11, 472, 350, -89], [12, 471, 327, -109], [13, 455, 428, -48], [14, 452, 389, -75], [15, 452, 365, -95], [16, 454, 343, -109], [17, 436, 444, -65], [18, 428, 416, -92], [19, 428, 396, -102], [20, 430, 378, -109]])

                if HandMarksCount >30:
                    action_word_symbol =  populate_book(HandOneLandMarksDict,HandTwoLandMarksDict,2)
            elif  (mi.cvs.config_data['include_action_words']['car_starting']=='i') and \
                    ( \
                    ( \
                    hand_1_data['is_hand_1']               == True  and \
                    hand_1_data['is_right_hand']           == True  and \
                    #hand_1_data['hand_orientation']        == 90    and \
                    hand_1_data['is_thumb_opened']         == False and \
                    hand_1_data['is_index_finger_opened']  == False and \
                    hand_1_data['is_middle_finger_opened'] == False and \
                    hand_1_data['is_ring_finger_opened']   == False and \
                    hand_1_data['is_little_finger_opened'] == False and \
                    hand_2_data['is_hand_1']               == False and \
                    hand_2_data['is_right_hand']           == False and \
                    #hand_2_data['hand_orientation']        == 90    and \
                    hand_2_data['is_thumb_opened']         == False and \
                    hand_2_data['is_index_finger_opened']  == False and \
                    hand_2_data['is_middle_finger_opened'] == False and \
                    hand_2_data['is_ring_finger_opened']   == False and \
                    hand_2_data['is_little_finger_opened'] == False    \
                    ) \
                    or \
                    ( \
                    hand_2_data['is_hand_1']               == False and \
                    hand_2_data['is_right_hand']           == True  and \
                    #hand_2_data['hand_orientation']        == 90    and \
                    hand_2_data['is_thumb_opened']         == False and \
                    hand_2_data['is_index_finger_opened']  == False and \
                    hand_2_data['is_middle_finger_opened'] == False and \
                    hand_2_data['is_ring_finger_opened']   == False and \
                    hand_2_data['is_little_finger_opened'] == False and \
                    hand_1_data['is_hand_1']               == True  and \
                    hand_1_data['is_right_hand']           == False and \
                    #hand_1_data['hand_orientation']        == 90    and \
                    hand_1_data['is_thumb_opened']         == False and \
                    hand_1_data['is_index_finger_opened']  == False and \
                    hand_1_data['is_middle_finger_opened'] == False and \
                    hand_1_data['is_ring_finger_opened']   == False and \
                    hand_1_data['is_little_finger_opened'] == False    \
                    ) \
                    ):
                action_word_symbol =  "car_starting"
                if mi.cvs.config_data['take_sample_data'] == "False":
                    HandOneLandMarksDict[HandMarksCount] = np.array(hand_detector.findPosition(action_word_video, 0, draw=False))
                    HandTwoLandMarksDict[HandMarksCount] = np.array(hand_detector.findPosition(action_word_video, 1, draw=False))
                    HandMarksCount +=1
                else:
                    HandOneLandMarksDict[0]=np.array([[0, 737, 504, 0], [1, 705, 479, -32], [2, 692, 444, -46], [3, 691, 414, -59], [4, 692, 389, -72], [5, 720, 407, -5], [6, 719, 372, -36], [7, 718, 350, -66], [8, 719, 329, -88], [9, 740, 407, -12], [10, 740, 368, -37], [11, 740, 342, -64], [12, 740, 319, -84], [13, 759, 413, -27], [14, 761, 377, -53], [15, 761, 354, -70], [16, 761, 333, -82], [17, 777, 427, -46], [18, 783, 397, -69], [19, 785, 378, -78], [20, 786, 360, -83]])

                    HandTwoLandMarksDict[0]=np.array([[0, 478, 515, 0], [1, 507, 491, -37], [2, 520, 458, -55], [3, 526, 430, -72], [4, 532, 405, -90], [5, 494, 418, -28], [6, 494, 381, -63], [7, 492, 358, -93], [8, 490, 338, -114], [9, 474, 419, -35], [10, 473, 377, -63], [11, 472, 350, -89], [12, 471, 327, -109], [13, 455, 428, -48], [14, 452, 389, -75], [15, 452, 365, -95], [16, 454, 343, -109], [17, 436, 444, -65], [18, 428, 416, -92], [19, 428, 396, -102], [20, 430, 378, -109]])
                if HandMarksCount >20:
                    action_word_symbol =  populate_car(HandOneLandMarksDict,HandTwoLandMarksDict,2)
            elif  (mi.cvs.config_data['include_action_words']['have_starting']=='i') and \
                    ( \
                    ( \
                    hand_1_data['is_hand_1']               == True  and \
                    hand_1_data['is_right_hand']           == True  and \
                    hand_1_data['hand_orientation']        == 90    and \
                    hand_1_data['is_thumb_opened']         == True  and \
                    hand_1_data['is_index_finger_opened']  == True  and \
                    hand_1_data['is_middle_finger_opened'] == True  and \
                    hand_1_data['is_ring_finger_opened']   == True  and \
                    hand_1_data['is_little_finger_opened'] == True  and \
                    hand_2_data['is_hand_1']               == False and \
                    hand_2_data['is_right_hand']           == True  and \
                    hand_2_data['hand_orientation']        == 90    and \
                    hand_2_data['is_thumb_opened']         == True  and \
                    hand_2_data['is_index_finger_opened']  == True  and \
                    hand_2_data['is_middle_finger_opened'] == True  and \
                    hand_2_data['is_ring_finger_opened']   == True  and \
                    hand_2_data['is_little_finger_opened'] == True     \
                    ) \
                    or \
                    ( \
                    hand_2_data['is_hand_1']               == False and \
                    hand_2_data['is_right_hand']           == True  and \
                    hand_2_data['hand_orientation']        == 90    and \
                    hand_2_data['is_thumb_opened']         == True  and \
                    hand_2_data['is_index_finger_opened']  == True  and \
                    hand_2_data['is_middle_finger_opened'] == True  and \
                    hand_2_data['is_ring_finger_opened']   == True  and \
                    hand_2_data['is_little_finger_opened'] == True  and \
                    hand_1_data['is_hand_1']               == True  and \
                    hand_1_data['is_right_hand']           == False and \
                    hand_1_data['hand_orientation']        == 90    and \
                    hand_1_data['is_thumb_opened']         == True  and \
                    hand_1_data['is_index_finger_opened']  == True  and \
                    hand_1_data['is_middle_finger_opened'] == True  and \
                    hand_1_data['is_ring_finger_opened']   == True  and \
                    hand_1_data['is_little_finger_opened'] == True     \
                    ) \
                    ):
                action_word_symbol =  "Have_starting"
                if mi.cvs.config_data['take_sample_data'] == "False":
                    HandOneLandMarksDict[HandMarksCount] = np.array(hand_detector.findPosition(action_word_video, 0, draw=False))
                    HandTwoLandMarksDict[HandMarksCount] = np.array(hand_detector.findPosition(action_word_video, 1, draw=False))
                    HandMarksCount +=1
                else:
                    HandOneLandMarksDict[0]=np.array([[0, 737, 504, 0], [1, 705, 479, -32], [2, 692, 444, -46], [3, 691, 414, -59], [4, 692, 389, -72], [5, 720, 407, -5], [6, 719, 372, -36], [7, 718, 350, -66], [8, 719, 329, -88], [9, 740, 407, -12], [10, 740, 368, -37], [11, 740, 342, -64], [12, 740, 319, -84], [13, 759, 413, -27], [14, 761, 377, -53], [15, 761, 354, -70], [16, 761, 333, -82], [17, 777, 427, -46], [18, 783, 397, -69], [19, 785, 378, -78], [20, 786, 360, -83]])
                    HandOneLandMarksDict[1]=np.array([[0, 735, 502, 0], [1, 705, 476, -32], [2, 693, 442, -47], [3, 691, 412, -61], [4, 693, 387, -75], [5, 719, 406, -7], [6, 718, 370, -39], [7, 718, 348, -69], [8, 720, 327, -91], [9, 739, 406, -15], [10, 740, 367, -41], [11, 740, 342, -67], [12, 740, 318, -87], [13, 757, 413, -30], [14, 760, 376, -57], [15, 761, 353, -73], [16, 761, 332, -84], [17, 776, 426, -50], [18, 782, 397, -73], [19, 784, 378, -81], [20, 785, 359, -85]])
                    HandOneLandMarksDict[2]=np.array([[0, 736, 503, 0], [1, 706, 477, -29], [2, 693, 442, -42], [3, 691, 412, -55], [4, 692, 388, -67], [5, 719, 407, -4], [6, 718, 370, -34], [7, 717, 347, -63], [8, 718, 326, -84], [9, 738, 406, -13], [10, 739, 366, -36], [11, 739, 340, -62], [12, 739, 317, -81], [13, 757, 413, -28], [14, 759, 375, -53], [15, 760, 351, -70], [16, 759, 329, -81], [17, 776, 426, -48], [18, 781, 397, -70], [19, 783, 377, -78], [20, 783, 359, -83]])
                    HandOneLandMarksDict[3]=np.array([[0, 736, 504, 0], [1, 707, 478, -30], [2, 693, 443, -43], [3, 691, 413, -56], [4, 692, 387, -68], [5, 719, 407, -2], [6, 718, 371, -31], [7, 718, 348, -61], [8, 719, 328, -82], [9, 739, 406, -10], [10, 739, 367, -34], [11, 739, 342, -60], [12, 740, 319, -80], [13, 758, 413, -26], [14, 760, 376, -51], [15, 760, 353, -67], [16, 760, 332, -78], [17, 777, 426, -46], [18, 782, 396, -68], [19, 784, 377, -76], [20, 784, 359, -80]])
                    HandOneLandMarksDict[4]=np.array([[0, 749, 530, 0], [1, 718, 506, -39], [2, 704, 472, -59], [3, 702, 443, -79], [4, 701, 417, -98], [5, 729, 437, -31], [6, 729, 398, -71], [7, 730, 375, -105], [8, 731, 353, -129], [9, 749, 437, -40], [10, 749, 393, -74], [11, 749, 364, -105], [12, 749, 338, -127], [13, 768, 445, -55], [14, 770, 406, -88], [15, 770, 382, -107], [16, 768, 362, -118], [17, 788, 460, -74], [18, 794, 430, -102], [19, 796, 411, -110], [20, 797, 394, -114]])
                    HandOneLandMarksDict[5]=np.array([[0, 751, 544, 0], [1, 723, 519, -30], [2, 709, 483, -45], [3, 705, 454, -61], [4, 701, 431, -77], [5, 733, 453, -17], [6, 734, 419, -52], [7, 734, 399, -83], [8, 733, 380, -107], [9, 753, 454, -28], [10, 755, 417, -59], [11, 754, 395, -87], [12, 752, 374, -109], [13, 772, 462, -45], [14, 775, 426, -78], [15, 775, 404, -97], [16, 773, 385, -109], [17, 792, 475, -66], [18, 800, 449, -95], [19, 803, 432, -104], [20, 805, 417, -110]])
                    HandOneLandMarksDict[6]=np.array([[0, 758, 562, 0], [1, 729, 540, -35], [2, 713, 506, -54], [3, 705, 479, -73], [4, 699, 456, -92], [5, 735, 473, -29], [6, 736, 442, -67], [7, 736, 423, -99], [8, 737, 405, -123], [9, 755, 476, -38], [10, 757, 443, -72], [11, 756, 421, -101], [12, 756, 401, -121], [13, 774, 486, -53], [14, 777, 454, -89], [15, 777, 433, -107], [16, 777, 414, -118], [17, 792, 501, -71], [18, 799, 479, -105], [19, 802, 463, -117], [20, 805, 448, -123]])
                    HandOneLandMarksDict[7]=np.array([[0, 782, 577, 0], [1, 745, 567, -43], [2, 718, 539, -68], [3, 706, 510, -89], [4, 701, 484, -106], [5, 736, 498, -37], [6, 731, 463, -70], [7, 728, 441, -95], [8, 727, 424, -112], [9, 758, 495, -36], [10, 752, 459, -65], [11, 750, 437, -87], [12, 750, 420, -102], [13, 779, 501, -42], [14, 777, 472, -77], [15, 776, 461, -90], [16, 775, 453, -94], [17, 800, 513, -52], [18, 802, 493, -83], [19, 801, 483, -91], [20, 801, 475, -93]])
                    HandOneLandMarksDict[8]=np.array([[0, 777, 602, 0], [1, 744, 589, -27], [2, 719, 565, -50], [3, 709, 543, -73], [4, 700, 524, -93], [5, 737, 521, -32], [6, 735, 495, -74], [7, 736, 495, -106], [8, 738, 498, -127], [9, 759, 523, -44], [10, 759, 497, -79], [11, 760, 492, -102], [12, 761, 492, -117], [13, 780, 533, -61], [14, 782, 513, -97], [15, 783, 507, -106], [16, 782, 503, -110], [17, 799, 549, -80], [18, 805, 536, -111], [19, 807, 529, -114], [20, 806, 523, -113]])
                    HandOneLandMarksDict[9]=np.array([[0, 780, 616, 0], [1, 750, 605, -33], [2, 723, 582, -56], [3, 708, 563, -74], [4, 698, 546, -91], [5, 740, 560, -59], [6, 740, 539, -90], [7, 742, 529, -115], [8, 743, 517, -134], [9, 758, 564, -64], [10, 760, 543, -92], [11, 760, 529, -107], [12, 761, 516, -122], [13, 776, 573, -72], [14, 776, 554, -105], [15, 777, 540, -112], [16, 779, 525, -117], [17, 793, 587, -82], [18, 796, 573, -114], [19, 799, 563, -118], [20, 802, 551, -121]])
                    HandOneLandMarksDict[10]=np.array([[0, 482, 607, 0], [1, 451, 613, -34], [2, 423, 611, -68], [3, 403, 606, -99], [4, 389, 599, -129], [5, 428, 584, -85], [6, 413, 568, -136], [7, 408, 567, -169], [8, 404, 567, -192], [9, 447, 580, -95], [10, 440, 569, -149], [11, 435, 565, -171], [12, 430, 562, -188], [13, 467, 579, -108], [14, 462, 567, -161], [15, 454, 560, -172], [16, 447, 555, -177], [17, 487, 580, -122], [18, 484, 569, -168], [19, 479, 561, -178], [20, 473, 555, -183]])
                    HandOneLandMarksDict[11]=np.array([[0, 477, 620, 0], [1, 453, 622, -36], [2, 430, 612, -63], [3, 415, 602, -84], [4, 404, 593, -105], [5, 438, 601, -92], [6, 427, 587, -137], [7, 420, 579, -166], [8, 412, 572, -187], [9, 452, 597, -97], [10, 447, 580, -141], [11, 440, 571, -162], [12, 433, 564, -178], [13, 469, 595, -102], [14, 465, 578, -146], [15, 459, 568, -157], [16, 450, 559, -164], [17, 485, 597, -110], [18, 484, 582, -148], [19, 481, 573, -157], [20, 476, 565, -162]])
                    HandOneLandMarksDict[12]=np.array([[0, 770, 632, 0], [1, 742, 625, -30], [2, 720, 606, -45], [3, 710, 589, -57], [4, 700, 573, -69], [5, 738, 594, -51], [6, 734, 577, -78], [7, 736, 567, -97], [8, 737, 558, -112], [9, 759, 596, -57], [10, 759, 577, -80], [11, 760, 566, -95], [12, 761, 555, -109], [13, 779, 602, -65], [14, 781, 585, -97], [15, 783, 572, -109], [16, 784, 559, -118], [17, 798, 612, -74], [18, 804, 598, -108], [19, 809, 588, -117], [20, 813, 577, -124]])
                    HandOneLandMarksDict[13]=np.array([[0, 466, 613, 0], [1, 439, 619, -21], [2, 413, 615, -48], [3, 395, 605, -71], [4, 387, 594, -95], [5, 426, 612, -80], [6, 412, 594, -118], [7, 408, 585, -139], [8, 405, 579, -154], [9, 446, 605, -91], [10, 438, 588, -127], [11, 431, 578, -138], [12, 425, 571, -149], [13, 466, 598, -101], [14, 459, 581, -141], [15, 452, 570, -146], [16, 444, 564, -150], [17, 485, 590, -111], [18, 482, 575, -147], [19, 477, 566, -151], [20, 471, 561, -154]])
                    HandOneLandMarksDict[14]=np.array([[0, 482, 609, 0], [1, 455, 612, -32], [2, 429, 604, -64], [3, 412, 596, -91], [4, 397, 591, -120], [5, 441, 598, -113], [6, 434, 584, -170], [7, 430, 573, -205], [8, 424, 564, -229], [9, 457, 595, -122], [10, 451, 578, -180], [11, 444, 566, -205], [12, 436, 557, -224], [13, 474, 593, -131], [14, 468, 576, -188], [15, 460, 564, -204], [16, 450, 555, -213], [17, 491, 590, -141], [18, 487, 574, -190], [19, 481, 564, -206], [20, 474, 557, -216]])
                    HandOneLandMarksDict[15]=np.array([[0, 473, 518, 0], [1, 498, 506, -54], [2, 513, 483, -84], [3, 515, 461, -107], [4, 517, 442, -132], [5, 486, 446, -71], [6, 483, 415, -111], [7, 479, 397, -141], [8, 474, 381, -160], [9, 465, 448, -69], [10, 463, 414, -100], [11, 460, 395, -125], [12, 457, 379, -143], [13, 446, 456, -70], [14, 442, 424, -99], [15, 440, 405, -115], [16, 439, 391, -127], [17, 427, 470, -76], [18, 419, 446, -102], [19, 415, 431, -111], [20, 413, 420, -116]])
                    HandOneLandMarksDict[16]=np.array([[0, 470, 513, 0], [1, 498, 500, -52], [2, 514, 474, -78], [3, 518, 448, -98], [4, 519, 426, -118], [5, 489, 435, -59], [6, 486, 402, -97], [7, 482, 382, -125], [8, 477, 364, -144], [9, 469, 435, -56], [10, 465, 400, -86], [11, 462, 377, -112], [12, 459, 358, -129], [13, 450, 443, -58], [14, 445, 410, -86], [15, 443, 390, -103], [16, 441, 373, -115], [17, 431, 457, -64], [18, 422, 432, -89], [19, 418, 416, -99], [20, 416, 402, -103]])
                    HandOneLandMarksDict[17]=np.array([[0, 474, 509, 0], [1, 501, 493, -51], [2, 517, 465, -74], [3, 519, 438, -92], [4, 521, 414, -111], [5, 492, 427, -53], [6, 489, 391, -90], [7, 485, 369, -118], [8, 481, 350, -137], [9, 471, 428, -50], [10, 468, 390, -82], [11, 465, 364, -107], [12, 463, 343, -125], [13, 452, 436, -54], [14, 448, 401, -84], [15, 447, 378, -102], [16, 446, 360, -114], [17, 434, 450, -61], [18, 426, 424, -90], [19, 423, 407, -101], [20, 421, 391, -106]])
                    HandOneLandMarksDict[18]=np.array([[0, 475, 509, 0], [1, 504, 489, -51], [2, 519, 460, -75], [3, 521, 433, -94], [4, 523, 408, -113], [5, 494, 422, -47], [6, 491, 388, -84], [7, 488, 366, -114], [8, 484, 346, -134], [9, 474, 423, -46], [10, 471, 384, -76], [11, 469, 358, -101], [12, 466, 336, -120], [13, 455, 430, -50], [14, 451, 395, -78], [15, 449, 373, -96], [16, 449, 354, -107], [17, 436, 444, -60], [18, 429, 418, -86], [19, 427, 400, -95], [20, 426, 384, -100]])
                    HandOneLandMarksDict[19]=np.array([[0, 475, 507, 0], [1, 505, 486, -44], [2, 520, 455, -62], [3, 522, 427, -77], [4, 524, 403, -91], [5, 495, 417, -32], [6, 493, 381, -64], [7, 489, 359, -91], [8, 484, 340, -110], [9, 475, 417, -31], [10, 473, 379, -57], [11, 470, 353, -81], [12, 466, 332, -99], [13, 457, 425, -38], [14, 454, 390, -62], [15, 452, 367, -80], [16, 450, 349, -92], [17, 439, 439, -48], [18, 432, 412, -73], [19, 429, 394, -83], [20, 427, 378, -88]])

                    HandTwoLandMarksDict[0]=np.array([[0, 478, 515, 0], [1, 507, 491, -37], [2, 520, 458, -55], [3, 526, 430, -72], [4, 532, 405, -90], [5, 494, 418, -28], [6, 494, 381, -63], [7, 492, 358, -93], [8, 490, 338, -114], [9, 474, 419, -35], [10, 473, 377, -63], [11, 472, 350, -89], [12, 471, 327, -109], [13, 455, 428, -48], [14, 452, 389, -75], [15, 452, 365, -95], [16, 454, 343, -109], [17, 436, 444, -65], [18, 428, 416, -92], [19, 428, 396, -102], [20, 430, 378, -109]])
                    HandTwoLandMarksDict[1]=np.array([[0, 474, 516, 0], [1, 506, 491, -36], [2, 519, 458, -52], [3, 525, 429, -69], [4, 532, 404, -86], [5, 493, 418, -20], [6, 494, 381, -54], [7, 492, 358, -84], [8, 490, 337, -106], [9, 474, 418, -27], [10, 474, 376, -55], [11, 473, 349, -82], [12, 471, 325, -102], [13, 456, 426, -41], [14, 453, 388, -69], [15, 452, 363, -89], [16, 453, 342, -103], [17, 437, 442, -59], [18, 429, 415, -86], [19, 429, 396, -98], [20, 431, 378, -105]])
                    HandTwoLandMarksDict[2]=np.array([[0, 474, 518, 0], [1, 506, 493, -36], [2, 520, 459, -51], [3, 526, 429, -66], [4, 533, 403, -81], [5, 494, 417, -9], [6, 493, 379, -38], [7, 492, 356, -67], [8, 489, 335, -88], [9, 473, 417, -15], [10, 472, 376, -38], [11, 472, 348, -65], [12, 472, 325, -85], [13, 454, 425, -28], [14, 451, 387, -52], [15, 452, 363, -71], [16, 454, 342, -85], [17, 435, 441, -46], [18, 428, 413, -70], [19, 428, 394, -80], [20, 432, 376, -86]])
                    HandTwoLandMarksDict[3]=np.array([[0, 477, 517, 0], [1, 507, 492, -44], [2, 521, 460, -65], [3, 525, 430, -85], [4, 531, 403, -104], [5, 494, 417, -19], [6, 493, 380, -54], [7, 492, 357, -86], [8, 490, 336, -110], [9, 474, 417, -23], [10, 473, 376, -51], [11, 472, 349, -81], [12, 471, 326, -103], [13, 455, 425, -35], [14, 452, 387, -64], [15, 452, 363, -85], [16, 454, 342, -100], [17, 436, 440, -52], [18, 429, 413, -80], [19, 430, 395, -92], [20, 432, 377, -99]])
                    HandTwoLandMarksDict[4]=np.array([[0, 478, 517, 0], [1, 508, 492, -45], [2, 521, 460, -66], [3, 524, 430, -85], [4, 530, 404, -104], [5, 493, 418, -26], [6, 492, 381, -62], [7, 491, 358, -95], [8, 489, 337, -118], [9, 472, 418, -30], [10, 472, 377, -60], [11, 471, 350, -89], [12, 471, 326, -110], [13, 454, 427, -41], [14, 450, 389, -72], [15, 450, 365, -92], [16, 452, 343, -107], [17, 435, 443, -58], [18, 426, 416, -87], [19, 427, 397, -99], [20, 431, 380, -107]])
                    HandTwoLandMarksDict[5]=np.array([[0, 472, 522, 0], [1, 505, 496, -28], [2, 519, 461, -37], [3, 524, 431, -49], [4, 531, 407, -62], [5, 492, 420, -8], [6, 492, 383, -39], [7, 490, 360, -67], [8, 488, 339, -88], [9, 472, 421, -19], [10, 472, 378, -45], [11, 471, 351, -72], [12, 470, 328, -92], [13, 454, 429, -36], [14, 450, 390, -63], [15, 451, 366, -84], [16, 452, 344, -100], [17, 434, 445, -57], [18, 425, 418, -84], [19, 426, 399, -96], [20, 431, 382, -103]])
                    HandTwoLandMarksDict[6]=np.array([[0, 476, 520, 0], [1, 507, 493, -30], [2, 519, 459, -42], [3, 522, 430, -55], [4, 528, 405, -68], [5, 492, 420, -4], [6, 491, 383, -33], [7, 489, 360, -62], [8, 487, 339, -83], [9, 472, 421, -13], [10, 471, 379, -37], [11, 469, 352, -64], [12, 468, 329, -84], [13, 454, 429, -29], [14, 450, 391, -55], [15, 450, 367, -75], [16, 451, 345, -89], [17, 435, 446, -49], [18, 426, 419, -75], [19, 426, 400, -86], [20, 428, 382, -93]])
                    HandTwoLandMarksDict[7]=np.array([[0, 470, 520, 0], [1, 504, 494, -32], [2, 518, 459, -44], [3, 522, 431, -57], [4, 527, 406, -70], [5, 491, 419, -10], [6, 491, 382, -41], [7, 489, 358, -70], [8, 486, 337, -90], [9, 471, 420, -18], [10, 471, 378, -44], [11, 469, 351, -70], [12, 467, 328, -89], [13, 453, 428, -33], [14, 449, 390, -59], [15, 449, 366, -77], [16, 449, 345, -91], [17, 434, 444, -52], [18, 426, 418, -77], [19, 426, 399, -87], [20, 429, 382, -93]])
                    HandTwoLandMarksDict[8]=np.array([[0, 469, 519, 0], [1, 502, 493, -34], [2, 516, 459, -45], [3, 520, 429, -58], [4, 526, 403, -70], [5, 490, 419, -3], [6, 490, 380, -30], [7, 488, 357, -58], [8, 484, 336, -77], [9, 471, 418, -9], [10, 470, 377, -30], [11, 468, 349, -54], [12, 466, 326, -73], [13, 452, 426, -22], [14, 449, 388, -43], [15, 449, 364, -60], [16, 449, 344, -72], [17, 432, 440, -40], [18, 426, 414, -61], [19, 426, 396, -68], [20, 429, 380, -73]])
                    HandTwoLandMarksDict[9]=np.array([[0, 472, 515, 0], [1, 502, 489, -40], [2, 516, 456, -57], [3, 519, 427, -74], [4, 524, 401, -90], [5, 489, 416, -12], [6, 489, 379, -44], [7, 487, 356, -75], [8, 485, 335, -97], [9, 469, 416, -16], [10, 469, 376, -41], [11, 468, 349, -68], [12, 466, 325, -88], [13, 451, 423, -28], [14, 448, 387, -53], [15, 448, 363, -71], [16, 449, 343, -83], [17, 431, 438, -45], [18, 426, 411, -68], [19, 426, 394, -76], [20, 427, 377, -81]])
                    HandTwoLandMarksDict[10]=np.array([[0, 471, 514, 0], [1, 501, 489, -44], [2, 515, 456, -63], [3, 518, 426, -82], [4, 524, 400, -100], [5, 490, 415, -21], [6, 490, 378, -56], [7, 487, 355, -88], [8, 484, 334, -110], [9, 470, 415, -25], [10, 470, 374, -53], [11, 468, 348, -80], [12, 467, 324, -101], [13, 450, 423, -36], [14, 448, 386, -64], [15, 449, 362, -83], [16, 449, 342, -97], [17, 431, 438, -52], [18, 425, 411, -79], [19, 425, 392, -90], [20, 427, 375, -96]])
                    HandTwoLandMarksDict[11]=np.array([[0, 462, 535, 0], [1, 495, 513, -42], [2, 510, 482, -59], [3, 512, 452, -74], [4, 520, 428, -90], [5, 486, 440, -25], [6, 486, 403, -56], [7, 484, 381, -83], [8, 482, 362, -103], [9, 465, 440, -28], [10, 464, 399, -52], [11, 463, 374, -77], [12, 462, 353, -95], [13, 445, 447, -36], [14, 443, 410, -62], [15, 442, 387, -79], [16, 443, 368, -90], [17, 425, 461, -50], [18, 418, 434, -74], [19, 416, 416, -83], [20, 415, 400, -87]])
                    HandTwoLandMarksDict[12]=np.array([[0, 457, 547, 0], [1, 488, 527, -45], [2, 506, 500, -68], [3, 513, 474, -90], [4, 518, 451, -112], [5, 482, 456, -34], [6, 482, 421, -70], [7, 480, 401, -102], [8, 478, 383, -124], [9, 461, 454, -38], [10, 460, 416, -64], [11, 459, 393, -90], [12, 458, 373, -110], [13, 442, 461, -48], [14, 438, 428, -72], [15, 437, 409, -86], [16, 439, 393, -96], [17, 421, 475, -63], [18, 413, 451, -85], [19, 412, 436, -89], [20, 413, 423, -90]])
                    HandTwoLandMarksDict[13]=np.array([[0, 450, 568, 0], [1, 486, 551, -54], [2, 505, 523, -84], [3, 509, 495, -109], [4, 516, 470, -136], [5, 481, 482, -61], [6, 479, 448, -104], [7, 477, 429, -137], [8, 475, 411, -161], [9, 460, 484, -62], [10, 458, 447, -99], [11, 456, 425, -129], [12, 455, 407, -152], [13, 440, 494, -69], [14, 436, 461, -108], [15, 435, 443, -130], [16, 435, 427, -145], [17, 421, 510, -81], [18, 415, 485, -118], [19, 412, 470, -133], [20, 410, 457, -142]])
                    HandTwoLandMarksDict[14]=np.array([[0, 774, 626, 0], [1, 746, 617, -33], [2, 723, 596, -58], [3, 711, 579, -78], [4, 703, 562, -98], [5, 739, 585, -78], [6, 736, 565, -117], [7, 737, 552, -142], [8, 738, 539, -162], [9, 759, 588, -84], [10, 759, 566, -123], [11, 760, 550, -144], [12, 760, 536, -162], [13, 779, 595, -92], [14, 781, 574, -135], [15, 784, 559, -149], [16, 785, 543, -158], [17, 799, 604, -100], [18, 805, 587, -142], [19, 809, 573, -154], [20, 812, 559, -162]])
                if HandMarksCount >30:
                    action_word_symbol =  populate_have(HandOneLandMarksDict,HandTwoLandMarksDict,2)
        else:
            if mi.cvs.config_data['take_sample_data'] == "False":
                HandOneLandMarksDict[HandMarksCount] = np.array(hand_detector.findPosition(action_word_video, 0, draw=False))
                HandTwoLandMarksDict[HandMarksCount] = np.array(hand_detector.findPosition(action_word_video, 1, draw=False))
                HandMarksCount +=1
            else:
                if action_word_symbol ==  "day_starting":
                    HandOneLandMarksDict[0] = np.array([[0, 824, 506, 0], [1, 847, 526, -1], [2, 874, 525, -6], [3, 891, 520, -18], [4, 908, 517, -30], [5, 907, 510, 13], [6, 938, 506, -12], [7, 961, 506, -37], [8, 981, 506, -55], [9, 907, 506, -6], [10, 940, 502, -30], [11, 964, 504, -51], [12, 986, 505, -67], [13, 905, 503, -32], [14, 938, 500, -52], [15, 961, 502, -65], [16, 980, 504, -73], [17, 900, 503, -60], [18, 927, 499, -75], [19, 946, 500, -80], [20, 961, 502, -83]]) 
                    HandOneLandMarksDict[1] = np.array([[0, 826, 507, 0], [1, 848, 526, 9], [2, 875, 525, 14], [3, 890, 521, 10], [4, 906, 517, 6], [5, 911, 510, 42], [6, 940, 506, 27], [7, 961, 506, 8], [8, 980, 506, -6], [9, 912, 507, 18], [10, 943, 503, 6], [11, 966, 503, -10], [12, 987, 504, -24], [13, 911, 503, -10], [14, 943, 500, -21], [15, 965, 502, -32], [16, 984, 503, -41], [17, 907, 502, -41], [18, 935, 499, -49], [19, 954, 501, -52], [20, 969, 504, -55]]) 
                    HandOneLandMarksDict[2] = np.array([[0, 827, 508, 0], [1, 850, 527, 5], [2, 875, 526, 5], [3, 890, 521, -2], [4, 906, 519, -11], [5, 911, 510, 32], [6, 941, 507, 12], [7, 962, 506, -10], [8, 981, 506, -27], [9, 912, 508, 8], [10, 945, 504, -8], [11, 968, 504, -28], [12, 988, 506, -43], [13, 911, 505, -20], [14, 944, 501, -36], [15, 966, 503, -48], [16, 985, 505, -58], [17, 906, 504, -52], [18, 933, 501, -63], [19, 951, 502, -67], [20, 967, 504, -71]]) 
                    HandOneLandMarksDict[3] = np.array([[0, 828, 506, 0], [1, 850, 525, 11], [2, 874, 526, 16], [3, 889, 522, 12], [4, 905, 518, 8], [5, 911, 509, 42], [6, 941, 506, 29], [7, 962, 506, 12], [8, 981, 506, -1], [9, 913, 506, 19], [10, 945, 503, 7], [11, 967, 504, -8], [12, 987, 506, -21], [13, 912, 504, -8], [14, 945, 501, -19], [15, 966, 503, -29], [16, 985, 505, -37], [17, 910, 503, -37], [18, 938, 501, -45], [19, 956, 503, -47], [20, 971, 504, -50]]) 
                    HandOneLandMarksDict[4] = np.array([[0, 824, 505, 0], [1, 846, 523, 0], [2, 873, 523, -2], [3, 889, 518, -10], [4, 906, 515, -19], [5, 906, 509, 22], [6, 937, 506, 0], [7, 959, 505, -25], [8, 979, 505, -43], [9, 908, 507, 2], [10, 939, 503, -17], [11, 963, 504, -39], [12, 985, 505, -54], [13, 907, 505, -22], [14, 939, 501, -40], [15, 962, 503, -52], [16, 981, 504, -60], [17, 903, 503, -50], [18, 930, 500, -63], [19, 949, 501, -67], [20, 965, 502, -69]]) 
                    HandOneLandMarksDict[5] = np.array([[0, 828, 507, 0], [1, 849, 525, 3], [2, 875, 524, 4], [3, 891, 520, -2], [4, 906, 517, -8], [5, 912, 511, 28], [6, 941, 507, 8], [7, 963, 507, -12], [8, 981, 507, -29], [9, 913, 508, 7], [10, 944, 504, -9], [11, 967, 505, -30], [12, 988, 505, -45], [13, 911, 505, -18], [14, 943, 502, -33], [15, 965, 503, -47], [16, 984, 503, -57], [17, 905, 503, -47], [18, 931, 500, -58], [19, 949, 500, -63], [20, 964, 501, -67]]) 
                    HandOneLandMarksDict[6] = np.array([[0, 827, 505, 0], [1, 849, 523, 5], [2, 873, 522, 6], [3, 888, 519, -1], [4, 904, 516, -8], [5, 910, 507, 32], [6, 940, 503, 11], [7, 961, 502, -10], [8, 981, 502, -27], [9, 911, 504, 9], [10, 943, 500, -9], [11, 966, 501, -29], [12, 988, 502, -45], [13, 910, 502, -18], [14, 942, 498, -35], [15, 964, 500, -47], [16, 983, 502, -56], [17, 906, 500, -48], [18, 933, 497, -61], [19, 951, 499, -65], [20, 967, 501, -68]]) 
                    HandOneLandMarksDict[7] = np.array([[0, 825, 504, 0], [1, 846, 522, 4], [2, 871, 523, 7], [3, 886, 518, 2], [4, 902, 514, -2], [5, 910, 508, 35], [6, 940, 505, 19], [7, 961, 504, 0], [8, 981, 503, -16], [9, 912, 505, 14], [10, 944, 502, 0], [11, 967, 502, -19], [12, 988, 503, -35], [13, 911, 502, -11], [14, 942, 500, -26], [15, 965, 501, -42], [16, 985, 501, -53], [17, 907, 499, -40], [18, 934, 497, -52], [19, 953, 497, -59], [20, 969, 498, -65]]) 
                    HandOneLandMarksDict[8] = np.array([[0, 826, 505, 0], [1, 847, 523, 1], [2, 872, 523, 1], [3, 888, 518, -6], [4, 905, 516, -13], [5, 912, 509, 30], [6, 941, 506, 11], [7, 962, 505, -10], [8, 980, 505, -26], [9, 913, 506, 8], [10, 945, 503, -7], [11, 967, 504, -28], [12, 988, 505, -44], [13, 911, 502, -17], [14, 943, 499, -34], [15, 965, 501, -49], [16, 984, 503, -60], [17, 906, 499, -46], [18, 932, 496, -59], [19, 950, 497, -66], [20, 965, 499, -72]]) 
                    HandOneLandMarksDict[9] = np.array([[0, 823, 500, 0], [1, 844, 521, 4], [2, 870, 522, 6], [3, 886, 518, 0], [4, 902, 514, -5], [5, 909, 509, 30], [6, 938, 505, 13], [7, 959, 504, -7], [8, 978, 504, -23], [9, 910, 505, 8], [10, 942, 501, -5], [11, 966, 502, -24], [12, 987, 502, -39], [13, 908, 500, -17], [14, 940, 497, -31], [15, 962, 499, -43], [16, 981, 501, -52], [17, 903, 496, -46], [18, 929, 494, -57], [19, 946, 496, -61], [20, 961, 498, -65]]) 
                    HandOneLandMarksDict[10]= np.array([[0, 824, 502, 0], [1, 846, 521, 1], [2, 873, 520, 0], [3, 891, 516, -8], [4, 908, 512, -17], [5, 910, 506, 26], [6, 940, 502, 5], [7, 962, 502, -18], [8, 981, 501, -36], [9, 911, 502, 4], [10, 943, 499, -15], [11, 966, 499, -36], [12, 988, 500, -53], [13, 909, 499, -22], [14, 941, 495, -41], [15, 963, 497, -54], [16, 982, 499, -64], [17, 903, 496, -52], [18, 930, 493, -67], [19, 948, 494, -74], [20, 964, 496, -79]]) 
                    HandOneLandMarksDict[11]= np.array([[0, 822, 500, 0], [1, 843, 519, -2], [2, 869, 520, -3], [3, 885, 516, -12], [4, 902, 513, -20], [5, 908, 505, 23], [6, 938, 501, 1], [7, 960, 501, -22], [8, 979, 501, -40], [9, 909, 501, 3], [10, 941, 498, -16], [11, 965, 499, -37], [12, 986, 500, -52], [13, 907, 497, -21], [14, 940, 495, -40], [15, 962, 497, -53], [16, 982, 498, -62], [17, 902, 494, -49], [18, 929, 492, -63], [19, 948, 493, -69], [20, 964, 495, -73]]) 
                    HandOneLandMarksDict[12]= np.array([[0, 822, 501, 0], [1, 844, 520, 5], [2, 869, 521, 8], [3, 886, 517, 3], [4, 903, 513, -1], [5, 909, 505, 39], [6, 938, 501, 22], [7, 959, 501, 1], [8, 978, 501, -15], [9, 911, 501, 16], [10, 942, 497, 1], [11, 965, 499, -18], [12, 986, 501, -33], [13, 909, 497, -11], [14, 940, 494, -27], [15, 963, 496, -41], [16, 983, 499, -52], [17, 905, 494, -42], [18, 932, 492, -56], [19, 951, 493, -62], [20, 967, 495, -67]]) 
                    HandOneLandMarksDict[13]= np.array([[0, 821, 501, 0], [1, 842, 519, 7], [2, 867, 520, 10], [3, 884, 515, 5], [4, 900, 512, 0], [5, 906, 508, 31], [6, 936, 503, 14], [7, 958, 502, -3], [8, 977, 501, -18], [9, 907, 505, 9], [10, 940, 499, -5], [11, 964, 499, -23], [12, 985, 500, -37], [13, 905, 500, -17], [14, 938, 495, -32], [15, 962, 496, -46], [16, 982, 498, -56], [17, 900, 494, -45], [18, 929, 490, -58], [19, 948, 492, -65], [20, 963, 494, -69]]) 
                    HandOneLandMarksDict[14]= np.array([[0, 820, 500, 0], [1, 843, 520, 3], [2, 868, 520, 3], [3, 884, 515, -4], [4, 902, 511, -11], [5, 906, 504, 34], [6, 935, 500, 14], [7, 957, 500, -8], [8, 976, 500, -26], [9, 907, 500, 11], [10, 939, 497, -6], [11, 962, 499, -27], [12, 984, 500, -42], [13, 906, 496, -18], [14, 938, 494, -36], [15, 960, 497, -49], [16, 980, 499, -58], [17, 900, 494, -49], [18, 929, 492, -64], [19, 948, 495, -69], [20, 964, 497, -73]]) 
                    HandOneLandMarksDict[15]= np.array([[0, 820, 500, 0], [1, 844, 520, 7], [2, 871, 520, 10], [3, 888, 516, 5], [4, 906, 512, 0], [5, 908, 505, 37], [6, 937, 501, 20], [7, 958, 501, 1], [8, 976, 502, -14], [9, 908, 501, 13], [10, 940, 497, -1], [11, 963, 499, -19], [12, 984, 501, -34], [13, 905, 497, -15], [14, 937, 494, -30], [15, 960, 496, -43], [16, 979, 499, -53], [17, 899, 494, -46], [18, 926, 491, -59], [19, 944, 493, -65], [20, 960, 495, -70]]) 
                    HandOneLandMarksDict[16]= np.array([[0, 821, 500, 0], [1, 843, 520, 6], [2, 868, 520, 8], [3, 883, 517, 1], [4, 899, 513, -4], [5, 907, 505, 37], [6, 936, 502, 19], [7, 957, 502, -2], [8, 976, 502, -18], [9, 908, 502, 13], [10, 940, 499, -1], [11, 963, 500, -21], [12, 984, 502, -36], [13, 906, 498, -16], [14, 938, 495, -31], [15, 961, 498, -44], [16, 980, 500, -54], [17, 901, 495, -47], [18, 928, 492, -59], [19, 947, 494, -65], [20, 963, 496, -69]]) 
                    HandOneLandMarksDict[17]= np.array([[0, 821, 501, 0], [1, 842, 520, 7], [2, 866, 521, 9], [3, 881, 516, 4], [4, 897, 512, 0], [5, 907, 508, 36], [6, 936, 503, 21], [7, 957, 503, 1], [8, 976, 503, -13], [9, 909, 504, 13], [10, 940, 500, 0], [11, 963, 500, -17], [12, 983, 501, -32], [13, 906, 499, -15], [14, 938, 496, -27], [15, 961, 497, -41], [16, 980, 499, -52], [17, 901, 494, -45], [18, 928, 492, -56], [19, 947, 493, -62], [20, 962, 495, -68]]) 
                    HandOneLandMarksDict[18]= np.array([[0, 819, 500, 0], [1, 840, 520, -1], [2, 866, 521, -1], [3, 883, 516, -9], [4, 899, 513, -16], [5, 905, 507, 25], [6, 934, 503, 5], [7, 956, 503, -16], [8, 975, 502, -32], [9, 906, 503, 5], [10, 938, 499, -13], [11, 961, 500, -35], [12, 983, 501, -51], [13, 904, 498, -20], [14, 936, 496, -39], [15, 959, 497, -56], [16, 979, 499, -67], [17, 898, 495, -48], [18, 925, 493, -64], [19, 943, 494, -72], [20, 959, 496, -78]]) 
                    HandOneLandMarksDict[19] = np.array([[0, 819, 501, 0], [1, 841, 521, 6], [2, 868, 521, 11], [3, 886, 517, 8], [4, 903, 513, 5], [5, 905, 508, 37], [6, 934, 503, 22], [7, 955, 503, 3], [8, 974, 503, -11], [9, 906, 504, 14], [10, 938, 500, 1], [11, 961, 501, -17], [12, 982, 502, -32], [13, 904, 499, -12], [14, 936, 496, -27], [15, 958, 499, -41], [16, 978, 501, -51], [17, 899, 496, -42], [18, 927, 494, -55], [19, 946, 495, -62], [20, 962, 498, -68]]) 
                    HandOneLandMarksDict[20] = np.array([[0, 818, 500, 0], [1, 838, 521, 0], [2, 865, 522, 0], [3, 883, 517, -5], [4, 899, 514, -10], [5, 904, 510, 29], [6, 933, 505, 10], [7, 954, 505, -10], [8, 972, 504, -27], [9, 905, 505, 9], [10, 936, 501, -6], [11, 959, 502, -26], [12, 980, 503, -41], [13, 903, 500, -14], [14, 933, 496, -31], [15, 955, 498, -44], [16, 974, 500, -54], [17, 897, 496, -42], [18, 923, 493, -55], [19, 940, 494, -61], [20, 954, 496, -66]]) 
                    HandOneLandMarksDict[21] = np.array([[0, 818, 500, 0], [1, 839, 520, 1], [2, 866, 521, 4], [3, 885, 516, 0], [4, 901, 512, -4], [5, 905, 507, 34], [6, 933, 502, 18], [7, 954, 502, -2], [8, 973, 502, -18], [9, 906, 503, 14], [10, 936, 499, -1], [11, 959, 499, -20], [12, 980, 500, -34], [13, 904, 498, -11], [14, 935, 495, -27], [15, 957, 497, -40], [16, 976, 498, -48], [17, 899, 495, -40], [18, 926, 492, -52], [19, 944, 494, -58], [20, 960, 496, -62]]) 
                    HandOneLandMarksDict[22] = np.array([[0, 816, 499, 0], [1, 838, 519, 4], [2, 864, 521, 8], [3, 881, 516, 4], [4, 897, 512, 0], [5, 903, 507, 36], [6, 932, 502, 21], [7, 953, 501, 1], [8, 972, 500, -13], [9, 905, 503, 14], [10, 936, 499, 0], [11, 959, 499, -17], [12, 980, 499, -32], [13, 902, 499, -12], [14, 934, 495, -26], [15, 957, 497, -40], [16, 977, 497, -50], [17, 897, 494, -40], [18, 925, 492, -52], [19, 943, 493, -58], [20, 959, 496, -63]]) 
                    HandOneLandMarksDict[23] = np.array([[0, 816, 501, 0], [1, 839, 520, 7], [2, 867, 520, 12], [3, 885, 514, 9], [4, 901, 511, 7], [5, 904, 507, 41], [6, 932, 502, 26], [7, 953, 502, 6], [8, 971, 502, -8], [9, 905, 503, 18], [10, 935, 499, 4], [11, 958, 500, -13], [12, 979, 501, -28], [13, 903, 499, -9], [14, 933, 495, -23], [15, 955, 497, -37], [16, 975, 498, -46], [17, 898, 495, -39], [18, 925, 492, -51], [19, 943, 493, -57], [20, 958, 495, -62]]) 
                    HandOneLandMarksDict[24] = np.array([[0, 814, 501, 0], [1, 837, 521, 7], [2, 863, 521, 11], [3, 880, 517, 7], [4, 896, 514, 2], [5, 902, 508, 34], [6, 930, 503, 18], [7, 951, 503, -1], [8, 970, 502, -17], [9, 902, 504, 10], [10, 933, 500, -3], [11, 957, 500, -23], [12, 978, 500, -39], [13, 899, 499, -17], [14, 930, 496, -31], [15, 953, 497, -45], [16, 973, 497, -57], [17, 893, 495, -47], [18, 920, 492, -60], [19, 938, 493, -66], [20, 953, 495, -72]]) 
                    HandOneLandMarksDict[25] = np.array([[0, 816, 500, 0], [1, 837, 520, 6], [2, 862, 521, 9], [3, 878, 516, 5], [4, 893, 513, 1], [5, 903, 508, 37], [6, 931, 503, 21], [7, 952, 502, 2], [8, 971, 502, -12], [9, 904, 503, 14], [10, 934, 499, 0], [11, 957, 500, -19], [12, 978, 501, -34], [13, 901, 499, -13], [14, 933, 496, -29], [15, 955, 497, -43], [16, 974, 498, -54], [17, 895, 496, -43], [18, 923, 492, -57], [19, 942, 494, -64], [20, 958, 495, -70]]) 
                    HandOneLandMarksDict[26] = np.array([[0, 815, 499, 0], [1, 836, 520, 0], [2, 862, 522, 3], [3, 879, 517, 0], [4, 896, 513, -3], [5, 902, 509, 36], [6, 930, 504, 21], [7, 951, 504, 0], [8, 969, 503, -15], [9, 903, 505, 17], [10, 933, 501, 4], [11, 956, 501, -14], [12, 977, 501, -28], [13, 902, 499, -6], [14, 932, 497, -20], [15, 953, 498, -31], [16, 972, 499, -40], [17, 897, 495, -33], [18, 923, 494, -44], [19, 940, 495, -48], [20, 955, 497, -51]]) 
                    HandOneLandMarksDict[27] = np.array([[0, 812, 500, 0], [1, 834, 520, 8], [2, 860, 522, 13], [3, 877, 518, 10], [4, 893, 514, 6], [5, 899, 507, 41], [6, 928, 503, 25], [7, 949, 502, 5], [8, 969, 502, -11], [9, 900, 504, 17], [10, 931, 500, 3], [11, 955, 500, -16], [12, 977, 500, -32], [13, 898, 499, -11], [14, 929, 496, -26], [15, 952, 498, -40], [16, 972, 499, -50], [17, 893, 496, -41], [18, 920, 493, -54], [19, 937, 495, -59], [20, 953, 497, -63]]) 
                    HandOneLandMarksDict[28] = np.array([[0, 813, 501, 0], [1, 836, 521, 4], [2, 863, 522, 8], [3, 881, 517, 4], [4, 898, 514, 1], [5, 900, 509, 39], [6, 929, 504, 24], [7, 950, 503, 4], [8, 969, 503, -10], [9, 902, 504, 17], [10, 932, 500, 3], [11, 956, 501, -15], [12, 977, 501, -30], [13, 900, 500, -8], [14, 931, 497, -23], [15, 953, 498, -36], [16, 972, 499, -45], [17, 894, 496, -37], [18, 922, 493, -49], [19, 940, 495, -55], [20, 955, 497, -59]]) 
                    HandOneLandMarksDict[29] = np.array([[0, 813, 502, 0], [1, 833, 522, 4], [2, 858, 523, 8], [3, 875, 518, 3], [4, 890, 515, -1], [5, 899, 509, 35], [6, 928, 505, 19], [7, 949, 504, 0], [8, 967, 503, -16], [9, 901, 505, 13], [10, 931, 501, 0], [11, 954, 501, -19], [12, 976, 501, -33], [13, 898, 501, -13], [14, 929, 497, -27], [15, 951, 498, -40], [16, 970, 499, -49], [17, 892, 496, -42], [18, 919, 493, -54], [19, 936, 494, -58], [20, 951, 497, -62]]) 
                    HandOneLandMarksDict[30] = np.array([[0, 814, 501, 0], [1, 835, 522, 5], [2, 861, 524, 11], [3, 879, 519, 9], [4, 894, 515, 7], [5, 901, 510, 40], [6, 929, 506, 27], [7, 950, 505, 10], [8, 968, 504, -3], [9, 902, 505, 19], [10, 933, 502, 7], [11, 955, 502, -10], [12, 976, 502, -24], [13, 900, 501, -6], [14, 931, 498, -19], [15, 953, 499, -34], [16, 972, 500, -45], [17, 895, 496, -34], [18, 922, 494, -46], [19, 940, 495, -53], [20, 956, 497, -59]]) 
                    HandOneLandMarksDict[31] = np.array([[0, 814, 503, 0], [1, 836, 523, 5], [2, 862, 524, 10], [3, 880, 519, 6], [4, 896, 516, 3], [5, 900, 510, 38], [6, 929, 506, 23], [7, 950, 505, 5], [8, 968, 505, -9], [9, 902, 506, 16], [10, 933, 502, 2], [11, 956, 503, -16], [12, 976, 504, -31], [13, 899, 502, -11], [14, 931, 499, -26], [15, 954, 500, -41], [16, 973, 501, -53], [17, 894, 498, -40], [18, 922, 495, -53], [19, 940, 497, -61], [20, 955, 498, -67]]) 
                    HandOneLandMarksDict[32] = np.array([[0, 815, 502, 0], [1, 835, 522, 1], [2, 861, 524, 4], [3, 878, 520, 0], [4, 893, 516, -4], [5, 901, 511, 31], [6, 929, 507, 15], [7, 950, 506, -4], [8, 968, 506, -20], [9, 902, 507, 10], [10, 933, 503, -4], [11, 956, 504, -24], [12, 977, 504, -39], [13, 900, 502, -14], [14, 931, 499, -30], [15, 953, 500, -46], [16, 972, 501, -57], [17, 894, 499, -42], [18, 920, 495, -56], [19, 938, 496, -64], [20, 953, 497, -70]]) 
                    HandOneLandMarksDict[33] = np.array([[0, 814, 502, 0], [1, 836, 522, 7], [2, 862, 524, 12], [3, 879, 519, 9], [4, 895, 516, 7], [5, 900, 511, 42], [6, 929, 508, 28], [7, 950, 507, 9], [8, 969, 506, -5], [9, 902, 507, 19], [10, 933, 504, 6], [11, 956, 504, -12], [12, 977, 504, -27], [13, 900, 502, -8], [14, 932, 500, -23], [15, 954, 501, -37], [16, 973, 502, -47], [17, 895, 498, -38], [18, 923, 496, -50], [19, 942, 497, -57], [20, 958, 499, -62]]) 
                    HandOneLandMarksDict[34] = np.array([[0, 816, 500, 0], [1, 836, 521, 7], [2, 862, 522, 13], [3, 879, 518, 11], [4, 895, 514, 10], [5, 902, 510, 44], [6, 930, 506, 32], [7, 950, 505, 15], [8, 969, 505, 0], [9, 904, 506, 22], [10, 934, 502, 12], [11, 956, 503, -4], [12, 977, 503, -18], [13, 902, 501, -4], [14, 933, 499, -16], [15, 954, 499, -28], [16, 973, 500, -38], [17, 898, 497, -33], [18, 925, 495, -44], [19, 943, 496, -50], [20, 959, 498, -55]]) 
                    HandOneLandMarksDict[35] = np.array([[0, 815, 499, 0], [1, 836, 520, 8], [2, 862, 522, 17], [3, 879, 518, 18], [4, 895, 515, 18], [5, 901, 510, 47], [6, 929, 506, 36], [7, 950, 505, 20], [8, 968, 505, 7], [9, 903, 506, 25], [10, 934, 503, 15], [11, 957, 503, 0], [12, 977, 503, -12], [13, 902, 501, -1], [14, 933, 499, -12], [15, 955, 500, -25], [16, 973, 501, -33], [17, 898, 496, -30], [18, 926, 495, -40], [19, 944, 496, -44], [20, 960, 498, -48]]) 
                    HandOneLandMarksDict[36] = np.array([[0, 814, 501, 0], [1, 835, 522, 5], [2, 862, 523, 13], [3, 881, 519, 12], [4, 898, 516, 13], [5, 900, 510, 46], [6, 929, 507, 34], [7, 950, 506, 16], [8, 968, 505, 1], [9, 903, 506, 26], [10, 933, 503, 15], [11, 956, 503, -1], [12, 976, 503, -15], [13, 902, 501, 0], [14, 932, 499, -10], [15, 953, 500, -22], [16, 972, 501, -31], [17, 897, 497, -27], [18, 924, 495, -37], [19, 942, 497, -41], [20, 957, 498, -45]]) 
                    HandOneLandMarksDict[37] = np.array([[0, 817, 501, 0], [1, 839, 522, 5], [2, 867, 523, 10], [3, 885, 518, 7], [4, 901, 515, 4], [5, 902, 511, 39], [6, 930, 507, 25], [7, 951, 507, 6], [8, 969, 506, -8], [9, 903, 506, 18], [10, 934, 503, 5], [11, 957, 503, -13], [12, 977, 503, -27], [13, 901, 501, -7], [14, 932, 499, -21], [15, 953, 499, -34], [16, 971, 500, -44], [17, 895, 496, -35], [18, 921, 494, -46], [19, 938, 496, -52], [20, 953, 497, -57]]) 
                    HandOneLandMarksDict[38] = np.array([[0, 815, 501, 0], [1, 836, 521, 6], [2, 863, 523, 14], [3, 880, 519, 13], [4, 897, 517, 12], [5, 900, 509, 43], [6, 929, 506, 29], [7, 950, 505, 10], [8, 969, 505, -3], [9, 902, 505, 20], [10, 933, 502, 7], [11, 956, 503, -10], [12, 977, 503, -25], [13, 901, 501, -6], [14, 931, 498, -21], [15, 953, 500, -34], [16, 972, 500, -44], [17, 896, 497, -35], [18, 924, 495, -48], [19, 942, 496, -54], [20, 958, 498, -58]]) 
                    HandOneLandMarksDict[39] = np.array([[0, 816, 501, 0], [1, 835, 521, 8], [2, 862, 522, 14], [3, 880, 517, 12], [4, 897, 514, 10], [5, 901, 511, 40], [6, 930, 506, 28], [7, 950, 505, 11], [8, 968, 505, -1], [9, 903, 507, 17], [10, 934, 502, 6], [11, 957, 502, -9], [12, 976, 503, -22], [13, 901, 502, -9], [14, 933, 498, -21], [15, 955, 499, -33], [16, 973, 500, -43], [17, 896, 497, -39], [18, 924, 494, -49], [19, 942, 496, -55], [20, 958, 498, -59]]) 
                    HandOneLandMarksDict[40] = np.array([[0, 816, 500, 0], [1, 837, 521, 9], [2, 864, 522, 18], [3, 883, 517, 19], [4, 899, 515, 21], [5, 902, 511, 49], [6, 930, 507, 39], [7, 950, 507, 23], [8, 968, 506, 10], [9, 904, 506, 27], [10, 934, 503, 18], [11, 956, 503, 2], [12, 976, 504, -10], [13, 903, 501, 0], [14, 933, 498, -9], [15, 954, 500, -21], [16, 972, 500, -30], [17, 899, 496, -27], [18, 925, 494, -37], [19, 943, 496, -42], [20, 958, 498, -46]]) 
                    HandOneLandMarksDict[41] = np.array([[0, 818, 503, 0], [1, 839, 522, 1], [2, 866, 522, 4], [3, 885, 516, 1], [4, 901, 515, -1], [5, 902, 511, 31], [6, 931, 507, 16], [7, 951, 507, -1], [8, 969, 506, -16], [9, 904, 507, 12], [10, 934, 503, -1], [11, 957, 503, -18], [12, 976, 503, -31], [13, 902, 502, -11], [14, 932, 499, -25], [15, 953, 500, -37], [16, 971, 501, -46], [17, 896, 497, -37], [18, 922, 495, -49], [19, 939, 496, -54], [20, 954, 498, -59]]) 
                    HandOneLandMarksDict[42] = np.array([[0, 818, 503, 0], [1, 840, 522, 7], [2, 866, 522, 12], [3, 883, 518, 10], [4, 900, 515, 7], [5, 903, 511, 40], [6, 931, 507, 26], [7, 951, 506, 8], [8, 970, 506, -5], [9, 904, 507, 18], [10, 935, 503, 6], [11, 957, 503, -9], [12, 977, 503, -22], [13, 903, 502, -8], [14, 933, 499, -20], [15, 955, 500, -31], [16, 973, 501, -39], [17, 898, 497, -38], [18, 925, 495, -48], [19, 943, 497, -52], [20, 958, 498, -56]]) 
                    HandOneLandMarksDict[43] = np.array([[0, 818, 502, 0], [1, 838, 522, 5], [2, 865, 524, 11], [3, 883, 519, 9], [4, 898, 517, 7], [5, 902, 512, 36], [6, 930, 508, 23], [7, 951, 508, 6], [8, 968, 507, -7], [9, 904, 507, 15], [10, 934, 503, 3], [11, 956, 504, -13], [12, 976, 505, -26], [13, 901, 502, -9], [14, 932, 499, -23], [15, 954, 500, -36], [16, 972, 501, -45], [17, 896, 498, -37], [18, 923, 495, -49], [19, 941, 496, -55], [20, 957, 498, -60]]) 
                    HandOneLandMarksDict[44] = np.array([[0, 818, 501, 0], [1, 839, 521, 2], [2, 866, 522, 8], [3, 885, 517, 6], [4, 902, 515, 5], [5, 903, 511, 36], [6, 931, 508, 22], [7, 951, 507, 5], [8, 969, 506, -9], [9, 904, 507, 17], [10, 934, 503, 4], [11, 957, 504, -12], [12, 976, 504, -26], [13, 902, 501, -6], [14, 933, 499, -20], [15, 954, 500, -32], [16, 972, 501, -41], [17, 897, 497, -33], [18, 923, 495, -45], [19, 941, 496, -51], [20, 956, 498, -56]]) 
                    HandOneLandMarksDict[45] = np.array([[0, 817, 502, 0], [1, 838, 522, 5], [2, 866, 522, 10], [3, 884, 518, 9], [4, 900, 516, 7], [5, 901, 511, 35], [6, 930, 507, 20], [7, 951, 507, 1], [8, 969, 506, -13], [9, 902, 506, 13], [10, 933, 503, -1], [11, 956, 504, -20], [12, 977, 504, -34], [13, 900, 501, -12], [14, 931, 499, -29], [15, 953, 500, -43], [16, 972, 501, -53], [17, 894, 497, -41], [18, 922, 495, -56], [19, 940, 497, -63], [20, 956, 499, -69]]) 
                    HandOneLandMarksDict[46] = np.array([[0, 816, 500, 0], [1, 836, 521, 8], [2, 862, 523, 16], [3, 879, 520, 15], [4, 894, 517, 15], [5, 901, 511, 42], [6, 930, 508, 31], [7, 950, 507, 14], [8, 969, 506, 0], [9, 903, 507, 19], [10, 934, 504, 9], [11, 956, 504, -6], [12, 977, 504, -19], [13, 902, 502, -7], [14, 933, 499, -18], [15, 954, 501, -29], [16, 973, 502, -37], [17, 897, 497, -36], [18, 925, 496, -46], [19, 943, 497, -50], [20, 958, 500, -54]]) 
                    HandOneLandMarksDict[47] = np.array([[0, 817, 501, 0], [1, 836, 522, 11], [2, 863, 523, 20], [3, 881, 519, 20], [4, 897, 517, 20], [5, 902, 512, 46], [6, 930, 508, 35], [7, 950, 507, 19], [8, 968, 506, 6], [9, 904, 508, 23], [10, 935, 504, 13], [11, 957, 505, -3], [12, 977, 505, -16], [13, 903, 503, -5], [14, 934, 500, -16], [15, 954, 501, -27], [16, 972, 502, -36], [17, 898, 498, -35], [18, 925, 496, -45], [19, 943, 498, -50], [20, 958, 499, -55]]) 
                    HandOneLandMarksDict[48] = np.array([[0, 817, 501, 0], [1, 836, 522, 3], [2, 863, 524, 10], [3, 882, 520, 10], [4, 899, 518, 10], [5, 902, 513, 41], [6, 930, 509, 29], [7, 951, 508, 11], [8, 969, 508, -3], [9, 904, 508, 21], [10, 934, 505, 10], [11, 957, 506, -6], [12, 977, 506, -20], [13, 903, 503, -3], [14, 933, 501, -16], [15, 954, 502, -28], [16, 972, 504, -36], [17, 898, 499, -31], [18, 925, 497, -43], [19, 943, 499, -48], [20, 958, 502, -52]]) 
                    HandOneLandMarksDict[49] = np.array([[0, 818, 504, 0], [1, 838, 524, -2], [2, 865, 525, -1], [3, 884, 519, -6], [4, 900, 518, -9], [5, 902, 514, 27], [6, 931, 510, 9], [7, 952, 510, -10], [8, 970, 510, -25], [9, 904, 509, 10], [10, 934, 506, -6], [11, 957, 506, -25], [12, 978, 507, -39], [13, 901, 504, -12], [14, 932, 501, -29], [15, 953, 503, -42], [16, 972, 504, -51], [17, 895, 500, -37], [18, 920, 497, -52], [19, 937, 498, -58], [20, 951, 499, -62]]) 
                    HandOneLandMarksDict[50] = np.array([[0, 820, 504, 0], [1, 839, 524, 4], [2, 867, 525, 10], [3, 886, 520, 8], [4, 902, 517, 6], [5, 904, 516, 35], [6, 932, 511, 22], [7, 952, 510, 5], [8, 969, 510, -8], [9, 905, 511, 14], [10, 936, 507, 2], [11, 959, 507, -13], [12, 978, 508, -26], [13, 903, 506, -10], [14, 934, 503, -23], [15, 956, 504, -35], [16, 974, 505, -44], [17, 898, 501, -37], [18, 924, 499, -49], [19, 942, 500, -54], [20, 956, 502, -59]]) 
                    HandOneLandMarksDict[51] = np.array([[0, 817, 500, 0], [1, 838, 523, 7], [2, 866, 526, 15], [3, 885, 523, 15], [4, 902, 521, 16], [5, 902, 514, 46], [6, 931, 511, 34], [7, 951, 510, 18], [8, 970, 511, 4], [9, 905, 510, 24], [10, 935, 506, 13], [11, 958, 507, -2], [12, 978, 509, -15], [13, 903, 505, -2], [14, 934, 503, -15], [15, 955, 505, -25], [16, 973, 507, -33], [17, 899, 501, -32], [18, 926, 499, -42], [19, 943, 501, -46], [20, 958, 503, -49]]) 
                    HandOneLandMarksDict[52] = np.array([[0, 819, 505, 0], [1, 839, 525, 2], [2, 866, 526, 6], [3, 885, 521, 4], [4, 901, 518, 2], [5, 905, 517, 33], [6, 933, 513, 19], [7, 953, 513, 1], [8, 971, 512, -13], [9, 906, 512, 14], [10, 937, 509, 0], [11, 959, 509, -17], [12, 979, 510, -31], [13, 904, 507, -10], [14, 934, 505, -25], [15, 955, 505, -38], [16, 974, 506, -49], [17, 898, 502, -36], [18, 923, 500, -49], [19, 940, 501, -57], [20, 955, 502, -63]]) 
                    HandOneLandMarksDict[53] = np.array([[0, 822, 504, 0], [1, 841, 525, 8], [2, 867, 526, 16], [3, 886, 522, 15], [4, 902, 519, 15], [5, 906, 517, 44], [6, 934, 513, 34], [7, 954, 512, 17], [8, 972, 512, 3], [9, 908, 512, 23], [10, 939, 509, 12], [11, 961, 509, -3], [12, 980, 510, -17], [13, 907, 507, -4], [14, 937, 505, -15], [15, 959, 507, -28], [16, 977, 507, -38], [17, 903, 502, -33], [18, 929, 501, -43], [19, 947, 503, -49], [20, 961, 505, -55]]) 
                    HandOneLandMarksDict[54] = np.array([[0, 821, 504, 0], [1, 840, 525, 0], [2, 868, 526, 2], [3, 886, 522, 0], [4, 903, 520, -2], [5, 903, 517, 27], [6, 933, 514, 11], [7, 953, 513, -6], [8, 971, 512, -20], [9, 905, 512, 9], [10, 937, 509, -5], [11, 960, 510, -23], [12, 980, 510, -36], [13, 903, 507, -13], [14, 934, 504, -29], [15, 956, 505, -42], [16, 974, 506, -51], [17, 897, 502, -38], [18, 924, 499, -52], [19, 942, 500, -59], [20, 956, 502, -64]]) 
                    HandOneLandMarksDict[55] = np.array([[0, 823, 504, 0], [1, 842, 525, 7], [2, 871, 525, 15], [3, 889, 521, 14], [4, 905, 520, 14], [5, 907, 516, 37], [6, 935, 513, 25], [7, 955, 513, 9], [8, 973, 512, -4], [9, 908, 512, 16], [10, 939, 509, 4], [11, 961, 509, -11], [12, 981, 510, -24], [13, 905, 506, -9], [14, 936, 504, -23], [15, 957, 505, -35], [16, 976, 506, -45], [17, 899, 502, -37], [18, 926, 499, -49], [19, 943, 500, -56], [20, 958, 502, -62]]) 
                    HandOneLandMarksDict[56] = np.array([[0, 822, 503, 0], [1, 843, 524, 4], [2, 871, 525, 8], [3, 890, 521, 5], [4, 905, 519, 2], [5, 906, 516, 31], [6, 935, 512, 15], [7, 956, 512, -2], [8, 974, 511, -17], [9, 907, 511, 10], [10, 939, 509, -4], [11, 962, 509, -23], [12, 983, 510, -38], [13, 905, 506, -15], [14, 936, 504, -31], [15, 958, 505, -45], [16, 977, 506, -55], [17, 900, 501, -42], [18, 926, 499, -57], [19, 944, 500, -64], [20, 960, 501, -71]]) 
                    HandOneLandMarksDict[57] = np.array([[0, 822, 504, 0], [1, 843, 524, 0], [2, 871, 525, 3], [3, 890, 521, 0], [4, 906, 519, -3], [5, 906, 516, 29], [6, 935, 512, 10], [7, 957, 512, -9], [8, 975, 512, -25], [9, 907, 511, 9], [10, 939, 507, -7], [11, 962, 508, -27], [12, 983, 509, -42], [13, 905, 506, -14], [14, 936, 503, -32], [15, 957, 505, -45], [16, 976, 506, -53], [17, 898, 502, -41], [18, 924, 499, -55], [19, 942, 500, -62], [20, 957, 502, -66]]) 
                    HandOneLandMarksDict[58] = np.array([[0, 821, 504, 0], [1, 841, 526, -1], [2, 870, 526, 0], [3, 889, 522, -3], [4, 905, 520, -6], [5, 905, 516, 25], [6, 934, 512, 7], [7, 956, 511, -12], [8, 974, 511, -28], [9, 906, 511, 7], [10, 938, 507, -10], [11, 961, 508, -29], [12, 982, 509, -44], [13, 903, 506, -15], [14, 934, 502, -34], [15, 956, 504, -48], [16, 975, 505, -56], [17, 897, 502, -41], [18, 923, 499, -57], [19, 940, 500, -64], [20, 955, 501, -69]]) 
                    HandOneLandMarksDict[59] = np.array([[0, 820, 505, 0], [1, 838, 525, 2], [2, 866, 527, 6], [3, 883, 523, 3], [4, 898, 522, 0], [5, 905, 517, 27], [6, 934, 513, 10], [7, 955, 513, -8], [8, 973, 513, -23], [9, 906, 512, 7], [10, 938, 509, -8], [11, 961, 510, -27], [12, 982, 511, -41], [13, 904, 507, -17], [14, 935, 504, -33], [15, 957, 505, -46], [16, 975, 507, -55], [17, 897, 502, -44], [18, 924, 499, -58], [19, 942, 500, -64], [20, 957, 502, -69]]) 
                    HandOneLandMarksDict[60]= np.array([[0, 821, 505, 0], [1, 840, 525, 1], [2, 866, 528, 4], [3, 884, 524, 1], [4, 899, 523, -1], [5, 906, 518, 28], [6, 934, 514, 12], [7, 955, 514, -6], [8, 973, 513, -21], [9, 907, 513, 9], [10, 938, 510, -6], [11, 961, 511, -25], [12, 982, 512, -39], [13, 905, 508, -14], [14, 936, 505, -30], [15, 958, 507, -45], [16, 977, 509, -55], [17, 899, 503, -41], [18, 926, 500, -54], [19, 944, 501, -62], [20, 960, 503, -67]]) 
                    HandOneLandMarksDict[61]= np.array([[0, 822, 506, 0], [1, 841, 526, 9], [2, 868, 527, 17], [3, 885, 524, 16], [4, 899, 523, 15], [5, 906, 519, 36], [6, 935, 515, 24], [7, 955, 514, 7], [8, 973, 513, -6], [9, 908, 514, 13], [10, 939, 511, 1], [11, 962, 512, -16], [12, 982, 512, -30], [13, 905, 509, -13], [14, 936, 506, -27], [15, 958, 508, -41], [16, 977, 509, -52], [17, 899, 504, -42], [18, 926, 500, -54], [19, 944, 502, -62], [20, 960, 504, -68]]) 
                    HandOneLandMarksDict[62]= np.array([[0, 821, 506, 0], [1, 840, 526, 5], [2, 868, 529, 9], [3, 886, 525, 7], [4, 901, 524, 5], [5, 905, 521, 29], [6, 934, 517, 14], [7, 955, 516, -4], [8, 973, 515, -19], [9, 907, 516, 7], [10, 938, 513, -6], [11, 962, 512, -26], [12, 983, 512, -41], [13, 903, 510, -17], [14, 935, 507, -33], [15, 956, 508, -48], [16, 976, 508, -60], [17, 896, 504, -44], [18, 922, 500, -58], [19, 938, 500, -66], [20, 953, 502, -73]]) 
                    HandOneLandMarksDict[63]= np.array([[0, 820, 506, 0], [1, 839, 525, 5], [2, 868, 528, 12], [3, 887, 524, 12], [4, 902, 524, 11], [5, 905, 520, 31], [6, 934, 518, 16], [7, 955, 517, -1], [8, 973, 516, -15], [9, 906, 515, 10], [10, 938, 513, -3], [11, 961, 512, -23], [12, 982, 512, -38], [13, 903, 510, -13], [14, 935, 507, -29], [15, 956, 507, -45], [16, 975, 507, -57], [17, 896, 504, -39], [18, 920, 499, -54], [19, 936, 499, -62], [20, 950, 499, -69]]) 
                    HandOneLandMarksDict[64]= np.array([[0, 819, 507, 0], [1, 838, 526, 3], [2, 865, 529, 7], [3, 881, 525, 4], [4, 895, 524, 2], [5, 905, 520, 33], [6, 933, 517, 18], [7, 954, 516, 0], [8, 973, 516, -15], [9, 906, 515, 13], [10, 937, 513, 0], [11, 960, 513, -20], [12, 981, 513, -35], [13, 904, 510, -11], [14, 935, 507, -26], [15, 956, 509, -40], [16, 976, 510, -50], [17, 898, 504, -38], [18, 924, 500, -50], [19, 941, 501, -56], [20, 956, 503, -61]]) 
                    HandOneLandMarksDict[65]= np.array([[0, 819, 506, 0], [1, 836, 526, 8], [2, 864, 529, 16], [3, 882, 526, 18], [4, 896, 526, 18], [5, 904, 522, 33], [6, 932, 519, 20], [7, 953, 518, 4], [8, 971, 517, -9], [9, 905, 517, 11], [10, 937, 514, 0], [11, 961, 514, -18], [12, 982, 514, -32], [13, 903, 511, -13], [14, 934, 507, -27], [15, 956, 508, -42], [16, 975, 509, -53], [17, 896, 505, -40], [18, 922, 501, -53], [19, 939, 501, -61], [20, 955, 503, -67]]) 
                    HandOneLandMarksDict[66]= np.array([[0, 817, 505, 0], [1, 834, 526, 7], [2, 862, 530, 16], [3, 880, 527, 17], [4, 894, 527, 17], [5, 902, 522, 35], [6, 932, 518, 22], [7, 952, 518, 5], [8, 971, 516, -8], [9, 904, 516, 12], [10, 937, 514, -1], [11, 961, 514, -20], [12, 982, 514, -35], [13, 902, 510, -13], [14, 935, 508, -31], [15, 959, 509, -48], [16, 979, 509, -60], [17, 896, 504, -41], [18, 925, 500, -58], [19, 944, 501, -68], [20, 962, 503, -76]]) 
                    HandOneLandMarksDict[67]= np.array([[0, 815, 503, 0], [1, 833, 524, 10], [2, 861, 528, 19], [3, 878, 526, 20], [4, 892, 526, 20], [5, 903, 519, 43], [6, 932, 515, 32], [7, 953, 514, 15], [8, 972, 513, 0], [9, 905, 515, 19], [10, 937, 512, 7], [11, 960, 513, -10], [12, 981, 513, -25], [13, 903, 509, -9], [14, 935, 506, -23], [15, 957, 508, -37], [16, 977, 509, -47], [17, 897, 504, -39], [18, 925, 500, -53], [19, 944, 501, -60], [20, 961, 503, -66]]) 
                    HandOneLandMarksDict[68]= np.array([[0, 816, 505, 0], [1, 837, 526, 12], [2, 864, 529, 22], [3, 882, 526, 22], [4, 898, 524, 22], [5, 904, 518, 48], [6, 932, 514, 37], [7, 953, 514, 19], [8, 971, 514, 4], [9, 906, 514, 24], [10, 937, 511, 12], [11, 959, 512, -5], [12, 980, 514, -19], [13, 904, 509, -5], [14, 935, 506, -18], [15, 956, 507, -32], [16, 975, 509, -41], [17, 898, 504, -36], [18, 925, 500, -49], [19, 944, 501, -55], [20, 960, 503, -61]]) 
                    HandOneLandMarksDict[69] = np.array([[0, 818, 504, 0], [1, 837, 526, 12], [2, 865, 529, 23], [3, 883, 526, 26], [4, 898, 525, 27], [5, 905, 520, 47], [6, 932, 517, 38], [7, 952, 517, 23], [8, 969, 516, 10], [9, 907, 515, 23], [10, 938, 513, 13], [11, 960, 514, -3], [12, 980, 514, -16], [13, 905, 510, -5], [14, 936, 507, -17], [15, 958, 508, -32], [16, 977, 509, -44], [17, 899, 505, -35], [18, 926, 501, -47], [19, 944, 502, -56], [20, 960, 503, -64]]) 
                    HandOneLandMarksDict[70] = np.array([[0, 817, 507, 0], [1, 837, 527, 14], [2, 863, 529, 24], [3, 881, 527, 25], [4, 895, 527, 26], [5, 902, 522, 46], [6, 931, 519, 36], [7, 951, 519, 21], [8, 969, 518, 8], [9, 905, 517, 21], [10, 937, 514, 11], [11, 959, 515, -5], [12, 979, 516, -18], [13, 903, 512, -8], [14, 935, 508, -20], [15, 957, 509, -34], [16, 975, 510, -45], [17, 897, 506, -38], [18, 925, 502, -51], [19, 943, 502, -59], [20, 960, 503, -65]]) 
                    HandOneLandMarksDict[71] = np.array([[0, 817, 506, 0], [1, 836, 526, 14], [2, 863, 530, 26], [3, 882, 527, 29], [4, 897, 526, 31], [5, 901, 523, 49], [6, 930, 521, 41], [7, 949, 521, 27], [8, 967, 520, 15], [9, 904, 518, 24], [10, 937, 516, 15], [11, 959, 517, 0], [12, 977, 517, -11], [13, 903, 511, -4], [14, 935, 509, -16], [15, 957, 510, -29], [16, 975, 511, -39], [17, 897, 505, -34], [18, 925, 501, -46], [19, 944, 502, -53], [20, 960, 503, -60]]) 
                    HandOneLandMarksDict[72] = np.array([[0, 816, 504, 0], [1, 835, 525, 14], [2, 863, 529, 28], [3, 881, 527, 31], [4, 896, 526, 34], [5, 901, 522, 52], [6, 929, 520, 45], [7, 948, 520, 32], [8, 966, 519, 19], [9, 903, 517, 28], [10, 935, 514, 20], [11, 957, 515, 4], [12, 976, 515, -7], [13, 902, 510, 0], [14, 933, 507, -11], [15, 954, 508, -24], [16, 972, 509, -34], [17, 896, 504, -30], [18, 923, 501, -42], [19, 941, 501, -49], [20, 957, 502, -55]]) 
                    HandOneLandMarksDict[73] = np.array([[0, 812, 506, 0], [1, 833, 525, 22], [2, 861, 529, 39], [3, 880, 527, 45], [4, 896, 528, 51], [5, 898, 522, 64], [6, 927, 519, 61], [7, 947, 519, 50], [8, 964, 518, 40], [9, 901, 517, 38], [10, 932, 514, 35], [11, 953, 515, 21], [12, 972, 516, 10], [13, 899, 511, 8], [14, 931, 508, 2], [15, 952, 508, -8], [16, 969, 509, -16], [17, 894, 504, -22], [18, 922, 500, -29], [19, 940, 501, -34], [20, 956, 503, -38]]) 
                    HandOneLandMarksDict[74] = np.array([[0, 816, 504, 0], [1, 837, 525, 27], [2, 864, 529, 43], [3, 883, 528, 47], [4, 899, 526, 50], [5, 901, 521, 65], [6, 929, 517, 62], [7, 948, 517, 50], [8, 965, 517, 38], [9, 903, 516, 35], [10, 934, 514, 32], [11, 955, 515, 19], [12, 972, 517, 6], [13, 901, 510, 1], [14, 932, 508, -4], [15, 952, 510, -13], [16, 969, 511, -23], [17, 895, 504, -33], [18, 923, 501, -40], [19, 941, 502, -45], [20, 957, 504, -50]]) 
                    HandOneLandMarksDict[75] = np.array([[0, 815, 505, 0], [1, 835, 524, 28], [2, 860, 528, 49], [3, 879, 527, 58], [4, 896, 526, 66], [5, 901, 519, 79], [6, 928, 516, 83], [7, 947, 515, 75], [8, 964, 514, 65], [9, 904, 515, 51], [10, 934, 512, 54], [11, 954, 513, 42], [12, 971, 513, 31], [13, 903, 509, 17], [14, 933, 506, 15], [15, 952, 508, 6], [16, 969, 509, -1], [17, 898, 503, -15], [18, 925, 500, -20], [19, 942, 502, -23], [20, 958, 504, -27]]) 
                    HandOneLandMarksDict[76] = np.array([[0, 816, 506, 0], [1, 837, 526, 13], [2, 863, 529, 23], [3, 882, 525, 23], [4, 897, 525, 23], [5, 901, 520, 45], [6, 929, 515, 37], [7, 948, 514, 22], [8, 965, 513, 10], [9, 902, 514, 22], [10, 934, 510, 13], [11, 955, 511, -2], [12, 974, 511, -14], [13, 899, 508, -5], [14, 930, 504, -16], [15, 950, 505, -28], [16, 967, 505, -37], [17, 892, 502, -33], [18, 918, 498, -45], [19, 935, 498, -51], [20, 950, 500, -56]]) 
                    HandOneLandMarksDict[77] = np.array([[0, 815, 504, 0], [1, 834, 525, 13], [2, 861, 527, 25], [3, 881, 524, 28], [4, 897, 524, 30], [5, 899, 518, 47], [6, 927, 514, 39], [7, 947, 514, 25], [8, 965, 513, 13], [9, 901, 513, 23], [10, 933, 510, 15], [11, 955, 510, 0], [12, 975, 511, -13], [13, 899, 507, -4], [14, 931, 504, -16], [15, 952, 505, -30], [16, 971, 505, -40], [17, 893, 502, -32], [18, 920, 498, -46], [19, 938, 498, -55], [20, 955, 500, -62]]) 
                    HandOneLandMarksDict[78] = np.array([[0, 812, 505, 0], [1, 832, 525, 22], [2, 860, 527, 39], [3, 879, 525, 45], [4, 896, 525, 50], [5, 896, 517, 64], [6, 925, 513, 60], [7, 945, 512, 48], [8, 962, 512, 38], [9, 899, 512, 36], [10, 931, 509, 32], [11, 954, 510, 19], [12, 973, 511, 7], [13, 897, 506, 4], [14, 930, 503, -3], [15, 952, 505, -15], [16, 970, 506, -25], [17, 892, 500, -27], [18, 920, 496, -37], [19, 939, 497, -43], [20, 956, 499, -49]]) 
                    HandOneLandMarksDict[79] = np.array([[0, 815, 504, 0], [1, 833, 525, 14], [2, 862, 527, 26], [3, 882, 523, 30], [4, 898, 523, 33], [5, 900, 518, 48], [6, 927, 516, 42], [7, 946, 517, 30], [8, 962, 517, 18], [9, 902, 513, 25], [10, 934, 510, 18], [11, 956, 511, 3], [12, 975, 511, -8], [13, 900, 506, -2], [14, 932, 503, -13], [15, 954, 504, -27], [16, 973, 505, -38], [17, 893, 500, -31], [18, 921, 496, -43], [19, 940, 496, -52], [20, 957, 498, -60]]) 
                    HandOneLandMarksDict[80] = np.array([[0, 814, 503, 0], [1, 832, 524, 9], [2, 859, 527, 19], [3, 879, 524, 21], [4, 895, 523, 22], [5, 900, 517, 42], [6, 928, 515, 33], [7, 948, 515, 19], [8, 965, 515, 7], [9, 901, 512, 20], [10, 934, 509, 12], [11, 956, 510, -3], [12, 976, 510, -15], [13, 899, 505, -5], [14, 931, 503, -16], [15, 952, 503, -30], [16, 970, 503, -40], [17, 891, 499, -33], [18, 918, 495, -45], [19, 935, 495, -52], [20, 951, 496, -59]]) 
                    HandOneLandMarksDict[81] = np.array([[0, 813, 502, 0], [1, 832, 523, 13], [2, 859, 527, 24], [3, 879, 524, 27], [4, 896, 523, 29], [5, 899, 517, 47], [6, 927, 514, 40], [7, 947, 513, 27], [8, 964, 512, 15], [9, 900, 512, 25], [10, 933, 509, 17], [11, 955, 509, 2], [12, 975, 508, -10], [13, 897, 505, -1], [14, 930, 503, -12], [15, 952, 503, -26], [16, 970, 502, -37], [17, 891, 497, -29], [18, 918, 494, -41], [19, 936, 494, -48], [20, 952, 495, -55]]) 
                    HandOneLandMarksDict[82] = np.array([[0, 810, 500, 0], [1, 829, 522, 6], [2, 857, 526, 14], [3, 877, 522, 15], [4, 895, 522, 16], [5, 897, 515, 38], [6, 927, 513, 27], [7, 947, 513, 12], [8, 964, 512, 0], [9, 899, 510, 17], [10, 932, 508, 6], [11, 956, 508, -10], [12, 976, 507, -24], [13, 896, 504, -8], [14, 929, 501, -23], [15, 951, 502, -38], [16, 970, 502, -49], [17, 888, 497, -35], [18, 917, 494, -50], [19, 935, 494, -60], [20, 951, 496, -67]]) 
                    HandOneLandMarksDict[83] = np.array([[0, 809, 499, 0], [1, 829, 521, 16], [2, 858, 525, 28], [3, 878, 523, 31], [4, 896, 524, 34], [5, 897, 515, 49], [6, 927, 513, 42], [7, 947, 513, 29], [8, 965, 513, 18], [9, 899, 510, 24], [10, 932, 508, 17], [11, 955, 508, 2], [12, 975, 508, -11], [13, 896, 503, -4], [14, 929, 501, -14], [15, 952, 502, -28], [16, 971, 501, -40], [17, 889, 496, -33], [18, 917, 493, -45], [19, 936, 493, -53], [20, 953, 494, -61]]) 
                    HandOneLandMarksDict[84] = np.array([[0, 810, 500, 0], [1, 830, 521, 3], [2, 858, 524, 9], [3, 880, 521, 8], [4, 898, 523, 8], [5, 898, 516, 38], [6, 927, 514, 26], [7, 947, 514, 10], [8, 964, 515, -2], [9, 899, 510, 18], [10, 932, 508, 6], [11, 955, 509, -10], [12, 975, 509, -23], [13, 897, 504, -5], [14, 930, 502, -20], [15, 952, 502, -34], [16, 971, 502, -44], [17, 891, 497, -31], [18, 919, 494, -46], [19, 937, 494, -55], [20, 954, 495, -61]]) 
                    HandOneLandMarksDict[85] = np.array([[0, 810, 498, 0], [1, 829, 520, 8], [2, 858, 524, 16], [3, 878, 521, 17], [4, 895, 522, 18], [5, 897, 515, 40], [6, 926, 512, 29], [7, 946, 512, 14], [8, 963, 512, 1], [9, 899, 509, 19], [10, 931, 506, 7], [11, 954, 507, -8], [12, 974, 507, -21], [13, 896, 502, -7], [14, 929, 500, -21], [15, 951, 500, -35], [16, 970, 501, -45], [17, 890, 495, -34], [18, 918, 491, -49], [19, 936, 492, -58], [20, 953, 493, -65]]) 
                    HandOneLandMarksDict[86] = np.array([[0, 810, 497, 0], [1, 831, 518, 12], [2, 860, 521, 22], [3, 882, 517, 24], [4, 899, 517, 25], [5, 897, 512, 43], [6, 927, 510, 35], [7, 946, 511, 21], [8, 963, 511, 10], [9, 899, 507, 20], [10, 932, 505, 11], [11, 955, 505, -3], [12, 975, 505, -15], [13, 895, 500, -6], [14, 929, 498, -18], [15, 950, 498, -31], [16, 969, 498, -41], [17, 889, 493, -35], [18, 917, 489, -47], [19, 935, 489, -55], [20, 951, 490, -62]]) 
                    HandOneLandMarksDict[87] = np.array([[0, 811, 494, 0], [1, 831, 517, 13], [2, 859, 520, 24], [3, 879, 517, 26], [4, 897, 518, 29], [5, 899, 510, 49], [6, 928, 506, 42], [7, 947, 506, 30], [8, 965, 506, 18], [9, 901, 505, 25], [10, 933, 502, 18], [11, 955, 502, 4], [12, 975, 503, -7], [13, 898, 499, -2], [14, 930, 496, -12], [15, 952, 497, -24], [16, 970, 497, -34], [17, 891, 492, -31], [18, 919, 488, -42], [19, 937, 489, -49], [20, 953, 491, -55]]) 
                    HandOneLandMarksDict[88] = np.array([[0, 810, 496, 0], [1, 830, 517, 12], [2, 858, 520, 23], [3, 879, 517, 25], [4, 897, 518, 27], [5, 898, 509, 48], [6, 927, 506, 40], [7, 947, 506, 27], [8, 964, 507, 15], [9, 899, 504, 25], [10, 932, 500, 17], [11, 955, 502, 3], [12, 975, 502, -7], [13, 897, 498, -2], [14, 930, 494, -13], [15, 951, 495, -24], [16, 970, 496, -33], [17, 890, 492, -31], [18, 918, 487, -42], [19, 935, 488, -48], [20, 951, 490, -53]]) 
                    HandOneLandMarksDict[89] = np.array([[0, 809, 494, 0], [1, 830, 516, 15], [2, 859, 519, 29], [3, 881, 517, 34], [4, 899, 518, 38], [5, 897, 508, 57], [6, 927, 506, 51], [7, 947, 506, 37], [8, 965, 506, 25], [9, 899, 503, 33], [10, 931, 501, 26], [11, 954, 502, 10], [12, 974, 503, -2], [13, 897, 498, 4], [14, 930, 495, -6], [15, 952, 496, -18], [16, 971, 497, -28], [17, 891, 491, -26], [18, 920, 489, -37], [19, 940, 490, -45], [20, 957, 491, -50]]) 
                    HandOneLandMarksDict[90] = np.array([[0, 808, 493, 0], [1, 830, 516, 26], [2, 860, 518, 45], [3, 881, 516, 53], [4, 899, 517, 61], [5, 896, 506, 71], [6, 925, 503, 71], [7, 945, 503, 61], [8, 963, 504, 51], [9, 898, 501, 42], [10, 931, 499, 40], [11, 954, 501, 27], [12, 974, 502, 16], [13, 896, 496, 8], [14, 930, 493, 1], [15, 952, 495, -9], [16, 971, 497, -19], [17, 890, 490, -25], [18, 920, 487, -33], [19, 939, 488, -39], [20, 955, 490, -44]]) 
                    HandOneLandMarksDict[91] = np.array([[0, 809, 494, 0], [1, 830, 516, 19], [2, 860, 518, 36], [3, 881, 515, 43], [4, 899, 516, 49], [5, 898, 506, 64], [6, 927, 504, 62], [7, 947, 504, 51], [8, 964, 504, 40], [9, 900, 502, 39], [10, 932, 500, 35], [11, 955, 501, 21], [12, 974, 502, 8], [13, 898, 496, 8], [14, 931, 493, 0], [15, 953, 495, -12], [16, 972, 496, -22], [17, 892, 489, -22], [18, 922, 486, -32], [19, 941, 488, -39], [20, 958, 490, -45]]) 
                    HandOneLandMarksDict[92] = np.array([[0, 810, 493, 0], [1, 831, 515, 24], [2, 861, 517, 43], [3, 882, 514, 50], [4, 900, 515, 58], [5, 899, 506, 69], [6, 927, 504, 69], [7, 947, 504, 59], [8, 964, 504, 48], [9, 901, 502, 41], [10, 933, 499, 41], [11, 955, 500, 29], [12, 975, 501, 18], [13, 899, 496, 9], [14, 932, 493, 5], [15, 954, 494, -4], [16, 973, 495, -12], [17, 894, 490, -23], [18, 924, 487, -29], [19, 943, 488, -34], [20, 960, 490, -38]]) 
                    HandOneLandMarksDict[93] = np.array([[0, 809, 493, 0], [1, 829, 515, 12], [2, 859, 518, 26], [3, 880, 515, 32], [4, 898, 517, 37], [5, 897, 506, 52], [6, 927, 503, 46], [7, 947, 502, 35], [8, 965, 501, 23], [9, 899, 501, 29], [10, 933, 498, 22], [11, 956, 499, 8], [12, 976, 500, -4], [13, 897, 495, 1], [14, 930, 492, -10], [15, 953, 494, -24], [16, 972, 495, -34], [17, 890, 488, -27], [18, 919, 485, -41], [19, 938, 486, -49], [20, 955, 487, -55]]) 
                    HandOneLandMarksDict[94] = np.array([[0, 809, 490, 0], [1, 829, 512, 12], [2, 859, 517, 24], [3, 880, 515, 26], [4, 897, 516, 29], [5, 897, 506, 50], [6, 927, 503, 42], [7, 947, 502, 29], [8, 964, 502, 17], [9, 899, 500, 27], [10, 932, 497, 18], [11, 955, 497, 2], [12, 976, 497, -9], [13, 896, 493, 0], [14, 930, 490, -12], [15, 952, 491, -24], [16, 971, 491, -33], [17, 890, 487, -29], [18, 918, 483, -40], [19, 937, 484, -46], [20, 952, 486, -50]]) 
                    HandOneLandMarksDict[95] = np.array([[0, 810, 491, 0], [1, 832, 513, 27], [2, 861, 515, 45], [3, 882, 513, 51], [4, 900, 515, 55], [5, 899, 506, 67], [6, 928, 503, 65], [7, 948, 503, 54], [8, 965, 503, 43], [9, 900, 501, 36], [10, 934, 498, 32], [11, 957, 498, 17], [12, 977, 498, 4], [13, 897, 494, 0], [14, 931, 492, -7], [15, 954, 492, -20], [16, 973, 492, -32], [17, 890, 487, -34], [18, 919, 483, -45], [19, 938, 483, -53], [20, 955, 484, -61]]) 
                    HandOneLandMarksDict[96] = np.array([[0, 810, 491, 0], [1, 829, 512, 17], [2, 856, 516, 28], [3, 876, 513, 30], [4, 894, 515, 31], [5, 898, 506, 50], [6, 929, 503, 42], [7, 949, 502, 30], [8, 966, 501, 18], [9, 900, 501, 23], [10, 934, 498, 16], [11, 957, 498, 1], [12, 977, 498, -11], [13, 897, 495, -6], [14, 932, 492, -17], [15, 954, 492, -30], [16, 973, 492, -41], [17, 890, 488, -37], [18, 919, 484, -49], [19, 937, 484, -56], [20, 953, 485, -62]]) 
                    HandOneLandMarksDict[97] = np.array([[0, 811, 489, 0], [1, 830, 510, 8], [2, 860, 512, 18], [3, 882, 508, 20], [4, 899, 508, 23], [5, 901, 504, 42], [6, 931, 500, 34], [7, 951, 500, 21], [8, 968, 500, 10], [9, 902, 499, 22], [10, 936, 495, 14], [11, 958, 496, 0], [12, 978, 496, -12], [13, 899, 492, -2], [14, 932, 489, -13], [15, 954, 491, -26], [16, 973, 491, -36], [17, 892, 485, -27], [18, 920, 482, -39], [19, 938, 482, -47], [20, 954, 483, -53]]) 
                    HandOneLandMarksDict[98] = np.array([[0, 810, 491, 0], [1, 831, 511, 13], [2, 860, 515, 24], [3, 881, 512, 26], [4, 898, 512, 27], [5, 899, 504, 46], [6, 930, 501, 38], [7, 950, 502, 25], [8, 967, 502, 13], [9, 901, 499, 22], [10, 935, 496, 13], [11, 958, 497, -1], [12, 978, 498, -13], [13, 897, 493, -6], [14, 932, 490, -18], [15, 954, 491, -30], [16, 972, 492, -41], [17, 890, 486, -35], [18, 919, 482, -48], [19, 937, 483, -55], [20, 953, 484, -61]]) 
                    HandOneLandMarksDict[99] = np.array([[0, 812, 491, 0], [1, 833, 513, 24], [2, 862, 515, 39], [3, 882, 511, 44], [4, 899, 511, 48], [5, 901, 504, 57], [6, 931, 501, 53], [7, 950, 502, 43], [8, 967, 501, 33], [9, 902, 499, 28], [10, 936, 496, 24], [11, 959, 497, 11], [12, 979, 497, 0], [13, 899, 493, -3], [14, 933, 490, -11], [15, 954, 490, -22], [16, 973, 491, -31], [17, 892, 487, -35], [18, 920, 483, -44], [19, 938, 483, -50], [20, 954, 484, -55]]) 
                    HandOneLandMarksDict[100] = np.array([[0, 813, 491, 0], [1, 834, 512, 10], [2, 863, 515, 21], [3, 883, 511, 25], [4, 900, 512, 28], [5, 902, 503, 47], [6, 932, 501, 39], [7, 951, 501, 27], [8, 969, 501, 16], [9, 904, 498, 25], [10, 937, 495, 16], [11, 960, 496, 1], [12, 980, 497, -10], [13, 901, 492, -1], [14, 934, 490, -14], [15, 956, 490, -28], [16, 975, 491, -39], [17, 894, 486, -29], [18, 922, 483, -42], [19, 940, 483, -51], [20, 957, 483, -58]]) 
                    HandOneLandMarksDict[101] = np.array([[0, 813, 491, 0], [1, 834, 512, 29], [2, 863, 515, 47], [3, 883, 512, 53], [4, 900, 512, 57], [5, 901, 504, 65], [6, 931, 501, 63], [7, 951, 501, 54], [8, 968, 501, 44], [9, 903, 499, 33], [10, 937, 495, 29], [11, 959, 496, 17], [12, 978, 498, 5], [13, 900, 493, -2], [14, 934, 489, -10], [15, 956, 491, -21], [16, 974, 492, -31], [17, 894, 487, -38], [18, 923, 482, -47], [19, 941, 483, -53], [20, 956, 485, -59]]) 
                    HandOneLandMarksDict[102] = np.array([[0, 813, 489, 0], [1, 834, 511, 33], [2, 862, 513, 51], [3, 882, 510, 56], [4, 899, 511, 60], [5, 903, 504, 69], [6, 932, 500, 69], [7, 951, 499, 61], [8, 968, 499, 52], [9, 904, 499, 34], [10, 938, 495, 33], [11, 961, 495, 21], [12, 980, 495, 9], [13, 901, 493, -3], [14, 935, 489, -9], [15, 957, 490, -20], [16, 975, 490, -31], [17, 894, 487, -40], [18, 922, 483, -49], [19, 941, 483, -54], [20, 957, 484, -61]]) 
                    HandOneLandMarksDict[103] = np.array([[0, 814, 490, 0], [1, 834, 510, 0], [2, 862, 514, 1], [3, 883, 508, -1], [4, 902, 508, -3], [5, 903, 503, 30], [6, 933, 499, 16], [7, 953, 498, 0], [8, 970, 498, -13], [9, 904, 497, 13], [10, 938, 494, -1], [11, 960, 494, -18], [12, 980, 494, -31], [13, 901, 491, -10], [14, 934, 488, -28], [15, 956, 489, -43], [16, 975, 488, -53], [17, 893, 485, -34], [18, 920, 482, -52], [19, 938, 481, -62], [20, 955, 481, -69]]) 
                    HandOneLandMarksDict[104] = np.array([[0, 814, 489, 0], [1, 835, 510, 31], [2, 864, 512, 49], [3, 884, 508, 54], [4, 902, 509, 57], [5, 903, 502, 68], [6, 932, 498, 66], [7, 952, 497, 57], [8, 969, 497, 47], [9, 904, 496, 33], [10, 938, 493, 29], [11, 961, 493, 16], [12, 980, 494, 3], [13, 901, 490, -5], [14, 935, 487, -14], [15, 957, 488, -26], [16, 975, 488, -37], [17, 894, 485, -43], [18, 923, 480, -54], [19, 941, 481, -61], [20, 957, 482, -69]]) 
                    HandOneLandMarksDict[105] = np.array([[0, 813, 491, 0], [1, 832, 510, -6], [2, 861, 513, -5], [3, 882, 506, -10], [4, 901, 505, -13], [5, 902, 502, 24], [6, 932, 498, 6], [7, 953, 497, -12], [8, 971, 497, -27], [9, 903, 496, 8], [10, 937, 492, -10], [11, 960, 493, -28], [12, 981, 494, -41], [13, 899, 490, -12], [14, 934, 486, -35], [15, 956, 488, -50], [16, 975, 489, -59], [17, 891, 485, -35], [18, 921, 481, -56], [19, 939, 482, -66], [20, 955, 483, -71]]) 
                    HandOneLandMarksDict[106] = np.array([[0, 814, 491, 0], [1, 835, 511, 31], [2, 864, 513, 49], [3, 885, 508, 54], [4, 902, 506, 58], [5, 903, 502, 61], [6, 933, 499, 59], [7, 952, 500, 51], [8, 969, 500, 41], [9, 904, 497, 28], [10, 938, 493, 24], [11, 961, 494, 12], [12, 980, 495, 0], [13, 901, 491, -8], [14, 935, 487, -15], [15, 956, 488, -25], [16, 974, 489, -35], [17, 893, 485, -43], [18, 922, 482, -52], [19, 940, 483, -58], [20, 956, 484, -65]]) 
                    HandOneLandMarksDict[107] = np.array([[0, 815, 490, 0], [1, 836, 511, 31], [2, 863, 514, 49], [3, 883, 511, 54], [4, 900, 511, 57], [5, 904, 502, 63], [6, 933, 498, 61], [7, 953, 498, 52], [8, 970, 497, 42], [9, 905, 497, 29], [10, 939, 493, 23], [11, 962, 494, 9], [12, 982, 495, -2], [13, 902, 491, -8], [14, 936, 488, -18], [15, 958, 489, -32], [16, 977, 490, -43], [17, 894, 485, -44], [18, 923, 482, -56], [19, 942, 482, -64], [20, 959, 484, -72]]) 
                    HandOneLandMarksDict[108] = np.array([[0, 813, 487, 0], [1, 833, 508, 45], [2, 859, 511, 72], [3, 879, 506, 83], [4, 897, 505, 92], [5, 902, 502, 95], [6, 931, 497, 105], [7, 951, 496, 102], [8, 968, 495, 95], [9, 905, 496, 55], [10, 939, 493, 61], [11, 961, 493, 52], [12, 980, 494, 41], [13, 903, 490, 12], [14, 937, 487, 10], [15, 957, 488, 0], [16, 975, 489, -8], [17, 897, 484, -30], [18, 926, 481, -34], [19, 944, 482, -38], [20, 960, 483, -44]]) 
                    HandOneLandMarksDict[109] = np.array([[0, 813, 490, 0], [1, 835, 511, 20], [2, 864, 514, 33], [3, 885, 509, 36], [4, 902, 508, 38], [5, 902, 502, 54], [6, 931, 498, 46], [7, 951, 497, 34], [8, 969, 497, 21], [9, 904, 497, 25], [10, 937, 493, 16], [11, 959, 493, 1], [12, 979, 494, -11], [13, 901, 491, -7], [14, 934, 487, -19], [15, 955, 488, -31], [16, 974, 488, -41], [17, 894, 485, -40], [18, 922, 481, -52], [19, 940, 482, -59], [20, 956, 483, -65]]) 
                    HandOneLandMarksDict[110]= np.array([[0, 815, 490, 0], [1, 834, 510, 15], [2, 860, 514, 27], [3, 880, 509, 28], [4, 897, 506, 29], [5, 903, 503, 51], [6, 932, 498, 44], [7, 951, 498, 31], [8, 968, 498, 19], [9, 905, 498, 24], [10, 938, 494, 16], [11, 960, 494, 1], [12, 980, 494, -12], [13, 903, 492, -6], [14, 935, 488, -18], [15, 957, 489, -31], [16, 975, 489, -42], [17, 896, 485, -37], [18, 924, 481, -51], [19, 943, 481, -59], [20, 959, 482, -65]]) 
                    HandOneLandMarksDict[111]= np.array([[0, 815, 490, 0], [1, 837, 511, 28], [2, 865, 512, 43], [3, 886, 508, 47], [4, 903, 507, 49], [5, 903, 502, 61], [6, 933, 497, 58], [7, 952, 497, 47], [8, 970, 497, 36], [9, 905, 497, 29], [10, 938, 493, 23], [11, 961, 493, 9], [12, 980, 494, -3], [13, 901, 491, -6], [14, 935, 487, -17], [15, 956, 487, -29], [16, 974, 488, -39], [17, 894, 485, -43], [18, 923, 480, -54], [19, 941, 481, -61], [20, 957, 482, -68]]) 
                    HandOneLandMarksDict[112]= np.array([[0, 814, 489, 0], [1, 836, 511, 21], [2, 865, 513, 35], [3, 886, 508, 38], [4, 903, 505, 40], [5, 903, 500, 56], [6, 933, 496, 50], [7, 953, 496, 37], [8, 971, 496, 25], [9, 905, 495, 27], [10, 938, 491, 19], [11, 961, 492, 5], [12, 980, 493, -7], [13, 902, 489, -5], [14, 935, 486, -17], [15, 956, 487, -28], [16, 974, 488, -37], [17, 895, 484, -39], [18, 924, 480, -51], [19, 942, 481, -58], [20, 958, 483, -64]]) 
                    HandOneLandMarksDict[113]= np.array([[0, 815, 488, 0], [1, 836, 510, 27], [2, 864, 512, 42], [3, 883, 506, 45], [4, 899, 503, 46], [5, 904, 501, 62], [6, 933, 496, 59], [7, 952, 495, 48], [8, 969, 495, 36], [9, 905, 496, 29], [10, 938, 490, 23], [11, 961, 491, 9], [12, 980, 491, -3], [13, 902, 489, -7], [14, 935, 485, -17], [15, 957, 485, -29], [16, 975, 486, -40], [17, 895, 483, -44], [18, 923, 478, -55], [19, 942, 478, -63], [20, 959, 479, -70]]) 
                    HandOneLandMarksDict[114]= np.array([[0, 815, 488, 0], [1, 837, 510, 18], [2, 865, 513, 30], [3, 885, 508, 31], [4, 901, 504, 31], [5, 903, 500, 51], [6, 933, 495, 44], [7, 953, 494, 30], [8, 970, 493, 18], [9, 905, 494, 24], [10, 937, 490, 16], [11, 960, 490, 0], [12, 980, 490, -11], [13, 901, 488, -6], [14, 934, 484, -18], [15, 956, 484, -31], [16, 974, 485, -42], [17, 894, 482, -39], [18, 921, 478, -50], [19, 938, 478, -57], [20, 953, 478, -63]]) 
                    HandOneLandMarksDict[115]= np.array([[0, 815, 487, 0], [1, 835, 508, 37], [2, 861, 510, 59], [3, 879, 507, 67], [4, 895, 505, 73], [5, 903, 500, 81], [6, 932, 495, 85], [7, 952, 494, 77], [8, 969, 493, 67], [9, 906, 495, 44], [10, 939, 490, 46], [11, 961, 491, 33], [12, 980, 490, 21], [13, 904, 488, 4], [14, 937, 485, 0], [15, 958, 485, -12], [16, 976, 486, -22], [17, 898, 482, -35], [18, 927, 477, -42], [19, 945, 478, -47], [20, 962, 479, -53]]) 
                    HandOneLandMarksDict[116]= np.array([[0, 816, 488, 0], [1, 839, 509, 40], [2, 867, 511, 61], [3, 886, 508, 65], [4, 903, 506, 67], [5, 905, 498, 79], [6, 934, 494, 80], [7, 953, 494, 70], [8, 970, 494, 59], [9, 907, 493, 39], [10, 939, 489, 37], [11, 962, 489, 24], [12, 981, 489, 10], [13, 904, 487, -4], [14, 936, 483, -11], [15, 958, 483, -22], [16, 976, 483, -33], [17, 897, 482, -48], [18, 924, 477, -57], [19, 942, 476, -62], [20, 958, 477, -69]]) 
                    HandOneLandMarksDict[117]= np.array([[0, 815, 487, 0], [1, 839, 508, 30], [2, 867, 510, 47], [3, 886, 507, 51], [4, 902, 505, 54], [5, 905, 498, 68], [6, 934, 494, 65], [7, 954, 493, 55], [8, 971, 492, 43], [9, 907, 493, 34], [10, 940, 489, 31], [11, 962, 489, 17], [12, 982, 489, 4], [13, 904, 487, -2], [14, 937, 483, -9], [15, 959, 483, -21], [16, 977, 484, -32], [17, 897, 480, -39], [18, 924, 475, -48], [19, 942, 474, -53], [20, 958, 475, -59]]) 
                    HandOneLandMarksDict[118]= np.array([[0, 814, 486, 0], [1, 837, 508, 54], [2, 864, 510, 83], [3, 883, 507, 93], [4, 900, 506, 101], [5, 904, 498, 95], [6, 933, 493, 101], [7, 953, 491, 96], [8, 971, 490, 86], [9, 905, 493, 48], [10, 939, 488, 51], [11, 962, 488, 39], [12, 981, 487, 26], [13, 903, 487, 0], [14, 936, 482, -3], [15, 957, 482, -13], [16, 976, 482, -25], [17, 896, 481, -47], [18, 924, 475, -53], [19, 942, 475, -58], [20, 959, 475, -65]]) 
                    HandOneLandMarksDict[119] = np.array([[0, 814, 484, 0], [1, 837, 506, 49], [2, 865, 509, 77], [3, 884, 506, 87], [4, 901, 502, 94], [5, 904, 496, 92], [6, 933, 492, 99], [7, 953, 492, 94], [8, 970, 491, 85], [9, 906, 492, 48], [10, 940, 487, 50], [11, 963, 488, 39], [12, 982, 488, 27], [13, 904, 485, 1], [14, 937, 482, -3], [15, 959, 482, -14], [16, 977, 483, -25], [17, 897, 480, -43], [18, 926, 475, -51], [19, 945, 476, -57], [20, 961, 477, -64]]) 
                    HandOneLandMarksDict[120] = np.array([[0, 816, 486, 0], [1, 839, 507, 40], [2, 866, 509, 62], [3, 886, 505, 69], [4, 901, 503, 73], [5, 906, 497, 78], [6, 935, 493, 80], [7, 955, 492, 73], [8, 972, 492, 63], [9, 907, 492, 39], [10, 942, 487, 37], [11, 964, 488, 24], [12, 983, 488, 12], [13, 904, 485, -2], [14, 938, 481, -9], [15, 960, 481, -22], [16, 978, 482, -33], [17, 896, 479, -43], [18, 924, 473, -52], [19, 942, 473, -59], [20, 958, 473, -66]]) 
                    HandOneLandMarksDict[121] = np.array([[0, 815, 487, 0], [1, 838, 508, 16], [2, 866, 510, 26], [3, 886, 506, 26], [4, 903, 504, 25], [5, 904, 498, 47], [6, 934, 493, 36], [7, 954, 492, 21], [8, 972, 492, 8], [9, 905, 493, 20], [10, 939, 488, 7], [11, 962, 488, -10], [12, 981, 488, -24], [13, 902, 486, -11], [14, 936, 482, -27], [15, 957, 482, -42], [16, 977, 482, -53], [17, 896, 480, -44], [18, 923, 474, -60], [19, 942, 473, -69], [20, 959, 474, -75]]) 
                    HandOneLandMarksDict[122] = np.array([[0, 819, 483, 0], [1, 842, 504, 107], [2, 865, 506, 159], [3, 880, 504, 184], [4, 895, 503, 202], [5, 905, 496, 144], [6, 933, 492, 169], [7, 952, 491, 180], [8, 968, 490, 180], [9, 906, 490, 71], [10, 942, 486, 83], [11, 964, 487, 81], [12, 982, 487, 76], [13, 903, 483, 0], [14, 938, 480, -2], [15, 960, 482, -8], [16, 978, 482, -16], [17, 898, 478, -66], [18, 928, 474, -79], [19, 947, 475, -90], [20, 963, 476, -100]]) 
                    HandOneLandMarksDict[123] = np.array([[0, 814, 487, 0], [1, 837, 507, 18], [2, 864, 509, 30], [3, 884, 505, 31], [4, 902, 504, 31], [5, 903, 496, 58], [6, 933, 491, 49], [7, 953, 491, 34], [8, 971, 491, 21], [9, 904, 491, 29], [10, 937, 486, 19], [11, 961, 487, 1], [12, 981, 487, -13], [13, 902, 485, -5], [14, 935, 481, -18], [15, 957, 481, -34], [16, 976, 481, -46], [17, 895, 480, -40], [18, 923, 475, -54], [19, 941, 474, -62], [20, 957, 474, -70]]) 
                    HandOneLandMarksDict[124] = np.array([[0, 815, 485, 0], [1, 839, 507, 72], [2, 866, 508, 108], [3, 885, 507, 121], [4, 901, 505, 131], [5, 904, 497, 111], [6, 933, 492, 123], [7, 952, 491, 122], [8, 969, 491, 115], [9, 905, 491, 54], [10, 939, 487, 59], [11, 962, 487, 48], [12, 981, 487, 36], [13, 902, 485, -3], [14, 936, 481, -7], [15, 957, 481, -18], [16, 976, 481, -30], [17, 895, 479, -57], [18, 924, 474, -66], [19, 942, 474, -73], [20, 958, 475, -81]]) 
                    HandOneLandMarksDict[125] = np.array([[0, 817, 487, 0], [1, 837, 508, 18], [2, 864, 510, 30], [3, 883, 505, 31], [4, 900, 503, 33], [5, 905, 498, 54], [6, 934, 494, 48], [7, 954, 493, 35], [8, 971, 492, 24], [9, 907, 493, 27], [10, 940, 489, 21], [11, 962, 489, 6], [12, 981, 489, -6], [13, 905, 487, -3], [14, 937, 483, -13], [15, 959, 483, -26], [16, 977, 483, -36], [17, 899, 480, -35], [18, 926, 475, -46], [19, 945, 474, -52], [20, 961, 475, -59]]) 
                    HandOneLandMarksDict[126] = np.array([[0, 816, 488, 0], [1, 837, 509, 14], [2, 865, 511, 23], [3, 885, 505, 23], [4, 902, 504, 22], [5, 904, 499, 44], [6, 933, 494, 34], [7, 953, 493, 19], [8, 971, 493, 6], [9, 905, 493, 18], [10, 938, 488, 7], [11, 961, 488, -8], [12, 981, 488, -21], [13, 902, 486, -11], [14, 935, 481, -24], [15, 957, 481, -38], [16, 975, 481, -48], [17, 895, 480, -42], [18, 922, 475, -55], [19, 939, 474, -62], [20, 955, 474, -68]]) 
                    HandOneLandMarksDict[127] = np.array([[0, 817, 488, 0], [1, 839, 510, 30], [2, 867, 511, 47], [3, 886, 507, 51], [4, 903, 506, 54], [5, 905, 499, 64], [6, 934, 494, 61], [7, 953, 493, 51], [8, 971, 493, 39], [9, 907, 494, 30], [10, 939, 489, 24], [11, 962, 489, 10], [12, 981, 489, -2], [13, 903, 487, -7], [14, 936, 483, -16], [15, 958, 483, -28], [16, 977, 483, -40], [17, 897, 481, -44], [18, 924, 475, -54], [19, 943, 475, -62], [20, 959, 476, -69]]) 
                    HandOneLandMarksDict[128] = np.array([[0, 816, 489, 0], [1, 837, 510, 12], [2, 864, 513, 20], [3, 885, 508, 19], [4, 902, 507, 17], [5, 904, 499, 39], [6, 934, 495, 27], [7, 953, 494, 12], [8, 971, 494, 0], [9, 905, 493, 14], [10, 939, 489, 2], [11, 963, 489, -13], [12, 982, 488, -26], [13, 901, 487, -13], [14, 936, 483, -28], [15, 958, 482, -42], [16, 977, 481, -52], [17, 894, 481, -42], [18, 922, 476, -57], [19, 941, 475, -66], [20, 957, 475, -72]]) 
                    HandOneLandMarksDict[129] = np.array([[0, 815, 488, 0], [1, 840, 509, 79], [2, 868, 509, 119], [3, 887, 506, 136], [4, 903, 504, 149], [5, 903, 500, 124], [6, 933, 496, 143], [7, 952, 495, 146], [8, 970, 494, 141], [9, 905, 494, 66], [10, 940, 489, 77], [11, 963, 489, 69], [12, 981, 489, 59], [13, 902, 488, 5], [14, 937, 483, 8], [15, 959, 484, 0], [16, 977, 484, -11], [17, 897, 482, -50], [18, 926, 477, -54], [19, 945, 477, -59], [20, 961, 478, -67]]) 
                    HandOneLandMarksDict[130] = np.array([[0, 814, 489, 0], [1, 836, 510, 30], [2, 863, 512, 47], [3, 883, 508, 51], [4, 900, 505, 54], [5, 903, 500, 68], [6, 933, 495, 67], [7, 952, 494, 57], [8, 969, 494, 46], [9, 905, 495, 34], [10, 938, 490, 30], [11, 961, 490, 17], [12, 980, 490, 5], [13, 902, 488, -3], [14, 936, 484, -11], [15, 957, 484, -22], [16, 975, 484, -32], [17, 895, 483, -41], [18, 924, 477, -50], [19, 941, 477, -56], [20, 957, 478, -62]]) 
                    HandOneLandMarksDict[131] = np.array([[0, 815, 489, 0], [1, 836, 510, 26], [2, 865, 511, 40], [3, 885, 505, 43], [4, 902, 503, 46], [5, 903, 501, 57], [6, 933, 496, 53], [7, 952, 496, 43], [8, 970, 496, 32], [9, 905, 495, 26], [10, 939, 490, 19], [11, 962, 490, 6], [12, 981, 490, -5], [13, 902, 489, -8], [14, 936, 484, -18], [15, 957, 484, -29], [16, 976, 484, -38], [17, 895, 483, -44], [18, 923, 477, -53], [19, 941, 476, -59], [20, 957, 477, -66]]) 
                    HandOneLandMarksDict[132] = np.array([[0, 815, 490, 0], [1, 836, 511, 11], [2, 864, 514, 21], [3, 884, 509, 21], [4, 902, 506, 22], [5, 903, 502, 47], [6, 932, 496, 38], [7, 952, 495, 24], [8, 969, 495, 11], [9, 905, 496, 24], [10, 937, 491, 15], [11, 960, 491, 0], [12, 979, 491, -12], [13, 902, 490, -3], [14, 934, 486, -15], [15, 955, 485, -26], [16, 973, 484, -34], [17, 896, 483, -33], [18, 923, 478, -44], [19, 940, 477, -49], [20, 956, 477, -54]]) 

                    HandTwoLandMarksDict[0] = np.array([[0, 671, 438, 0], [1, 643, 424, 29], [2, 617, 421, 30], [3, 599, 429, 24], [4, 589, 442, 14], [5, 604, 410, 0], [6, 576, 430, -11], [7, 565, 444, -17], [8, 560, 456, -19], [9, 604, 425, -24], [10, 571, 438, -33], [11, 559, 451, -36], [12, 553, 464, -37], [13, 608, 442, -45], [14, 573, 451, -51], [15, 561, 461, -48], [16, 555, 469, -45], [17, 614, 461, -64], [18, 583, 465, -68], [19, 570, 468, -61], [20, 561, 472, -53]]) 
                    HandTwoLandMarksDict[1] = np.array([[0, 670, 439, 0], [1, 644, 424, 30], [2, 619, 421, 32], [3, 600, 429, 27], [4, 591, 442, 17], [5, 606, 411, 4], [6, 577, 430, -6], [7, 566, 444, -12], [8, 561, 456, -14], [9, 605, 424, -20], [10, 571, 437, -29], [11, 559, 450, -32], [12, 553, 464, -32], [13, 608, 441, -42], [14, 573, 450, -48], [15, 560, 460, -44], [16, 554, 469, -42], [17, 614, 461, -60], [18, 583, 465, -64], [19, 571, 469, -56], [20, 562, 473, -48]]) 
                    HandTwoLandMarksDict[2] = np.array([[0, 669, 442, 0], [1, 643, 426, 25], [2, 618, 421, 24], [3, 599, 429, 17], [4, 589, 442, 5], [5, 604, 412, 1], [6, 576, 431, -13], [7, 564, 445, -23], [8, 558, 457, -27], [9, 604, 426, -21], [10, 572, 439, -32], [11, 559, 452, -37], [12, 553, 465, -40], [13, 608, 443, -41], [14, 574, 451, -48], [15, 562, 461, -46], [16, 555, 471, -45], [17, 613, 462, -59], [18, 584, 465, -63], [19, 571, 469, -56], [20, 562, 474, -50]]) 
                    HandTwoLandMarksDict[3] = np.array([[0, 669, 440, 0], [1, 643, 425, 27], [2, 617, 422, 29], [3, 598, 430, 24], [4, 589, 444, 14], [5, 605, 413, 0], [6, 576, 431, -9], [7, 565, 445, -16], [8, 559, 457, -18], [9, 605, 426, -21], [10, 573, 440, -29], [11, 560, 452, -33], [12, 554, 465, -34], [13, 608, 443, -40], [14, 575, 452, -44], [15, 562, 461, -41], [16, 554, 469, -39], [17, 614, 462, -56], [18, 584, 466, -58], [19, 572, 469, -50], [20, 562, 473, -43]]) 
                    HandTwoLandMarksDict[4] = np.array([[0, 670, 440, 0], [1, 644, 425, 28], [2, 619, 422, 28], [3, 600, 430, 21], [4, 591, 443, 10], [5, 606, 411, 1], [6, 577, 430, -13], [7, 565, 444, -22], [8, 560, 456, -25], [9, 605, 425, -23], [10, 572, 437, -33], [11, 560, 451, -37], [12, 555, 465, -38], [13, 609, 442, -44], [14, 574, 450, -50], [15, 562, 460, -46], [16, 556, 469, -43], [17, 615, 461, -62], [18, 585, 464, -65], [19, 572, 468, -57], [20, 563, 471, -49]]) 
                    HandTwoLandMarksDict[5] = np.array([[0, 669, 440, 0], [1, 642, 424, 31], [2, 618, 421, 32], [3, 600, 429, 24], [4, 590, 441, 12], [5, 606, 412, 3], [6, 577, 431, -12], [7, 565, 446, -21], [8, 560, 458, -25], [9, 605, 426, -23], [10, 572, 440, -34], [11, 559, 453, -39], [12, 554, 466, -41], [13, 609, 444, -45], [14, 574, 453, -52], [15, 561, 463, -50], [16, 555, 472, -47], [17, 615, 462, -65], [18, 584, 466, -70], [19, 571, 470, -62], [20, 561, 474, -54]]) 
                    HandTwoLandMarksDict[6] = np.array([[0, 668, 438, 0], [1, 642, 423, 24], [2, 616, 419, 25], [3, 596, 427, 19], [4, 584, 438, 10], [5, 603, 409, 0], [6, 574, 428, -12], [7, 562, 442, -21], [8, 556, 454, -25], [9, 604, 423, -20], [10, 572, 437, -29], [11, 559, 450, -34], [12, 553, 462, -38], [13, 607, 440, -39], [14, 575, 449, -44], [15, 561, 458, -42], [16, 554, 467, -41], [17, 612, 459, -55], [18, 583, 463, -59], [19, 570, 466, -52], [20, 560, 470, -47]]) 
                    HandTwoLandMarksDict[7] = np.array([[0, 667, 436, 0], [1, 640, 422, 23], [2, 613, 419, 22], [3, 593, 429, 16], [4, 583, 442, 6], [5, 602, 408, -1], [6, 573, 427, -13], [7, 562, 441, -22], [8, 557, 452, -26], [9, 603, 423, -21], [10, 570, 437, -30], [11, 559, 450, -34], [12, 553, 461, -37], [13, 606, 440, -38], [14, 573, 450, -42], [15, 561, 459, -38], [16, 555, 466, -36], [17, 611, 458, -53], [18, 583, 462, -54], [19, 570, 465, -46], [20, 561, 468, -39]]) 
                    HandTwoLandMarksDict[8] = np.array([[0, 666, 431, 0], [1, 640, 415, 20], [2, 612, 410, 20], [3, 592, 417, 14], [4, 580, 428, 6], [5, 600, 405, 0], [6, 570, 419, -14], [7, 556, 431, -27], [8, 548, 442, -34], [9, 601, 421, -18], [10, 570, 431, -26], [11, 554, 441, -33], [12, 545, 452, -38], [13, 605, 438, -34], [14, 573, 445, -37], [15, 557, 451, -37], [16, 547, 458, -38], [17, 610, 456, -49], [18, 582, 459, -49], [19, 568, 461, -43], [20, 557, 464, -38]]) 
                    HandTwoLandMarksDict[9] = np.array([[0, 658, 426, 0], [1, 634, 408, 18], [2, 607, 403, 14], [3, 585, 409, 6], [4, 572, 420, -4], [5, 596, 397, -25], [6, 560, 408, -45], [7, 544, 420, -55], [8, 535, 431, -58], [9, 598, 412, -44], [10, 558, 422, -57], [11, 540, 432, -59], [12, 529, 441, -59], [13, 601, 431, -60], [14, 564, 440, -67], [15, 546, 448, -64], [16, 536, 455, -62], [17, 607, 450, -74], [18, 576, 456, -78], [19, 561, 459, -71], [20, 551, 463, -66]]) 
                    HandTwoLandMarksDict[10]= np.array([[0, 658, 423, 0], [1, 632, 404, 19], [2, 604, 399, 13], [3, 584, 407, 4], [4, 571, 419, -8], [5, 594, 393, -23], [6, 559, 400, -44], [7, 541, 410, -56], [8, 529, 420, -62], [9, 595, 410, -45], [10, 556, 416, -58], [11, 535, 423, -64], [12, 521, 431, -67], [13, 599, 429, -63], [14, 562, 436, -71], [15, 544, 444, -72], [16, 532, 450, -73], [17, 605, 449, -78], [18, 576, 453, -82], [19, 561, 456, -76], [20, 551, 458, -71]]) 
                    HandTwoLandMarksDict[11]= np.array([[0, 659, 419, 0], [1, 633, 401, 23], [2, 605, 397, 21], [3, 586, 404, 15], [4, 574, 415, 4], [5, 596, 390, -20], [6, 560, 394, -37], [7, 540, 399, -45], [8, 527, 405, -48], [9, 597, 407, -43], [10, 554, 412, -56], [11, 531, 417, -62], [12, 514, 424, -65], [13, 600, 426, -61], [14, 561, 435, -71], [15, 541, 441, -74], [16, 528, 446, -76], [17, 607, 446, -77], [18, 576, 451, -82], [19, 560, 455, -78], [20, 549, 457, -74]]) 
                    HandTwoLandMarksDict[12]= np.array([[0, 659, 418, 0], [1, 632, 399, 22], [2, 604, 394, 20], [3, 585, 400, 12], [4, 573, 410, 0], [5, 594, 387, -19], [6, 559, 389, -38], [7, 539, 393, -47], [8, 525, 399, -51], [9, 594, 405, -43], [10, 552, 409, -56], [11, 529, 414, -62], [12, 512, 419, -66], [13, 597, 424, -63], [14, 559, 433, -71], [15, 540, 440, -75], [16, 527, 445, -78], [17, 603, 444, -79], [18, 574, 450, -84], [19, 559, 454, -80], [20, 548, 456, -76]]) 
                    HandTwoLandMarksDict[13]= np.array([[0, 659, 415, 0], [1, 631, 396, 23], [2, 604, 391, 20], [3, 585, 398, 11], [4, 573, 408, -1], [5, 593, 385, -20], [6, 558, 385, -40], [7, 538, 389, -50], [8, 525, 394, -54], [9, 593, 402, -44], [10, 551, 405, -58], [11, 527, 409, -64], [12, 511, 415, -68], [13, 596, 422, -65], [14, 558, 430, -74], [15, 538, 437, -76], [16, 526, 441, -78], [17, 603, 442, -82], [18, 573, 448, -87], [19, 558, 452, -82], [20, 547, 453, -77]]) 
                    HandTwoLandMarksDict[14]= np.array([[0, 660, 411, 0], [1, 631, 391, 24], [2, 604, 386, 21], [3, 587, 394, 12], [4, 576, 404, -1], [5, 594, 380, -15], [6, 559, 379, -35], [7, 539, 382, -46], [8, 524, 385, -51], [9, 593, 399, -40], [10, 552, 400, -54], [11, 528, 404, -63], [12, 510, 407, -69], [13, 596, 418, -62], [14, 558, 426, -70], [15, 538, 432, -74], [16, 525, 437, -79], [17, 602, 437, -80], [18, 573, 444, -84], [19, 558, 448, -80], [20, 546, 449, -76]]) 
                    HandTwoLandMarksDict[15]= np.array([[0, 659, 403, 0], [1, 632, 381, 16], [2, 606, 375, 12], [3, 588, 382, 3], [4, 576, 391, -7], [5, 597, 369, -15], [6, 561, 367, -34], [7, 541, 369, -44], [8, 525, 371, -49], [9, 594, 388, -35], [10, 552, 387, -50], [11, 529, 390, -58], [12, 511, 393, -62], [13, 594, 408, -52], [14, 558, 412, -60], [15, 540, 417, -64], [16, 526, 422, -67], [17, 598, 427, -67], [18, 572, 433, -69], [19, 558, 436, -64], [20, 547, 439, -60]]) 
                    HandTwoLandMarksDict[16]= np.array([[0, 656, 393, 0], [1, 632, 370, 16], [2, 606, 362, 12], [3, 587, 368, 2], [4, 576, 378, -10], [5, 598, 356, -23], [6, 562, 352, -42], [7, 542, 353, -51], [8, 527, 355, -56], [9, 594, 374, -44], [10, 553, 372, -59], [11, 529, 373, -67], [12, 511, 375, -72], [13, 595, 394, -61], [14, 559, 399, -71], [15, 539, 404, -76], [16, 524, 407, -81], [17, 598, 414, -76], [18, 572, 420, -82], [19, 558, 425, -79], [20, 545, 428, -77]]) 
                    HandTwoLandMarksDict[17]= np.array([[0, 657, 384, 0], [1, 634, 359, 17], [2, 609, 351, 13], [3, 592, 359, 4], [4, 582, 371, -9], [5, 599, 345, -22], [6, 565, 340, -42], [7, 544, 340, -51], [8, 529, 342, -57], [9, 594, 363, -44], [10, 554, 360, -60], [11, 530, 361, -69], [12, 512, 363, -75], [13, 594, 383, -63], [14, 557, 388, -74], [15, 538, 393, -81], [16, 525, 396, -87], [17, 598, 403, -78], [18, 573, 410, -87], [19, 558, 414, -86], [20, 546, 417, -85]]) 
                    HandTwoLandMarksDict[18]= np.array([[0, 664, 373, 0], [1, 639, 351, 19], [2, 612, 344, 15], [3, 593, 351, 5], [4, 580, 361, -7], [5, 604, 335, -24], [6, 570, 328, -45], [7, 549, 327, -56], [8, 533, 327, -62], [9, 600, 353, -48], [10, 559, 348, -63], [11, 535, 348, -72], [12, 516, 349, -78], [13, 600, 373, -67], [14, 562, 376, -78], [15, 542, 380, -84], [16, 526, 383, -90], [17, 603, 393, -84], [18, 575, 399, -92], [19, 560, 403, -91], [20, 547, 406, -90]]) 
                    HandTwoLandMarksDict[19] = np.array([[0, 662, 368, 0], [1, 640, 344, 19], [2, 616, 334, 15], [3, 598, 341, 4], [4, 588, 351, -9], [5, 608, 326, -23], [6, 574, 317, -43], [7, 554, 315, -53], [8, 538, 315, -58], [9, 602, 345, -46], [10, 562, 337, -62], [11, 539, 335, -71], [12, 520, 336, -77], [13, 601, 365, -65], [14, 564, 366, -76], [15, 544, 369, -83], [16, 529, 371, -89], [17, 603, 384, -81], [18, 577, 390, -88], [19, 562, 393, -87], [20, 549, 395, -87]]) 
                    HandTwoLandMarksDict[20] = np.array([[0, 664, 359, 0], [1, 643, 333, 18], [2, 619, 324, 13], [3, 601, 331, 2], [4, 590, 342, -11], [5, 611, 315, -22], [6, 578, 304, -42], [7, 558, 301, -52], [8, 542, 301, -57], [9, 605, 333, -45], [10, 565, 323, -61], [11, 542, 321, -69], [12, 523, 322, -74], [13, 603, 354, -64], [14, 566, 353, -75], [15, 546, 355, -80], [16, 531, 357, -85], [17, 604, 374, -81], [18, 579, 379, -87], [19, 564, 381, -85], [20, 551, 382, -83]]) 
                    HandTwoLandMarksDict[21] = np.array([[0, 670, 350, 0], [1, 649, 325, 20], [2, 626, 316, 17], [3, 609, 321, 8], [4, 599, 332, -3], [5, 618, 306, -18], [6, 585, 292, -36], [7, 566, 287, -45], [8, 550, 284, -49], [9, 610, 322, -40], [10, 571, 310, -52], [11, 548, 306, -58], [12, 530, 306, -63], [13, 607, 342, -59], [14, 571, 339, -65], [15, 550, 340, -71], [16, 535, 342, -78], [17, 607, 361, -75], [18, 581, 364, -78], [19, 566, 367, -77], [20, 553, 368, -76]]) 
                    HandTwoLandMarksDict[22] = np.array([[0, 671, 340, 0], [1, 652, 313, 18], [2, 629, 302, 13], [3, 611, 306, 3], [4, 600, 316, -10], [5, 622, 292, -25], [6, 591, 277, -44], [7, 572, 272, -52], [8, 556, 270, -57], [9, 613, 309, -47], [10, 575, 295, -60], [11, 553, 290, -66], [12, 535, 289, -70], [13, 609, 329, -65], [14, 573, 325, -73], [15, 553, 325, -79], [16, 538, 326, -85], [17, 608, 350, -80], [18, 581, 351, -84], [19, 566, 352, -83], [20, 554, 352, -82]]) 
                    HandTwoLandMarksDict[23] = np.array([[0, 674, 333, 0], [1, 657, 305, 21], [2, 635, 292, 17], [3, 617, 295, 7], [4, 604, 304, -6], [5, 628, 283, -26], [6, 596, 266, -45], [7, 577, 260, -53], [8, 562, 257, -56], [9, 619, 299, -49], [10, 581, 283, -64], [11, 558, 278, -70], [12, 539, 276, -74], [13, 614, 318, -69], [14, 577, 313, -79], [15, 557, 313, -85], [16, 542, 314, -90], [17, 613, 339, -84], [18, 585, 341, -92], [19, 569, 342, -91], [20, 556, 342, -91]]) 
                    HandTwoLandMarksDict[24] = np.array([[0, 676, 328, 0], [1, 661, 299, 17], [2, 640, 284, 10], [3, 620, 284, 0], [4, 605, 291, -14], [5, 632, 276, -33], [6, 602, 258, -55], [7, 582, 251, -65], [8, 567, 247, -69], [9, 623, 292, -55], [10, 585, 276, -73], [11, 561, 269, -79], [12, 543, 266, -84], [13, 618, 313, -72], [14, 579, 306, -85], [15, 559, 305, -90], [16, 545, 304, -94], [17, 616, 333, -87], [18, 588, 334, -96], [19, 572, 334, -96], [20, 559, 333, -94]]) 
                    HandTwoLandMarksDict[25] = np.array([[0, 678, 322, 0], [1, 663, 293, 18], [2, 644, 278, 9], [3, 626, 280, -3], [4, 612, 289, -21], [5, 636, 270, -33], [6, 606, 252, -55], [7, 587, 245, -65], [8, 572, 240, -71], [9, 626, 286, -56], [10, 589, 269, -74], [11, 565, 262, -82], [12, 548, 258, -87], [13, 620, 306, -75], [14, 583, 299, -89], [15, 562, 297, -96], [16, 548, 296, -102], [17, 619, 326, -91], [18, 591, 327, -103], [19, 574, 328, -104], [20, 561, 327, -104]]) 
                    HandTwoLandMarksDict[26] = np.array([[0, 683, 320, 0], [1, 668, 291, 16], [2, 648, 275, 9], [3, 629, 276, -3], [4, 615, 283, -19], [5, 643, 265, -31], [6, 613, 246, -54], [7, 595, 238, -65], [8, 579, 232, -72], [9, 632, 281, -54], [10, 596, 263, -72], [11, 573, 255, -80], [12, 555, 251, -86], [13, 626, 301, -73], [14, 589, 293, -86], [15, 568, 290, -93], [16, 553, 289, -99], [17, 623, 322, -90], [18, 594, 321, -101], [19, 578, 320, -102], [20, 565, 318, -102]]) 
                    HandTwoLandMarksDict[27] = np.array([[0, 686, 311, 0], [1, 673, 281, 18], [2, 652, 266, 12], [3, 634, 269, 1], [4, 622, 279, -13], [5, 647, 257, -25], [6, 620, 236, -46], [7, 602, 227, -55], [8, 587, 221, -61], [9, 635, 272, -48], [10, 601, 252, -63], [11, 580, 243, -70], [12, 562, 239, -75], [13, 628, 291, -67], [14, 594, 282, -77], [15, 574, 279, -84], [16, 559, 277, -89], [17, 625, 312, -83], [18, 598, 310, -90], [19, 583, 309, -90], [20, 570, 307, -90]]) 
      
                    HandTwoLandMarksDict[28] = np.array([[0, 697, 305, 0], [1, 684, 275, 15], [2, 661, 259, 11], [3, 644, 263, 3], [4, 631, 274, -8], [5, 655, 248, -18], [6, 628, 225, -35], [7, 610, 215, -44], [8, 595, 209, -49], [9, 642, 263, -39], [10, 609, 241, -50], [11, 589, 232, -57], [12, 571, 226, -63], [13, 634, 281, -56], [14, 600, 270, -63], [15, 581, 266, -70], [16, 566, 264, -78], [17, 630, 301, -72], [18, 604, 298, -77], [19, 588, 296, -78], [20, 575, 294, -78]]) 
                    HandTwoLandMarksDict[29] = np.array([[0, 704, 300, 0], [1, 691, 269, 17], [2, 670, 253, 13], [3, 653, 253, 4], [4, 640, 261, -8], [5, 662, 240, -19], [6, 636, 216, -37], [7, 618, 204, -47], [8, 604, 197, -53], [9, 650, 254, -41], [10, 617, 231, -54], [11, 596, 220, -61], [12, 579, 215, -68], [13, 642, 273, -60], [14, 608, 260, -68], [15, 588, 256, -76], [16, 573, 253, -84], [17, 638, 293, -77], [18, 611, 289, -83], [19, 596, 287, -84], [20, 583, 285, -84]]) 
                    HandTwoLandMarksDict[30] = np.array([[0, 709, 293, 0], [1, 699, 261, 16], [2, 680, 242, 10], [3, 662, 241, 0], [4, 649, 249, -14], [5, 669, 231, -22], [6, 645, 207, -41], [7, 628, 195, -50], [8, 614, 187, -56], [9, 656, 245, -43], [10, 624, 221, -56], [11, 604, 210, -63], [12, 587, 204, -69], [13, 647, 263, -62], [14, 613, 249, -70], [15, 595, 245, -77], [16, 580, 243, -84], [17, 643, 283, -78], [18, 616, 278, -84], [19, 601, 276, -84], [20, 588, 274, -84]]) 
                    HandTwoLandMarksDict[31] = np.array([[0, 730, 283, 0], [1, 721, 250, 22], [2, 700, 230, 22], [3, 681, 229, 15], [4, 666, 237, 4], [5, 695, 212, -8], [6, 672, 184, -25], [7, 656, 171, -34], [8, 642, 162, -40], [9, 680, 224, -32], [10, 652, 197, -44], [11, 633, 183, -52], [12, 616, 174, -60], [13, 670, 241, -54], [14, 637, 224, -62], [15, 619, 217, -72], [16, 606, 212, -80], [17, 662, 261, -72], [18, 635, 253, -81], [19, 619, 248, -85], [20, 607, 244, -87]]) 
                    HandTwoLandMarksDict[32] = np.array([[0, 737, 274, 0], [1, 728, 241, 26], [2, 708, 223, 25], [3, 689, 224, 16], [4, 674, 234, 3], [5, 702, 206, -10], [6, 680, 179, -25], [7, 664, 166, -34], [8, 651, 156, -40], [9, 688, 217, -36], [10, 658, 190, -45], [11, 639, 176, -52], [12, 623, 167, -58], [13, 677, 234, -59], [14, 643, 217, -64], [15, 624, 210, -71], [16, 610, 206, -78], [17, 670, 253, -79], [18, 642, 246, -82], [19, 626, 242, -82], [20, 614, 238, -82]]) 
                    HandTwoLandMarksDict[33] = np.array([[0, 742, 281, 0], [1, 751, 256, 3], [2, 747, 234, -5], [3, 744, 219, -21], [4, 747, 207, -37], [5, 709, 205, -13], [6, 688, 178, -30], [7, 673, 163, -42], [8, 659, 153, -52], [9, 692, 216, -31], [10, 665, 187, -44], [11, 646, 172, -56], [12, 630, 163, -66], [13, 681, 232, -48], [14, 650, 214, -60], [15, 630, 205, -72], [16, 616, 201, -80], [17, 673, 253, -64], [18, 647, 243, -76], [19, 631, 237, -80], [20, 618, 234, -82]]) 
                    HandTwoLandMarksDict[34] = np.array([[0, 749, 283, 0], [1, 747, 251, 18], [2, 729, 227, 20], [3, 709, 221, 16], [4, 691, 223, 10], [5, 715, 203, 2], [6, 694, 174, -7], [7, 679, 159, -15], [8, 666, 149, -20], [9, 698, 212, -16], [10, 673, 183, -20], [11, 655, 168, -25], [12, 639, 159, -29], [13, 686, 228, -33], [14, 655, 208, -35], [15, 637, 201, -41], [16, 623, 197, -48], [17, 676, 247, -49], [18, 651, 236, -52], [19, 635, 232, -53], [20, 622, 229, -53]]) 
                    HandTwoLandMarksDict[35] = np.array([[0, 755, 275, 0], [1, 752, 242, 29], [2, 734, 219, 36], [3, 716, 211, 34], [4, 701, 211, 30], [5, 721, 198, 10], [6, 701, 169, 2], [7, 687, 154, -2], [8, 675, 144, -5], [9, 706, 206, -13], [10, 679, 177, -14], [11, 661, 163, -16], [12, 646, 153, -18], [13, 693, 221, -34], [14, 662, 201, -32], [15, 644, 193, -36], [16, 632, 188, -41], [17, 682, 240, -52], [18, 656, 230, -51], [19, 641, 226, -48], [20, 628, 222, -47]]) 
                    HandTwoLandMarksDict[36] = np.array([[0, 759, 268, 0], [1, 755, 235, 34], [2, 740, 212, 41], [3, 724, 204, 39], [4, 709, 205, 34], [5, 729, 193, 9], [6, 709, 165, 0], [7, 695, 150, -6], [8, 684, 139, -9], [9, 714, 202, -16], [10, 688, 172, -21], [11, 670, 157, -25], [12, 654, 146, -29], [13, 701, 216, -39], [14, 669, 197, -41], [15, 651, 188, -47], [16, 637, 183, -54], [17, 690, 234, -59], [18, 664, 225, -61], [19, 648, 220, -60], [20, 636, 216, -60]]) 
                    HandTwoLandMarksDict[37] = np.array([[0, 765, 263, 0], [1, 759, 228, 27], [2, 741, 204, 30], [3, 722, 196, 25], [4, 705, 198, 17], [5, 737, 190, 0], [6, 717, 160, -14], [7, 703, 145, -21], [8, 691, 133, -26], [9, 722, 198, -24], [10, 696, 168, -33], [11, 678, 151, -38], [12, 662, 140, -42], [13, 709, 212, -46], [14, 678, 192, -50], [15, 659, 183, -56], [16, 644, 177, -62], [17, 698, 229, -65], [18, 671, 219, -68], [19, 655, 215, -67], [20, 642, 210, -67]]) 
                    HandTwoLandMarksDict[38] = np.array([[0, 770, 260, 0], [1, 766, 225, 29], [2, 750, 202, 31], [3, 732, 195, 26], [4, 716, 197, 17], [5, 744, 186, -2], [6, 726, 156, -16], [7, 712, 140, -24], [8, 700, 129, -29], [9, 729, 195, -27], [10, 704, 163, -37], [11, 686, 146, -43], [12, 670, 134, -47], [13, 716, 209, -50], [14, 685, 187, -56], [15, 667, 177, -62], [16, 652, 170, -69], [17, 705, 226, -69], [18, 678, 215, -73], [19, 663, 209, -72], [20, 650, 204, -72]]) 
                    HandTwoLandMarksDict[39] = np.array([[0, 773, 255, 0], [1, 768, 218, 27], [2, 752, 194, 28], [3, 734, 186, 21], [4, 717, 188, 11], [5, 750, 181, -7], [6, 733, 151, -22], [7, 720, 135, -29], [8, 708, 124, -33], [9, 736, 189, -32], [10, 712, 157, -43], [11, 694, 140, -49], [12, 679, 129, -55], [13, 723, 203, -54], [14, 692, 180, -63], [15, 674, 171, -72], [16, 660, 164, -79], [17, 711, 220, -73], [18, 684, 208, -80], [19, 669, 203, -82], [20, 656, 199, -83]]) 
                    HandTwoLandMarksDict[40] = np.array([[0, 775, 251, 0], [1, 773, 216, 29], [2, 759, 191, 29], [3, 741, 184, 22], [4, 725, 186, 11], [5, 758, 179, -11], [6, 739, 148, -26], [7, 726, 132, -33], [8, 714, 121, -37], [9, 742, 187, -37], [10, 717, 154, -47], [11, 700, 136, -52], [12, 685, 125, -56], [13, 727, 201, -58], [14, 696, 176, -65], [15, 678, 166, -70], [16, 666, 159, -75], [17, 715, 217, -76], [18, 688, 204, -81], [19, 673, 198, -80], [20, 662, 193, -79]]) 
                    HandTwoLandMarksDict[41] = np.array([[0, 776, 248, 0], [1, 776, 212, 25], [2, 764, 188, 21], [3, 745, 179, 12], [4, 728, 179, 0], [5, 763, 177, -25], [6, 746, 146, -44], [7, 732, 130, -51], [8, 720, 119, -56], [9, 748, 185, -50], [10, 724, 151, -65], [11, 706, 133, -71], [12, 692, 121, -76], [13, 733, 200, -71], [14, 701, 173, -83], [15, 683, 163, -90], [16, 671, 156, -96], [17, 720, 216, -87], [18, 693, 202, -98], [19, 678, 195, -99], [20, 667, 190, -99]]) 
                    HandTwoLandMarksDict[42] = np.array([[0, 779, 246, 0], [1, 780, 212, 22], [2, 767, 187, 18], [3, 748, 175, 8], [4, 731, 172, -4], [5, 768, 175, -24], [6, 750, 145, -43], [7, 737, 129, -52], [8, 725, 118, -57], [9, 753, 184, -49], [10, 729, 150, -66], [11, 711, 132, -73], [12, 696, 119, -80], [13, 737, 198, -70], [14, 707, 172, -84], [15, 689, 161, -93], [16, 676, 153, -100], [17, 724, 214, -87], [18, 698, 201, -100], [19, 683, 194, -104], [20, 671, 187, -106]]) 
                    HandTwoLandMarksDict[43] = np.array([[0, 786, 246, 0], [1, 786, 213, 23], [2, 773, 187, 18], [3, 755, 173, 9], [4, 737, 170, -2], [5, 774, 174, -25], [6, 757, 144, -43], [7, 744, 128, -51], [8, 732, 117, -55], [9, 759, 183, -50], [10, 735, 148, -64], [11, 718, 129, -70], [12, 703, 117, -75], [13, 744, 196, -70], [14, 713, 169, -82], [15, 696, 157, -89], [16, 683, 150, -94], [17, 730, 213, -86], [18, 704, 197, -97], [19, 689, 189, -98], [20, 677, 184, -99]]) 
                    HandTwoLandMarksDict[44] = np.array([[0, 792, 241, 0], [1, 792, 207, 27], [2, 780, 181, 25], [3, 763, 170, 17], [4, 746, 168, 4], [5, 782, 171, -17], [6, 766, 139, -34], [7, 754, 122, -41], [8, 743, 111, -45], [9, 767, 178, -43], [10, 745, 143, -54], [11, 729, 125, -59], [12, 715, 113, -63], [13, 751, 191, -64], [14, 722, 164, -73], [15, 704, 153, -78], [16, 692, 146, -84], [17, 737, 206, -82], [18, 711, 191, -88], [19, 696, 185, -86], [20, 685, 181, -85]]) 
                    HandTwoLandMarksDict[45] = np.array([[0, 798, 238, 0], [1, 801, 204, 22], [2, 791, 178, 18], [3, 774, 166, 8], [4, 757, 164, -4], [5, 793, 169, -24], [6, 779, 136, -44], [7, 767, 119, -52], [8, 756, 107, -57], [9, 777, 176, -49], [10, 757, 139, -64], [11, 741, 120, -70], [12, 727, 108, -74], [13, 761, 188, -69], [14, 735, 159, -80], [15, 718, 147, -87], [16, 705, 139, -92], [17, 747, 203, -86], [18, 723, 186, -94], [19, 709, 178, -93], [20, 698, 172, -92]]) 
                    HandTwoLandMarksDict[46] = np.array([[0, 808, 235, 0], [1, 812, 202, 23], [2, 802, 177, 18], [3, 785, 168, 8], [4, 770, 169, -6], [5, 805, 165, -21], [6, 791, 133, -40], [7, 779, 116, -49], [8, 769, 103, -55], [9, 789, 171, -47], [10, 770, 135, -62], [11, 755, 116, -69], [12, 741, 103, -75], [13, 772, 182, -69], [14, 747, 153, -81], [15, 730, 141, -89], [16, 717, 133, -97], [17, 757, 197, -88], [18, 733, 180, -97], [19, 719, 172, -98], [20, 708, 165, -99]]) 
                    HandTwoLandMarksDict[47] = np.array([[0, 813, 233, 0], [1, 819, 200, 21], [2, 810, 174, 15], [3, 795, 162, 4], [4, 778, 159, -10], [5, 814, 163, -26], [6, 801, 130, -47], [7, 789, 114, -56], [8, 779, 102, -61], [9, 797, 169, -51], [10, 778, 132, -66], [11, 763, 112, -72], [12, 750, 99, -76], [13, 780, 180, -71], [14, 754, 150, -82], [15, 737, 137, -87], [16, 726, 130, -92], [17, 763, 194, -88], [18, 740, 176, -97], [19, 726, 168, -97], [20, 715, 162, -96]]) 
                    HandTwoLandMarksDict[48] = np.array([[0, 823, 235, 0], [1, 827, 200, 25], [2, 818, 174, 22], [3, 803, 162, 11], [4, 787, 159, -2], [5, 822, 162, -19], [6, 809, 130, -38], [7, 799, 113, -47], [8, 789, 101, -52], [9, 805, 168, -46], [10, 787, 130, -60], [11, 773, 110, -66], [12, 760, 96, -72], [13, 788, 179, -70], [14, 763, 148, -80], [15, 747, 134, -87], [16, 734, 125, -93], [17, 772, 194, -89], [18, 748, 176, -98], [19, 735, 166, -98], [20, 724, 159, -98]]) 
                    HandTwoLandMarksDict[49] = np.array([[0, 831, 236, 0], [1, 835, 202, 25], [2, 827, 176, 22], [3, 811, 166, 11], [4, 795, 165, -2], [5, 831, 162, -13], [6, 820, 129, -31], [7, 810, 111, -41], [8, 800, 99, -47], [9, 814, 166, -40], [10, 797, 129, -53], [11, 783, 109, -60], [12, 771, 95, -66], [13, 797, 177, -64], [14, 774, 146, -73], [15, 758, 132, -81], [16, 745, 122, -88], [17, 780, 191, -85], [18, 758, 173, -93], [19, 744, 163, -94], [20, 733, 155, -95]]) 
                    HandTwoLandMarksDict[50] = np.array([[0, 838, 235, 0], [1, 843, 201, 26], [2, 836, 173, 21], [3, 820, 159, 10], [4, 803, 154, -4], [5, 841, 161, -21], [6, 830, 127, -42], [7, 819, 109, -52], [8, 809, 96, -57], [9, 824, 167, -49], [10, 807, 127, -66], [11, 793, 106, -73], [12, 781, 91, -78], [13, 807, 178, -73], [14, 783, 144, -86], [15, 767, 129, -93], [16, 755, 119, -98], [17, 790, 192, -93], [18, 766, 171, -104], [19, 752, 159, -104], [20, 742, 150, -104]]) 
                    HandTwoLandMarksDict[51] = np.array([[0, 844, 234, 0], [1, 850, 199, 27], [2, 843, 171, 23], [3, 828, 158, 12], [4, 811, 154, -3], [5, 848, 159, -16], [6, 836, 125, -36], [7, 826, 107, -46], [8, 816, 94, -53], [9, 831, 163, -45], [10, 815, 125, -60], [11, 802, 104, -68], [12, 790, 88, -75], [13, 813, 174, -70], [14, 790, 141, -81], [15, 774, 127, -89], [16, 762, 117, -96], [17, 796, 188, -91], [18, 773, 168, -99], [19, 760, 157, -100], [20, 750, 149, -100]]) 
                    HandTwoLandMarksDict[52] = np.array([[0, 849, 236, 0], [1, 855, 201, 26], [2, 848, 175, 22], [3, 833, 164, 10], [4, 817, 162, -6], [5, 854, 160, -16], [6, 843, 126, -35], [7, 834, 108, -45], [8, 825, 94, -51], [9, 836, 164, -44], [10, 821, 125, -57], [11, 809, 104, -65], [12, 797, 88, -72], [13, 818, 174, -69], [14, 796, 141, -78], [15, 781, 126, -86], [16, 769, 117, -93], [17, 800, 188, -90], [18, 779, 166, -98], [19, 766, 155, -98], [20, 756, 147, -99]]) 
                    HandTwoLandMarksDict[53] = np.array([[0, 853, 235, 0], [1, 859, 200, 29], [2, 854, 172, 25], [3, 839, 159, 13], [4, 823, 155, -2], [5, 859, 159, -19], [6, 848, 124, -38], [7, 840, 106, -47], [8, 831, 93, -53], [9, 843, 164, -49], [10, 827, 124, -63], [11, 815, 102, -70], [12, 804, 87, -76], [13, 825, 175, -74], [14, 802, 140, -86], [15, 787, 125, -92], [16, 775, 115, -98], [17, 808, 189, -96], [18, 785, 165, -105], [19, 772, 153, -105], [20, 762, 144, -104]]) 
                    HandTwoLandMarksDict[54] = np.array([[0, 856, 234, 0], [1, 864, 199, 30], [2, 859, 171, 26], [3, 845, 159, 14], [4, 829, 155, -1], [5, 864, 158, -19], [6, 855, 123, -38], [7, 846, 105, -47], [8, 837, 93, -52], [9, 847, 163, -48], [10, 833, 122, -62], [11, 821, 100, -69], [12, 809, 85, -74], [13, 829, 173, -73], [14, 807, 138, -84], [15, 792, 123, -91], [16, 780, 113, -97], [17, 811, 187, -94], [18, 789, 163, -103], [19, 776, 151, -103], [20, 766, 142, -102]]) 
                    HandTwoLandMarksDict[55] = np.array([[0, 860, 233, 0], [1, 867, 198, 29], [2, 862, 171, 24], [3, 848, 159, 12], [4, 832, 155, -4], [5, 868, 158, -21], [6, 860, 123, -41], [7, 851, 105, -50], [8, 843, 92, -55], [9, 851, 163, -50], [10, 839, 123, -64], [11, 827, 101, -71], [12, 815, 85, -78], [13, 833, 173, -74], [14, 813, 138, -85], [15, 798, 122, -94], [16, 786, 112, -102], [17, 815, 186, -94], [18, 794, 163, -104], [19, 781, 151, -107], [20, 771, 141, -108]]) 
                    HandTwoLandMarksDict[56] = np.array([[0, 864, 233, 0], [1, 872, 199, 28], [2, 867, 171, 23], [3, 853, 158, 10], [4, 838, 152, -6], [5, 873, 159, -22], [6, 864, 124, -42], [7, 855, 106, -53], [8, 847, 92, -59], [9, 857, 163, -52], [10, 844, 123, -67], [11, 832, 100, -75], [12, 820, 84, -82], [13, 839, 173, -77], [14, 818, 137, -90], [15, 802, 121, -99], [16, 790, 111, -106], [17, 821, 187, -99], [18, 798, 162, -110], [19, 785, 150, -111], [20, 775, 141, -112]]) 
                    HandTwoLandMarksDict[57] = np.array([[0, 869, 233, 0], [1, 878, 199, 29], [2, 874, 171, 25], [3, 860, 157, 14], [4, 844, 151, -1], [5, 879, 159, -21], [6, 870, 122, -40], [7, 861, 103, -48], [8, 853, 91, -52], [9, 862, 163, -50], [10, 849, 121, -64], [11, 838, 99, -69], [12, 827, 83, -74], [13, 843, 172, -74], [14, 823, 135, -85], [15, 808, 119, -90], [16, 797, 109, -95], [17, 825, 184, -94], [18, 804, 160, -103], [19, 791, 148, -102], [20, 782, 139, -101]]) 
                    HandTwoLandMarksDict[58] = np.array([[0, 875, 234, 0], [1, 884, 200, 28], [2, 880, 172, 24], [3, 866, 158, 13], [4, 850, 152, -3], [5, 887, 159, -15], [6, 879, 125, -35], [7, 871, 106, -46], [8, 863, 92, -53], [9, 870, 162, -45], [10, 857, 122, -60], [11, 847, 100, -68], [12, 836, 83, -75], [13, 851, 171, -71], [14, 832, 136, -83], [15, 817, 119, -91], [16, 806, 107, -98], [17, 832, 184, -94], [18, 812, 160, -104], [19, 799, 148, -105], [20, 789, 137, -106]]) 
                    HandTwoLandMarksDict[59] = np.array([[0, 881, 234, 0], [1, 890, 200, 27], [2, 886, 172, 23], [3, 873, 156, 10], [4, 857, 150, -5], [5, 894, 159, -17], [6, 886, 124, -38], [7, 878, 105, -49], [8, 870, 91, -55], [9, 877, 163, -47], [10, 865, 122, -61], [11, 854, 99, -69], [12, 844, 82, -76], [13, 858, 171, -72], [14, 840, 135, -83], [15, 826, 118, -90], [16, 814, 107, -97], [17, 838, 183, -94], [18, 818, 159, -104], [19, 806, 147, -104], [20, 796, 137, -104]]) 
                    HandTwoLandMarksDict[60]= np.array([[0, 888, 235, 0], [1, 898, 201, 27], [2, 895, 173, 23], [3, 882, 158, 11], [4, 866, 153, -4], [5, 903, 161, -15], [6, 896, 126, -35], [7, 888, 107, -47], [8, 880, 93, -54], [9, 885, 163, -45], [10, 875, 123, -59], [11, 865, 101, -67], [12, 854, 84, -74], [13, 866, 171, -70], [14, 848, 135, -81], [15, 834, 119, -88], [16, 823, 107, -95], [17, 846, 183, -93], [18, 827, 160, -100], [19, 815, 148, -100], [20, 806, 138, -101]]) 
                    HandTwoLandMarksDict[61]= np.array([[0, 894, 236, 0], [1, 905, 202, 26], [2, 903, 173, 22], [3, 890, 156, 10], [4, 875, 147, -4], [5, 911, 163, -22], [6, 905, 128, -44], [7, 896, 108, -55], [8, 888, 94, -61], [9, 895, 166, -51], [10, 884, 125, -67], [11, 873, 102, -75], [12, 863, 84, -82], [13, 875, 174, -75], [14, 857, 137, -88], [15, 843, 119, -95], [16, 832, 107, -102], [17, 855, 185, -95], [18, 835, 160, -106], [19, 823, 147, -107], [20, 813, 137, -108]]) 
                    HandTwoLandMarksDict[62]= np.array([[0, 901, 237, 0], [1, 913, 204, 28], [2, 911, 175, 25], [3, 899, 157, 15], [4, 884, 147, 0], [5, 919, 164, -24], [6, 913, 128, -44], [7, 905, 108, -53], [8, 897, 94, -57], [9, 903, 167, -52], [10, 892, 125, -67], [11, 882, 101, -73], [12, 872, 85, -77], [13, 884, 175, -75], [14, 865, 137, -87], [15, 851, 120, -92], [16, 841, 108, -97], [17, 864, 186, -95], [18, 844, 161, -104], [19, 832, 148, -104], [20, 822, 137, -104]]) 
                    HandTwoLandMarksDict[63]= np.array([[0, 907, 240, 0], [1, 920, 206, 27], [2, 919, 177, 24], [3, 907, 161, 12], [4, 892, 153, -3], [5, 927, 166, -17], [6, 920, 131, -38], [7, 913, 111, -49], [8, 906, 97, -56], [9, 909, 168, -47], [10, 901, 127, -62], [11, 891, 104, -70], [12, 881, 86, -78], [13, 890, 175, -72], [14, 873, 139, -83], [15, 860, 121, -92], [16, 849, 109, -99], [17, 869, 186, -94], [18, 850, 161, -103], [19, 839, 148, -104], [20, 829, 137, -104]]) 
                    HandTwoLandMarksDict[64]= np.array([[0, 911, 241, 0], [1, 925, 208, 26], [2, 924, 178, 21], [3, 912, 161, 10], [4, 898, 152, -5], [5, 933, 169, -21], [6, 928, 132, -42], [7, 921, 112, -53], [8, 914, 98, -59], [9, 915, 171, -48], [10, 908, 129, -63], [11, 899, 105, -71], [12, 889, 87, -78], [13, 895, 178, -71], [14, 880, 140, -82], [15, 867, 122, -89], [16, 857, 109, -96], [17, 874, 187, -91], [18, 856, 162, -99], [19, 846, 148, -99], [20, 837, 137, -99]]) 
                    HandTwoLandMarksDict[65]= np.array([[0, 918, 243, 0], [1, 930, 209, 29], [2, 929, 180, 26], [3, 918, 164, 16], [4, 904, 156, 1], [5, 937, 169, -16], [6, 933, 133, -36], [7, 927, 113, -46], [8, 920, 99, -51], [9, 921, 171, -45], [10, 913, 129, -59], [11, 905, 105, -66], [12, 896, 88, -72], [13, 901, 177, -70], [14, 885, 140, -79], [15, 873, 122, -87], [16, 863, 109, -94], [17, 881, 187, -90], [18, 862, 162, -97], [19, 851, 149, -98], [20, 843, 138, -98]]) 
                    HandTwoLandMarksDict[66]= np.array([[0, 921, 245, 0], [1, 934, 211, 29], [2, 934, 182, 25], [3, 923, 164, 14], [4, 909, 154, 0], [5, 943, 173, -26], [6, 940, 135, -49], [7, 933, 115, -60], [8, 926, 100, -64], [9, 928, 176, -55], [10, 920, 131, -73], [11, 911, 107, -80], [12, 901, 89, -85], [13, 908, 183, -80], [14, 892, 143, -93], [15, 878, 124, -99], [16, 868, 111, -105], [17, 888, 192, -99], [18, 869, 165, -110], [19, 857, 150, -110], [20, 849, 139, -109]]) 
                    HandTwoLandMarksDict[67]= np.array([[0, 926, 249, 0], [1, 939, 216, 29], [2, 939, 186, 25], [3, 927, 170, 15], [4, 913, 160, 0], [5, 949, 176, -20], [6, 945, 139, -41], [7, 939, 119, -51], [8, 932, 104, -57], [9, 932, 177, -49], [10, 926, 134, -65], [11, 917, 110, -73], [12, 908, 91, -80], [13, 912, 183, -74], [14, 897, 145, -86], [15, 883, 126, -95], [16, 873, 113, -102], [17, 891, 192, -94], [18, 873, 165, -104], [19, 862, 151, -106], [20, 854, 140, -106]]) 
                    HandTwoLandMarksDict[68]= np.array([[0, 931, 250, 0], [1, 944, 217, 29], [2, 945, 187, 25], [3, 934, 168, 14], [4, 920, 157, -1], [5, 954, 178, -22], [6, 951, 140, -44], [7, 945, 120, -54], [8, 938, 105, -60], [9, 939, 181, -52], [10, 931, 136, -67], [11, 923, 112, -74], [12, 914, 94, -80], [13, 919, 187, -76], [14, 904, 147, -88], [15, 891, 128, -95], [16, 882, 114, -101], [17, 898, 196, -97], [18, 880, 168, -106], [19, 869, 153, -106], [20, 860, 142, -106]]) 
                    HandTwoLandMarksDict[69] = np.array([[0, 935, 251, 0], [1, 950, 219, 28], [2, 952, 189, 24], [3, 940, 170, 13], [4, 926, 160, -1], [5, 961, 179, -24], [6, 957, 141, -45], [7, 951, 121, -55], [8, 944, 106, -60], [9, 944, 182, -52], [10, 938, 138, -67], [11, 930, 114, -74], [12, 921, 96, -80], [13, 924, 188, -76], [14, 910, 148, -87], [15, 897, 129, -93], [16, 888, 116, -99], [17, 903, 196, -95], [18, 886, 168, -103], [19, 875, 154, -103], [20, 867, 143, -102]]) 
                    HandTwoLandMarksDict[70] = np.array([[0, 940, 253, 0], [1, 955, 221, 27], [2, 957, 191, 23], [3, 946, 173, 12], [4, 932, 162, -2], [5, 966, 183, -24], [6, 963, 145, -46], [7, 958, 124, -56], [8, 952, 109, -60], [9, 950, 185, -52], [10, 944, 140, -68], [11, 936, 115, -75], [12, 928, 97, -81], [13, 930, 190, -74], [14, 916, 151, -87], [15, 903, 131, -95], [16, 894, 117, -102], [17, 909, 197, -93], [18, 892, 170, -103], [19, 881, 156, -104], [20, 873, 144, -105]]) 
                    HandTwoLandMarksDict[71] = np.array([[0, 944, 255, 0], [1, 959, 223, 26], [2, 960, 193, 20], [3, 950, 174, 8], [4, 936, 163, -7], [5, 971, 185, -28], [6, 968, 146, -51], [7, 962, 126, -61], [8, 956, 111, -66], [9, 955, 187, -56], [10, 950, 142, -73], [11, 942, 117, -81], [12, 933, 99, -88], [13, 935, 193, -79], [14, 921, 152, -93], [15, 908, 132, -102], [16, 898, 119, -108], [17, 913, 200, -98], [18, 896, 171, -109], [19, 886, 156, -111], [20, 877, 145, -111]]) 
                    HandTwoLandMarksDict[72] = np.array([[0, 948, 257, 0], [1, 963, 225, 28], [2, 965, 196, 24], [3, 956, 177, 15], [4, 943, 165, 0], [5, 975, 187, -27], [6, 972, 149, -48], [7, 967, 128, -57], [8, 961, 112, -61], [9, 959, 190, -54], [10, 955, 146, -70], [11, 947, 120, -77], [12, 939, 102, -82], [13, 939, 195, -76], [14, 926, 155, -89], [15, 913, 135, -97], [16, 904, 121, -103], [17, 918, 202, -94], [18, 901, 173, -104], [19, 891, 158, -106], [20, 883, 147, -106]]) 
                    HandTwoLandMarksDict[73] = np.array([[0, 951, 260, 0], [1, 967, 229, 29], [2, 970, 200, 25], [3, 960, 182, 14], [4, 947, 172, -1], [5, 979, 191, -22], [6, 978, 154, -43], [7, 973, 133, -53], [8, 966, 118, -59], [9, 963, 192, -51], [10, 960, 148, -66], [11, 953, 123, -74], [12, 944, 104, -81], [13, 943, 197, -75], [14, 930, 157, -87], [15, 918, 137, -96], [16, 909, 124, -103], [17, 922, 204, -94], [18, 906, 176, -105], [19, 896, 161, -106], [20, 887, 150, -106]]) 
                    HandTwoLandMarksDict[74] = np.array([[0, 956, 265, 0], [1, 972, 234, 27], [2, 974, 204, 22], [3, 963, 186, 11], [4, 950, 175, -4], [5, 985, 195, -27], [6, 984, 157, -49], [7, 978, 136, -60], [8, 972, 120, -65], [9, 968, 197, -55], [10, 966, 153, -72], [11, 959, 127, -81], [12, 951, 107, -87], [13, 948, 201, -78], [14, 936, 161, -91], [15, 924, 141, -99], [16, 915, 126, -105], [17, 927, 208, -97], [18, 911, 179, -107], [19, 901, 164, -108], [20, 894, 152, -108]]) 
                    HandTwoLandMarksDict[75] = np.array([[0, 959, 266, 0], [1, 977, 236, 26], [2, 980, 206, 20], [3, 970, 187, 8], [4, 956, 176, -7], [5, 990, 198, -27], [6, 990, 160, -50], [7, 985, 139, -61], [8, 978, 124, -66], [9, 974, 200, -54], [10, 971, 156, -71], [11, 964, 130, -80], [12, 956, 110, -86], [13, 953, 204, -77], [14, 941, 163, -90], [15, 929, 143, -98], [16, 920, 129, -104], [17, 932, 210, -95], [18, 917, 181, -105], [19, 907, 166, -106], [20, 900, 154, -105]]) 
                    HandTwoLandMarksDict[76] = np.array([[0, 965, 270, 0], [1, 981, 240, 26], [2, 985, 211, 21], [3, 975, 192, 11], [4, 963, 180, -3], [5, 995, 202, -31], [6, 995, 163, -55], [7, 989, 141, -64], [8, 983, 126, -67], [9, 979, 204, -59], [10, 977, 158, -78], [11, 970, 132, -85], [12, 962, 113, -90], [13, 959, 208, -81], [14, 946, 166, -97], [15, 935, 146, -105], [16, 926, 132, -110], [17, 937, 215, -99], [18, 922, 184, -112], [19, 912, 168, -113], [20, 905, 157, -112]]) 
                    HandTwoLandMarksDict[77] = np.array([[0, 968, 274, 0], [1, 986, 243, 27], [2, 990, 214, 22], [3, 980, 195, 10], [4, 967, 184, -4], [5, 1000, 206, -27], [6, 1001, 168, -50], [7, 996, 147, -60], [8, 990, 131, -65], [9, 983, 207, -55], [10, 982, 162, -72], [11, 976, 136, -80], [12, 968, 117, -86], [13, 962, 211, -77], [14, 952, 170, -90], [15, 941, 149, -99], [16, 932, 135, -106], [17, 941, 216, -96], [18, 927, 186, -106], [19, 917, 171, -107], [20, 909, 160, -107]]) 
                    HandTwoLandMarksDict[78] = np.array([[0, 971, 277, 0], [1, 989, 247, 24], [2, 994, 218, 19], [3, 985, 198, 7], [4, 972, 187, -7], [5, 1005, 209, -28], [6, 1006, 171, -51], [7, 1001, 150, -63], [8, 995, 134, -69], [9, 988, 210, -54], [10, 987, 166, -72], [11, 981, 140, -81], [12, 974, 120, -89], [13, 967, 213, -76], [14, 956, 173, -90], [15, 946, 153, -101], [16, 937, 139, -108], [17, 945, 219, -94], [18, 932, 190, -106], [19, 922, 175, -108], [20, 915, 163, -109]]) 
                    HandTwoLandMarksDict[79] = np.array([[0, 975, 282, 0], [1, 992, 252, 26], [2, 997, 222, 20], [3, 988, 201, 8], [4, 975, 188, -7], [5, 1009, 215, -36], [6, 1010, 175, -60], [7, 1004, 153, -70], [8, 998, 137, -73], [9, 993, 218, -64], [10, 993, 171, -85], [11, 986, 144, -92], [12, 979, 124, -97], [13, 973, 222, -86], [14, 962, 179, -103], [15, 950, 157, -111], [16, 941, 142, -116], [17, 951, 228, -103], [18, 937, 194, -117], [19, 927, 178, -119], [20, 919, 165, -119]]) 
                    HandTwoLandMarksDict[80] = np.array([[0, 978, 287, 0], [1, 996, 257, 26], [2, 1001, 227, 21], [3, 992, 206, 10], [4, 979, 194, -4], [5, 1013, 220, -30], [6, 1014, 180, -53], [7, 1008, 158, -64], [8, 1002, 142, -69], [9, 997, 221, -57], [10, 997, 176, -76], [11, 991, 149, -84], [12, 983, 129, -91], [13, 976, 224, -79], [14, 965, 181, -95], [15, 953, 161, -103], [16, 944, 147, -109], [17, 955, 229, -97], [18, 940, 197, -109], [19, 930, 182, -111], [20, 923, 169, -111]]) 
                    HandTwoLandMarksDict[81] = np.array([[0, 982, 293, 0], [1, 1000, 263, 25], [2, 1005, 233, 19], [3, 995, 213, 7], [4, 982, 201, -9], [5, 1018, 226, -31], [6, 1019, 185, -55], [7, 1013, 163, -66], [8, 1007, 147, -71], [9, 1001, 227, -58], [10, 1002, 181, -77], [11, 995, 154, -86], [12, 988, 134, -91], [13, 980, 229, -80], [14, 971, 187, -96], [15, 959, 166, -104], [16, 950, 151, -108], [17, 958, 234, -98], [18, 945, 202, -111], [19, 936, 186, -112], [20, 928, 174, -111]]) 
                    HandTwoLandMarksDict[82] = np.array([[0, 987, 297, 0], [1, 1005, 268, 24], [2, 1012, 238, 17], [3, 1003, 217, 5], [4, 990, 204, -11], [5, 1024, 232, -34], [6, 1025, 192, -59], [7, 1020, 170, -70], [8, 1014, 154, -75], [9, 1007, 233, -60], [10, 1007, 186, -80], [11, 1002, 160, -87], [12, 995, 140, -92], [13, 985, 236, -82], [14, 976, 193, -97], [15, 966, 171, -103], [16, 958, 156, -107], [17, 963, 240, -99], [18, 951, 208, -111], [19, 942, 192, -110], [20, 935, 180, -107]]) 
                    HandTwoLandMarksDict[83] = np.array([[0, 992, 303, 0], [1, 1013, 275, 21], [2, 1019, 244, 14], [3, 1009, 224, 2], [4, 996, 212, -12], [5, 1030, 239, -33], [6, 1033, 198, -57], [7, 1028, 175, -67], [8, 1021, 158, -72], [9, 1011, 238, -57], [10, 1015, 193, -76], [11, 1011, 166, -83], [12, 1004, 146, -89], [13, 990, 239, -77], [14, 982, 198, -89], [15, 973, 177, -97], [16, 965, 162, -102], [17, 969, 241, -93], [18, 958, 211, -102], [19, 949, 196, -102], [20, 943, 184, -101]]) 
                    HandTwoLandMarksDict[84] = np.array([[0, 997, 306, 0], [1, 1018, 279, 22], [2, 1027, 250, 13], [3, 1018, 228, 1], [4, 1005, 214, -15], [5, 1038, 246, -46], [6, 1040, 203, -74], [7, 1034, 179, -84], [8, 1027, 162, -88], [9, 1020, 246, -71], [10, 1023, 198, -92], [11, 1018, 170, -99], [12, 1011, 150, -104], [13, 999, 248, -89], [14, 990, 202, -106], [15, 980, 180, -111], [16, 973, 165, -114], [17, 977, 250, -103], [18, 965, 215, -116], [19, 957, 199, -114], [20, 951, 187, -111]]) 
                    HandTwoLandMarksDict[85] = np.array([[0, 1003, 314, 0], [1, 1022, 287, 27], [2, 1029, 257, 19], [3, 1019, 235, 6], [4, 1005, 221, -10], [5, 1044, 251, -43], [6, 1045, 208, -71], [7, 1037, 185, -84], [8, 1029, 169, -89], [9, 1027, 253, -72], [10, 1030, 204, -95], [11, 1024, 177, -104], [12, 1018, 157, -110], [13, 1006, 256, -95], [14, 997, 208, -115], [15, 986, 186, -122], [16, 978, 171, -126], [17, 983, 259, -113], [18, 971, 223, -132], [19, 961, 207, -133], [20, 955, 194, -132]]) 
                    HandTwoLandMarksDict[86] = np.array([[0, 1006, 322, 0], [1, 1024, 295, 21], [2, 1032, 265, 9], [3, 1021, 241, -6], [4, 1006, 226, -27], [5, 1048, 259, -49], [6, 1048, 215, -80], [7, 1038, 191, -95], [8, 1028, 173, -101], [9, 1031, 261, -76], [10, 1037, 212, -102], [11, 1030, 185, -110], [12, 1023, 165, -114], [13, 1010, 263, -98], [14, 1002, 216, -120], [15, 991, 194, -124], [16, 983, 179, -125], [17, 987, 267, -116], [18, 976, 230, -134], [19, 967, 213, -134], [20, 961, 201, -131]]) 
                    HandTwoLandMarksDict[87] = np.array([[0, 1010, 331, 0], [1, 1029, 303, 17], [2, 1037, 272, 3], [3, 1027, 247, -14], [4, 1013, 231, -34], [5, 1052, 268, -53], [6, 1052, 222, -85], [7, 1041, 196, -99], [8, 1031, 179, -105], [9, 1034, 270, -78], [10, 1040, 219, -105], [11, 1035, 192, -112], [12, 1028, 173, -116], [13, 1012, 272, -99], [14, 1006, 223, -121], [15, 995, 201, -124], [16, 988, 187, -124], [17, 990, 274, -115], [18, 981, 237, -134], [19, 973, 220, -132], [20, 966, 208, -128]]) 
                    HandTwoLandMarksDict[88] = np.array([[0, 1011, 333, 0], [1, 1032, 309, 11], [2, 1041, 278, -6], [3, 1029, 251, -26], [4, 1014, 234, -48], [5, 1057, 274, -58], [6, 1057, 227, -93], [7, 1047, 202, -109], [8, 1036, 184, -116], [9, 1039, 276, -80], [10, 1046, 225, -110], [11, 1040, 198, -119], [12, 1034, 179, -123], [13, 1017, 277, -98], [14, 1011, 228, -122], [15, 1000, 206, -124], [16, 994, 191, -124], [17, 994, 277, -112], [18, 984, 241, -131], [19, 976, 225, -130], [20, 970, 212, -127]]) 
                    HandTwoLandMarksDict[89] = np.array([[0, 1013, 339, 0], [1, 1035, 314, 15], [2, 1046, 284, 0], [3, 1037, 258, -15], [4, 1023, 241, -35], [5, 1060, 280, -60], [6, 1062, 234, -91], [7, 1053, 209, -105], [8, 1044, 191, -111], [9, 1041, 281, -82], [10, 1048, 231, -108], [11, 1044, 204, -114], [12, 1040, 185, -119], [13, 1019, 282, -99], [14, 1013, 234, -120], [15, 1004, 211, -123], [16, 998, 197, -125], [17, 997, 282, -112], [18, 988, 246, -130], [19, 981, 229, -130], [20, 976, 216, -129]]) 
                    HandTwoLandMarksDict[90] = np.array([[0, 1018, 349, 0], [1, 1038, 323, 19], [2, 1048, 292, 4], [3, 1039, 266, -12], [4, 1025, 248, -33], [5, 1065, 286, -61], [6, 1065, 239, -96], [7, 1054, 213, -110], [8, 1044, 196, -116], [9, 1047, 289, -87], [10, 1054, 236, -117], [11, 1048, 209, -122], [12, 1043, 191, -125], [13, 1025, 291, -108], [14, 1019, 240, -132], [15, 1009, 217, -133], [16, 1003, 202, -133], [17, 1001, 294, -124], [18, 994, 254, -145], [19, 987, 237, -145], [20, 983, 223, -142]]) 
                    HandTwoLandMarksDict[91] = np.array([[0, 1019, 354, 0], [1, 1041, 328, 14], [2, 1051, 296, -2], [3, 1041, 269, -21], [4, 1026, 251, -43], [5, 1068, 293, -64], [6, 1066, 244, -98], [7, 1055, 218, -113], [8, 1044, 200, -120], [9, 1049, 295, -88], [10, 1055, 242, -117], [11, 1051, 216, -123], [12, 1047, 197, -127], [13, 1026, 296, -107], [14, 1019, 246, -130], [15, 1011, 222, -131], [16, 1005, 207, -131], [17, 1003, 297, -122], [18, 995, 257, -139], [19, 989, 240, -135], [20, 986, 228, -131]]) 
                    HandTwoLandMarksDict[92] = np.array([[0, 1020, 361, 0], [1, 1042, 334, 9], [2, 1050, 302, -11], [3, 1036, 273, -33], [4, 1019, 253, -58], [5, 1069, 301, -65], [6, 1066, 253, -100], [7, 1053, 226, -116], [8, 1041, 207, -125], [9, 1050, 304, -87], [10, 1054, 253, -118], [11, 1049, 230, -123], [12, 1043, 216, -126], [13, 1027, 305, -106], [14, 1021, 253, -131], [15, 1012, 230, -130], [16, 1006, 215, -130], [17, 1005, 305, -122], [18, 999, 265, -139], [19, 993, 248, -136], [20, 989, 235, -133]]) 
                    HandTwoLandMarksDict[93] = np.array([[0, 1024, 370, 0], [1, 1048, 344, 19], [2, 1058, 313, 3], [3, 1047, 285, -15], [4, 1032, 266, -38], [5, 1075, 312, -55], [6, 1068, 263, -89], [7, 1054, 238, -106], [8, 1040, 220, -115], [9, 1055, 312, -81], [10, 1058, 259, -108], [11, 1050, 233, -114], [12, 1042, 217, -118], [13, 1032, 312, -102], [14, 1025, 262, -121], [15, 1015, 240, -119], [16, 1008, 227, -118], [17, 1010, 312, -119], [18, 1004, 274, -132], [19, 999, 258, -127], [20, 994, 247, -123]]) 
                    HandTwoLandMarksDict[94] = np.array([[0, 1027, 382, 0], [1, 1049, 357, 4], [2, 1059, 324, -14], [3, 1044, 292, -32], [4, 1028, 272, -52], [5, 1079, 326, -53], [6, 1074, 275, -89], [7, 1059, 249, -108], [8, 1044, 234, -117], [9, 1058, 327, -69], [10, 1059, 274, -96], [11, 1048, 251, -103], [12, 1039, 238, -108], [13, 1037, 325, -83], [14, 1031, 277, -101], [15, 1021, 255, -99], [16, 1014, 241, -99], [17, 1015, 323, -95], [18, 1012, 286, -107], [19, 1006, 271, -102], [20, 1002, 260, -99]]) 
                    HandTwoLandMarksDict[95] = np.array([[0, 1035, 392, 0], [1, 1057, 365, 21], [2, 1067, 334, 2], [3, 1058, 306, -19], [4, 1042, 286, -45], [5, 1091, 334, -52], [6, 1082, 287, -94], [7, 1065, 263, -118], [8, 1048, 249, -129], [9, 1074, 337, -81], [10, 1074, 284, -114], [11, 1062, 260, -123], [12, 1049, 246, -127], [13, 1051, 337, -106], [14, 1043, 288, -131], [15, 1031, 265, -128], [16, 1022, 251, -125], [17, 1027, 337, -128], [18, 1020, 299, -143], [19, 1014, 282, -137], [20, 1011, 269, -132]]) 
                    HandTwoLandMarksDict[96] = np.array([[0, 1035, 397, 0], [1, 1058, 374, 4], [2, 1072, 344, -19], [3, 1061, 311, -44], [4, 1045, 290, -71], [5, 1091, 346, -69], [6, 1086, 296, -116], [7, 1068, 271, -143], [8, 1050, 257, -157], [9, 1071, 347, -88], [10, 1073, 294, -122], [11, 1060, 273, -130], [12, 1047, 262, -136], [13, 1049, 346, -105], [14, 1046, 297, -128], [15, 1036, 276, -125], [16, 1028, 264, -123], [17, 1026, 343, -119], [18, 1024, 305, -135], [19, 1019, 289, -130], [20, 1014, 277, -125]]) 
                    HandTwoLandMarksDict[97] = np.array([[0, 1037, 423, 0], [1, 1059, 404, -29], [2, 1071, 371, -64], [3, 1056, 332, -91], [4, 1040, 307, -118], [5, 1099, 376, -82], [6, 1095, 325, -129], [7, 1078, 300, -157], [8, 1063, 288, -170], [9, 1078, 375, -83], [10, 1073, 326, -120], [11, 1059, 307, -133], [12, 1048, 299, -142], [13, 1057, 372, -84], [14, 1052, 326, -113], [15, 1044, 308, -113], [16, 1038, 298, -113], [17, 1035, 368, -86], [18, 1032, 331, -106], [19, 1030, 315, -106], [20, 1029, 303, -104]]) 
                    HandTwoLandMarksDict[98] = np.array([[0, 1043, 434, 0], [1, 1066, 411, 8], [2, 1079, 380, -17], [3, 1067, 347, -44], [4, 1051, 324, -74], [5, 1104, 383, -68], [6, 1094, 334, -111], [7, 1076, 312, -136], [8, 1058, 300, -148], [9, 1085, 385, -91], [10, 1084, 332, -120], [11, 1072, 311, -128], [12, 1059, 299, -135], [13, 1062, 385, -110], [14, 1059, 335, -133], [15, 1049, 316, -129], [16, 1041, 304, -127], [17, 1037, 382, -126], [18, 1035, 341, -143], [19, 1031, 325, -137], [20, 1029, 311, -133]]) 
                    HandTwoLandMarksDict[99] = np.array([[0, 1043, 442, 0], [1, 1059, 418, -16], [2, 1071, 387, -47], [3, 1060, 354, -74], [4, 1044, 330, -103], [5, 1104, 390, -64], [6, 1093, 343, -102], [7, 1077, 321, -124], [8, 1062, 310, -135], [9, 1087, 394, -73], [10, 1082, 345, -100], [11, 1068, 324, -111], [12, 1054, 310, -121], [13, 1066, 395, -82], [14, 1060, 348, -106], [15, 1050, 328, -106], [16, 1042, 313, -107], [17, 1041, 393, -89], [18, 1038, 353, -110], [19, 1035, 335, -108], [20, 1032, 321, -106]]) 
                    HandTwoLandMarksDict[100] = np.array([[0, 1044, 449, 0], [1, 1067, 427, 12], [2, 1081, 397, -10], [3, 1072, 365, -34], [4, 1056, 343, -63], [5, 1107, 400, -63], [6, 1093, 352, -101], [7, 1075, 331, -123], [8, 1057, 319, -133], [9, 1089, 401, -88], [10, 1086, 349, -115], [11, 1074, 328, -122], [12, 1060, 315, -127], [13, 1066, 400, -109], [14, 1062, 350, -131], [15, 1053, 330, -125], [16, 1045, 318, -121], [17, 1040, 396, -126], [18, 1038, 356, -142], [19, 1035, 340, -134], [20, 1034, 327, -128]]) 
       
                    #Second Left hand at 90 degrees
                    HandTwoLandMarksDict[101] = np.array([[0, 1039, 452, 0], [1, 1060, 431, -9], [2, 1075, 402, -37], [3, 1069, 369, -62], [4, 1057, 346, -90], [5, 1103, 402, -73], [6, 1092, 355, -115], [7, 1075, 333, -140], [8, 1060, 320, -153], [9, 1087, 404, -86], [10, 1078, 355, -118], [11, 1065, 335, -127], [12, 1052, 323, -135], [13, 1066, 403, -97], [14, 1057, 358, -126], [15, 1048, 340, -124], [16, 1041, 329, -121], [17, 1042, 399, -107], [18, 1038, 361, -132], [19, 1036, 344, -132], [20, 1034, 330, -129]]) 
                    #Second Right hand at 90 degrees
                    HandTwoLandMarksDict[102] = np.array([[0, 1044, 461, 0], [1, 1063, 436, 3], [2, 1074, 404, -22], [3, 1062, 371, -49], [4, 1047, 347, -79], [5, 1107, 409, -59], [6, 1094, 362, -98], [7, 1075, 342, -122], [8, 1059, 330, -134], [9, 1091, 412, -81], [10, 1086, 362, -109], [11, 1072, 342, -117], [12, 1059, 330, -127], [13, 1069, 412, -100], [14, 1066, 363, -126], [15, 1055, 343, -123], [16, 1046, 329, -123], [17, 1043, 409, -117], [18, 1042, 370, -140], [19, 1040, 351, -140], [20, 1039, 336, -139]]) 
                    #Second Left hand at 180 degrees
                    HandTwoLandMarksDict[103] = np.array([[0, 1039, 471, 0], [1, 1053, 444, -19], [2, 1065, 414, -50], [3, 1057, 380, -77], [4, 1046, 355, -106], [5, 1108, 419, -61], [6, 1093, 375, -98], [7, 1076, 354, -122], [8, 1060, 344, -135], [9, 1093, 423, -70], [10, 1086, 376, -99], [11, 1071, 356, -114], [12, 1056, 343, -125], [13, 1072, 425, -80], [14, 1067, 378, -108], [15, 1057, 357, -110], [16, 1047, 343, -110], [17, 1046, 422, -88], [18, 1044, 381, -114], [19, 1042, 361, -114], [20, 1041, 348, -112]]) 
                    #Second Right hand at 90 degrees
                    HandTwoLandMarksDict[104] = np.array([[0, 1041, 474, 0], [1, 1065, 453, -4], [2, 1077, 422, -35], [3, 1065, 386, -64], [4, 1048, 363, -98], [5, 1106, 428, -73], [6, 1091, 381, -112], [7, 1073, 360, -135], [8, 1058, 348, -147], [9, 1086, 430, -90], [10, 1080, 380, -121], [11, 1068, 359, -130], [12, 1055, 347, -140], [13, 1063, 430, -105], [14, 1060, 380, -133], [15, 1052, 360, -129], [16, 1045, 349, -127], [17, 1038, 425, -118], [18, 1039, 385, -141], [19, 1039, 366, -138], [20, 1040, 352, -135]]) 
                    #Second Left hand at 90 degrees
                    HandTwoLandMarksDict[105] = np.array([[0, 1042, 479, 0], [1, 1060, 457, -2], [2, 1072, 423, -31], [3, 1061, 389, -59], [4, 1047, 365, -90], [5, 1108, 429, -67], [6, 1093, 386, -106], [7, 1075, 366, -127], [8, 1059, 354, -139], [9, 1093, 432, -87], [10, 1088, 385, -119], [11, 1073, 364, -129], [12, 1058, 351, -136], [13, 1072, 431, -104], [14, 1068, 384, -133], [15, 1058, 363, -130], [16, 1049, 349, -126], [17, 1046, 427, -118], [18, 1044, 386, -142], [19, 1042, 368, -137], [20, 1041, 355, -132]]) 
                    HandTwoLandMarksDict[106] = np.array([[0, 1038, 478, 0], [1, 1053, 457, -25], [2, 1065, 429, -58], [3, 1060, 396, -85], [4, 1050, 372, -114], [5, 1107, 436, -75], [6, 1092, 391, -114], [7, 1075, 370, -140], [8, 1060, 358, -155], [9, 1094, 438, -79], [10, 1085, 391, -110], [11, 1071, 370, -122], [12, 1057, 358, -133], [13, 1075, 437, -84], [14, 1067, 392, -113], [15, 1058, 371, -113], [16, 1050, 359, -112], [17, 1050, 432, -89], [18, 1046, 393, -116], [19, 1044, 374, -115], [20, 1041, 362, -112]]) 
                    HandTwoLandMarksDict[107] = np.array([[0, 1042, 487, 0], [1, 1061, 468, 1], [2, 1074, 437, -23], [3, 1068, 405, -47], [4, 1054, 382, -75], [5, 1108, 444, -66], [6, 1093, 398, -100], [7, 1077, 377, -120], [8, 1063, 365, -131], [9, 1092, 446, -86], [10, 1085, 397, -112], [11, 1073, 376, -118], [12, 1060, 363, -126], [13, 1070, 445, -102], [14, 1066, 398, -129], [15, 1057, 376, -125], [16, 1049, 362, -124], [17, 1044, 441, -116], [18, 1045, 400, -141], [19, 1044, 381, -139], [20, 1042, 368, -136]]) 
                    HandTwoLandMarksDict[108] = np.array([[0, 1040, 493, 0], [1, 1060, 474, 5], [2, 1072, 445, -20], [3, 1067, 414, -46], [4, 1055, 391, -76], [5, 1108, 450, -70], [6, 1092, 406, -104], [7, 1075, 384, -120], [8, 1060, 373, -128], [9, 1093, 453, -91], [10, 1087, 405, -117], [11, 1072, 384, -120], [12, 1058, 371, -123], [13, 1072, 452, -107], [14, 1068, 403, -132], [15, 1058, 382, -123], [16, 1049, 371, -116], [17, 1046, 446, -120], [18, 1045, 404, -142], [19, 1043, 385, -134], [20, 1041, 374, -125]]) 
                    HandTwoLandMarksDict[109] = np.array([[0, 1037, 498, 0], [1, 1053, 477, -11], [2, 1064, 446, -40], [3, 1058, 413, -68], [4, 1046, 389, -98], [5, 1108, 456, -66], [6, 1092, 413, -105], [7, 1075, 392, -133], [8, 1061, 379, -150], [9, 1095, 460, -79], [10, 1088, 415, -111], [11, 1074, 393, -125], [12, 1060, 379, -135], [13, 1075, 459, -92], [14, 1070, 413, -123], [15, 1062, 392, -122], [16, 1053, 378, -120], [17, 1050, 454, -103], [18, 1050, 414, -128], [19, 1049, 396, -126], [20, 1047, 383, -122]]) 
                    HandTwoLandMarksDict[110]= np.array([[0, 1040, 500, 0], [1, 1060, 483, -4], [2, 1071, 453, -36], [3, 1064, 419, -66], [4, 1051, 396, -100], [5, 1108, 463, -88], [6, 1093, 419, -126], [7, 1076, 397, -142], [8, 1061, 385, -151], [9, 1093, 467, -107], [10, 1087, 418, -140], [11, 1072, 397, -147], [12, 1058, 385, -152], [13, 1070, 466, -121], [14, 1067, 416, -155], [15, 1057, 394, -150], [16, 1048, 382, -145], [17, 1044, 460, -132], [18, 1046, 417, -161], [19, 1044, 398, -156], [20, 1042, 386, -149]]) 
                    HandTwoLandMarksDict[111]= np.array([[0, 1038, 509, 0], [1, 1063, 494, -3], [2, 1077, 467, -33], [3, 1073, 435, -61], [4, 1059, 413, -93], [5, 1102, 471, -97], [6, 1088, 423, -133], [7, 1073, 400, -144], [8, 1059, 387, -148], [9, 1083, 472, -114], [10, 1077, 420, -144], [11, 1064, 398, -144], [12, 1051, 386, -145], [13, 1061, 469, -127], [14, 1059, 420, -154], [15, 1052, 398, -145], [16, 1044, 386, -138], [17, 1037, 463, -136], [18, 1041, 423, -163], [19, 1041, 404, -158], [20, 1039, 391, -151]]) 
                    HandTwoLandMarksDict[112]= np.array([[0, 1037, 516, 0], [1, 1055, 496, 1], [2, 1067, 464, -25], [3, 1060, 432, -51], [4, 1047, 410, -82], [5, 1102, 471, -73], [6, 1087, 426, -107], [7, 1070, 405, -124], [8, 1055, 394, -133], [9, 1087, 475, -93], [10, 1080, 426, -122], [11, 1065, 405, -131], [12, 1051, 392, -139], [13, 1066, 475, -109], [14, 1062, 426, -137], [15, 1054, 403, -136], [16, 1045, 388, -135], [17, 1040, 470, -122], [18, 1040, 428, -147], [19, 1039, 409, -145], [20, 1038, 395, -142]]) 
                    HandTwoLandMarksDict[113]= np.array([[0, 1034, 521, 0], [1, 1055, 503, 2], [2, 1069, 475, -21], [3, 1067, 445, -46], [4, 1056, 424, -75], [5, 1099, 479, -72], [6, 1085, 434, -108], [7, 1068, 412, -125], [8, 1053, 401, -134], [9, 1084, 482, -92], [10, 1078, 433, -122], [11, 1063, 411, -127], [12, 1049, 398, -132], [13, 1063, 480, -108], [14, 1060, 433, -135], [15, 1051, 411, -130], [16, 1042, 398, -126], [17, 1039, 475, -121], [18, 1039, 434, -145], [19, 1037, 416, -140], [20, 1034, 402, -135]]) 
                    #Second Right hand at 90 degrees
                    HandTwoLandMarksDict[114]= np.array([[0, 1034, 528, 0], [1, 1057, 512, 7], [2, 1071, 483, -16], [3, 1066, 453, -39], [4, 1052, 433, -68], [5, 1097, 488, -75], [6, 1082, 442, -106], [7, 1065, 422, -119], [8, 1051, 411, -125], [9, 1080, 489, -98], [10, 1075, 440, -125], [11, 1062, 418, -128], [12, 1048, 405, -133], [13, 1057, 487, -114], [14, 1057, 439, -140], [15, 1049, 417, -136], [16, 1040, 403, -134], [17, 1031, 481, -127], [18, 1033, 441, -149], [19, 1032, 423, -144], [20, 1030, 409, -139]]) 
                    HandTwoLandMarksDict[115]= np.array([[0, 1025, 557, 0], [1, 1051, 543, -2], [2, 1067, 515, -29], [3, 1063, 484, -53], [4, 1049, 463, -81], [5, 1088, 521, -103], [6, 1075, 474, -130], [7, 1060, 452, -133], [8, 1049, 439, -134], [9, 1069, 523, -120], [10, 1065, 472, -147], [11, 1052, 450, -144], [12, 1040, 438, -146], [13, 1046, 520, -130], [14, 1046, 471, -155], [15, 1040, 448, -150], [16, 1032, 434, -148], [17, 1021, 512, -136], [18, 1025, 473, -164], [19, 1026, 454, -164], [20, 1025, 439, -164]]) 
                    HandTwoLandMarksDict[116]= np.array([[0, 1022, 561, 0], [1, 1045, 546, -7], [2, 1060, 518, -39], [3, 1050, 482, -68], [4, 1034, 459, -100], [5, 1085, 527, -100], [6, 1073, 478, -135], [7, 1056, 457, -148], [8, 1042, 446, -155], [9, 1066, 528, -116], [10, 1063, 475, -145], [11, 1051, 454, -150], [12, 1037, 443, -157], [13, 1043, 526, -125], [14, 1046, 476, -152], [15, 1039, 454, -148], [16, 1031, 440, -146], [17, 1019, 518, -132], [18, 1025, 479, -155], [19, 1026, 461, -151], [20, 1025, 449, -148]]) 
                    HandTwoLandMarksDict[117]= np.array([[0, 1020, 567, 0], [1, 1044, 553, -5], [2, 1059, 524, -37], [3, 1051, 490, -65], [4, 1037, 468, -97], [5, 1083, 532, -96], [6, 1072, 485, -131], [7, 1056, 464, -142], [8, 1043, 455, -148], [9, 1065, 533, -113], [10, 1062, 482, -145], [11, 1050, 460, -150], [12, 1037, 449, -155], [13, 1043, 529, -125], [14, 1044, 481, -155], [15, 1037, 458, -153], [16, 1029, 446, -151], [17, 1019, 522, -134], [18, 1024, 484, -161], [19, 1025, 465, -161], [20, 1024, 452, -160]]) 
                    #Second Left hand at 90 degrees
                    HandTwoLandMarksDict[118]= np.array([[0, 1016, 571, 0], [1, 1039, 557, -5], [2, 1054, 528, -32], [3, 1048, 495, -55], [4, 1035, 473, -83], [5, 1084, 533, -90], [6, 1068, 489, -119], [7, 1053, 469, -128], [8, 1039, 458, -132], [9, 1066, 535, -106], [10, 1060, 485, -136], [11, 1047, 465, -140], [12, 1033, 453, -144], [13, 1044, 533, -118], [14, 1042, 483, -148], [15, 1035, 462, -145], [16, 1026, 449, -143], [17, 1018, 527, -126], [18, 1022, 485, -153], [19, 1021, 467, -151], [20, 1020, 454, -148]]) 
                    HandTwoLandMarksDict[119] = np.array([[0, 1016, 574, 0], [1, 1031, 555, -19], [2, 1042, 523, -55], [3, 1033, 488, -84], [4, 1021, 462, -115], [5, 1080, 537, -103], [6, 1066, 491, -134], [7, 1050, 470, -146], [8, 1036, 459, -154], [9, 1066, 539, -111], [10, 1061, 489, -140], [11, 1047, 470, -145], [12, 1033, 459, -151], [13, 1045, 536, -115], [14, 1044, 487, -142], [15, 1035, 468, -134], [16, 1026, 458, -131], [17, 1019, 528, -118], [18, 1021, 487, -142], [19, 1020, 470, -138], [20, 1018, 459, -134]]) 
                    #Second Right hand at 90 degrees
                    HandTwoLandMarksDict[120] = np.array([[0, 1015, 579, 0], [1, 1037, 565, -2], [2, 1051, 534, -29], [3, 1045, 500, -52], [4, 1031, 478, -80], [5, 1079, 541, -89], [6, 1065, 495, -116], [7, 1050, 475, -121], [8, 1037, 466, -122], [9, 1062, 543, -106], [10, 1057, 492, -132], [11, 1044, 471, -132], [12, 1031, 460, -134], [13, 1040, 541, -118], [14, 1039, 491, -144], [15, 1032, 469, -138], [16, 1024, 456, -134], [17, 1014, 534, -126], [18, 1019, 493, -150], [19, 1019, 475, -146], [20, 1017, 463, -143]]) 
                    HandTwoLandMarksDict[121] = np.array([[0, 1013, 582, 0], [1, 1036, 569, -1], [2, 1051, 542, -29], [3, 1044, 509, -53], [4, 1029, 488, -82], [5, 1078, 546, -95], [6, 1064, 500, -127], [7, 1048, 480, -135], [8, 1034, 470, -140], [9, 1059, 549, -113], [10, 1055, 498, -143], [11, 1042, 476, -146], [12, 1029, 464, -151], [13, 1035, 547, -125], [14, 1037, 498, -155], [15, 1029, 475, -153], [16, 1021, 462, -151], [17, 1009, 541, -133], [18, 1016, 501, -160], [19, 1016, 482, -157], [20, 1015, 470, -154]]) 
                    #Second Left hand at 90 degrees
                    HandTwoLandMarksDict[122] = np.array([[0, 1011, 588, 0], [1, 1032, 572, -8], [2, 1045, 541, -39], [3, 1036, 507, -67], [4, 1022, 484, -98], [5, 1076, 550, -88], [6, 1063, 505, -123], [7, 1047, 486, -136], [8, 1034, 477, -143], [9, 1060, 552, -105], [10, 1057, 503, -140], [11, 1041, 483, -147], [12, 1028, 471, -154], [13, 1038, 550, -118], [14, 1039, 501, -153], [15, 1030, 479, -154], [16, 1020, 466, -154], [17, 1013, 542, -128], [18, 1018, 505, -161], [19, 1018, 485, -164], [20, 1016, 472, -164]]) 
                    #Second Right hand at 90 degrees
                    HandTwoLandMarksDict[123] = np.array([[0, 1007, 590, 0], [1, 1031, 577, 0], [2, 1048, 551, -26], [3, 1047, 520, -48], [4, 1035, 499, -75], [5, 1074, 554, -92], [6, 1062, 508, -123], [7, 1046, 487, -131], [8, 1033, 477, -135], [9, 1055, 555, -109], [10, 1052, 504, -138], [11, 1040, 484, -139], [12, 1028, 473, -143], [13, 1032, 552, -121], [14, 1033, 504, -148], [15, 1026, 482, -144], [16, 1018, 469, -141], [17, 1006, 545, -130], [18, 1012, 506, -153], [19, 1013, 488, -149], [20, 1012, 476, -146]]) 
                    #Second Left hand at 90 degrees
                    HandTwoLandMarksDict[124] = np.array([[0, 1004, 595, 0], [1, 1029, 582, 2], [2, 1046, 556, -22], [3, 1043, 524, -45], [4, 1030, 502, -73], [5, 1071, 559, -88], [6, 1059, 512, -118], [7, 1045, 492, -128], [8, 1032, 481, -132], [9, 1052, 560, -107], [10, 1048, 509, -135], [11, 1036, 488, -140], [12, 1025, 477, -145], [13, 1029, 558, -120], [14, 1030, 509, -147], [15, 1024, 487, -146], [16, 1016, 474, -144], [17, 1005, 551, -128], [18, 1011, 511, -151], [19, 1012, 494, -148], [20, 1011, 482, -145]]) 
                    HandTwoLandMarksDict[125] = np.array([[0, 1004, 598, 0], [1, 1027, 584, -5], [2, 1043, 556, -36], [3, 1037, 523, -63], [4, 1025, 500, -93], [5, 1073, 564, -99], [6, 1061, 518, -132], [7, 1045, 497, -143], [8, 1031, 488, -147], [9, 1054, 566, -115], [10, 1051, 515, -148], [11, 1038, 493, -151], [12, 1026, 483, -154], [13, 1031, 563, -126], [14, 1031, 514, -157], [15, 1023, 491, -152], [16, 1016, 480, -148], [17, 1005, 556, -133], [18, 1010, 515, -158], [19, 1010, 496, -154], [20, 1009, 485, -149]]) 
                    HandTwoLandMarksDict[126] = np.array([[0, 1003, 601, 0], [1, 993, 576, -73], [2, 998, 544, -126], [3, 1008, 517, -154], [4, 1012, 495, -180], [5, 1038, 570, -201], [6, 1032, 522, -243], [7, 1023, 498, -251], [8, 1017, 482, -253], [9, 1054, 575, -172], [10, 1052, 522, -214], [11, 1036, 500, -210], [12, 1022, 489, -207], [13, 1061, 572, -136], [14, 1053, 521, -166], [15, 1037, 504, -149], [16, 1027, 499, -138], [17, 1061, 565, -103], [18, 1055, 527, -127], [19, 1041, 513, -119], [20, 1033, 508, -110]]) 
                    HandTwoLandMarksDict[127] = np.array([[0, 1003, 602, 0], [1, 1024, 589, -7], [2, 1038, 563, -38], [3, 1032, 531, -64], [4, 1019, 510, -96], [5, 1069, 573, -99], [6, 1057, 528, -131], [7, 1043, 505, -143], [8, 1030, 493, -150], [9, 1052, 577, -114], [10, 1048, 525, -145], [11, 1035, 504, -151], [12, 1023, 492, -158], [13, 1030, 574, -123], [14, 1029, 524, -153], [15, 1022, 501, -150], [16, 1015, 487, -148], [17, 1005, 567, -129], [18, 1010, 526, -154], [19, 1010, 508, -149], [20, 1009, 497, -144]]) 
                    HandTwoLandMarksDict[128] = np.array([[0, 997, 605, 0], [1, 1020, 593, -11], [2, 1037, 567, -44], [3, 1033, 534, -71], [4, 1021, 511, -104], [5, 1068, 576, -102], [6, 1056, 531, -136], [7, 1041, 508, -148], [8, 1029, 496, -154], [9, 1050, 579, -116], [10, 1047, 530, -148], [11, 1034, 507, -153], [12, 1022, 494, -160], [13, 1028, 575, -123], [14, 1028, 528, -155], [15, 1021, 505, -151], [16, 1014, 491, -148], [17, 1003, 567, -128], [18, 1008, 527, -153], [19, 1008, 510, -148], [20, 1007, 498, -142]]) 
                    HandTwoLandMarksDict[129] = np.array([[0, 997, 606, 0], [1, 1022, 595, -2], [2, 1039, 571, -29], [3, 1039, 542, -53], [4, 1029, 521, -84], [5, 1068, 578, -97], [6, 1056, 533, -128], [7, 1042, 511, -138], [8, 1029, 498, -144], [9, 1049, 581, -114], [10, 1045, 532, -146], [11, 1033, 509, -152], [12, 1021, 495, -160], [13, 1025, 578, -125], [14, 1026, 531, -157], [15, 1020, 508, -156], [16, 1014, 494, -156], [17, 1000, 570, -133], [18, 1006, 531, -161], [19, 1006, 512, -161], [20, 1007, 499, -158]]) 
                    action_word_symbol = "Day"
                else:
                    action_word_symbol = ""   #"Not Available"

        if action_word_symbol != previous_action_word_symbol:
            previous_action_word_symbol = action_word_symbol

        mi.vision.putText(action_word_video, action_word_symbol, (20, 200), mi.vision.FONT_HERSHEY_COMPLEX,2, (255, 0, 0), 2)
        mi.vision.imshow("Image", action_word_video)
        mi.vision.waitKey(1)

    if mi.cvs.config_data['log_hand_landmarks_to_file'] == "True":
        if mi.cvs.config_data['take_sample_data'] == "False":
            #mi.cvs.log.open_log_file(mi.cvs.config_data['take_sample_data_for_symbol'])

            is_log_active = False
            mi.cvs.log.write_message("Log Ended","hand_1")
            mi.cvs.log.write_message("Log Ended","hand_2")

    
    #screen.release()
    return action_word_symbol

def draw_landmarks(image, results):
    mi.mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS) # Draw face connections
    mi.mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS) # Draw pose connections
    mi.mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS) # Draw left hand connections
    mi.mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS) # Draw right hand connections

HandOneLandMarksDict = {}
HandOneLandMarksCount = -1
HandOneLandMarksDiffDict = {}
HandOneLandMarksDiffCount = -1 

HandTwoLandMarksDict = {}
HandTwoLandMarksCount = -1 
HandTwoLandMarksDiffDict = {}
HandTwoLandMarksDiffCount = -1 

HandLandMarksDict = {}
HandLandMarksCount = 0
DiffHandLandMarksDict = {}
DiffHandLandMarksCount = 0

no_of_signs_changed = 0
is_positive = True
display_word = False

your_sign_number = 0
your_sign_display = False

is_handone_moving = False
is_handtwo_moving = False
is_handone_moving_x_direction = False
is_handone_moving_y_direction = False
is_handone_moving_z_direction = False
is_handtwo_moving_x_direction = False
is_handtwo_moving_y_direction = False
is_handtwo_moving_z_direction = False

def is_hand_stand_still(DiffHandLandMarks,tolerance):
    if mi.cfs.diff(DiffHandLandMarks[8][1],0,tolerance)  == True and mi.cfs.diff(DiffHandLandMarks[12][1],0,tolerance) == True and \
       mi.cfs.diff(DiffHandLandMarks[16][1],0,tolerance) == True and mi.cfs.diff(DiffHandLandMarks[20][1],0,tolerance) == True and \
       mi.cfs.diff(DiffHandLandMarks[8][2],0,tolerance)  == True and mi.cfs.diff(DiffHandLandMarks[12][2],0,tolerance) == True and \
       mi.cfs.diff(DiffHandLandMarks[16][2],0,tolerance) == True and mi.cfs.diff(DiffHandLandMarks[20][2],0,tolerance) == True and \
       mi.cfs.diff(DiffHandLandMarks[8][3],0,tolerance)  == True and mi.cfs.diff(DiffHandLandMarks[12][3],0,tolerance) == True and \
       mi.cfs.diff(DiffHandLandMarks[16][3],0,tolerance) == True and mi.cfs.diff(DiffHandLandMarks[20][3],0,tolerance) == True :
        return True
    else:
        return False

def is_moving_in_a_direction(DiffHandLandMarks,direction,tolerance):
    co_ordinate_no = 0
    if direction == "x" or direction == "X":
        co_ordinate_no = 1
    elif direction == "y" or direction == "Y":
        co_ordinate_no = 2
    elif direction == "z" or direction == "Z":
        co_ordinate_no = 3
    else:
        return None

    if mi.cfs.diff_in_direction(DiffHandLandMarks[8][co_ordinate_no],0,tolerance)  == 0 and mi.cfs.diff_in_direction(DiffHandLandMarks[12][co_ordinate_no],0,tolerance) == 0 and \
       mi.cfs.diff_in_direction(DiffHandLandMarks[16][co_ordinate_no],0,tolerance) == 0 and mi.cfs.diff_in_direction(DiffHandLandMarks[20][co_ordinate_no],0,tolerance) == 0:
        return 0
    else:
        if mi.cfs.diff_in_direction(DiffHandLandMarks[8][co_ordinate_no],0,tolerance)  > 0 and mi.cfs.diff_in_direction(DiffHandLandMarks[12][co_ordinate_no],0,tolerance) > 0 and \
           mi.cfs.diff_in_direction(DiffHandLandMarks[16][co_ordinate_no],0,tolerance) > 0 and mi.cfs.diff_in_direction(DiffHandLandMarks[20][co_ordinate_no],0,tolerance) > 0 :
           return 1
        elif mi.cfs.diff_in_direction(DiffHandLandMarks[8][co_ordinate_no],0,tolerance)  < 0 and mi.cfs.diff_in_direction(DiffHandLandMarks[12][co_ordinate_no],0,tolerance) < 0 and \
             mi.cfs.diff_in_direction(DiffHandLandMarks[16][co_ordinate_no],0,tolerance) < 0 and mi.cfs.diff_in_direction(DiffHandLandMarks[20][co_ordinate_no],0,tolerance) < 0 :
           return -1
        else:
           return -2

def hand_movement_in_direction(is_hand_one,direction,HandOneLandMarksDiff_element,tolerance,point,print=False):
    hand_name = ""
    if is_hand_one == True:
        hand_name = "Hand 1"
    else:
        hand_name = "Hand 2"

    specific_direction_movement = is_moving_in_a_direction(HandOneLandMarksDiff_element,direction,tolerance)
    return specific_direction_movement

def get_action_word(hand_1_data,hand_2_data):
    action_word_pattern_mached = False
    action_word_symbol = ""

    return action_word_symbol

def action_words_display():  
    global is_log_active
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

    mi.cvs.log = mi.log.logging()
    if mi.cvs.config_data['log_hand_landmarks_to_file'] == "True":
        if mi.cvs.config_data['take_sample_data'] == "False":
            mi.cvs.log.open_log_file(mi.cvs.config_data['take_sample_data_for_symbol'])

            is_log_active = True
            mi.cvs.log.write_message("Log started","hand_1")
            mi.cvs.log.write_message("Log started","hand_2")

    hand_detector = mi.HandTrackingModule.handDetector()
    while True:
        success, screen_video = screen.read()  
        if screen_video is None:
            return symbol
            #break

        screen_video = mi.vision.flip(screen_video,1)
        mi.vision.putText(screen_video, "Action Words" , (800, 50), mi.vision.FONT_HERSHEY_COMPLEX,1, (255, 0, 0), 2)

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
           symbol = get_single_hand_action_word(screen)
        elif NoOfHands == 2:
           symbol = get_two_hand_action_word(screen)
        else:
            symbol = get_two_hand_action_word(screen)

        if symbol != previous_symbol and symbol !="":
            previous_symbol = symbol

        #print(action_word_symbol + " at action_words_display function")
        mi.vision.putText(screen_video, "Action Words", (800, 50), mi.vision.FONT_HERSHEY_COMPLEX,1, (255, 0, 0), 2)
        mi.vision.putText(screen_video, symbol, (20, 200), mi.vision.FONT_HERSHEY_COMPLEX,2, (255, 0, 0), 2)
        mi.vision.imshow("Image", screen_video)
        mi.vision.waitKey(1)

    if mi.cvs.config_data['log_hand_landmarks_to_file'] == "True":
        if mi.cvs.config_data['take_sample_data'] == "False":
            #mi.cvs.log.open_log_file(mi.cvs.config_data['take_sample_data_for_symbol'])

            is_log_active = False
            mi.cvs.log.write_message("Log Ended","hand_1")
            mi.cvs.log.write_message("Log Ended","hand_2")

    
    screen.release()
    return symbol

