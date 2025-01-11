import modules_imported as mi

def double_hand_letters_display(hand_1_data,hand_2_data):
    symbol_matched = False
    symbol = ""

    if (\
         (\
            (hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0] - 1][1])\
            and \
            (hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0] - 1][1])\
         )\
         or \
         (\
            (hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0] - 1][1])\
            and \
            (hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0] - 1][1])\
         )\
       )\
         and \
         (\
          hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 2][2] \
          and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 2][2] \
          and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 2][2] \
          and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4] - 2][2] \
        ) \
        and \
        ( \
            hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4] - 2][2] \
        ) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],35):
        return "CapsLock"
    elif (mi.cvs.config_data['include_letters']['a']=='i') and \
        ((hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0] - 1][1] \
        or 
        hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0] - 1][1]) \
        and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 2][2] \
        and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 2][2] \
        and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 2][2] \
        and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4] - 2][2] \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 2][1],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 2][1],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 2][1],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4] - 2][1],35) \
        and (hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0] - 1][1] \
             or
            hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0] - 1][1]) \
        and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 2][2] \
        and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 2][2] \
        and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 2][2] \
        and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4] - 2][2] \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 2][1],35) \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 2][1],35) \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 2][1],35) \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4] - 2][1],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1],55) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][2],55)):
        if mi.cvs.config_data['CapsLock'] == "True":
            return "A"
        else:
            return "a"
    elif (mi.cvs.config_data['include_letters']['b']=='i') and \
        (mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][1],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][1],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][1],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][2],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2],35) \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1],35) \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][1],35) \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][1],35) \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][1],35) \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][2],35) \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2],35) \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2],35) \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1],55) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],55) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][1],55) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][1],55) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][1],55) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][2],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2],35)):
        if mi.cvs.config_data['CapsLock'] == "True":
            return "B"
        else:
            return "b"
    if (mi.cvs.config_data['include_letters']['d']=='i'):
        if len(hand_1_data['HandLandMarks']) !=0 and len(hand_2_data['HandLandMarks']) !=0:
            #print("FirstRightHandLandMarks and SecondLeftHandLandMarks")
            if (
            (   hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4] - 2][2] \
            and mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-1][1],35) \
            and mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-1][2],35) \
            and mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-3][1],35) \
            and mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-3][2],35)\
            )\
            or\
            (   hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4] - 2][2] \
            and mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-1][1],35) \
            and mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-1][2],35) \
            and mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-3][1],35) \
            and mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-3][2],35)\
            )\
            ):
             symbol_matched = True
        elif len(hand_2_data['HandLandMarks']) !=0 and len(hand_1_data['HandLandMarks']) !=0:
            #print("FirstLeftHandLandMarks and SecondRightHandLandMarks")
            if ( 
            (   hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4] - 2][2] \
            and mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-1][1],35) \
            and mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-1][2],35)\
            and mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-3][1],35) \
            and mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-3][2],35)\
            )\
            or\
            (   hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4] - 2][2] \
            and mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-1][1],35) \
            and mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-1][2],35) \
            and mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-3][1],35) \
            and mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-3][2],35)\
            )\
            ):
             symbol_matched = True
        elif len(hand_1_data['HandLandMarks']) !=0 and len(hand_2_data['HandLandMarks']) !=0:
            #print("FirstRightHandLandMarks and SecondRightHandLandMarks")
            if (
            (   hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4] - 2][2] \
            and mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-1][1],35) \
            and mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-1][2],35) \
            and mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-3][1],35) \
            and mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-3][2],35)\
            )\
            or\
            (   hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4] - 2][2] \
            and mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-1][1],35) \
            and mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-1][2],35) \
            and mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-3][1],35) \
            and mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-3][2],35)\
            )\
            ) :
             symbol_matched = True
        elif len(hand_1_data['HandLandMarks']) !=0 and len(hand_2_data['HandLandMarks']) !=0:
            #print("FirstLeftHandLandMarks and SecondLeftHandLandMarks")
            if( 
            (   hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4] - 2][2] \
            and mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-1][1],35) \
            and mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-1][2],35)\
            and mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-3][1],35) \
            and mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-3][2],35)\
            )\
            or\
            (   hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4] - 2][2] \
            and mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-1][1],35) \
            and mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-1][2],35) \
            and mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-3][1],35) \
            and mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-3][2],35)\
            )\
            ):
             symbol_matched = True
        if symbol_matched == True:
            #print("D")
            if mi.cvs.config_data['CapsLock'] == "True":
                return "D"
            else:
                return "d"
    if (mi.cvs.config_data['include_letters']['e']=='i') and \
       ( \
           ( \
            hand_1_data['is_hand_1']               == True  and \
            hand_1_data['is_right_hand']           == False and \
            hand_1_data['hand_orientation']        == 180   and \
            hand_1_data['is_thumb_opened']         == False and \
            hand_1_data['is_index_finger_opened']  == True  and \
            hand_1_data['is_middle_finger_opened'] == True  and \
            hand_1_data['is_ring_finger_opened']   == True  and \
            hand_1_data['is_little_finger_opened'] == False \
            #and hand_2_data['is_hand_1']               == False and \
            #hand_2_data['is_right_hand']           == False and \
            #hand_2_data['hand_orientation']        == 180   and \
            #hand_2_data['is_thumb_opened']         == True  and \
            #hand_2_data['is_index_finger_opened']  == False and \
            #hand_2_data['is_middle_finger_opened'] == False and \
            #hand_2_data['is_ring_finger_opened']   == False and \
            #hand_2_data['is_little_finger_opened'] == False \
            #and mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][8][1],hand_1_data['HandLandMarks'][5][1],hand_1_data['HandLandMarks'][8][1],35) and \
            #mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][7][2],hand_1_data['HandLandMarks'][5][2],hand_1_data['HandLandMarks'][13][2],35) \
           ) \
           or \
           ( \
            #hand_2_data['is_hand_1']               == False  and \
            hand_2_data['is_right_hand']           == False and \
            hand_2_data['hand_orientation']        == 180   and \
            hand_2_data['is_thumb_opened']         == False and \
            hand_2_data['is_index_finger_opened']  == True  and \
            hand_2_data['is_middle_finger_opened'] == True  and \
            hand_2_data['is_ring_finger_opened']   == True  and \
            hand_2_data['is_little_finger_opened'] == False \
            #and hand_1_data['is_hand_1']               == True and \
            #hand_1_data['is_right_hand']           == False and \
            #hand_1_data['hand_orientation']        == 180   and \
            #hand_1_data['is_thumb_opened']         == True  and \
            #hand_1_data['is_index_finger_opened']  == False and \
            #hand_1_data['is_middle_finger_opened'] == False and \
            #hand_1_data['is_ring_finger_opened']   == False and \
            #hand_1_data['is_little_finger_opened'] == False \
            #and mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][8][1],hand_2_data['HandLandMarks'][5][1],hand_1_data['HandLandMarks'][8][1],35) and \
            #mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][7][2],hand_2_data['HandLandMarks'][5][2],hand_1_data['HandLandMarks'][13][2],35) \
           ) \
       ):   
        if mi.cvs.config_data['CapsLock'] == "True":
            return "E"
        else:
            return "e"
    elif (mi.cvs.config_data['include_letters']['f']=='i') and \
         ( \
           ( \
            hand_1_data['is_hand_1']               == True  and \
            hand_1_data['is_right_hand']           == True and \
            hand_1_data['hand_orientation']        == 0     and \
            hand_1_data['is_thumb_opened']         == False and \
            hand_1_data['is_index_finger_opened']  == True  and \
            hand_1_data['is_middle_finger_opened'] == True  and \
            hand_1_data['is_ring_finger_opened']   == False and \
            hand_1_data['is_little_finger_opened'] == False and \
            hand_2_data['is_hand_1']               == False and \
            hand_2_data['is_right_hand']           == False and \
            hand_2_data['hand_orientation']        == 270   and \
            hand_2_data['is_thumb_opened']         == False and \
            hand_2_data['is_index_finger_opened']  == True  and \
            hand_2_data['is_middle_finger_opened'] == True  and \
            hand_2_data['is_ring_finger_opened']   == False and \
            hand_2_data['is_little_finger_opened'] == False and \
            mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][8][1],hand_1_data['HandLandMarks'][9][1],hand_1_data['HandLandMarks'][12][1],35) and \
            mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][8][2],hand_1_data['HandLandMarks'][5][2],hand_1_data['HandLandMarks'][9][2],35)  and \
            mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][12][1],hand_1_data['HandLandMarks'][9][1],hand_1_data['HandLandMarks'][12][1],35) and \
            mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][12][2],hand_1_data['HandLandMarks'][5][2],hand_1_data['HandLandMarks'][9][2],35) \
           ) \
           or \
           ( \
            hand_2_data['is_hand_1']               == False and \
            hand_2_data['is_right_hand']           == True  and \
            hand_2_data['hand_orientation']        == 0     and \
            hand_2_data['is_thumb_opened']         == False and \
            hand_2_data['is_index_finger_opened']  == True  and \
            hand_2_data['is_middle_finger_opened'] == True  and \
            hand_2_data['is_ring_finger_opened']   == False and \
            hand_2_data['is_little_finger_opened'] == False and \
            hand_1_data['is_hand_1']               == True  and \
            hand_1_data['is_right_hand']           == False and \
            hand_1_data['hand_orientation']        == 270   and \
            hand_1_data['is_thumb_opened']         == False and \
            hand_1_data['is_index_finger_opened']  == True  and \
            hand_1_data['is_middle_finger_opened'] == True  and \
            hand_1_data['is_ring_finger_opened']   == False and \
            hand_1_data['is_little_finger_opened'] == False and \
            mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][8][1],hand_2_data['HandLandMarks'][9][1],hand_2_data['HandLandMarks'][12][1],35) and \
            mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][8][2],hand_2_data['HandLandMarks'][5][2],hand_2_data['HandLandMarks'][9][2],35)  and \
            mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][12][1],hand_2_data['HandLandMarks'][9][1],hand_2_data['HandLandMarks'][12][1],35) and \
            mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][12][2],hand_2_data['HandLandMarks'][5][2],hand_2_data['HandLandMarks'][9][2],35) \
           ) \
         ):
        if mi.cvs.config_data['CapsLock'] == "True":
            return "F"
        else:
            return "f"
    elif (mi.cvs.config_data['include_letters']['g']=='i') and \
         ( \
           ( \
            hand_1_data['is_hand_1']               == True  and \
            hand_1_data['is_right_hand']           == False and \
            hand_1_data['hand_orientation']        == 180   and \
            hand_1_data['is_thumb_opened']         == False and \
            hand_1_data['is_index_finger_opened']  == False and \
            hand_1_data['is_middle_finger_opened'] == False and \
            hand_1_data['is_ring_finger_opened']   == False and \
            hand_1_data['is_little_finger_opened'] == False and \
            hand_2_data['is_hand_1']               == False and \
            hand_2_data['is_right_hand']           == True  and \
            hand_2_data['hand_orientation']        == 0     and \
            hand_2_data['is_thumb_opened']         == False and \
            hand_2_data['is_index_finger_opened']  == False and \
            hand_2_data['is_middle_finger_opened'] == False and \
            hand_2_data['is_ring_finger_opened']   == False and \
            hand_2_data['is_little_finger_opened'] == False and \
            ((hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2]) \
            or \
            (hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2]))\
           ) \
           or \
           ( \
            hand_2_data['is_hand_1']               == False  and \
            hand_2_data['is_right_hand']           == False and \
            hand_2_data['hand_orientation']        == 180   and \
            hand_2_data['is_thumb_opened']         == False and \
            hand_2_data['is_index_finger_opened']  == False and \
            hand_2_data['is_middle_finger_opened'] == False and \
            hand_2_data['is_ring_finger_opened']   == False and \
            hand_2_data['is_little_finger_opened'] == False and \
            hand_1_data['is_hand_1']               == True  and \
            hand_1_data['is_right_hand']           == True  and \
            hand_1_data['hand_orientation']        == 0     and \
            hand_1_data['is_thumb_opened']         == False and \
            hand_1_data['is_index_finger_opened']  == False and \
            hand_1_data['is_middle_finger_opened'] == False and \
            hand_1_data['is_ring_finger_opened']   == False and \
            hand_1_data['is_little_finger_opened'] == False and \
            ((hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2]) \
            or \
            (hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2]))\
           ) \
         ):
        if mi.cvs.config_data['CapsLock'] == "True":
            return "G"
        else:
            return "g"
    elif (mi.cvs.config_data['include_letters']['h']=='i') and \
         ( \
           ( \
            hand_1_data['is_hand_1']               == True  and \
            hand_1_data['is_right_hand']           == False and \
            hand_1_data['hand_orientation']        == 180   and \
            hand_1_data['is_thumb_opened']         == True  and \
            hand_1_data['is_index_finger_opened']  == True  and \
            hand_1_data['is_middle_finger_opened'] == True  and \
            hand_1_data['is_ring_finger_opened']   == True  and \
            hand_1_data['is_little_finger_opened'] == True  and \
            hand_2_data['is_hand_1']               == False and \
            hand_2_data['is_right_hand']           == False and \
            hand_2_data['hand_orientation']        == 90    and \
            hand_2_data['is_thumb_opened']         == True  and \
            hand_2_data['is_index_finger_opened']  == True  and \
            hand_2_data['is_middle_finger_opened'] == True  and \
            hand_2_data['is_ring_finger_opened']   == True  and \
            hand_2_data['is_little_finger_opened'] == True  \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][1] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][1] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][1] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][1] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][1] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][1] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][1] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] \
           ) \
           or \
           ( \
            hand_2_data['is_hand_1']               == False and \
            hand_2_data['is_right_hand']           == False and \
            hand_2_data['hand_orientation']        == 180   and \
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
            hand_1_data['is_little_finger_opened'] == True  \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][1] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][1] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][1] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][1] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][1] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][1] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][1] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] \
           ) \
         ):
        if mi.cvs.config_data['CapsLock'] == "True":
            return "H"
        else:
            return "h"
    elif (mi.cvs.config_data['include_letters']['j']=='i') and \
         ( \
           ( \
            hand_1_data['is_hand_1']               == True  and \
            hand_1_data['is_right_hand']           == False and \
            #hand_1_data['hand_orientation']        == 180   and \
            hand_1_data['is_thumb_opened']         == False and \
            hand_1_data['is_index_finger_opened']  == True  and \
            hand_1_data['is_middle_finger_opened'] == False and \
            hand_1_data['is_ring_finger_opened']   == False and \
            hand_1_data['is_little_finger_opened'] == False and \
            hand_2_data['is_hand_1']               == False and \
            hand_2_data['is_right_hand']           == True  and \
            #(hand_2_data['hand_orientation']       == 90   or  hand_2_data['hand_orientation']        == 0) and \
            hand_2_data['is_thumb_opened']         == True  and \
            hand_2_data['is_index_finger_opened']  == True  and \
            hand_2_data['is_middle_finger_opened'] == False and \
            hand_2_data['is_ring_finger_opened']   == False and \
            hand_2_data['is_little_finger_opened'] == False \
           ) \
           or \
           ( \
            hand_2_data['is_hand_1']               == False and \
            hand_2_data['is_right_hand']           == False and \
            #hand_2_data['hand_orientation']        == 180   and \
            hand_2_data['is_thumb_opened']         == False and \
            hand_2_data['is_index_finger_opened']  == True  and \
            hand_2_data['is_middle_finger_opened'] == False and \
            hand_2_data['is_ring_finger_opened']   == False and \
            hand_2_data['is_little_finger_opened'] == False and \
            hand_1_data['is_hand_1']               == True  and \
            hand_1_data['is_right_hand']           == True  and \
            #(hand_1_data['hand_orientation']       == 90   or  hand_1_data['hand_orientation']        == 0) and \
            hand_1_data['is_thumb_opened']         == True  and \
            hand_1_data['is_index_finger_opened']  == True  and \
            hand_1_data['is_middle_finger_opened'] == False and \
            hand_1_data['is_ring_finger_opened']   == False and \
            hand_1_data['is_little_finger_opened'] == False \
           ) \
         ):
        if mi.cvs.config_data['CapsLock'] == "True":
            return "J"
        else:
            return "j"
    elif (mi.cvs.config_data['include_letters']['k']=='i') and \
        ((hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0] - 1][1] \
        and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 2][2] \
        and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 2][2] \
        and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 2][2] \
        and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4] - 2][2] \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][2],55) \
        #and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],35) \
        and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][1] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-1][1] \
        and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][1] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-3][1]) \
        or \
        (hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0] - 1][1] \
        and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 2][2] \
        and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 2][2] \
        and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 2][2] \
        and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4] - 2][2] \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][2],55) \
        #and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],35) \
        and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][1] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-1][1] \
        and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][1] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-3][1]) \
       ):
        if mi.cvs.config_data['CapsLock'] == "True":
            return "K"
        else:
            return "k"
    elif (mi.cvs.config_data['include_letters']['m']=='i') and \
        ( \
        ( \
        hand_1_data['is_hand_1']               == True  and \
        hand_1_data['is_right_hand']           == False and \
        hand_1_data['hand_orientation']        == 180   and \
        hand_1_data['is_thumb_opened']         == True  and \
        hand_1_data['is_index_finger_opened']  == True  and \
        hand_1_data['is_middle_finger_opened'] == True  and \
        hand_1_data['is_ring_finger_opened']   == True  and \
        hand_1_data['is_little_finger_opened'] == True  and \
        hand_2_data['is_hand_1']               == False and \
        hand_2_data['is_right_hand']           == False and \
        hand_2_data['hand_orientation']        == 90    and \
        hand_2_data['is_thumb_opened']         == False and \
        hand_2_data['is_index_finger_opened']  == True  and \
        hand_2_data['is_middle_finger_opened'] == True  and \
        hand_2_data['is_ring_finger_opened']   == True  and \
        hand_2_data['is_little_finger_opened'] == False \
        #mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][8][1],hand_1_data['HandLandMarks'][9][1],hand_1_data['HandLandMarks'][12][1],35) and \
        #mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][8][2],hand_1_data['HandLandMarks'][5][2],hand_1_data['HandLandMarks'][9][2],35)  and \
        #mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][12][1],hand_1_data['HandLandMarks'][9][1],hand_1_data['HandLandMarks'][12][1],35) and \
        #mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][12][2],hand_1_data['HandLandMarks'][5][2],hand_1_data['HandLandMarks'][9][2],35) \
       )\
       or \
        ( \
        hand_2_data['is_hand_1']               == False and \
        hand_2_data['is_right_hand']           == False and \
        hand_2_data['hand_orientation']        == 180   and \
        hand_2_data['is_thumb_opened']         == True  and \
        hand_2_data['is_index_finger_opened']  == True  and \
        hand_2_data['is_middle_finger_opened'] == True  and \
        hand_2_data['is_ring_finger_opened']   == True  and \
        hand_2_data['is_little_finger_opened'] == True  and \
        hand_1_data['is_hand_1']               == True  and \
        hand_1_data['is_right_hand']           == False and \
        hand_1_data['hand_orientation']        == 90    and \
        hand_1_data['is_thumb_opened']         == False and \
        hand_1_data['is_index_finger_opened']  == True  and \
        hand_1_data['is_middle_finger_opened'] == True  and \
        hand_1_data['is_ring_finger_opened']   == True  and \
        hand_1_data['is_little_finger_opened'] == False \
        #mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][8][1],hand_1_data['HandLandMarks'][9][1],hand_1_data['HandLandMarks'][12][1],35) and \
        #mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][8][2],hand_1_data['HandLandMarks'][5][2],hand_1_data['HandLandMarks'][9][2],35)  and \
        #mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][12][1],hand_1_data['HandLandMarks'][9][1],hand_1_data['HandLandMarks'][12][1],35) and \
        #mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][12][2],hand_1_data['HandLandMarks'][5][2],hand_1_data['HandLandMarks'][9][2],35) \
       )\
        ):
        if mi.cvs.config_data['CapsLock'] == "True":
            return "M"
        else:
            return "m"
    elif (mi.cvs.config_data['include_letters']['n']=='i') and \
        ( \
        ( \
        hand_1_data['is_hand_1']               == True  and \
        hand_1_data['is_right_hand']           == False and \
        hand_1_data['hand_orientation']        == 180   and \
        hand_1_data['is_thumb_opened']         == True  and \
        hand_1_data['is_index_finger_opened']  == True  and \
        hand_1_data['is_middle_finger_opened'] == True  and \
        hand_1_data['is_ring_finger_opened']   == True  and \
        hand_1_data['is_little_finger_opened'] == True  and \
        hand_2_data['is_hand_1']               == False and \
        hand_2_data['is_right_hand']           == False and \
        hand_2_data['hand_orientation']        == 90    and \
        hand_2_data['is_thumb_opened']         == False and \
        hand_2_data['is_index_finger_opened']  == True  and \
        hand_2_data['is_middle_finger_opened'] == True  and \
        hand_2_data['is_ring_finger_opened']   == False and \
        hand_2_data['is_little_finger_opened'] == False \
        #mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][8][1],hand_1_data['HandLandMarks'][9][1],hand_1_data['HandLandMarks'][12][1],35) and \
        #mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][8][2],hand_1_data['HandLandMarks'][5][2],hand_1_data['HandLandMarks'][9][2],35)  and \
        #mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][12][1],hand_1_data['HandLandMarks'][9][1],hand_1_data['HandLandMarks'][12][1],35) and \
        #mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][12][2],hand_1_data['HandLandMarks'][5][2],hand_1_data['HandLandMarks'][9][2],35) \
       )\
       or \
        ( \
        hand_2_data['is_hand_1']               == False and \
        hand_2_data['is_right_hand']           == False and \
        hand_2_data['hand_orientation']        == 180   and \
        hand_2_data['is_thumb_opened']         == True  and \
        hand_2_data['is_index_finger_opened']  == True  and \
        hand_2_data['is_middle_finger_opened'] == True  and \
        hand_2_data['is_ring_finger_opened']   == True  and \
        hand_2_data['is_little_finger_opened'] == True  and \
        hand_1_data['is_hand_1']               == True  and \
        hand_1_data['is_right_hand']           == False and \
        hand_1_data['hand_orientation']        == 90    and \
        hand_1_data['is_thumb_opened']         == False and \
        hand_1_data['is_index_finger_opened']  == True  and \
        hand_1_data['is_middle_finger_opened'] == True  and \
        hand_1_data['is_ring_finger_opened']   == False and \
        hand_1_data['is_little_finger_opened'] == False \
        #mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][8][1],hand_1_data['HandLandMarks'][9][1],hand_1_data['HandLandMarks'][12][1],35) and \
        #mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][8][2],hand_1_data['HandLandMarks'][5][2],hand_1_data['HandLandMarks'][9][2],35)  and \
        #mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][12][1],hand_1_data['HandLandMarks'][9][1],hand_1_data['HandLandMarks'][12][1],35) and \
        #mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][12][2],hand_1_data['HandLandMarks'][5][2],hand_1_data['HandLandMarks'][9][2],35) \
       )\
        ):
        if mi.cvs.config_data['CapsLock'] == "True":
            return "N"
        else:
            return "n"
    elif (mi.cvs.config_data['include_letters']['p']=='i') and \
        ((mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][1],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][1],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][1],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][2],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2],35) \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],35) \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],35) \
        and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 2][2] \
        and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 2][2] \
        and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 2][2] \
        and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4] - 2][2]) \
        or \
        (mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1],35) \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][1],35) \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][1],35) \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][1],35) \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][2],35) \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2],35) \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2],35) \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],35) \
        and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 2][2] \
        and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 2][2] \
        and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 2][2] \
        and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4] - 2][2])):
        if mi.cvs.config_data['CapsLock'] == "True":
            return "P"
        else:
            return "p"
    elif (mi.cvs.config_data['include_letters']['q']=='i') and \
        ((mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][1],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][1],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][1],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][2],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2],35) \
        and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2],35) \
        and mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]-2][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]-1][1],35) \
        and mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]-2][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]-1][2],35) \
        and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 2][2] \
        and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 2][2] \
        and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 2][2] \
        and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4] - 2][2]) \
        or \
        (mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1],35) \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][1],35) \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][1],35) \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][1],35) \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][2],35) \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2],35) \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2],35) \
        and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2],35) \
        and mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]-2][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]-1][1],35) \
        and mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]-2][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]-1][2],35) \
        and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 2][2] \
        and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 2][2] \
        and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 2][2] \
        and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4] - 2][2])):
        if mi.cvs.config_data['CapsLock'] == "True":
            return "Q"
        else:
            return "q"
    elif (mi.cvs.config_data['include_letters']['r']=='i') and \
         ( \
           ( \
            hand_1_data['is_hand_1']               == True  and \
            hand_1_data['is_right_hand']           == False and \
            hand_1_data['hand_orientation']        == 180   and \
            #hand_1_data['is_thumb_opened']         == False and \
            hand_1_data['is_index_finger_opened']  == True  and \
            hand_1_data['is_middle_finger_opened'] == True  and \
            hand_1_data['is_ring_finger_opened']   == True  and \
            hand_1_data['is_little_finger_opened'] == True  \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][2] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]-2][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][2] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]-2][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][2] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]-2][2] \
           ) \
           or \
           ( \
            hand_2_data['is_hand_1']               == False and \
            hand_2_data['is_right_hand']           == False and \
            hand_2_data['hand_orientation']        == 180   and \
            #hand_2_data['is_thumb_opened']         == False and \
            hand_2_data['is_index_finger_opened']  == True  and \
            hand_2_data['is_middle_finger_opened'] == True  and \
            hand_2_data['is_ring_finger_opened']   == True  and \
            hand_2_data['is_little_finger_opened'] == True  \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][2] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]-2][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][2] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]-2][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][2] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]-2][2] \
           ) \
         ):
        if mi.cvs.config_data['CapsLock'] == "True":
            return "R"
        else:
            return "r"
    elif (mi.cvs.config_data['include_letters']['s']=='i') and \
       ( \
        hand_1_data['is_hand_1']               == True  and \
        hand_1_data['is_right_hand']           == True  and \
        hand_1_data['hand_orientation']        == 90    and \
        hand_1_data['is_thumb_opened']         == False and \
        hand_1_data['is_index_finger_opened']  == False and \
        hand_1_data['is_middle_finger_opened'] == False and \
        hand_1_data['is_ring_finger_opened']   == False and \
        hand_1_data['is_little_finger_opened'] == True  and \
        hand_2_data['is_hand_1']               == False and \
        hand_2_data['is_right_hand']           == True  and \
        hand_2_data['hand_orientation']        == 0     and \
        hand_2_data['is_thumb_opened']         == True  and \
        hand_2_data['is_index_finger_opened']  == False and \
        hand_2_data['is_middle_finger_opened'] == False and \
        hand_2_data['is_ring_finger_opened']   == False and \
        hand_2_data['is_little_finger_opened'] == True \
       ):
        if mi.cvs.config_data['CapsLock'] == "True":
            return "S"
        else:
            return "s"
    elif (mi.cvs.config_data['include_letters']['t']=='i') and \
       ( \
           ( \
            hand_1_data['is_hand_1']               == True  and \
            hand_1_data['is_right_hand']           == False and \
            hand_1_data['hand_orientation']        == 0     and \
            hand_1_data['is_thumb_opened']         == False and \
            hand_1_data['is_index_finger_opened']  == True  and \
            hand_1_data['is_middle_finger_opened'] == False and \
            hand_1_data['is_ring_finger_opened']   == False and \
            hand_1_data['is_little_finger_opened'] == False and \
            hand_2_data['is_hand_1']               == False and \
            hand_2_data['is_right_hand']           == True  and \
            hand_2_data['hand_orientation']        == 90    and \
            hand_2_data['is_thumb_opened']         == False and \
            hand_2_data['is_index_finger_opened']  == True  and \
            hand_2_data['is_middle_finger_opened'] == False and \
            hand_2_data['is_ring_finger_opened']   == False and \
            hand_2_data['is_little_finger_opened'] == False and \
            mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][8][1],hand_1_data['HandLandMarks'][5][1],hand_1_data['HandLandMarks'][8][1],35) and\
            mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][8][2],hand_1_data['HandLandMarks'][5][2],hand_1_data['HandLandMarks'][8][2],35) \
           )\
           or \
           ( \
            hand_2_data['is_hand_1']               == False and \
            hand_2_data['is_right_hand']           == False and \
            hand_2_data['hand_orientation']        == 0     and \
            hand_2_data['is_thumb_opened']         == False and \
            hand_2_data['is_index_finger_opened']  == True  and \
            hand_2_data['is_middle_finger_opened'] == False and \
            hand_2_data['is_ring_finger_opened']   == False and \
            hand_2_data['is_little_finger_opened'] == False and \
            hand_1_data['is_hand_1']               == True  and \
            hand_1_data['is_right_hand']           == True  and \
            hand_1_data['hand_orientation']        == 90    and \
            hand_1_data['is_thumb_opened']         == False and \
            hand_1_data['is_index_finger_opened']  == True  and \
            hand_1_data['is_middle_finger_opened'] == False and \
            hand_1_data['is_ring_finger_opened']   == False and \
            hand_1_data['is_little_finger_opened'] == False and \
            mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][8][1],hand_2_data['HandLandMarks'][5][1],hand_2_data['HandLandMarks'][8][1],35) and\
            mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][8][2],hand_2_data['HandLandMarks'][5][2],hand_2_data['HandLandMarks'][8][2],35) \
           )\
        ): 
        if mi.cvs.config_data['CapsLock'] == "True":
            return "T"
        else:
            return "t"
    elif (mi.cvs.config_data['include_letters']['w']=='i') and \
       ( \
        (   hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 2][2] \
        and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 2][2] \
        and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 2][2] \
        and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4] - 2][2] \
        and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 2][2] \
        and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 2][2] \
        and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 2][2] \
        and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4] - 2][2] \
        and mi.cfs.diff_between(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1], hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-3][1], hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1], hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 2][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 3][1],55) \
        and mi.cfs.diff_between(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][1], hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]-2][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]-3][1], hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][1], hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 2][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 3][1],55) \
        and mi.cfs.diff_between(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][1], hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]-2][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]-3][1], hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][1], hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 2][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 3][1],55) \
        and mi.cfs.diff_between(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2], hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-3][2], hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2], hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 2][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 3][2],55) \
        and mi.cfs.diff_between(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2], hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]-2][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]-3][2], hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2], hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 2][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 3][2],55) \
        and mi.cfs.diff_between(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2], hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]-2][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]-3][2], hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2], hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 2][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 3][2],55))\
       ):
        if mi.cvs.config_data['CapsLock'] == "True":
            return "W"
        else:
            return "w"
    elif (mi.cvs.config_data['include_letters']['x']=='i') and \
       (\
           ( \
            hand_1_data['is_hand_1']               == True  and \
            hand_1_data['is_right_hand']           == False and \
            #hand_1_data['hand_orientation']        == 90    and \
            hand_1_data['is_thumb_opened']         == False and \
            hand_1_data['is_index_finger_opened']  == True  and \
            hand_1_data['is_middle_finger_opened'] == False and \
            hand_1_data['is_ring_finger_opened']   == False and \
            hand_1_data['is_little_finger_opened'] == False and \
            hand_2_data['is_hand_1']               == False and \
            hand_2_data['is_right_hand']           == True  and \
            #hand_2_data['hand_orientation']        == 90    and \
            hand_2_data['is_thumb_opened']         == False and \
            hand_2_data['is_index_finger_opened']  == True  and \
            hand_2_data['is_middle_finger_opened'] == False and \
            hand_2_data['is_ring_finger_opened']   == False and \
            hand_2_data['is_little_finger_opened'] == False and \
             (\
                (mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][6][1],hand_2_data['HandLandMarks'][5][1],hand_2_data['HandLandMarks'][8][1],35) and\
                 mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][6][2],hand_2_data['HandLandMarks'][5][2],hand_2_data['HandLandMarks'][8][2],35))\
                 or \
                (mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][6][1],hand_1_data['HandLandMarks'][5][1],hand_1_data['HandLandMarks'][8][1],35) and\
                 mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][6][2],hand_1_data['HandLandMarks'][5][2],hand_1_data['HandLandMarks'][8][2],35))\
             )\
           )\
           or \
           ( \
            hand_2_data['is_hand_1']               == False and \
            hand_2_data['is_right_hand']           == False and \
            #hand_2_data['hand_orientation']        == 90    and \
            hand_2_data['is_thumb_opened']         == False and \
            hand_2_data['is_index_finger_opened']  == True  and \
            hand_2_data['is_middle_finger_opened'] == False and \
            hand_2_data['is_ring_finger_opened']   == False and \
            hand_2_data['is_little_finger_opened'] == False and \
            hand_1_data['is_hand_1']               == True  and \
            hand_1_data['is_right_hand']           == True  and \
            #hand_1_data['hand_orientation']        == 90    and \
            hand_1_data['is_thumb_opened']         == False and \
            hand_1_data['is_index_finger_opened']  == True  and \
            hand_1_data['is_middle_finger_opened'] == False and \
            hand_1_data['is_ring_finger_opened']   == False and \
            hand_1_data['is_little_finger_opened'] == False and \
             (\
                (mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][6][1],hand_1_data['HandLandMarks'][5][1],hand_1_data['HandLandMarks'][8][1],35) and\
                 mi.cfs.x_inbetween(hand_2_data['HandLandMarks'][6][2],hand_1_data['HandLandMarks'][5][2],hand_1_data['HandLandMarks'][8][2],35))\
                 or \
                (mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][6][1],hand_2_data['HandLandMarks'][5][1],hand_2_data['HandLandMarks'][8][1],35) and\
                 mi.cfs.x_inbetween(hand_1_data['HandLandMarks'][6][2],hand_2_data['HandLandMarks'][5][2],hand_2_data['HandLandMarks'][8][2],35))\
             )\
           )\
        ):
        if mi.cvs.config_data['CapsLock'] == "True":
            return "X"
        else:
            return "x"
    elif (mi.cvs.config_data['include_letters']['y']=='i') and \
        ( \
            (   \
                hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4] - 2][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]-1][1] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]-2][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]-2][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]-2][2] \
            ) \
            or \
            (   hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] < hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] > hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4] - 2][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]][1] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[0]-1][1] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2] < hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]-2][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]-2][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]-2][2] \
            and hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2] > hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]-2][2] \
            ) \
        ):
        if mi.cvs.config_data['CapsLock'] == "True":
            return "Y"
        else:
            return "y"
    elif (mi.cvs.config_data['include_letters']['z']=='i') and \
        ( \
            (\
                (   mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][1],35) \
                and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][1],35) \
                and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][1],35) \
                and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2],35) \
                and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2],35) \
                and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2],35) \
            )\
            or \
            (  \
                    mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][1],35) \
                and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][1],35) \
                and mi.cfs.diff(hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][1],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][1],35) \
                and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[2]][2],35) \
                and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[3]][2],35) \
                and mi.cfs.diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[4]][2],35) \
            )\
        )\
        and \
        mi.cfs.outside_diff(hand_1_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],hand_2_data['HandLandMarks'][mi.ccs.FingerTipLandMarks[1]][2],155)\
        ):
        if mi.cvs.config_data['CapsLock'] == "True":
            return "Z"
        else:
            return "z"

    return symbol

