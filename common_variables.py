#common variables used across files

config_data = {'config_file_path':'configuration.json','include_letters':{},'include_words':{},
               'webcam':'',
               'CapsLock':None,'debug':None,'to_control_flow_for_debug':None,
               'log_file_path':'','log_file_path_for_sample_data':'','log_hand_landmarks_to_file':None,
               'take_sample_data':None,'take_sample_data_for_symbol':'',
               'take_images_of_symbols':None,
               'include_sound':None
               }

video_device          = 0
screen                = None
hand_detector         = None
hand_1                = None
hand_2                = None
hand_1_data           = None
hand_2_data           = None
Hand_1_LandMarks      = []
Hand_2_LandMarks      = []

log                   = None

previous_symbol = ''
symbol          = ''
symbol_matched  = False

previous_word_symbol = ''
word_symbol          = ''

