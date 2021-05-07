# ARC-ASL-OnlineGrader
Very basic implementation of our ASLNet as an open access server used for generating Homework Reports.

**Note:** Given images must be RGB, not RGBA

![image](https://user-images.githubusercontent.com/36856910/115450424-b791fe80-a1d0-11eb-98eb-a3d2b56ce07c.png)

To be used in conjunction with https://github.com/design-hub-arc/ASL-NET and Tested on linux with an Apache server.

**Project Setup: (assuming server is ready)**

* First setup the ASLNet Neural Network on the server and follow the instructions here: https://github.com/design-hub-arc/ASL-NET
* Next git clone https://github.com/design-hub-arc/ARC-ASL-OnlineGrader.git this repository
* Unzip into the web facing directory
    - make sure to put the ASLNet directory containing the network is in the same directory as savefile.py
* pip install PyMuPDF
