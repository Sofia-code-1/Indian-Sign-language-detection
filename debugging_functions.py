from common_functions import *

def print_and_show_hand_landmarks(RightHandLandMarks,LeftHandLandMarks,vision,image,symbol,left=100,top=20,gap=25,color=(0,200,0)): 

    if len(RightHandLandMarks) !=0:
        vision.putText(image,"First Hand:",(left, top+0*gap), vision.FONT_HERSHEY_COMPLEX,1, color, 2)
        vision.putText(image,str(RightHandLandMarks[0]),(left, top+1*gap), vision.FONT_HERSHEY_COMPLEX,1, color, 2)
        vision.putText(image,str(RightHandLandMarks[1]),(left, top+2*gap), vision.FONT_HERSHEY_COMPLEX,1, color, 2)
        vision.putText(image,str(RightHandLandMarks[2]),(left, top+3*gap), vision.FONT_HERSHEY_COMPLEX,1, color, 2)
        vision.putText(image,str(RightHandLandMarks[3]),(left, top+4*gap), vision.FONT_HERSHEY_COMPLEX,1, color, 2)
        vision.putText(image,str(RightHandLandMarks[4]),(left, top+5*gap), vision.FONT_HERSHEY_COMPLEX,1, color, 2)

    if len(LeftHandLandMarks) !=0:
        vision.putText(image,"Second Hand:",(left, top+6*gap), vision.FONT_HERSHEY_COMPLEX,1, (0,255, 0), 2)
        vision.putText(image,str(LeftHandLandMarks[0]),(left, top+7*gap), vision.FONT_HERSHEY_COMPLEX,1, color, 2)
        vision.putText(image,str(LeftHandLandMarks[1]),(left, top+8*gap), vision.FONT_HERSHEY_COMPLEX,1, color, 2)
        vision.putText(image,str(LeftHandLandMarks[2]),(left, top+9*gap), vision.FONT_HERSHEY_COMPLEX,1, color, 2)
        vision.putText(image,str(LeftHandLandMarks[3]),(left, top+10*gap), vision.FONT_HERSHEY_COMPLEX,1, color, 2)
        vision.putText(image,str(LeftHandLandMarks[4]),(left, top+11*gap), vision.FONT_HERSHEY_COMPLEX,1, color, 2)
    
    if len(RightHandLandMarks) !=0:
        print("First Hand: " + str(RightHandLandMarks[0]))
        print(str(RightHandLandMarks[1])+","+str(RightHandLandMarks[2])+","+str(RightHandLandMarks[3])+","+str(RightHandLandMarks[4]))
        print(str(RightHandLandMarks[5])+","+str(RightHandLandMarks[6])+","+str(RightHandLandMarks[7])+","+str(RightHandLandMarks[8]))
        print(str(RightHandLandMarks[9])+","+str(RightHandLandMarks[10])+","+str(RightHandLandMarks[11])+","+str(RightHandLandMarks[12]))
        print(str(RightHandLandMarks[13])+","+str(RightHandLandMarks[14])+","+str(RightHandLandMarks[15])+","+str(RightHandLandMarks[16]))
        print(str(RightHandLandMarks[17])+","+str(RightHandLandMarks[18])+","+str(RightHandLandMarks[19])+","+str(RightHandLandMarks[20]))

    if len(LeftHandLandMarks) !=0:
        print("Second Hand: " + str(LeftHandLandMarks[0]))
        print(str(LeftHandLandMarks[1])+","+str(LeftHandLandMarks[2])+","+str(LeftHandLandMarks[3])+","+str(LeftHandLandMarks[4]))
        print(str(LeftHandLandMarks[5])+","+str(LeftHandLandMarks[6])+","+str(LeftHandLandMarks[7])+","+str(LeftHandLandMarks[8]))
        print(str(LeftHandLandMarks[9])+","+str(LeftHandLandMarks[10])+","+str(LeftHandLandMarks[11])+","+str(LeftHandLandMarks[12]))
        print(str(LeftHandLandMarks[13])+","+str(LeftHandLandMarks[14])+","+str(LeftHandLandMarks[15])+","+str(LeftHandLandMarks[16]))
        print(str(LeftHandLandMarks[17])+","+str(LeftHandLandMarks[18])+","+str(LeftHandLandMarks[19])+","+str(LeftHandLandMarks[20]))

    print(symbol + " and " + str(data['CapsLock']))

