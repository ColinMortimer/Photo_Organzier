# sorts images into folders by month

import os
import image
import time
import glob
import shutil

path = raw_input('Enter path to photo directory: ')

os.chdir(path)

for file in glob.glob('*.jpg'):
    ctime = os.path.getctime(file)
    ltime = time.localtime(ctime)
    tm_yday = ltime[7]
    tm_year = ltime[0]
    filename = str(tm_year) + '_' + str(tm_yday)
    if filename not in glob.glob('*'):
        os.makedirs(filename)
    src = os.path.join(path, file)
    dst = os.path.join(path, filename)
    shutil.move(src, dst)

print('Photo organizaton complete')
    
        
    

    
 
