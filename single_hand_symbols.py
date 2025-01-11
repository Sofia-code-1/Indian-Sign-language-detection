import modules_imported as mi

def digit_display(HandLandMarks):
    is_right = None
    symbol = -1
    if len(HandLandMarks) != 0:
        if HandLandMarks[5][1] < HandLandMarks[17][1]:
            is_right = True
        else:
            is_right = False

        if is_right == False:
            if thumbs_up(HandLandMarks) == True:
                symbol = "Exit"
            elif HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]:
                symbol =  "Exit"
            elif HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]:
                if mi.cvs.config_data['CapsLock'] == True:
                    symbol = ')'
                else:
                    symbol = 0
            elif HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]:
                if mi.cvs.config_data['CapsLock'] == True:
                    symbol = '!'
                else:
                    symbol = 1
            elif HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]:
                if mi.cvs.config_data['CapsLock'] == True:
                    symbol = '@'
                else:
                    symbol = 2
            elif HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]:
                if mi.cvs.config_data['CapsLock'] == True:
                    symbol = '#'
                else:
                    symbol = 3
            elif HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 2][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]:
                if mi.cvs.config_data['CapsLock'] == True:
                    symbol = '$'
                else:
                    symbol = 4
            elif HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 2][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]:
                if mi.cvs.config_data['CapsLock'] == True:
                    symbol = '%'
                else:
                    symbol = 5
            elif HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]:
                if mi.cvs.config_data['CapsLock'] == True:
                    symbol = '^'
                else:
                    symbol = 6
            elif HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]:
                if mi.cvs.config_data['CapsLock'] == True:
                    symbol = '&'
                else:
                    symbol = 7
            elif   HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]:
                if mi.cvs.config_data['CapsLock'] == True:
                    symbol = '*'
                else:
                    symbol = 8
            elif HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]:
                if mi.cvs.config_data['CapsLock'] == True:
                    symbol = '('
                else:
                    symbol = 9
            elif   HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]:
                if mi.cvs.config_data['CapsLock'] == True:
                    symbol = 11
                else:
                    symbol = 11
            elif   HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]:
                if mi.cvs.config_data['CapsLock'] == True:
                    symbol = 13
                else:
                    symbol = 13
            elif thumbs_up(HandLandMarks) == True:
                symbol = "Exit"
            else:
                if thumbs_down(HandLandMarks)==True:
                    symbol = "Thumbs down"
                else:
                    symbol = ""
        else:       
            if thumbs_up(HandLandMarks) == True:
                symbol = "Exit"
            elif HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]:
                if mi.cvs.config_data['CapsLock'] == True:
                    symbol = ')'
                else:
                    symbol = 0
            elif HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]:
                if mi.cvs.config_data['CapsLock'] == True:
                    symbol = '!'
                else:
                    symbol = 1
            elif HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]:
                if mi.cvs.config_data['CapsLock'] == True:
                    symbol = '@'
                else:
                    symbol = 2
            elif HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]:
                if mi.cvs.config_data['CapsLock'] == True:
                    symbol = '#'
                else:
                    symbol = 3
            elif HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 2][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]:
                if mi.cvs.config_data['CapsLock'] == True:
                    symbol = '$'
                else:
                    symbol = 4
            elif HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 2][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]:
                if mi.cvs.config_data['CapsLock'] == True:
                    symbol = '%'
                else:
                    symbol = 5
            elif HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]:
                if mi.cvs.config_data['CapsLock'] == True:
                    symbol = '^'
                else:
                    symbol = 6
            elif HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]:
                if mi.cvs.config_data['CapsLock'] == True:
                    symbol = '&'
                else:
                    symbol = 7
            elif   HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]:
                if mi.cvs.config_data['CapsLock'] == True:
                    symbol = '*'
                else:
                    symbol = 8
            elif HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
                and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]:
                if mi.cvs.config_data['CapsLock'] == True:
                    symbol = '('
                else:
                    symbol = 9
            else:
                if thumbs_down(HandLandMarks)==True:
                    symbol = "Thumbs down"
                else:
                    symbol = ""

    return symbol

