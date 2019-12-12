import ascii_art
import string

def test_ascii_art():
  image = '''\
 ##  ###   ##  #### ####  ##  #  #   ## #  # #    ###  ###  #  # #   ##### 
#  # #  # #  # #    #    #  # #  #    # # #  #    #  # #  # #  # #   #   # 
#  # ###  #    ###  ###  #    ####    # ##   #    #  # #  # #  #  # #   #  
#### #  # #    #    #    # ## #  #    # # #  #    ###  ###  #  #   #   #   
#  # #  # #  # #    #    #  # #  # #  # # #  #    #    # #  #  #   #  #    
#  # ###   ##  #### #     ### #  #  ##  #  # #### #    #  #  ##    #  #### '''
  assert ascii_art.text_to_image(string.ascii_uppercase) == image
  assert ascii_art.image_to_text(image) == 'ABCEFGHJKLPRUYZ'
