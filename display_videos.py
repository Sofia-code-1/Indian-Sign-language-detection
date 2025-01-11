import modules_imported as mi
import os

def video_symbol_display():   
    text_colors = [(255,0,0),(0,255,0),(0,0,255)]
    no_of_text_colors = len(text_colors)
    text_color_number = 0

    lines = []
    with open("Sentence.txt", "r") as f:
        lines = f.readlines()
        f.close()
    for line in lines:
        words = line.split()
        for word in words:
            try:
                selected_file = "H:/8 Semester/Honors/Videos/" + word + ".mov"
            except Exception as e:
                continue
            screen = mi.vision.VideoCapture(selected_file)
            while True:
                success, action_video = screen.read()  
                if action_video is None:
                    break
                mi.vision.putText(action_video, "Narration" , (800, 50), mi.vision.FONT_HERSHEY_COMPLEX,1, (255, 0, 0), 2)
                word = word.replace('_',' ')
                mi.vision.putText(action_video, word, (100, 400), mi.vision.FONT_HERSHEY_COMPLEX,4, text_colors[text_color_number], 5)
                mi.vision.imshow("Image", action_video)
                mi.vision.waitKey(5)
            screen.release()

        text_color_number += 1
        if text_color_number >= no_of_text_colors:
            text_color_number = 0

    mi.vision.destroyAllWindows()   

    return "Exit"