def single_hand_letters_display(HandLandMarks):
    symbol = ""
    if len(HandLandMarks) != 0:
        if  (mi.cvs.config_data['include_letters'][' ']=='i') and \
            HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]:
            symbol = " "
        elif   (mi.cvs.config_data['include_letters']['c']=='i') and \
            mi.cfs.outside_diff(HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],HandLandMarks[mi.ccs.FingerTipLandMarks[0]][2],20) \
            and mi.cfs.diff(HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2],35) \
            and mi.cfs.diff(HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2],35) \
            and mi.cfs.diff(HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2],35) \
            and mi.cfs.diff(HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1],35) \
            and mi.cfs.diff(HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],HandLandMarks[mi.ccs.FingerTipLandMarks[2]][1],35) \
            and mi.cfs.diff(HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],HandLandMarks[mi.ccs.FingerTipLandMarks[3]][1],35) \
            and mi.cfs.diff(HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],HandLandMarks[mi.ccs.FingerTipLandMarks[4]][1],35):
            if mi.cvs.config_data['CapsLock'] == True:
                symbol = "C"
            else:
                symbol = "c"
        elif (mi.cvs.config_data['include_letters']['i']=='i') and \
            HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2] \
            and mi.cfs.outside_diff(HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1], 25):
            if mi.cvs.config_data['CapsLock'] == True:
                symbol = "I"
            else:
                symbol = "i"
        elif (mi.cvs.config_data['include_letters']['l']=='i') and \
            HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]:
            if mi.cvs.config_data['CapsLock'] == True:
                symbol = "L"
            else:
                symbol = "l"
        elif   (mi.cvs.config_data['include_letters']['o']=='i') and \
            mi.cfs.diff(HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1],35) \
            and mi.cfs.diff(HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],HandLandMarks[mi.ccs.FingerTipLandMarks[2]][1],35) \
            and mi.cfs.diff(HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],HandLandMarks[mi.ccs.FingerTipLandMarks[3]][1],35) \
            and mi.cfs.diff(HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],HandLandMarks[mi.ccs.FingerTipLandMarks[4]][1],35) \
            and mi.cfs.diff(HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],HandLandMarks[mi.ccs.FingerTipLandMarks[0]][2],35) \
            and mi.cfs.diff(HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2],35) \
            and mi.cfs.diff(HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2],35) \
            and mi.cfs.diff(HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2],35):
            if mi.cvs.config_data['CapsLock'] == True:
                symbol = "O"
            else:
                symbol = "o"
        elif   (mi.cvs.config_data['include_letters']['u']=='i') and \
            mi.cfs.outside_diff(HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1],20) \
            and mi.cfs.diff(HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],HandLandMarks[mi.ccs.FingerTipLandMarks[2]][1],35) \
            and mi.cfs.diff(HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],HandLandMarks[mi.ccs.FingerTipLandMarks[3]][1],35) \
            and mi.cfs.diff(HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1],HandLandMarks[mi.ccs.FingerTipLandMarks[4]][1],35) \
            and mi.cfs.diff(HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],HandLandMarks[mi.ccs.FingerTipLandMarks[0]][2],35) \
            and mi.cfs.diff(HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2],35) \
            and mi.cfs.diff(HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2],35) \
            and mi.cfs.diff(HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2],HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2],35):
            if mi.cvs.config_data['CapsLock'] == True:
                symbol = "U"
            else:
                symbol = "u"
        elif (mi.cvs.config_data['include_letters']['v']=='i') and \
            HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]:
            if mi.cvs.config_data['CapsLock'] == True:
                symbol = "V"
            else:
                symbol = "v"
        elif HandLandMarks[mi.ccs.FingerTipLandMarks[0]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1]:
            symbol =  "BackSpace"
        elif HandLandMarks[mi.ccs.FingerTipLandMarks[0]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1]:
            symbol =  "Dummy"
        elif HandLandMarks[mi.ccs.FingerTipLandMarks[0]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][2] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][1] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][1] > HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][1] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][1] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][1]:
            symbol =  "Delete"
        elif HandLandMarks[mi.ccs.FingerTipLandMarks[0]][1] < HandLandMarks[mi.ccs.FingerTipLandMarks[0] - 1][1] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[1]][2] > HandLandMarks[mi.ccs.FingerTipLandMarks[1] - 2][2] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[2]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[2] - 2][2] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[3]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[3] - 2][2] \
            and HandLandMarks[mi.ccs.FingerTipLandMarks[4]][2] < HandLandMarks[mi.ccs.FingerTipLandMarks[4] - 2][2]:
            symbol =  "Exit"
        elif thumbs_up(HandLandMarks) == True:
                symbol = "Exit"
        else:
            symbol = ""

    return symbol

