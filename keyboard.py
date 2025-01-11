import modules_imported as mi
import hand_information as hi
import single_hand_symbols as shs 

def get_Keyboard_letter(hand_1_symbol,hand_0_symbol):
    keyboard_letter = ''
    if hand_0_symbol != -1 and hand_1_symbol == -1:
        keyboard_letter = hand_0_symbol
    elif hand_1_symbol != -1 and hand_0_symbol != -1:
        keyboard_letter = ''
        if   hand_1_symbol == 0 and hand_0_symbol == 1:
            keyboard_letter = '1'
        elif hand_1_symbol == 0 and hand_0_symbol == 2:
            keyboard_letter = '2'
        elif hand_1_symbol == 0 and hand_0_symbol == 3:
            keyboard_letter = '3'
        elif hand_1_symbol == 0 and hand_0_symbol == 4:
            keyboard_letter = '4'
        elif hand_1_symbol == 0 and hand_0_symbol == 5:
            keyboard_letter = '5'
        elif hand_1_symbol == 0 and hand_0_symbol == 6:
            keyboard_letter = '6'
        elif hand_1_symbol == 0 and hand_0_symbol == 7:
            keyboard_letter = '7'
        elif hand_1_symbol == 0 and hand_0_symbol == 8:
            keyboard_letter = '8'
        elif hand_1_symbol == 0 and hand_0_symbol == 9:
            keyboard_letter = '9'
        elif hand_1_symbol == 0 and hand_0_symbol == 0:
            keyboard_letter = '0'
        elif hand_1_symbol == 1 and hand_0_symbol == 1:
            keyboard_letter = 'q'
        elif hand_1_symbol == 1 and hand_0_symbol == 2:
            keyboard_letter = 'w'
        elif hand_1_symbol == 1 and hand_0_symbol == 3:
            keyboard_letter = 'e'
        elif hand_1_symbol == 1 and hand_0_symbol == 4:
            keyboard_letter = 'r'
        elif hand_1_symbol == 1 and hand_0_symbol == 5:
            keyboard_letter = 't'
        elif hand_1_symbol == 1 and hand_0_symbol == 6:
            keyboard_letter = 'y'
        elif hand_1_symbol == 1 and hand_0_symbol == 7:
            keyboard_letter = 'u'
        elif hand_1_symbol == 1 and hand_0_symbol == 8:
            keyboard_letter = 'i'
        elif hand_1_symbol == 1 and hand_0_symbol == 9:
            keyboard_letter = 'o'
        elif hand_1_symbol == 1 and hand_0_symbol == 0:
            keyboard_letter = 'p'
        elif hand_1_symbol == 2 and hand_0_symbol == 1:
            keyboard_letter = 'a'
        elif hand_1_symbol == 2 and hand_0_symbol == 2:
            keyboard_letter = 's'
        elif hand_1_symbol == 2 and hand_0_symbol == 3:
            keyboard_letter = 'd'
        elif hand_1_symbol == 2 and hand_0_symbol == 4:
            keyboard_letter = 'f'
        elif hand_1_symbol == 2 and hand_0_symbol == 5:
            keyboard_letter = 'g'
        elif hand_1_symbol == 2 and hand_0_symbol == 6:
            keyboard_letter = 'h'
        elif hand_1_symbol == 2 and hand_0_symbol == 7:
            keyboard_letter = 'j'
        elif hand_1_symbol == 2 and hand_0_symbol == 8:
            keyboard_letter = 'k'
        elif hand_1_symbol == 2 and hand_0_symbol == 9:
            keyboard_letter = 'l'
        elif hand_1_symbol == 2 and hand_0_symbol == 0:
            keyboard_letter = ';'
        elif hand_1_symbol == 3 and hand_0_symbol == 1:
            keyboard_letter = 'z'
        elif hand_1_symbol == 3 and hand_0_symbol == 2:
            keyboard_letter = 'x'
        elif hand_1_symbol == 3 and hand_0_symbol == 3:
            keyboard_letter = 'c'
        elif hand_1_symbol == 3 and hand_0_symbol == 4:
            keyboard_letter = 'v'
        elif hand_1_symbol == 3 and hand_0_symbol == 5:
            keyboard_letter = 'b'
        elif hand_1_symbol == 3 and hand_0_symbol == 6:
            keyboard_letter = 'n'
        elif hand_1_symbol == 3 and hand_0_symbol == 7:
            keyboard_letter = 'm'
        elif hand_1_symbol == 3 and hand_0_symbol == 8:
            keyboard_letter = ','
        elif hand_1_symbol == 3 and hand_0_symbol == 9:
            keyboard_letter = '.'
        elif hand_1_symbol == 3 and hand_0_symbol == 0:
            keyboard_letter = '/'
        elif hand_1_symbol == 4 and hand_0_symbol == 1:
            keyboard_letter = 'Esc'
        elif hand_1_symbol == 4 and hand_0_symbol == 2:
            keyboard_letter = 'Del'
        elif hand_1_symbol == 4 and hand_0_symbol == 3:
            keyboard_letter = '`'
        elif hand_1_symbol == 4 and hand_0_symbol == 4:
            keyboard_letter = '-'
        elif hand_1_symbol == 4 and hand_0_symbol == 5:
            keyboard_letter = '='
        elif hand_1_symbol == 4 and hand_0_symbol == 6:
            keyboard_letter = 'backspace'
        elif hand_1_symbol == 4 and hand_0_symbol == 7:
            keyboard_letter = '['
        elif hand_1_symbol == 4 and hand_0_symbol == 8:
            keyboard_letter = ']'
        elif hand_1_symbol == 4 and hand_0_symbol == 9:
            keyboard_letter = '\\'
        elif hand_1_symbol == 4 and hand_0_symbol == 0:
            keyboard_letter = '\''
        elif hand_1_symbol == 9 and hand_0_symbol == 1:
            keyboard_letter = '!'
        elif hand_1_symbol == 9 and hand_0_symbol == 2:
            keyboard_letter = '@'
        elif hand_1_symbol == 9 and hand_0_symbol == 3:
            keyboard_letter = '#'
        elif hand_1_symbol == 9 and hand_0_symbol == 4:
            keyboard_letter = '$'
        elif hand_1_symbol == 9 and hand_0_symbol == 5:
            keyboard_letter = '%'
        elif hand_1_symbol == 9 and hand_0_symbol == 6:
            keyboard_letter = '^'
        elif hand_1_symbol == 9 and hand_0_symbol == 7:
            keyboard_letter = '&'
        elif hand_1_symbol == 9 and hand_0_symbol == 8:
            keyboard_letter = '*'
        elif hand_1_symbol == 9 and hand_0_symbol == 9:
            keyboard_letter = '('
        elif hand_1_symbol == 9 and hand_0_symbol == 0:
            keyboard_letter = ')'
        elif hand_1_symbol == 11 and hand_0_symbol == 1:
            keyboard_letter = 'Q'
        elif hand_1_symbol == 11 and hand_0_symbol == 2:
            keyboard_letter = 'W'
        elif hand_1_symbol == 11 and hand_0_symbol == 3:
            keyboard_letter = 'E'
        elif hand_1_symbol == 11 and hand_0_symbol == 4:
            keyboard_letter = 'R'
        elif hand_1_symbol == 11 and hand_0_symbol == 5:
            keyboard_letter = 'T'
        elif hand_1_symbol == 11 and hand_0_symbol == 6:
            keyboard_letter = 'Y'
        elif hand_1_symbol == 11 and hand_0_symbol == 7:
            keyboard_letter = 'U'
        elif hand_1_symbol == 11 and hand_0_symbol == 8:
            keyboard_letter = 'I'
        elif hand_1_symbol == 11 and hand_0_symbol == 9:
            keyboard_letter = 'O'
        elif hand_1_symbol == 11 and hand_0_symbol == 0:
            keyboard_letter = 'P'
        elif hand_1_symbol == 8 and hand_0_symbol == 1:
            keyboard_letter = 'A'
        elif hand_1_symbol == 8 and hand_0_symbol == 2:
            keyboard_letter = 'S'
        elif hand_1_symbol == 8 and hand_0_symbol == 3:
            keyboard_letter = 'D'
        elif hand_1_symbol == 8 and hand_0_symbol == 4:
            keyboard_letter = 'F'
        elif hand_1_symbol == 8 and hand_0_symbol == 5:
            keyboard_letter = 'G'
        elif hand_1_symbol == 8 and hand_0_symbol == 6:
            keyboard_letter = 'H'
        elif hand_1_symbol == 8 and hand_0_symbol == 7:
            keyboard_letter = 'J'
        elif hand_1_symbol == 8 and hand_0_symbol == 8:
            keyboard_letter = 'K'
        elif hand_1_symbol == 8 and hand_0_symbol == 9:
            keyboard_letter = 'L'
        elif hand_1_symbol == 8 and hand_0_symbol == 0:
            keyboard_letter = ':'
        elif hand_1_symbol == 13 and hand_0_symbol == 1:
            keyboard_letter = 'Z'
        elif hand_1_symbol == 13 and hand_0_symbol == 2:
            keyboard_letter = 'X'
        elif hand_1_symbol == 13 and hand_0_symbol == 3:
            keyboard_letter = 'C'
        elif hand_1_symbol == 13 and hand_0_symbol == 4:
            keyboard_letter = 'V'
        elif hand_1_symbol == 13 and hand_0_symbol == 5:
            keyboard_letter = 'B'
        elif hand_1_symbol == 13 and hand_0_symbol == 6:
            keyboard_letter = 'N'
        elif hand_1_symbol == 13 and hand_0_symbol == 7:
            keyboard_letter = 'M'
        elif hand_1_symbol == 13 and hand_0_symbol == 8:
            keyboard_letter = 'less than'
        elif hand_1_symbol == 13 and hand_0_symbol == 9:
            keyboard_letter = '>'
        elif hand_1_symbol == 13 and hand_0_symbol == 0:
            keyboard_letter = '?'
        elif hand_1_symbol == 5 and hand_0_symbol == 1:
            keyboard_letter = ' '
        elif hand_1_symbol == 5 and hand_0_symbol == 2:
            keyboard_letter = 'Del'
        elif hand_1_symbol == 5 and hand_0_symbol == 3:
            keyboard_letter = '~'
        elif hand_1_symbol == 5 and hand_0_symbol == 4:
            keyboard_letter = '_'
        elif hand_1_symbol == 5 and hand_0_symbol == 5:
            keyboard_letter = '+'
        elif hand_1_symbol == 5 and hand_0_symbol == 6:
            keyboard_letter = 'Enter'
        elif hand_1_symbol == 5 and hand_0_symbol == 7:
            keyboard_letter = '{'
        elif hand_1_symbol == 5 and hand_0_symbol == 8:
            keyboard_letter = '}'
        elif hand_1_symbol == 5 and hand_0_symbol == 9:
            keyboard_letter = '|'
        elif hand_1_symbol == 5 and hand_0_symbol == 0:
            keyboard_letter = '"'

    return keyboard_letter