def print_hand_landmarks(RightHandLandMarks,LeftHandLandMarks):
    if len(RightHandLandMarks) !=0:
        print("First Hand: " + str(RightHandLandMarks[0]))
        print(str(RightHandLandMarks[1])+","+str(RightHandLandMarks[2])+","+str(RightHandLandMarks[3])+","+str(RightHandLandMarks[4]))
        print(str(RightHandLandMarks[5])+","+str(RightHandLandMarks[6])+","+str(RightHandLandMarks[7])+","+str(RightHandLandMarks[8]))
        print(str(RightHandLandMarks[9])+","+str(RightHandLandMarks[10])+","+str(RightHandLandMarks[11])+","+str(RightHandLandMarks[12]))
        print(str(RightHandLandMarks[13])+","+str(RightHandLandMarks[14])+","+str(RightHandLandMarks[15])+","+str(RightHandLandMarks[16]))
        print(str(RightHandLandMarks[17])+","+str(RightHandLandMarks[18])+","+str(RightHandLandMarks[19])+","+str(RightHandLandMarks[20]))

    if len(LeftHandLandMarks) !=0:
        print("Second Hand: " + str(LeftHandLandMarks[0]))
        print(str(LeftHandLandMarks[1])+","+str(LeftHandLandMarks[2])+","+str(LeftHandLandMarks[3])+","+str(LeftHandLandMarks[4]))
        print(str(LeftHandLandMarks[5])+","+str(LeftHandLandMarks[6])+","+str(LeftHandLandMarks[7])+","+str(LeftHandLandMarks[8]))
        print(str(LeftHandLandMarks[9])+","+str(LeftHandLandMarks[10])+","+str(LeftHandLandMarks[11])+","+str(LeftHandLandMarks[12]))
        print(str(LeftHandLandMarks[13])+","+str(LeftHandLandMarks[14])+","+str(LeftHandLandMarks[15])+","+str(LeftHandLandMarks[16]))
        print(str(LeftHandLandMarks[17])+","+str(LeftHandLandMarks[18])+","+str(LeftHandLandMarks[19])+","+str(LeftHandLandMarks[20]))