def thumbs_up(HandLandMarks,flip=0):
    if len(HandLandMarks) == 0:
        return False
        if flip == 0:
            if HandLandMarks[4][2]       < HandLandMarks[3][2]  \
                and HandLandMarks[4][2]  < HandLandMarks[2][2]  \
                and HandLandMarks[5][2]  < HandLandMarks[9][2]  \
                and HandLandMarks[5][2]  < HandLandMarks[13][2] \
                and HandLandMarks[5][2]  < HandLandMarks[17][2] \
                and HandLandMarks[9][2]  < HandLandMarks[13][2] \
                and HandLandMarks[9][2]  < HandLandMarks[17][2] \
                and HandLandMarks[13][2] < HandLandMarks[17][2] \
                and HandLandMarks[5][1]  < HandLandMarks[6][1]  \
                and HandLandMarks[9][1]  < HandLandMarks[10][1] \
                and HandLandMarks[13][1] < HandLandMarks[14][1] \
                and HandLandMarks[17][1] < HandLandMarks[18][1]:
                return True
        else:
            if HandLandMarks[4][2]       < HandLandMarks[3][2]  \
                and HandLandMarks[4][2]  < HandLandMarks[2][2]  \
                and HandLandMarks[5][2]  < HandLandMarks[9][2]  \
                and HandLandMarks[5][2]  < HandLandMarks[13][2] \
                and HandLandMarks[5][2]  < HandLandMarks[17][2] \
                and HandLandMarks[9][2]  < HandLandMarks[13][2] \
                and HandLandMarks[9][2]  < HandLandMarks[17][2] \
                and HandLandMarks[13][2] < HandLandMarks[17][2] \
                and HandLandMarks[5][1]  > HandLandMarks[6][1]  \
                and HandLandMarks[9][1]  > HandLandMarks[10][1] \
                and HandLandMarks[13][1] > HandLandMarks[14][1] \
                and HandLandMarks[17][1] > HandLandMarks[18][1]:
                return True
    else:
        return False


def thumbs_down(HandLandMarks):
    if len(HandLandMarks) == 0:
        return False

    if HandLandMarks[4][2]       > HandLandMarks[3][2]  \
        and HandLandMarks[4][2]  > HandLandMarks[2][2]  \
        and HandLandMarks[8][2]  > HandLandMarks[12][2] \
        and HandLandMarks[8][2]  > HandLandMarks[16][2] \
        and HandLandMarks[8][2]  > HandLandMarks[20][2] \
        and HandLandMarks[12][2] > HandLandMarks[16][2] \
        and HandLandMarks[12][2] > HandLandMarks[20][2] \
        and HandLandMarks[16][2] > HandLandMarks[20][2] \
        and HandLandMarks[8][1]  < HandLandMarks[6][1]  \
        and HandLandMarks[12][1] < HandLandMarks[10][1] \
        and HandLandMarks[16][1] < HandLandMarks[14][1] \
        and HandLandMarks[20][1] < HandLandMarks[18][1]:
        return True
    else:
        return False
