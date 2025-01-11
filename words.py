
import modules_imported as mi
import hand_information as hi
import single_hand_symbols as shs 
import double_hand_letters as dhs
import sample_data      as sdata
import pyttsx3          as tts

       
def get_single_hand_word(hand_data):
    word_pattern_mached = False
    word_symbol = ""

    if (mi.cvs.config_data['include_words']['word']=='i') and \
         ( \
           ( \
            hand_data['is_hand_1']               == True  and \
            hand_data['is_right_hand']           == False and \
            hand_data['hand_orientation']        == 180    and \
            hand_data['is_thumb_opened']         == True  and \
            hand_data['is_index_finger_opened']  == True  and \
            hand_data['is_middle_finger_opened'] == False and \
            hand_data['is_ring_finger_opened']   == False and \
            hand_data['is_little_finger_opened'] == False  \
           ) \
         ):
        word_symbol =  "Word"
    elif (mi.cvs.config_data['include_words']['ii']=='i') and \
         ( \
           ( \
            hand_data['is_hand_1']               == True  and \
            hand_data['is_right_hand']           == True  and \
            hand_data['hand_orientation']        == 90    and \
            hand_data['is_thumb_opened']         == False and \
            hand_data['is_index_finger_opened']  == True  and \
            hand_data['is_middle_finger_opened'] == False and \
            hand_data['is_ring_finger_opened']   == False and \
            hand_data['is_little_finger_opened'] == False  \
           ) \
         )and hand_data['HandLandMarks'][5][3]>0 \
          and hand_data['HandLandMarks'][6][3]>0 \
          and hand_data['HandLandMarks'][7][3]>0 \
          and hand_data['HandLandMarks'][8][3]>0 \
          and hand_data['HandLandMarks'][6][3]  > hand_data['HandLandMarks'][5][3] \
          and hand_data['HandLandMarks'][7][3]  > hand_data['HandLandMarks'][5][3] \
          and hand_data['HandLandMarks'][9][3]  < hand_data['HandLandMarks'][8][3] \
          and hand_data['HandLandMarks'][13][3] < hand_data['HandLandMarks'][8][3] \
          and hand_data['HandLandMarks'][17][3] < hand_data['HandLandMarks'][8][3] :
        word_symbol =  "I"
    elif (mi.cvs.config_data['include_words']['you']=='i') and \
         ( \
           ( \
            hand_data['is_hand_1']               == True  and \
            hand_data['is_right_hand']           == True  and \
            hand_data['hand_orientation']        == 90    and \
            hand_data['is_thumb_opened']         == False and \
            hand_data['is_index_finger_opened']  == True  and \
            hand_data['is_middle_finger_opened'] == False and \
            hand_data['is_ring_finger_opened']   == False and \
            hand_data['is_little_finger_opened'] == False  \
           ) \
         )and hand_data['HandLandMarks'][5][3]<0 \
          and hand_data['HandLandMarks'][6][3]<0 \
          and hand_data['HandLandMarks'][7][3]<0 \
          and hand_data['HandLandMarks'][8][3]<0 \
          and hand_data['HandLandMarks'][6][3]  < hand_data['HandLandMarks'][5][3] \
          and hand_data['HandLandMarks'][7][3]  < hand_data['HandLandMarks'][5][3] \
          and hand_data['HandLandMarks'][9][3]  > hand_data['HandLandMarks'][8][3] \
          and hand_data['HandLandMarks'][13][3] > hand_data['HandLandMarks'][8][3] \
          and hand_data['HandLandMarks'][17][3] > hand_data['HandLandMarks'][8][3] :
        word_symbol =  "You"
    elif (mi.cvs.config_data['include_words']['this']=='i') and \
         ( \
           ( \
            hand_data['is_hand_1']               == True  and \
            hand_data['is_right_hand']           == True  and \
            hand_data['hand_orientation']        == 270   and \
            hand_data['is_thumb_opened']         == False and \
            hand_data['is_index_finger_opened']  == True  and \
            hand_data['is_middle_finger_opened'] == False and \
            hand_data['is_ring_finger_opened']   == False and \
            hand_data['is_little_finger_opened'] == False  \
           ) \
         )and hand_data['HandLandMarks'][5][3]<0 \
          and hand_data['HandLandMarks'][6][3]<0 \
          and hand_data['HandLandMarks'][7][3]<0 \
          and hand_data['HandLandMarks'][8][3]<0:
        word_symbol =  "This"
    elif (mi.cvs.config_data['include_words']['that']=='i') and \
         ( \
           ( \
            hand_data['is_hand_1']               == True  and \
            hand_data['is_right_hand']           == False and \
            hand_data['hand_orientation']        == 180   and \
            hand_data['is_thumb_opened']         == False and \
            hand_data['is_index_finger_opened']  == True  and \
            hand_data['is_middle_finger_opened'] == False and \
            hand_data['is_ring_finger_opened']   == False and \
            hand_data['is_little_finger_opened'] == False  \
           ) \
         )and hand_data['HandLandMarks'][5][3]<0 \
          and hand_data['HandLandMarks'][6][3]<0 \
          and hand_data['HandLandMarks'][7][3]<0 \
          and hand_data['HandLandMarks'][8][3]<0:
        word_symbol =  "That"
    elif len(hand_data['HandLandMarks']) !=0:
            if hand_data['HandLandMarks'][4][2]   < hand_data['HandLandMarks'][3][2]  \
                and hand_data['HandLandMarks'][4][2]  < hand_data['HandLandMarks'][2][2]  \
                and hand_data['HandLandMarks'][5][2]  < hand_data['HandLandMarks'][9][2]  \
                and hand_data['HandLandMarks'][5][2]  < hand_data['HandLandMarks'][13][2] \
                and hand_data['HandLandMarks'][5][2]  < hand_data['HandLandMarks'][17][2] \
                and hand_data['HandLandMarks'][9][2]  < hand_data['HandLandMarks'][13][2] \
                and hand_data['HandLandMarks'][9][2]  < hand_data['HandLandMarks'][17][2] \
                and hand_data['HandLandMarks'][13][2] < hand_data['HandLandMarks'][17][2] \
                and hand_data['HandLandMarks'][5][1]  > hand_data['HandLandMarks'][6][1]  \
                and hand_data['HandLandMarks'][9][1]  > hand_data['HandLandMarks'][10][1] \
                and hand_data['HandLandMarks'][13][1] > hand_data['HandLandMarks'][14][1] \
                and hand_data['HandLandMarks'][17][1] > hand_data['HandLandMarks'][18][1]:
                 word_symbol =  "Okay"
            else: 
                if hand_data['HandLandMarks'][4][2]   > hand_data['HandLandMarks'][3][2]  \
                    and hand_data['HandLandMarks'][4][2]  > hand_data['HandLandMarks'][2][2]  \
                    and hand_data['HandLandMarks'][5][2]  > hand_data['HandLandMarks'][9][2]  \
                    and hand_data['HandLandMarks'][5][2]  > hand_data['HandLandMarks'][13][2] \
                    and hand_data['HandLandMarks'][5][2]  > hand_data['HandLandMarks'][17][2] \
                    and hand_data['HandLandMarks'][9][2]  > hand_data['HandLandMarks'][13][2] \
                    and hand_data['HandLandMarks'][9][2]  > hand_data['HandLandMarks'][17][2] \
                    and hand_data['HandLandMarks'][13][2] > hand_data['HandLandMarks'][17][2] \
                    and hand_data['HandLandMarks'][5][1]  > hand_data['HandLandMarks'][6][1]  \
                    and hand_data['HandLandMarks'][9][1]  > hand_data['HandLandMarks'][10][1] \
                    and hand_data['HandLandMarks'][13][1] > hand_data['HandLandMarks'][14][1] \
                    and hand_data['HandLandMarks'][17][1] > hand_data['HandLandMarks'][18][1]:
                      word_symbol =  "Not Okay"
    elif shs.thumbs_up(hand_data['HandLandMarks']) == True:
        word_symbol = "Exit"

    return word_symbol