def check_w_conditions(RightHandLandMarks,LeftHandLandMarks):
    #print_hand_landmarks(RightHandLandMarks,LeftHandLandMarks)
    print("RightHandLandMarks[RightHandFingerTipLandMarks[1]][2] < RightHandLandMarks[RightHandFingerTipLandMarks[1] - 2][2] " +\
          str(RightHandLandMarks[RightHandFingerTipLandMarks[1]][2])+" , "+str(RightHandLandMarks[RightHandFingerTipLandMarks[1] - 2][2]) +" , "+ \
          str(RightHandLandMarks[RightHandFingerTipLandMarks[1]][2] < RightHandLandMarks[RightHandFingerTipLandMarks[1] - 2][2]))

    print("RightHandLandMarks[RightHandFingerTipLandMarks[2]][2] < RightHandLandMarks[RightHandFingerTipLandMarks[2] - 2][2] " +\
          str(RightHandLandMarks[RightHandFingerTipLandMarks[2]][2])+" , "+str(RightHandLandMarks[RightHandFingerTipLandMarks[2] - 2][2]) +" , "+ \
          str(RightHandLandMarks[RightHandFingerTipLandMarks[2]][2] < RightHandLandMarks[RightHandFingerTipLandMarks[2] - 2][2]))

    print("RightHandLandMarks[RightHandFingerTipLandMarks[3]][2] < RightHandLandMarks[RightHandFingerTipLandMarks[3] - 2][2] " +\
          str(RightHandLandMarks[RightHandFingerTipLandMarks[3]][2])+" , "+str(RightHandLandMarks[RightHandFingerTipLandMarks[3] - 2][2]) +" , "+ \
          str(RightHandLandMarks[RightHandFingerTipLandMarks[3]][2] < RightHandLandMarks[RightHandFingerTipLandMarks[3] - 2][2]))

    print("RightHandLandMarks[RightHandFingerTipLandMarks[4]][2] < RightHandLandMarks[RightHandFingerTipLandMarks[4] - 2][2] " +\
          str(RightHandLandMarks[RightHandFingerTipLandMarks[4]][2])+" , "+str(RightHandLandMarks[RightHandFingerTipLandMarks[4] - 2][2]) +" , "+ \
          str(RightHandLandMarks[RightHandFingerTipLandMarks[4]][2] < RightHandLandMarks[RightHandFingerTipLandMarks[4] - 2][2]))

    print("LeftHandLandMarks[LeftHandFingerTipLandMarks[1]][2] < LeftHandLandMarks[LeftHandFingerTipLandMarks[1] - 2][2] " +\
          str(LeftHandLandMarks[LeftHandFingerTipLandMarks[1]][2])+" , "+str(LeftHandLandMarks[LeftHandFingerTipLandMarks[1] - 2][2]) +" , "+ \
          str(LeftHandLandMarks[LeftHandFingerTipLandMarks[1]][2] < LeftHandLandMarks[LeftHandFingerTipLandMarks[1] - 2][2]))

    print("LeftHandLandMarks[LeftHandFingerTipLandMarks[2]][2] < LeftHandLandMarks[LeftHandFingerTipLandMarks[2] - 2][2] " +\
          str(LeftHandLandMarks[LeftHandFingerTipLandMarks[2]][2])+" , "+str(LeftHandLandMarks[LeftHandFingerTipLandMarks[2] - 2][2]) +" , "+ \
          str(LeftHandLandMarks[LeftHandFingerTipLandMarks[2]][2] < LeftHandLandMarks[LeftHandFingerTipLandMarks[2] - 2][2]))

    print("LeftHandLandMarks[LeftHandFingerTipLandMarks[3]][2] < LeftHandLandMarks[LeftHandFingerTipLandMarks[3] - 2][2] " +\
          str(LeftHandLandMarks[LeftHandFingerTipLandMarks[3]][2])+" , "+str(LeftHandLandMarks[LeftHandFingerTipLandMarks[3] - 2][2]) +" , "+ \
          str(LeftHandLandMarks[LeftHandFingerTipLandMarks[3]][2] < LeftHandLandMarks[LeftHandFingerTipLandMarks[3] - 2][2]))

    print("LeftHandLandMarks[LeftHandFingerTipLandMarks[4]][2] < LeftHandLandMarks[LeftHandFingerTipLandMarks[4] - 2][2] " +\
          str(LeftHandLandMarks[LeftHandFingerTipLandMarks[4]][2])+" , "+str(LeftHandLandMarks[LeftHandFingerTipLandMarks[4] - 2][2]) +" , "+ \
          str(LeftHandLandMarks[LeftHandFingerTipLandMarks[4]][2] < LeftHandLandMarks[LeftHandFingerTipLandMarks[4] - 2][2]))

    print("diff_between(RightHandLandMarks[RightHandFingerTipLandMarks[1]][1], RightHandLandMarks[RightHandFingerTipLandMarks[1]-2][1],\
           RightHandLandMarks[RightHandFingerTipLandMarks[1]-3][1], \
           LeftHandLandMarks[LeftHandFingerTipLandMarks[1]][1], LeftHandLandMarks[LeftHandFingerTipLandMarks[1] - 2][1],\
           LeftHandLandMarks[LeftHandFingerTipLandMarks[1] - 3][1],55)" +" , " +\
         str(RightHandLandMarks[RightHandFingerTipLandMarks[1]][1])+" , "+ str(RightHandLandMarks[RightHandFingerTipLandMarks[1]-2][1]) +" , " +\
         str(RightHandLandMarks[RightHandFingerTipLandMarks[1]-3][1])+" , "+\
         str(LeftHandLandMarks[LeftHandFingerTipLandMarks[1]][1])+ " , "+ str(LeftHandLandMarks[LeftHandFingerTipLandMarks[1] - 2][1]) + " , " +\
         str(LeftHandLandMarks[LeftHandFingerTipLandMarks[1] - 3][1]) + " , " +\
         str(diff_between(RightHandLandMarks[RightHandFingerTipLandMarks[1]][1], RightHandLandMarks[RightHandFingerTipLandMarks[1]-2][1],\
         RightHandLandMarks[RightHandFingerTipLandMarks[1]-3][1], \
         LeftHandLandMarks[LeftHandFingerTipLandMarks[1]][1], LeftHandLandMarks[LeftHandFingerTipLandMarks[1] - 2][1],\
         LeftHandLandMarks[LeftHandFingerTipLandMarks[1] - 3][1],55)))

    print("diff_between(RightHandLandMarks[RightHandFingerTipLandMarks[2]-1][1], RightHandLandMarks[RightHandFingerTipLandMarks[2]-2][1],\
           RightHandLandMarks[RightHandFingerTipLandMarks[2]-3][1], \
           LeftHandLandMarks[LeftHandFingerTipLandMarks[2] - 1][1], LeftHandLandMarks[LeftHandFingerTipLandMarks[2] - 2][1],\
           LeftHandLandMarks[LeftHandFingerTipLandMarks[2] - 3][1],55)" +" , " +\
         str(RightHandLandMarks[RightHandFingerTipLandMarks[2]-1][1])+" , "+ str(RightHandLandMarks[RightHandFingerTipLandMarks[2]-2][1]) +" , " +\
         str(RightHandLandMarks[RightHandFingerTipLandMarks[2]-3][1])+" , "+\
         str(LeftHandLandMarks[LeftHandFingerTipLandMarks[2] - 1][1])+ " , "+ str(LeftHandLandMarks[LeftHandFingerTipLandMarks[2] - 2][1]) + " , " +\
         str(LeftHandLandMarks[LeftHandFingerTipLandMarks[2] - 3][1]) + " , " +\
         str(diff_between(RightHandLandMarks[RightHandFingerTipLandMarks[2]-1][1], RightHandLandMarks[RightHandFingerTipLandMarks[2]-2][1],\
         RightHandLandMarks[RightHandFingerTipLandMarks[2]-3][1], \
         LeftHandLandMarks[LeftHandFingerTipLandMarks[2] - 1][1], LeftHandLandMarks[LeftHandFingerTipLandMarks[2] - 2][1],\
         LeftHandLandMarks[LeftHandFingerTipLandMarks[2] - 3][1],55)))

    print("diff_between(RightHandLandMarks[RightHandFingerTipLandMarks[3]-1][1], RightHandLandMarks[RightHandFingerTipLandMarks[3]-2][1],\
           RightHandLandMarks[RightHandFingerTipLandMarks[3]-3][1], \
           LeftHandLandMarks[LeftHandFingerTipLandMarks[3] - 1][1], LeftHandLandMarks[LeftHandFingerTipLandMarks[3] - 2][1],\
           LeftHandLandMarks[LeftHandFingerTipLandMarks[3] - 3][1],55)" +" , " +\
         str(RightHandLandMarks[RightHandFingerTipLandMarks[3]-1][1])+" , "+ str(RightHandLandMarks[RightHandFingerTipLandMarks[3]-2][1]) +" , " +\
         str(RightHandLandMarks[RightHandFingerTipLandMarks[3]-3][1])+" , "+\
         str(LeftHandLandMarks[LeftHandFingerTipLandMarks[3] - 1][1])+ " , "+ str(LeftHandLandMarks[LeftHandFingerTipLandMarks[3] - 2][1]) + " , " +\
         str(LeftHandLandMarks[LeftHandFingerTipLandMarks[3] - 3][1]) + " , " +\
         str(diff_between(RightHandLandMarks[RightHandFingerTipLandMarks[3]-1][1], RightHandLandMarks[RightHandFingerTipLandMarks[3]-2][1],\
         RightHandLandMarks[RightHandFingerTipLandMarks[3]-3][1], \
         LeftHandLandMarks[LeftHandFingerTipLandMarks[3] - 1][1], LeftHandLandMarks[LeftHandFingerTipLandMarks[3] - 2][1],\
         LeftHandLandMarks[LeftHandFingerTipLandMarks[3] - 3][1],55)))

    print("diff_between(RightHandLandMarks[RightHandFingerTipLandMarks[4]-1][1], RightHandLandMarks[RightHandFingerTipLandMarks[4]-2][1],\
           RightHandLandMarks[RightHandFingerTipLandMarks[4]-3][1], \
           LeftHandLandMarks[LeftHandFingerTipLandMarks[4] - 1][1], LeftHandLandMarks[LeftHandFingerTipLandMarks[4] - 2][1],\
           LeftHandLandMarks[LeftHandFingerTipLandMarks[4] - 3][1],55)" +" , " +\
         str(RightHandLandMarks[RightHandFingerTipLandMarks[4]-1][1])+" , "+ str(RightHandLandMarks[RightHandFingerTipLandMarks[4]-2][1]) +" , " +\
         str(RightHandLandMarks[RightHandFingerTipLandMarks[4]-3][1])+" , "+\
         str(LeftHandLandMarks[LeftHandFingerTipLandMarks[4] - 1][1])+ " , "+ str(LeftHandLandMarks[LeftHandFingerTipLandMarks[4] - 2][1]) + " , " +\
         str(LeftHandLandMarks[LeftHandFingerTipLandMarks[4] - 3][1]) + " , " +\
         str(diff_between(RightHandLandMarks[RightHandFingerTipLandMarks[4]-1][1], RightHandLandMarks[RightHandFingerTipLandMarks[4]-2][1],\
         RightHandLandMarks[RightHandFingerTipLandMarks[4]-3][1], \
         LeftHandLandMarks[LeftHandFingerTipLandMarks[4] - 1][1], LeftHandLandMarks[LeftHandFingerTipLandMarks[4] - 2][1],\
         LeftHandLandMarks[LeftHandFingerTipLandMarks[4] - 3][1],55)))

    print("diff_between(RightHandLandMarks[RightHandFingerTipLandMarks[1]-1][2], RightHandLandMarks[RightHandFingerTipLandMarks[1]-2][2],\
           RightHandLandMarks[RightHandFingerTipLandMarks[1]-3][2], \
           LeftHandLandMarks[LeftHandFingerTipLandMarks[1] - 1][2], LeftHandLandMarks[LeftHandFingerTipLandMarks[1] - 2][2],\
           LeftHandLandMarks[LeftHandFingerTipLandMarks[1] - 3][2],55)" +" , " +\
         str(RightHandLandMarks[RightHandFingerTipLandMarks[1]-1][2])+" , "+ str(RightHandLandMarks[RightHandFingerTipLandMarks[1]-2][2]) +" , " +\
         str(RightHandLandMarks[RightHandFingerTipLandMarks[1]-3][2])+" , "+\
         str(LeftHandLandMarks[LeftHandFingerTipLandMarks[1] - 1][2])+ " , "+ str(LeftHandLandMarks[LeftHandFingerTipLandMarks[1] - 2][2]) + " , " +\
         str(LeftHandLandMarks[LeftHandFingerTipLandMarks[1] - 3][2]) + " , " +\
         str(diff_between(RightHandLandMarks[RightHandFingerTipLandMarks[1]-1][2], RightHandLandMarks[RightHandFingerTipLandMarks[1]-2][2],\
         RightHandLandMarks[RightHandFingerTipLandMarks[1]-3][2], \
         LeftHandLandMarks[LeftHandFingerTipLandMarks[1] - 1][2], LeftHandLandMarks[LeftHandFingerTipLandMarks[1] - 2][2],\
         LeftHandLandMarks[LeftHandFingerTipLandMarks[1] - 3][2],55)))

    print("diff_between(RightHandLandMarks[RightHandFingerTipLandMarks[2]-1][2], RightHandLandMarks[RightHandFingerTipLandMarks[2]-2][2],\
           RightHandLandMarks[RightHandFingerTipLandMarks[2]-3][2], \
           LeftHandLandMarks[LeftHandFingerTipLandMarks[2] - 1][2], LeftHandLandMarks[LeftHandFingerTipLandMarks[2] - 2][2],\
           LeftHandLandMarks[LeftHandFingerTipLandMarks[2] - 3][2],55)" +" , " +\
         str(RightHandLandMarks[RightHandFingerTipLandMarks[2]-1][2])+" , "+ str(RightHandLandMarks[RightHandFingerTipLandMarks[2]-2][2]) +" , " +\
         str(RightHandLandMarks[RightHandFingerTipLandMarks[2]-3][2])+" , "+\
         str(LeftHandLandMarks[LeftHandFingerTipLandMarks[2] - 1][2])+ " , "+ str(LeftHandLandMarks[LeftHandFingerTipLandMarks[2] - 2][2]) + " , " +\
         str(LeftHandLandMarks[LeftHandFingerTipLandMarks[2] - 3][2]) + " , " +\
         str(diff_between(RightHandLandMarks[RightHandFingerTipLandMarks[2]-1][2], RightHandLandMarks[RightHandFingerTipLandMarks[2]-2][2],\
         RightHandLandMarks[RightHandFingerTipLandMarks[2]-3][2], \
         LeftHandLandMarks[LeftHandFingerTipLandMarks[2] - 1][2], LeftHandLandMarks[LeftHandFingerTipLandMarks[2] - 2][2],\
         LeftHandLandMarks[LeftHandFingerTipLandMarks[2] - 3][2],55)))

    print("diff_between(RightHandLandMarks[RightHandFingerTipLandMarks[3]-1][2], RightHandLandMarks[RightHandFingerTipLandMarks[3]-2][2],\
           RightHandLandMarks[RightHandFingerTipLandMarks[3]-3][2], \
           LeftHandLandMarks[LeftHandFingerTipLandMarks[3] - 1][2], LeftHandLandMarks[LeftHandFingerTipLandMarks[3] - 2][2],\
           LeftHandLandMarks[LeftHandFingerTipLandMarks[3] - 3][2],55)" +" , " +\
         str(RightHandLandMarks[RightHandFingerTipLandMarks[3]-1][2])+" , "+ str(RightHandLandMarks[RightHandFingerTipLandMarks[3]-2][2]) +" , " +\
         str(RightHandLandMarks[RightHandFingerTipLandMarks[3]-3][2])+" , "+\
         str(LeftHandLandMarks[LeftHandFingerTipLandMarks[3] - 1][2])+ " , "+ str(LeftHandLandMarks[LeftHandFingerTipLandMarks[3] - 2][2]) + " , " +\
         str(LeftHandLandMarks[LeftHandFingerTipLandMarks[3] - 3][2]) + " , " +\
         str(diff_between(RightHandLandMarks[RightHandFingerTipLandMarks[3]-1][2], RightHandLandMarks[RightHandFingerTipLandMarks[3]-2][2],\
         RightHandLandMarks[RightHandFingerTipLandMarks[3]-3][2], \
         LeftHandLandMarks[LeftHandFingerTipLandMarks[3] - 1][2], LeftHandLandMarks[LeftHandFingerTipLandMarks[3] - 2][2],\
         LeftHandLandMarks[LeftHandFingerTipLandMarks[3] - 3][2],55)))

    print("diff_between(RightHandLandMarks[RightHandFingerTipLandMarks[4]-1][2], RightHandLandMarks[RightHandFingerTipLandMarks[4]-2][2],\
           RightHandLandMarks[RightHandFingerTipLandMarks[4]-3][2], \
           LeftHandLandMarks[LeftHandFingerTipLandMarks[4] - 1][2], LeftHandLandMarks[LeftHandFingerTipLandMarks[4] - 2][2],\
           LeftHandLandMarks[LeftHandFingerTipLandMarks[4] - 3][2],55)" +" , " +\
         str(RightHandLandMarks[RightHandFingerTipLandMarks[4]-1][2])+" , "+ str(RightHandLandMarks[RightHandFingerTipLandMarks[4]-2][2]) +" , " +\
         str(RightHandLandMarks[RightHandFingerTipLandMarks[4]-3][2])+" , "+\
         str(LeftHandLandMarks[LeftHandFingerTipLandMarks[4] - 1][2])+ " , "+ str(LeftHandLandMarks[LeftHandFingerTipLandMarks[4] - 2][2]) + " , " +\
         str(LeftHandLandMarks[LeftHandFingerTipLandMarks[4] - 3][2]) + " , " +\
         str(diff_between(RightHandLandMarks[RightHandFingerTipLandMarks[4]-1][2], RightHandLandMarks[RightHandFingerTipLandMarks[4]-2][2],\
         RightHandLandMarks[RightHandFingerTipLandMarks[4]-3][2], \
         LeftHandLandMarks[LeftHandFingerTipLandMarks[4] - 1][2], LeftHandLandMarks[LeftHandFingerTipLandMarks[4] - 2][2],\
         LeftHandLandMarks[LeftHandFingerTipLandMarks[4] - 3][2],55)))