def double_hand_letters_display_olds(FirstRightHandLandMarks,SecondLeftHandLandMarks,FirstLeftHandLandMarks,SecondRightHandLandMarks):
    symbol_matched = False
    symbol = ""

    RightHandLandMarks = []
    LeftHandLandMarks  = []

    if (len(FirstRightHandLandMarks) == 0 and len(FirstLeftHandLandMarks) == 0) and (len(SecondRightHandLandMarks) == 0 and len(SecondLeftHandLandMarks) == 0):
        return symbol

    if len(FirstRightHandLandMarks) != 0:
        RightHandLandMarks = FirstRightHandLandMarks
        print("FirstRightHandLandMarks", end=" ")
    elif len(FirstLeftHandLandMarks) != 0:
        RightHandLandMarks = FirstLeftHandLandMarks
        print("FirstLeftHandLandMarks", end=" ")

    if len(SecondLeftHandLandMarks) != 0:
        LeftHandLandMarks = SecondLeftHandLandMarks
        print("SecondLeftHandLandMarks")
    elif len(SecondRightHandLandMarks) != 0:
        LeftHandLandMarks = SecondRightHandLandMarks
        print("SecondRightHandLandMarks")

    if (\
         (\
            (RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1])\
            and \
            (LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1])\
         )\
         or \
         (\
            (RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1])\
            and \
            (LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1])\
         )\
       )\
         and \
         (\
          RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
          and RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
          and RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
          and RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
        ) \
        and \
        ( \
            LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
        ) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],35):
        symbol = "CapsLock"
    elif (mi.cvs.config_data['include_letters']['a']=='i') and \
        ((RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
        or 
        RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1]) \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1],35) \
        and (LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
             or
            LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1]) \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1],35) \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1],35) \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1],35) \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1],55) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2],55)):
        if mi.cvs.config_data['CapsLock'] == "True":
            return "A"
        else:
            return "a"
    elif (mi.cvs.config_data['include_letters']['b']=='i') and \
        (mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2],35) \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1],35) \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1],35) \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1],35) \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1],35) \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2],35) \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2],35) \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2],35) \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1],55) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],55) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1],55) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1],55) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1],55) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2],35)):
        if mi.cvs.config_data['CapsLock'] == "True":
            return "B"
        else:
            return "b"
    elif mi.cvs.config_data['include_letters']['d']=='i':
        if len(FirstRightHandLandMarks) !=0 and len(SecondLeftHandLandMarks) !=0:
            #print("FirstRightHandLandMarks and SecondLeftHandLandMarks")
            if (
            (   FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
            and mi.cfs.x_inbetween(SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-1][1],35) \
            and mi.cfs.x_inbetween(SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-1][2],35) \
            and mi.cfs.x_inbetween(SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1],FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][1],35) \
            and mi.cfs.x_inbetween(SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2],FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2],FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][2],35)\
            )\
            or\
            (   SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
            and mi.cfs.x_inbetween(FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-1][1],35) \
            and mi.cfs.x_inbetween(FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-1][2],35) \
            and mi.cfs.x_inbetween(FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1],SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][1],35) \
            and mi.cfs.x_inbetween(FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2],SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2],SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][2],35)\
            )\
            ):
             symbol_matched = True
        elif len(FirstLeftHandLandMarks) !=0 and len(SecondRightHandLandMarks) !=0:
            #print("FirstLeftHandLandMarks and SecondRightHandLandMarks")
            if ( 
            (   FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
            and mi.cfs.x_inbetween(SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-1][1],35) \
            and mi.cfs.x_inbetween(SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-1][2],35)\
            and mi.cfs.x_inbetween(SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][1],35) \
            and mi.cfs.x_inbetween(SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][2],35)\
            )\
            or\
            (   SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
            and mi.cfs.x_inbetween(FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-1][1],35) \
            and mi.cfs.x_inbetween(FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-1][2],35) \
            and mi.cfs.x_inbetween(FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][1],35) \
            and mi.cfs.x_inbetween(FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][2],35)\
            )\
            ):
             symbol_matched = True
        elif len(FirstRightHandLandMarks) !=0 and len(SecondRightHandLandMarks) !=0:
            #print("FirstRightHandLandMarks and SecondRightHandLandMarks")
            if (
            (   FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
            and mi.cfs.x_inbetween(SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-1][1],35) \
            and mi.cfs.x_inbetween(SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-1][2],35) \
            and mi.cfs.x_inbetween(SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1],FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][1],35) \
            and mi.cfs.x_inbetween(SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2],FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2],FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][2],35)\
            )\
            or\
            (   SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
            and mi.cfs.x_inbetween(FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-1][1],35) \
            and mi.cfs.x_inbetween(FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-1][2],35) \
            and mi.cfs.x_inbetween(FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][1],35) \
            and mi.cfs.x_inbetween(FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][2],35)\
            )\
            ) :
             symbol_matched = True
        elif len(FirstLeftHandLandMarks) !=0 and len(SecondLeftHandLandMarks) !=0:
            #print("FirstLeftHandLandMarks and SecondLeftHandLandMarks")
            if( 
            (   FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
            and mi.cfs.x_inbetween(SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-1][1],35) \
            and mi.cfs.x_inbetween(SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-1][2],35)\
            and mi.cfs.x_inbetween(SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][1],35) \
            and mi.cfs.x_inbetween(SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][2],35)\
            )\
            or\
            (   SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
            and mi.cfs.x_inbetween(FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-1][1],35) \
            and mi.cfs.x_inbetween(FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-1][2],35) \
            and mi.cfs.x_inbetween(FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1],SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][1],35) \
            and mi.cfs.x_inbetween(FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2],SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2],SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][2],35)\
            )\
            ):
             symbol_matched = True
        
        if symbol_matched == True:
            #print("D")
            if mi.cvs.config_data['CapsLock'] == "True":
                return "D"
            else:
                return "d"
    if mi.cvs.config_data['include_letters']['e']=='i':
        if len(FirstRightHandLandMarks) !=0 and len(SecondRightHandLandMarks) !=0:
            print("FirstRightHandLandMarks and SecondRightHandLandMarks")
            if (\
            (   FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2] < FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] < FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] < FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] < FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
            #and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] > FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
            and mi.cfs.x_inbetween(SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2]   , FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 1][2],FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 3][2],35) \
            and mi.cfs.x_inbetween(SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-1][2] , FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 1][2],FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 3][2],35) \
            and mi.cfs.x_inbetween(SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] , FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 1][2],FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 3][2],35)\
            )\
            or \
            (   SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2] < SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] < SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] < SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] < SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] > SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
            and mi.cfs.x_inbetween(FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2]   , SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 1][2],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 3][2],35) \
            and mi.cfs.x_inbetween(FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-1][2] , SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 1][2],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 3][2],35)\
            and mi.cfs.x_inbetween(FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] , SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 1][2],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 3][2],35)\
            )\
            ):
                symbol_matched = True
        elif len(FirstLeftHandLandMarks) !=0 and len(SecondLeftHandLandMarks) !=0:
            print("FirstLeftHandLandMarks and SecondLeftHandLandMarks")
            if (\
            (   FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2] < FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
            #and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] < FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
            and mi.cfs.x_inbetween(SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2]   , FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 1][2],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 3][2],35) \
            and mi.cfs.x_inbetween(SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-1][2] , FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 1][2],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 3][2],35) \
            and mi.cfs.x_inbetween(SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] , FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 1][2],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 3][2],35)\
            )\
            or \
            (   SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2] < SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] > SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] > SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
            #and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] < SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
            and mi.cfs.x_inbetween(FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2]   , SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 1][2],SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 3][2],35) \
            and mi.cfs.x_inbetween(FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-1][2] , SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 1][2],SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 3][2],35)\
            and mi.cfs.x_inbetween(FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] , SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 1][2],SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 3][2],35)\
            )\
            ):
                symbol_matched = True

        elif len(FirstLeftHandLandMarks) !=0 and len(SecondRightHandLandMarks) !=0:
            print("FirstLeftHandLandMarks and SecondRightHandLandMarks")
            if (\
            (   FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2] < FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
            #and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] < FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
            and mi.cfs.x_inbetween(SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2]   , FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 1][2],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 3][2],35) \
            and mi.cfs.x_inbetween(SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-1][2] , FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 1][2],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 3][2],35) \
            and mi.cfs.x_inbetween(SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] , FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 1][2],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 3][2],35)\
            )\
            or \
            (   SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2] < SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] < SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] < SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] < SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
            #and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] > SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
            and mi.cfs.x_inbetween(FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2]   , SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 1][2],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 3][2],35) \
            and mi.cfs.x_inbetween(FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-1][2] , SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 1][2],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 3][2],35)\
            and mi.cfs.x_inbetween(FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] , SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 1][2],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 3][2],35)\
            )\
            ):
                symbol_matched = True
        elif len(FirstRightHandLandMarks) !=0 and len(SecondLeftHandLandMarks) !=0:
            print("FirstRightHandLandMarks and SecondLeftHandLandMarks")
            if (\
            (   FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2] < FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] < FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] < FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] < FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
            #and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] > FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
            and mi.cfs.x_inbetween(SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2]   , FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 1][2],FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 3][2],35) \
            and mi.cfs.x_inbetween(SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-1][2] , FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 1][2],FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 3][2],35) \
            and mi.cfs.x_inbetween(SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] , FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 1][2],FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 3][2],35)\
            )\
            or \
            (   SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2] < SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] > SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] > SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
            #and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] < SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
            and mi.cfs.x_inbetween(FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2]   , SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 1][2],SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 3][2],35) \
            and mi.cfs.x_inbetween(FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-1][2] , SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 1][2],SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 3][2],35)\
            and mi.cfs.x_inbetween(FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] , SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 1][2],SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 3][2],35)\
            )\
            ):
                symbol_matched = True
        
        if symbol_matched == True:
            if mi.cvs.config_data['CapsLock'] == "True":
                return "E"
            else:
                return "e"

    if mi.cvs.config_data['include_letters']['f']=='i':
        if len(FirstRightHandLandMarks) !=0 and len(SecondLeftHandLandMarks) !=0:
            print("FirstRightHandLandMarks and SecondLeftHandLandMarks")
            if(\
            (   FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1]  < FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2]  < FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2]  < FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2]  > FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2]  > FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2] > SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] > SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] < SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] < SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
            and mi.cfs.x_inbetween(FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][2],35) \
            and mi.cfs.x_inbetween(FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2],SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2],SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]-3][2],35) \
            )\
            or\
            (   SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1]  < SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2]  < SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2]  < SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2]  > SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2]  > SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2]   < FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1]   < FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1]   < FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1]   > FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1]   > FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
            and mi.cfs.x_inbetween(SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][2],35) \
            and mi.cfs.x_inbetween(SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2],FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2],FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[2]-3][2],35) \
            )\
            ):
              symbol_matched = True
        elif len(FirstLeftHandLandMarks) !=0 and len(SecondRightHandLandMarks) !=0:
            print("FirstLeftHandLandMarks and SecondRightHandLandMarks")
            if(\
            (   SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1]  < SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2]  < SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2]  < SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2]  > SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2]  > SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2] > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] < FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] < FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
            and mi.cfs.x_inbetween(SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][2],35) \
            and mi.cfs.x_inbetween(SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]-3][2],35) \
            )\
            or\
            (   FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2]  < FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1]  < FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1]  < FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1]  > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1]  > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2]   < SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1]   < SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1]   < SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1]   > SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1]   > SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
            and mi.cfs.x_inbetween(FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][2],35) \
            and mi.cfs.x_inbetween(FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[2]-3][2],35) \
            )\
            ):
              symbol_matched = True
        elif len(FirstRightHandLandMarks) !=0 and len(SecondRightHandLandMarks) !=0:
            print("FirstRightHandLandMarks and SecondRightHandLandMarks")
            if(\
            (   FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1]  < FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2]  < FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2]  < FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2]  > FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2]  > FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2] > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] < FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] < FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
            and mi.cfs.x_inbetween(SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][2],35) \
            and mi.cfs.x_inbetween(SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2],FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]-3][2],35) \
            )\
            or\
            (   SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1]  < SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2]  < SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2]  < SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2]  > SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2]  > SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2]   > FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1]   < FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1]   < FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1]   > FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
            and FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1]   > FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
            and mi.cfs.x_inbetween(FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][2],35) \
            and mi.cfs.x_inbetween(FirstRightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2],SecondRightHandLandMarks[mi.ccs.FingerTipLandMarks[2]-3][2],35) \
            )\
            ):
              symbol_matched = True
        elif len(FirstLeftHandLandMarks) !=0 and len(SecondLeftHandLandMarks) !=0:
            print("FirstLeftHandLandMarks and SecondLeftHandLandMarks")
            if(\
            (   FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1]  > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2]  < FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2]  < FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2]  > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2]  > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2] > SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] < SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] < SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] > SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] > SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
            )\
            or\
            (   SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1]  > SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2]  < SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2]  < SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2]  > SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2]  > SecondLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2]   > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1]   < FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1]   < FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1]   > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
            and FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1]   > FirstLeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
            )\
            ):
              symbol_matched = True

        if symbol_matched == True:
            if mi.cvs.config_data['CapsLock'] == "True":
               return "F"
            else:
               return "f"

    elif (mi.cvs.config_data['include_letters']['g']=='i') and \
        (((RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]-2][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]-2][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]-2][1]) \
        or \
        (LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]-2][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]-2][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]-2][1])) \
        and \
        ((LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2]) \
        or \
        (LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2]))):
        if mi.cvs.config_data['CapsLock'] == "True":
            symbol = "G"
        else:
            symbol = "g"
    elif (mi.cvs.config_data['include_letters']['h']=='i') and \
        ((RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
        #and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],35) \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]-2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]-2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]-2][2]) \
        or \
        (LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
        #and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],35) \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]-2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]-2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]-2][2])):
        if mi.cvs.config_data['CapsLock'] == "True":
            symbol = "H"
        else:
            symbol = "h"
    elif (mi.cvs.config_data['include_letters']['j']=='i') and \
        ((RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],35)) \
        or \
        (LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],35))):
        if mi.cvs.config_data['CapsLock'] == "True":
            symbol = "J"
        else:
            symbol = "j"
    elif (mi.cvs.config_data['include_letters']['k']=='i') and \
        ((RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2],35) \
        #and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],35) \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-1][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][1]) \
        or \
        (LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2],RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2],35) \
        #and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],35) \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-1][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][1])):
        if mi.cvs.config_data['CapsLock'] == "True":
            symbol = "K"
        else:
            symbol = "k"
    elif (mi.cvs.config_data['include_letters']['m']=='i') and \
        ((RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]-2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]-2][2]) \
        or \
        (LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]-2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]-2][2])):
        if mi.cvs.config_data['CapsLock'] == "True":
            symbol = "M"
        else:
            symbol = "m"
    elif (mi.cvs.config_data['include_letters']['n']=='i') and \
        ((RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]-2][2]) \
        or \
        (LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]-2][2])):
        if mi.cvs.config_data['CapsLock'] == "True":
            symbol = "N"
        else:
            symbol = "n"
    elif (mi.cvs.config_data['include_letters']['p']=='i') and \
        ((mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2],35) \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],35) \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],35) \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]) \
        or \
        (mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1],35) \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1],35) \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1],35) \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1],35) \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2],35) \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2],35) \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2],35) \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],35) \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2])):
        if mi.cvs.config_data['CapsLock'] == "True":
            symbol = "P"
        else:
            symbol = "p"
    elif (mi.cvs.config_data['include_letters']['q']=='i') and \
        ((mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2],35) \
        and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2],35) \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]-1][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]-2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]-2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]-2][2]) \
        or \
        (mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1],35) \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1],35) \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1],35) \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1],35) \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2],35) \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2],35) \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2],35) \
        and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2],35) \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]-1][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]-2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]-2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]-2][2])):
        if mi.cvs.config_data['CapsLock'] == "True":
            symbol = "Q"
        else:
            symbol = "q"
    elif (mi.cvs.config_data['include_letters']['r']=='i') and \
        ((RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
        #and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],35) \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]-2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]-2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]-2][2]) \
        or \
        (LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
        #and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],35) \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]-2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]-2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]-2][2])):
        if mi.cvs.config_data['CapsLock'] == "True":
            symbol = "R"
        else:
            symbol = "r"
    elif (mi.cvs.config_data['include_letters']['s']=='i') and \
        (((RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]-2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]-2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]-2][2]) \
        or \
        (LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]-2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]-2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]-2][2]))\
        and\
        (
            mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1],35)\
            and \
            mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2],35)\
        )):
        if mi.cvs.config_data['CapsLock'] == "True":
            symbol = "S"
        else:
            symbol = "s"
    elif (mi.cvs.config_data['include_letters']['t']=='i') and \
         (( \
            (RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
            and RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
            and RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
            and RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
            and RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1]) \
            and \
            (LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2])  \
            and 
            mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],35) \
            and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],35) \
        )or\
        ( \
            (LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
            and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
            and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
            and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
            and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1]) \
            and \
            (RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2])  \
            and 
            mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],35) \
            and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2],RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],35) \
        )):
        if mi.cvs.config_data['CapsLock'] == "True":
            symbol = "T"
        else:
            symbol = "t"
    elif (mi.cvs.config_data['include_letters']['w']=='i') and \
        (RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
        and mi.cfs.diff_between(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1], RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][1], LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1], LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 3][1],55) \
        and mi.cfs.diff_between(RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1], RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]-2][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]-3][1], LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1], LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 3][1],55) \
        and mi.cfs.diff_between(RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1], RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]-2][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]-3][1], LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1], LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 3][1],55) \
        and mi.cfs.diff_between(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2], RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2],RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][2], LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2], LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 3][2],55) \
        and mi.cfs.diff_between(RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2], RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]-2][2],RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]-3][2], LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2], LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 3][2],55) \
        and mi.cfs.diff_between(RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2], RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]-2][2],RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]-3][2], LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2], LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 3][2],55)):

        if mi.cvs.config_data['CapsLock'] == "True":
            return "W"
        else:
            return "w"
    elif (mi.cvs.config_data['include_letters']['x']=='i') and \
        (RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
        and mi.cfs.diff_between(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1], RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][1], LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1], LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 3][1],55) \
        and mi.cfs.diff_between(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2], RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2],RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-3][2], LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2], LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 3][2],55)):
        if mi.cvs.config_data['CapsLock'] == "True":
            symbol = "X"
        else:
            symbol = "x"
    elif (mi.cvs.config_data['include_letters']['y']=='i') and \
        ((RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1]\
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]-1][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]-2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]-2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]-2][2]) \
        or \
        (LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1]\
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]-1][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]-2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]-2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]-2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]-2][2])):
        if mi.cvs.config_data['CapsLock'] == "True":
            symbol = "Y"
        else:
            symbol = "y"
    elif (mi.cvs.config_data['include_letters']['z']=='i') and \
        ( \
            (\
                (mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1],35) \
                and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1],35) \
                and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1],35) \
                and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2],35) \
                and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2],35) \
                and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2],35))\
                or \
                (mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][1],35) \
                and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][1],35) \
                and mi.cfs.diff(LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][1],35) \
                and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2],35) \
                and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2],35) \
                and mi.cfs.diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2],35))\
            )\
            and\
            mi.cfs.outside_diff(RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],155)\
        ):
        if mi.cvs.config_data['CapsLock'] == "True":
            symbol = "Z"
        else:
            symbol = "z"
    elif (RightHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] > RightHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
        and RightHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] < RightHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]) \
        or \
        (LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] > LeftHandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
        and LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] < LeftHandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]):
        symbol =  "Exit"
    else:
        if mi.cvs.config_data['debug'] == "True":                
           symbol =  "Debug"
        else:
           symbol = ""

    return symbol