def get_two_hand_word(hand_1_data,hand_2_data):
    word_pattern_mached = False
    word_symbol = ""

    if  (mi.cvs.config_data['include_words']['place']=='i') and \
         ( \
           ( \
            hand_1_data['is_hand_1']               == True  and \
            hand_1_data['is_right_hand']           == True  and \
            #hand_1_data['hand_orientation']        == 0     and \
            hand_1_data['is_thumb_opened']         == False and \
            hand_1_data['is_index_finger_opened']  == True  and \
            hand_1_data['is_middle_finger_opened'] == False and \
            hand_1_data['is_ring_finger_opened']   == False and \
            hand_1_data['is_little_finger_opened'] == False and \
            hand_2_data['is_hand_1']               == False and \
            hand_2_data['is_right_hand']           == True  and \
            #hand_2_data['hand_orientation']        == 180   and \
            hand_2_data['is_thumb_opened']         == True  and \
            hand_2_data['is_index_finger_opened']  == True  and \
            hand_2_data['is_middle_finger_opened'] == True  and \
            hand_2_data['is_ring_finger_opened']   == True  and \
            hand_2_data['is_little_finger_opened'] == True      \
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
            hand_1_data['is_right_hand']           == True  and \
            #hand_1_data['hand_orientation']        == 180   and \
            hand_1_data['is_thumb_opened']         == True  and \
            hand_1_data['is_index_finger_opened']  == True  and \
            hand_1_data['is_middle_finger_opened'] == True  and \
            hand_1_data['is_ring_finger_opened']   == True  and \
            hand_1_data['is_little_finger_opened'] == True      \
           ) \
         ):
       word_symbol =  "Place"
    elif (mi.cvs.config_data['include_words']['time']=='i') and \
         ( \
           ( \
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
        word_symbol =  "Time"
    elif (mi.cvs.config_data['include_words']['doctor']=='i') and \
         ( \
           ( \
            hand_1_data['is_hand_1']               == True  and \
            hand_1_data['is_right_hand']           == True  and \
            #hand_1_data['hand_orientation']        == 0     and \
            #hand_1_data['is_thumb_opened']         == False and \
            hand_1_data['is_index_finger_opened']  == True  and \
            hand_1_data['is_middle_finger_opened'] == True  and \
            hand_1_data['is_ring_finger_opened']   == True  and \
            hand_1_data['is_little_finger_opened'] == True  and \
            hand_2_data['is_hand_1']               == False and \
            hand_2_data['is_right_hand']           == False and \
            #hand_2_data['hand_orientation']        == 180   and \
            #hand_2_data['is_thumb_opened']         == False and \
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
            #hand_2_data['is_thumb_opened']         == False and \
            hand_2_data['is_index_finger_opened']  == True  and \
            hand_2_data['is_middle_finger_opened'] == True  and \
            hand_2_data['is_ring_finger_opened']   == True  and \
            hand_2_data['is_little_finger_opened'] == True  and \
            hand_1_data['is_hand_1']               == True  and \
            hand_1_data['is_right_hand']           == False and \
            #hand_1_data['hand_orientation']        == 180   and \
            #hand_1_data['is_thumb_opened']         == False and \
            hand_1_data['is_index_finger_opened']  == False and \
            hand_1_data['is_middle_finger_opened'] == False and \
            hand_1_data['is_ring_finger_opened']   == False and \
            hand_1_data['is_little_finger_opened'] == False     \
           ) \
         ):
        word_symbol =  "Doctor"
    elif (mi.cvs.config_data['include_words']['name']=='i') and \
         ( \
           ( \
            hand_1_data['is_hand_1']               == True  and \
            hand_1_data['is_right_hand']           == True  and \
            #hand_1_data['hand_orientation']        == 0     and \
            hand_1_data['is_thumb_opened']         == False and \
            hand_1_data['is_index_finger_opened']  == True  and \
            hand_1_data['is_middle_finger_opened'] == True  and \
            hand_1_data['is_ring_finger_opened']   == False and \
            hand_1_data['is_little_finger_opened'] == False and \
            hand_2_data['is_hand_1']               == False and \
            hand_2_data['is_right_hand']           == True  and \
            #hand_2_data['hand_orientation']        == 180   and \
            hand_2_data['is_thumb_opened']         == True  and \
            hand_2_data['is_index_finger_opened']  == True  and \
            hand_2_data['is_middle_finger_opened'] == True  and \
            hand_2_data['is_ring_finger_opened']   == True  and \
            hand_2_data['is_little_finger_opened'] == True      \
           ) \
           or \
           ( \
            hand_2_data['is_hand_1']               == False and \
            hand_2_data['is_right_hand']           == True  and \
            #hand_2_data['hand_orientation']        == 0     and \
            hand_2_data['is_thumb_opened']         == False and \
            hand_2_data['is_index_finger_opened']  == True  and \
            hand_2_data['is_middle_finger_opened'] == True  and \
            hand_2_data['is_ring_finger_opened']   == False and \
            hand_2_data['is_little_finger_opened'] == False and \
            hand_1_data['is_hand_1']               == True  and \
            hand_1_data['is_right_hand']           == True  and \
            #hand_1_data['hand_orientation']        == 180   and \
            hand_1_data['is_thumb_opened']         == True  and \
            hand_1_data['is_index_finger_opened']  == True  and \
            hand_1_data['is_middle_finger_opened'] == True  and \
            hand_1_data['is_ring_finger_opened']   == True  and \
            hand_1_data['is_little_finger_opened'] == True      \
           ) \
         ):
        word_symbol =  "Name"
    elif hand_1_data['HandLandMarks'][4][2]     < hand_1_data['HandLandMarks'][3][2]  \
        and hand_1_data['HandLandMarks'][4][2]  < hand_1_data['HandLandMarks'][2][2]  \
        and hand_1_data['HandLandMarks'][5][2]  < hand_1_data['HandLandMarks'][9][2]  \
        and hand_1_data['HandLandMarks'][5][2]  < hand_1_data['HandLandMarks'][13][2] \
        and hand_1_data['HandLandMarks'][5][2]  < hand_1_data['HandLandMarks'][17][2] \
        and hand_1_data['HandLandMarks'][9][2]  < hand_1_data['HandLandMarks'][13][2] \
        and hand_1_data['HandLandMarks'][9][2]  < hand_1_data['HandLandMarks'][17][2] \
        and hand_1_data['HandLandMarks'][13][2] < hand_1_data['HandLandMarks'][17][2] \
        and hand_1_data['HandLandMarks'][5][1]  > hand_1_data['HandLandMarks'][6][1]  \
        and hand_1_data['HandLandMarks'][9][1]  > hand_1_data['HandLandMarks'][10][1] \
        and hand_1_data['HandLandMarks'][13][1] > hand_1_data['HandLandMarks'][14][1] \
        and hand_1_data['HandLandMarks'][17][1] > hand_1_data['HandLandMarks'][18][1] \
        and hand_2_data['HandLandMarks'][4][2]  < hand_2_data['HandLandMarks'][3][2]  \
        and hand_2_data['HandLandMarks'][4][2]  < hand_2_data['HandLandMarks'][2][2]  \
        and hand_2_data['HandLandMarks'][5][2]  < hand_2_data['HandLandMarks'][9][2]  \
        and hand_2_data['HandLandMarks'][5][2]  < hand_2_data['HandLandMarks'][13][2] \
        and hand_2_data['HandLandMarks'][5][2]  < hand_2_data['HandLandMarks'][17][2] \
        and hand_2_data['HandLandMarks'][9][2]  < hand_2_data['HandLandMarks'][13][2] \
        and hand_2_data['HandLandMarks'][9][2]  < hand_2_data['HandLandMarks'][17][2] \
        and hand_2_data['HandLandMarks'][13][2] < hand_2_data['HandLandMarks'][17][2] \
        and hand_2_data['HandLandMarks'][5][1]  < hand_2_data['HandLandMarks'][6][1]  \
        and hand_2_data['HandLandMarks'][9][1]  < hand_2_data['HandLandMarks'][10][1] \
        and hand_2_data['HandLandMarks'][13][1] < hand_2_data['HandLandMarks'][14][1] \
        and hand_2_data['HandLandMarks'][17][1] < hand_2_data['HandLandMarks'][18][1]:
        action_word_symbol =  "Alright"
    else:
        word_symbol = "" #"Not Available"

    return word_symbol

def words_display():  
    sd =  sdata.sample_data()
    previous_symbol = ""
    symbol = ""
    screen = mi.vision.VideoCapture(0)
    screen_width, screen_height = mi.cfs.get_screen_widht_height()
    screen.set(3, screen_width)
    screen.set(4, screen_height)

    Hand_1_LandMarks = []
    Hand_2_LandMarks = []
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
            break

        screen_video = mi.vision.flip(screen_video,1)
        mi.vision.putText(screen_video, "Words" , (800, 50), mi.vision.FONT_HERSHEY_COMPLEX,1, (255, 0, 0), 2)

        if (mi.cvs.config_data['take_sample_data']=='False'): 
            screen_video = hand_detector.findHands(screen_video)
            Hand_1_LandMarks = hand_detector.findPosition(screen_video, 0, draw=False)
            Hand_2_LandMarks = hand_detector.findPosition(screen_video, 1, draw=False)
        else:
            Hand_1_LandMarks = sd.get_sample_data_for_symbol(mi.cvs.config_data['take_sample_data_for_symbol'],"hand_1") 
            Hand_2_LandMarks = sd.get_sample_data_for_symbol(mi.cvs.config_data['take_sample_data_for_symbol'],"hand_2") 


        hand_1_data = hand_1.get_hand_information(Hand_1_LandMarks,True) 
        hand_2_data = hand_2.get_hand_information(Hand_2_LandMarks,False) 
        
        if mi.cvs.config_data['log_hand_landmarks_to_file'] == "True":
            if mi.cvs.config_data['take_sample_data'] == "False" and is_log_active == True:
                if len(hand_1.HandLandMarks) != 0:
                    mi.cvs.log.write_hand_landmarks(hand_1,"hand_1")
                if len(hand_2.HandLandMarks) != 0:
                    mi.cvs.log.write_hand_landmarks(hand_2,"hand_2")

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
           symbol = get_single_hand_word(hand_data)
        elif NoOfHands == 2:
           symbol = get_two_hand_word(hand_1_data,hand_2_data)
        else:
            symbol = ""

        if symbol != previous_symbol:
            previous_symbol = symbol

        mi.vision.putText(screen_video, symbol, (100, 400), mi.vision.FONT_HERSHEY_COMPLEX,4, (255,0,0), 5)
        mi.vision.imshow("Image", screen_video)
        mi.vision.waitKey(1)

    if mi.cvs.config_data['log_hand_landmarks_to_file'] == "True":
        if mi.cvs.config_data['take_sample_data'] == "False":
            mi.cvs.log.open_log_file(mi.cvs.config_data['take_sample_data_for_symbol'])

            is_log_active = False
            mi.cvs.log.write_message("Log Ended","hand_1")
            mi.cvs.log.write_message("Log Ended","hand_2")

    screen.release()
    
    return symbol