def keyboard_symbol_display():  #hand_1_data,hand_2_data):
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
    while True:
        success, screen_video = screen.read()  
        if screen_video is None:
            break

        screen_video    = mi.vision.flip(screen_video,1)
        mi.vision.putText(screen_video, "Keyboard" , (800, 50), mi.vision.FONT_HERSHEY_COMPLEX,1, (255, 0, 0), 2)

        screen_video = hand_detector.findHands(screen_video)
        Hand_1_LandMarks = hand_detector.findPosition(screen_video, 0, draw=False)
        Hand_2_LandMarks = hand_detector.findPosition(screen_video, 1, draw=False)

        hand_1_data = hand_1.get_hand_information(Hand_1_LandMarks,True) 
        hand_2_data = hand_2.get_hand_information(Hand_2_LandMarks,False) 
        
        hand_0_symbol = -1
        hand_1_symbol = -1

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
           hand_0_symbol = shs.digit_display(hand_data['HandLandMarks'])
        elif NoOfHands == 2:
           hand_0_symbol = shs.digit_display(hand_1_data['HandLandMarks'])
           hand_1_symbol = shs.digit_display(hand_2_data['HandLandMarks'])
        else:
           symbol = ""

        if hand_0_symbol == "Exit" or hand_1_symbol == "Exit":
            symbol = "Exit"
            screen.release()
            break

        if symbol != previous_symbol:
            previous_symbol = symbol

        symbol = get_Keyboard_letter(hand_1_symbol,hand_0_symbol)
        if symbol != 11 and symbol != 13: 
            mi.vision.putText(screen_video, str(symbol), (150, 450), mi.vision.FONT_HERSHEY_COMPLEX,10, (255, 0, 0), 10)
        mi.vision.imshow("Image", screen_video)
        mi.vision.waitKey(1)
    screen.release()
    
    return symbol

