import os

print('-------------Getting opencv--------------')
    
output=os.system('wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.0.0.zip')
output=os.system('unzip opencv.zip')+output
output=os.system('sudo rm opencv.zip')+output
output=os.system('wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.0.0.zip')+output
output=os.system('unzip opencv_contrib.zip')+output
output=os.system('sudo rm opencv_contrib.zip')+output

if output==0:
    print('success download of opencv')
else :
    print('failed download of opencv')
    
    
output=os.system('wget https://bootstrap.pypa.io/get-pip.py')
output=os.system('sudo python3 get-pip.py')

output=os.system('pip3 install numpy')
output=os.system('cd opencv-3.0.0; mkdir build;cd build')+output
output1=os.system('cd opencv-3.0.0/build/;cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D ENABLE_PRECOMPILED_HEADERS=OFF \
    -D WITH_FFMPEG=OFF\
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.0.0/modules \
    -D BUILD_EXAMPLES=ON ..')

if output==0:
    print('success pre-install of opencv')
else :
    print('failed pre-install of opencv')
      
if output1==1:
    print('success pre-install of opencv')
else :
    print('Errors but should be fine...')


output=os.system('cd opencv-3.0.0/build/;make;sudo make install')
if output==0:
    print('success make/install of opencv')
else :
    print('failed make/install of opencv')
      
output=os.system('sudo rm -r opencv-3.0.0;sudo rm -r opencv_contrib-3.0.0;sudo rm -r build')
if output==0:
    print('success removing files')
else :
    print('failed removing files')