import os

class logging:
    def __init__(self):
        self.hand_1_log_count = 0
        self.hand_2_log_count = 0
        self.log_folder = "Logging/"
        self.log_file_name_prefix = "Logging"
        self.log_file_name_suffix = "txt"
        self.log_file_path = ''
        self.hand_one_log_file_path = ''
        self.hand_two_log_file_path = ''
        self.log_file_path_for_array = ''
        self.hand_one_log_file_path_for_array = ''
        self.hand_two_log_file_path_for_array = ''
        self.symbol = ''

    def create_log_files(self,symbol=''):
        self.symbol = symbol
        if symbol != "":
            self.log_file_path = self.log_folder + symbol + "_" + self.log_file_name_prefix + "." + self.log_file_name_suffix
            with open(self.log_file_path, 'w') as f: 
                f.write("logging for symbol " + symbol + "!!!") 
                f.write("\n")
                f.close()

            self.log_file_path_for_array = self.log_folder + symbol + "_" + self.log_file_name_prefix + "_array." + self.log_file_name_suffix
            with open(self.log_file_path_for_array, 'w') as f: 
                f.write("logging for symbol " + symbol + "!!!") 
                f.write("\n")
                f.close()

            self.hand_one_log_file_path = self.log_folder + symbol + "_" + "HandOne_" + self.log_file_name_prefix + "." + self.log_file_name_suffix
            with open(self.hand_one_log_file_path, 'w') as f: 
                f.write("HandOne logging for symbol " + symbol + "!!!") 
                f.write("\n")
                f.close()

            self.hand_one_log_file_path_for_array = self.log_folder + symbol + "_" + "HandOne_" + self.log_file_name_prefix + "_array." + self.log_file_name_suffix
            with open(self.hand_one_log_file_path_for_array, 'w') as f: 
                f.write("HandOne logging for symbol " + symbol + "!!!") 
                f.write("\n")
                f.close()

            self.hand_two_log_file_path = self.log_folder + symbol + "_" + "HandTwo_" + self.log_file_name_prefix + "." + self.log_file_name_suffix
            with open(self.hand_two_log_file_path, 'w') as f: 
                f.write("HandTwo logging for symbol " + symbol + "!!!") 
                f.write("\n")
                f.close()
            self.hand_two_log_file_path_for_array = self.log_folder + symbol + "_" + "HandTwo_" + self.log_file_name_prefix + "_array." + self.log_file_name_suffix
            with open(self.hand_two_log_file_path_for_array, 'w') as f: 
                f.write("HandTwo logging for symbol " + symbol + "!!!") 
                f.write("\n")
                f.close()
        else:
            self.log_file_path = self.log_folder + self.log_file_name_prefix + "." + self.log_file_name_suffix
            with open(self.log_file_path, 'w') as f: 
                f.write("logging!!!") 
                f.write("\n")
                f.close()

            self.log_file_path_for_array = self.log_folder + self.log_file_name_prefix + "_array." + self.log_file_name_suffix
            with open(self.log_file_path_for_array, 'w') as f: 
                f.write("logging!!!") 
                f.write("\n")
                f.close()

    def open_log_file(self,symbol=''):
        self.create_log_files(symbol)

    def write_message(self,message,hand_name=''):
        f = None
        open_mode = ""
        if message == "Log started":
            self.hand_1_log_count = 0
            self.hand_2_log_count = 0
            open_mode = "w"
        else:
            open_mode = "a"

        if hand_name == "hand_1":
           with open(self.hand_one_log_file_path, open_mode) as f:
                f.write(message) 
                f.write("\n")
                f.close()
           with open(self.hand_one_log_file_path_for_array,open_mode) as f:
                f.write(message) 
                f.write("\n")
                f.close()
        elif hand_name == "hand_2":
           with open(self.hand_two_log_file_path, open_mode) as f:
                f.write(message) 
                f.write("\n")
                f.close()
           with open(self.hand_two_log_file_path_for_array, open_mode) as f:
                f.write(message) 
                f.write("\n")
                f.close()
        else:
            with open(self.log_file_path, open_mode) as f: 
                f.write(message) 
                f.write("\n")
                f.close()
            with open(self.log_file_path_for_array, open_mode) as f: 
                f.write(message) 
                f.write("\n")
                f.close()


    def write_hand_landmarks(self,hand_info,hand_name=''):
        f = None
        if hand_name == "hand_1":
           with open(self.hand_one_log_file_path_for_array, "a") as f_array:
               with open(self.hand_one_log_file_path, "a") as f:
                   f.write(str(self.hand_1_log_count) + "." + str(hand_info))
                   f.write("\n")
                   f.close()

                   f_array.write("HandOneLandMarksDict[" + str(self.hand_1_log_count) + "]=np.array(")
                   f_array.write(str(hand_info.HandLandMarks)) 
                   f_array.write(")\n")
                   f_array.close()
              
                   self.hand_1_log_count +=1
        elif hand_name == "hand_2":
           with open(self.hand_two_log_file_path_for_array, "a") as f_array:
               with open(self.hand_two_log_file_path, "a") as f:
                   f.write(str(self.hand_2_log_count) + "." + str(hand_info))
                   f.write("\n")
                   f.close()

                   f_array.write("HandTwoLandMarksDict[" + str(self.hand_2_log_count) + "]=np.array(")
                   f_array.write(str(hand_info.HandLandMarks)) 
                   f_array.write(")\n")
                   f_array.close()
              
                   self.hand_2_log_count +=1
        else:
          with open(self.log_file_path_for_array, "a") as f_array: 
              with open(self.log_file_path, "a") as f: 
                f.write(str(self.hand_1_log_count) + "." + str(hand_info))
                f.write("\n")
                f.close()

                f_array.write("HandTwoLandMarksDict[" + str(self.hand_1_log_count) + "]=np.array(")
                f_array.write(str(hand_info.HandLandMarks)) 
                f_array.write(")\n")
                f_array.close()
              
                self.hand_1_log_count +=1




