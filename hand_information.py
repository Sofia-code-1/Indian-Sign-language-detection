import modules_imported as mi

class hand_info:

  def __init__(self):
    self.clear_hand_information()

  def __del__(self):
    if len(self.HandLandMarks) !=0:
        self.HandLandMarks.clear()

  def clear_hand_information(self):
    self.is_hand_1                  = None
    self.is_right_hand              = None
    self.hand_orientation           = None
    self.HandLandMarks              = []
    self.is_thumb_opened            = None
    self.is_index_finger_opened     = None
    self.is_middle_finger_opened    = None
    self.is_ring_finger_opened      = None
    self.is_little_finger_opened    = None
    self.separator                  = '\n'
    self.data                       = {'is_hand_1':self.is_hand_1,'is_right_hand':self.is_right_hand,'hand_orientation':self.hand_orientation, \
                                       'HandLandMarks':self.HandLandMarks,\
                                       'is_thumb_opened':self.is_thumb_opened,\
                                       'is_index_finger_opened':self.is_index_finger_opened, \
                                       'is_middle_finger_opened':self.is_middle_finger_opened, \
                                       'is_ring_finger_opened':self.is_ring_finger_opened, \
                                       'is_little_finger_opened':self.is_little_finger_opened}

  def fill_data_with_info(self):
    self.data['is_hand_1']               = self.is_hand_1
    self.data['is_right_hand']           = self.is_right_hand
    self.data['hand_orientation']        = self.hand_orientation
    self.data['HandLandMarks']           = self.HandLandMarks
    self.data['is_thumb_opened']         = self.is_thumb_opened
    self.data['is_index_finger_opened']  = self.is_index_finger_opened
    self.data['is_middle_finger_opened'] = self.is_middle_finger_opened
    self.data['is_ring_finger_opened']   = self.is_ring_finger_opened
    self.data['is_little_finger_opened'] = self.is_little_finger_opened

  def set_log_separator(self, separator):
    self.separator = separator

  def get_hand_information(self,HandLandMarks,is_hand_1=True):
    self.clear_hand_information()

    self.HandLandMarks = HandLandMarks
    self.is_hand_1     = is_hand_1

    self.get_hand_direction()
    if self.is_right_hand == None or self.hand_orientation == None:
        #return self.data  # empty one
        self.get_hand_direction_new()

    if self.is_right_hand == None or self.hand_orientation == None:
        return self.data  # empty one
    if self.is_right_hand   == True and self.hand_orientation ==   0:
        self.get_right_hand_0_degrees_finger_positions()
    elif self.is_right_hand == True and self.hand_orientation ==  90:
        self.get_right_hand_90_degrees_finger_positions()
    elif self.is_right_hand == True and self.hand_orientation == 180:
        self.get_right_hand_180_degrees_finger_positions()
    elif self.is_right_hand == True and self.hand_orientation == 270:
        self.get_right_hand_270_degrees_finger_positions()
    elif self.is_right_hand == False and self.hand_orientation ==   0:
        self.get_left_hand_0_degrees_finger_positions()
    elif self.is_right_hand == False and self.hand_orientation ==  90:
        self.get_left_hand_90_degrees_finger_positions()
    elif self.is_right_hand == False and self.hand_orientation == 180:
        self.get_left_hand_180_degrees_finger_positions()
    elif self.is_right_hand == False and self.hand_orientation == 270:
        self.get_left_hand_270_degrees_finger_positions()

    self.fill_data_with_info()
    return self.data

  def get_hand_direction_new(self):
      if len(self.HandLandMarks) !=0:
          # Right 0                
          if self.HandLandMarks[0][1] > self.HandLandMarks[17][1] and self.HandLandMarks[0][1] > self.HandLandMarks[5][1] and \
          self.HandLandMarks[5][2] < self.HandLandMarks[17][2]:
              self.is_right_hand = True
              self.hand_orientation = 0
              return self.is_right_hand, self.hand_orientation

          # Right 90               
          if self.HandLandMarks[0][2] > self.HandLandMarks[17][2] and self.HandLandMarks[0][2] < self.HandLandMarks[5][2] and \
          self.HandLandMarks[5][1] > self.HandLandMarks[17][1]:
              self.is_right_hand = True
              self.hand_orientation = 90
              return self.is_right_hand, self.hand_orientation

          # Right 180              
          if self.HandLandMarks[0][1] < self.HandLandMarks[17][1] and self.HandLandMarks[0][1] < self.HandLandMarks[5][1] and \
          self.HandLandMarks[5][2] > self.HandLandMarks[17][2]:
              self.is_right_hand = True
              self.hand_orientation = 180
              return self.is_right_hand, self.hand_orientation

          # Right 270              
          if self.HandLandMarks[0][2] < self.HandLandMarks[17][2] and self.HandLandMarks[0][2] < self.HandLandMarks[5][2] and \
          self.HandLandMarks[5][1] < self.HandLandMarks[17][1]:
              self.is_right_hand = True
              self.hand_orientation = 270
              return self.is_right_hand, self.hand_orientation


          # Left 0                 
          if self.HandLandMarks[0][1] > self.HandLandMarks[17][1] and self.HandLandMarks[0][1] > self.HandLandMarks[5][1] and \
          self.HandLandMarks[5][2] > self.HandLandMarks[17][2]:
              self.is_right_hand = False                                          
              self.hand_orientation = 0
              return self.is_right_hand, self.hand_orientation

          # Left 90                
          #if  mi.cfs.diff(self.HandLandMarks[0][1],self.HandLandMarks[17][1],55) and 
          if  self.HandLandMarks[0][2] > self.HandLandMarks[17][2] and self.HandLandMarks[0][2] > self.HandLandMarks[5][2] and \
              self.HandLandMarks[5][1] < self.HandLandMarks[17][1]:
              self.is_right_hand = False
              self.hand_orientation = 90
              return self.is_right_hand, self.hand_orientation

          # Left 180               
          if self.HandLandMarks[0][1] < self.HandLandMarks[17][1] and self.HandLandMarks[0][1] < self.HandLandMarks[5][1] and \
          self.HandLandMarks[5][2] < self.HandLandMarks[17][2]:
              self.is_right_hand = False
              self.hand_orientation = 180
              return self.is_right_hand, self.hand_orientation

          # Left 270               
          if self.HandLandMarks[0][2] < self.HandLandMarks[17][2] and self.HandLandMarks[0][2] < self.HandLandMarks[5][2] and \
          self.HandLandMarks[5][2] > self.HandLandMarks[17][2]:
              self.is_right_hand = False
              self.hand_orientation = 270
              return self.is_right_hand, self.hand_orientation

          if self.is_right_hand is None and self.hand_orientation is None:
              # second try
              # Left 90   for Q             
              if  self.HandLandMarks[0][1] < self.HandLandMarks[17][1] and \
                  mi.cfs.diff(self.HandLandMarks[0][1],self.HandLandMarks[5][1],100) and \
                  self.HandLandMarks[0][2] > self.HandLandMarks[17][2] and self.HandLandMarks[0][2] > self.HandLandMarks[5][2]:
                  self.is_right_hand = False
                  self.hand_orientation = 90
                  return self.is_right_hand, self.hand_orientation

              # Right 90               
              if  self.HandLandMarks[0][1] > self.HandLandMarks[17][1] and \
                  mi.cfs.diff(self.HandLandMarks[0][1],self.HandLandMarks[5][1] ,100) and \
                  self.HandLandMarks[0][2] > self.HandLandMarks[17][2] and self.HandLandMarks[0][2] > self.HandLandMarks[5][2]:
                  self.is_right_hand = True
                  self.hand_orientation = 90
                  return self.is_right_hand, self.hand_orientation
            
  
      return self.is_right_hand, self.hand_orientation

  def get_hand_direction(self):
      if len(self.HandLandMarks) !=0:
          # Right 0                
          if self.HandLandMarks[0][1] > self.HandLandMarks[17][1] and self.HandLandMarks[0][1] > self.HandLandMarks[5][1] and \
          self.HandLandMarks[0][2] < self.HandLandMarks[17][2] and self.HandLandMarks[0][2] > self.HandLandMarks[5][2]:
              self.is_right_hand = True
              self.hand_orientation = 0

          # Right 90               
          if self.HandLandMarks[0][1] > self.HandLandMarks[17][1] and self.HandLandMarks[0][1] < self.HandLandMarks[5][1] and \
          self.HandLandMarks[0][2] > self.HandLandMarks[17][2] and self.HandLandMarks[0][2] > self.HandLandMarks[5][2]:
              self.is_right_hand = True
              self.hand_orientation = 90

          # Right 180              
          if self.HandLandMarks[0][1] < self.HandLandMarks[17][1] and self.HandLandMarks[0][1] < self.HandLandMarks[5][1] and \
          self.HandLandMarks[0][2] > self.HandLandMarks[17][2] and self.HandLandMarks[0][2] < self.HandLandMarks[5][2]:
              self.is_right_hand = True
              self.hand_orientation = 180

          # Right 270              
          if self.HandLandMarks[0][1] < self.HandLandMarks[17][1] and self.HandLandMarks[0][1] > self.HandLandMarks[5][1] and \
          self.HandLandMarks[0][2] < self.HandLandMarks[17][2] and self.HandLandMarks[0][2] < self.HandLandMarks[5][2]:
              self.is_right_hand = True
              self.hand_orientation = 270


          # Left 0                 
          if self.HandLandMarks[0][1] > self.HandLandMarks[17][1] and self.HandLandMarks[0][1] > self.HandLandMarks[5][1] and \
          self.HandLandMarks[0][2] > self.HandLandMarks[17][2] and \
          mi.cfs.diff(self.HandLandMarks[0][2],self.HandLandMarks[5][2],55):
              self.is_right_hand = False                                          
              self.hand_orientation = 0

          # Left 90                
          #if  mi.cfs.diff(self.HandLandMarks[0][1],self.HandLandMarks[17][1],55) and 
          if  self.HandLandMarks[0][1] < self.HandLandMarks[17][1] and \
              mi.cfs.diff(self.HandLandMarks[0][1],self.HandLandMarks[5][1],35) and \
              self.HandLandMarks[0][2] > self.HandLandMarks[17][2] and self.HandLandMarks[0][2] > self.HandLandMarks[5][2]:
              self.is_right_hand = False
              self.hand_orientation = 90

          # Left 180               
          if self.HandLandMarks[0][1] < self.HandLandMarks[17][1] and self.HandLandMarks[0][1] < self.HandLandMarks[5][1] and \
          self.HandLandMarks[5][2] < self.HandLandMarks[17][2] and self.HandLandMarks[0][2] > self.HandLandMarks[5][2]:
              self.is_right_hand = False
              self.hand_orientation = 180

          # Left 270               
          if self.HandLandMarks[0][1] > self.HandLandMarks[17][1] and self.HandLandMarks[0][1] < self.HandLandMarks[5][1] and \
          self.HandLandMarks[0][2] < self.HandLandMarks[17][2] and self.HandLandMarks[0][2] < self.HandLandMarks[5][2]:
              self.is_right_hand = False
              self.hand_orientation = 270

          
          if self.is_right_hand is None and self.hand_orientation is None:
              # second try
              # Left 90   for Q             
              if  self.HandLandMarks[0][1] < self.HandLandMarks[17][1] and \
                  mi.cfs.diff(self.HandLandMarks[0][1],self.HandLandMarks[5][1],100) and \
                  self.HandLandMarks[0][2] > self.HandLandMarks[17][2] and self.HandLandMarks[0][2] > self.HandLandMarks[5][2]:
                  self.is_right_hand = False
                  self.hand_orientation = 90

              # Right 90               
              if  self.HandLandMarks[0][1] > self.HandLandMarks[17][1] and \
                  mi.cfs.diff(self.HandLandMarks[0][1],self.HandLandMarks[5][1] ,100) and \
                  self.HandLandMarks[0][2] > self.HandLandMarks[17][2] and self.HandLandMarks[0][2] > self.HandLandMarks[5][2]:
                  self.is_right_hand = True
                  self.hand_orientation = 90
            
  
      return self.is_right_hand, self.hand_orientation

  def __str__(self):
     hand_name = "No hand"
     if   self.is_hand_1 == True and  self.is_right_hand == True:
         hand_name = "First Right hand"
     elif self.is_hand_1 == True and  self.is_right_hand == False:
         hand_name = "First Left hand"
     elif self.is_hand_1 == False and self.is_right_hand == True:
         hand_name = "Second Right hand"
     elif self.is_hand_1 == False and self.is_right_hand == False:
         hand_name = "Second Left hand"

     hand_orientation_direction = " at " + str(self.hand_orientation) + " degrees"
     
     thumb_position = "None" 
     if self.is_thumb_opened == True:
         thumb_position = "Opened"
     elif self.is_thumb_opened == False:
         thumb_position = "Closed"

     index_finger_position = "None"
     if self.is_index_finger_opened == True:
         index_finger_position = "Opened"
     elif self.is_index_finger_opened == False:
         index_finger_position = "Closed"

     middle_finger_position = "None"
     if self.is_middle_finger_opened == True:
         middle_finger_position = "Opened"
     elif self.is_middle_finger_opened == False:
         middle_finger_position = "Closed"

     ring_finger_position = "None"
     if self.is_ring_finger_opened == True:
         ring_finger_position = "Opened"
     elif self.is_ring_finger_opened == False:
         ring_finger_position = "Closed"

     little_finger_position = "None"
     if self.is_little_finger_opened == True:
         little_finger_position = "Opened"
     elif self.is_little_finger_opened == False:
         little_finger_position = "Closed"

     return ( hand_name + hand_orientation_direction + self.separator +\
             'Thumb is ' + thumb_position + self.separator +\
             'Index finger is ' + index_finger_position + self.separator +\
             'Middle finger is ' + middle_finger_position + self.separator +\
             'Ring finger is ' + ring_finger_position + self.separator +\
             'Little finger is ' + little_finger_position + self.separator +\
             'HandLandMarks: ' + str(self.HandLandMarks))
    
  def get_right_hand_0_degrees_finger_positions(self):
                
    if self.HandLandMarks[4][2]   <  self.HandLandMarks[3][2]:
        self.is_thumb_opened = True
    elif self.HandLandMarks[4][2] >= self.HandLandMarks[3][2]:
        self.is_thumb_opened = False

    if self.HandLandMarks[8][1]   <  self.HandLandMarks[6][1]:
        self.is_index_finger_opened = True
    elif self.HandLandMarks[8][1] >= self.HandLandMarks[6][1]:
        self.is_index_finger_opened = False

    if self.HandLandMarks[12][1]   <  self.HandLandMarks[10][1]:
        self.is_middle_finger_opened = True
    elif self.HandLandMarks[12][1] >= self.HandLandMarks[10][1]:
        self.is_middle_finger_opened = False

    if self.HandLandMarks[16][1]   <  self.HandLandMarks[14][1]:
        self.is_ring_finger_opened = True
    elif self.HandLandMarks[16][1] >= self.HandLandMarks[14][1]:
        self.is_ring_finger_opened = False

    if self.HandLandMarks[20][1]   <  self.HandLandMarks[18][1]:
        self.is_little_finger_opened = True
    elif self.HandLandMarks[20][1] >= self.HandLandMarks[18][1]:
        self.is_little_finger_opened = False

  def get_right_hand_90_degrees_finger_positions(self):
        
    if self.HandLandMarks[4][1]   >  self.HandLandMarks[3][1]:
        self.is_thumb_opened = True
    elif self.HandLandMarks[4][1] <= self.HandLandMarks[3][1]:
        self.is_thumb_opened = False

    if self.HandLandMarks[8][2]   <  self.HandLandMarks[6][2]:
        self.is_index_finger_opened = True
    elif self.HandLandMarks[8][2] >= self.HandLandMarks[6][2]:
        self.is_index_finger_opened = False

    if self.HandLandMarks[12][2]   <  self.HandLandMarks[10][2]:
        self.is_middle_finger_opened = True
    elif self.HandLandMarks[12][2] >= self.HandLandMarks[10][2]:
        self.is_middle_finger_opened = False

    if self.HandLandMarks[16][2]   <  self.HandLandMarks[14][2]:
        self.is_ring_finger_opened = True
    elif self.HandLandMarks[16][2] >= self.HandLandMarks[14][2]:
        self.is_ring_finger_opened = False

    if self.HandLandMarks[20][2]   <  self.HandLandMarks[18][2]:
        self.is_little_finger_opened = True
    elif self.HandLandMarks[20][2] >= self.HandLandMarks[18][2]:
        self.is_little_finger_opened = False

  def get_right_hand_180_degrees_finger_positions(self):
        
    if self.HandLandMarks[4][2]   >  self.HandLandMarks[3][2]:
        self.is_thumb_opened = True
    elif self.HandLandMarks[4][2] <= self.HandLandMarks[3][2]:
        self.is_thumb_opened = False

    if self.HandLandMarks[8][1]   >  self.HandLandMarks[6][1]:
        self.is_index_finger_opened = True
    elif self.HandLandMarks[8][1] <= self.HandLandMarks[6][1]:
        self.is_index_finger_opened = False

    if self.HandLandMarks[12][1]   >  self.HandLandMarks[10][1]:
        self.is_middle_finger_opened = True
    elif self.HandLandMarks[12][1] <= self.HandLandMarks[10][1]:
        self.is_middle_finger_opened = False

    if self.HandLandMarks[16][1]   >  self.HandLandMarks[14][1]:
        self.is_ring_finger_opened = True
    elif self.HandLandMarks[16][1] <= self.HandLandMarks[14][1]:
        self.is_ring_finger_opened = False

    if self.HandLandMarks[20][1]   >  self.HandLandMarks[18][1]:
        self.is_little_finger_opened = True
    elif self.HandLandMarks[20][1] <= self.HandLandMarks[18][1]:
        self.is_little_finger_opened = False

  def get_right_hand_270_degrees_finger_positions(self):

    if self.HandLandMarks[4][1]   <  self.HandLandMarks[3][1]:
        self.is_thumb_opened = True
    elif self.HandLandMarks[4][1] >= self.HandLandMarks[3][1]:
        self.is_thumb_opened = False

    if self.HandLandMarks[8][2]   >  self.HandLandMarks[6][2]:
        self.is_index_finger_opened = True
    elif self.HandLandMarks[8][2] <= self.HandLandMarks[6][2]:
        self.is_index_finger_opened = False

    if self.HandLandMarks[12][2]   >  self.HandLandMarks[10][2]:
        self.is_middle_finger_opened = True
    elif self.HandLandMarks[12][2] <= self.HandLandMarks[10][2]:
        self.is_middle_finger_opened = False

    if self.HandLandMarks[16][2]   >  self.HandLandMarks[14][2]:
        self.is_ring_finger_opened = True
    elif self.HandLandMarks[16][2] <= self.HandLandMarks[14][2]:
        self.is_ring_finger_opened = False

    if self.HandLandMarks[20][2]   >  self.HandLandMarks[18][2]:
        self.is_little_finger_opened = True
    elif self.HandLandMarks[20][2] <= self.HandLandMarks[18][2]:
        self.is_little_finger_opened = False

  def get_left_hand_0_degrees_finger_positions(self):
        
    if self.HandLandMarks[4][2]   >  self.HandLandMarks[3][2]:
        self.is_thumb_opened = True
    elif self.HandLandMarks[4][2] <= self.HandLandMarks[3][2]:
        self.is_thumb_opened = False

    if self.HandLandMarks[8][1]   <  self.HandLandMarks[6][1]:
        self.is_index_finger_opened = True
    elif self.HandLandMarks[8][1] >= self.HandLandMarks[6][1]:
        self.is_index_finger_opened = False

    if self.HandLandMarks[12][1]   <  self.HandLandMarks[10][1]:
        self.is_middle_finger_opened = True
    elif self.HandLandMarks[12][1] >= self.HandLandMarks[10][1]:
        self.is_middle_finger_opened = False

    if self.HandLandMarks[16][1]   <  self.HandLandMarks[14][1]:
        self.is_ring_finger_opened = True
    elif self.HandLandMarks[16][1] >= self.HandLandMarks[14][1]:
        self.is_ring_finger_opened = False

    if self.HandLandMarks[20][1]   <  self.HandLandMarks[18][1]:
        self.is_little_finger_opened = True
    elif self.HandLandMarks[20][1] >= self.HandLandMarks[18][1]:
        self.is_little_finger_opened = False

  def get_left_hand_90_degrees_finger_positions(self):
        
    if self.HandLandMarks[4][1]   <  self.HandLandMarks[3][1]:
        self.is_thumb_opened = True
    elif self.HandLandMarks[4][1] >= self.HandLandMarks[3][1]:
        self.is_thumb_opened = False

    if self.HandLandMarks[8][2]   <  self.HandLandMarks[6][2]:
        self.is_index_finger_opened = True
    elif self.HandLandMarks[8][2] >= self.HandLandMarks[6][2]:
        self.is_index_finger_opened = False

    if self.HandLandMarks[12][2]   <  self.HandLandMarks[10][2]:
        self.is_middle_finger_opened = True
    elif self.HandLandMarks[12][2] >= self.HandLandMarks[10][2]:
        self.is_middle_finger_opened = False

    if self.HandLandMarks[16][2]   <  self.HandLandMarks[14][2]:
        self.is_ring_finger_opened = True
    elif self.HandLandMarks[16][2] >= self.HandLandMarks[14][2]:
        self.is_ring_finger_opened = False

    if self.HandLandMarks[20][2]   <  self.HandLandMarks[18][2]:
        self.is_little_finger_opened = True
    elif self.HandLandMarks[20][2] >= self.HandLandMarks[18][2]:
        self.is_little_finger_opened = False

  def get_left_hand_180_degrees_finger_positions(self):
        
    if self.HandLandMarks[4][2]   <  self.HandLandMarks[3][2]:
        self.is_thumb_opened = True
    elif self.HandLandMarks[4][2] >= self.HandLandMarks[3][2]:
        self.is_thumb_opened = False

    if self.HandLandMarks[8][1]   >  self.HandLandMarks[6][1]:
        self.is_index_finger_opened = True
    elif self.HandLandMarks[8][1] <= self.HandLandMarks[6][1]:
        self.is_index_finger_opened = False

    if self.HandLandMarks[12][1]   >  self.HandLandMarks[10][1]:
        self.is_middle_finger_opened = True
    elif self.HandLandMarks[12][1] <= self.HandLandMarks[10][1]:
        self.is_middle_finger_opened = False

    if self.HandLandMarks[16][1]   >  self.HandLandMarks[14][1]:
        self.is_ring_finger_opened = True
    elif self.HandLandMarks[16][1] <= self.HandLandMarks[14][1]:
        self.is_ring_finger_opened = False

    if self.HandLandMarks[20][1]   >  self.HandLandMarks[18][1]:
        self.is_little_finger_opened = True
    elif self.HandLandMarks[20][1] <= self.HandLandMarks[18][1]:
        self.is_little_finger_opened = False

  def get_left_hand_270_degrees_finger_positions(self):
        
    if self.HandLandMarks[4][1]   >  self.HandLandMarks[3][1]:
        self.is_thumb_opened = True
    elif self.HandLandMarks[4][1] <= self.HandLandMarks[3][1]:
        self.is_thumb_opened = False

    if self.HandLandMarks[8][2]   >  self.HandLandMarks[6][2]:
        self.is_index_finger_opened = True
    elif self.HandLandMarks[8][2] <= self.HandLandMarks[6][2]:
        self.is_index_finger_opened = False

    if self.HandLandMarks[12][2]   >  self.HandLandMarks[10][2]:
        self.is_middle_finger_opened = True
    elif self.HandLandMarks[12][2] <= self.HandLandMarks[10][2]:
        self.is_middle_finger_opened = False

    if self.HandLandMarks[16][2]   >  self.HandLandMarks[14][2]:
        self.is_ring_finger_opened = True
    elif self.HandLandMarks[16][2] <= self.HandLandMarks[14][2]:
        self.is_ring_finger_opened = False

    if self.HandLandMarks[20][2]   >  self.HandLandMarks[18][2]:
        self.is_little_finger_opened = True
    elif self.HandLandMarks[20][2] <= self.HandLandMarks[18][2]:
        self.is_little_finger_opened = False


