# Manage Render Window Size
# Facebook = 
# Instagram = 1350x1080 max (i use 1:1)
# Linkedin = 

def SetRenderWindowSizeCustom(sizeX, sizeY):
        vrOSGWidget.setFixedRenderWindowSize(sizeX, sizeY)
        print("Render Window Size Active: " + str(sizeX) + "x" + str(sizeY))

def SetRenderWindowSizeDynamic(ratiox, ratioy):
        # reset windows size to dynamic
        SetRenderWindowSizeCustom(0,0)
        currentRenderWindowX = vrOSGWidget.getRenderWindowWidth(0)
        currentRenderWindowY = vrOSGWidget.getRenderWindowHeight(0)
        print("Current Render Window Size: " + str(currentRenderWindowX) + "x" + str(currentRenderWindowY))
        if ratiox > ratioy:
            # Orizontal
            sizeX = int(currentRenderWindowX)
            sizeY = int(currentRenderWindowX/ratiox*ratioy)
            # check if the the new Y size is bigger than the current
            if sizeY > currentRenderWindowY:
                sizeX = int(currentRenderWindowY/ratioy*ratiox)
                sizeY = int(currentRenderWindowY)
        else:
            #Vertical
            sizeX = int(currentRenderWindowY/ratioy*ratiox)
            sizeY = int(currentRenderWindowY)
            # check if the the new X size is bigger than the current
            if sizeX > currentRenderWindowX:
                sizeX = int(currentRenderWindowX)
                sizeY = int(currentRenderWindowX/ratiox*ratioy)
        vrOSGWidget.setFixedRenderWindowSize(sizeX, sizeY)
        print("Render Window Size Active: " + str(sizeX) + "x" + str(sizeY))

        
def calcCurrentRenderSize():
    currentRenderWindowX = vrOSGWidget.getRenderWindowWidth(0)
    currentRenderWindowY = vrOSGWidget.getRenderWindowHeight(0)
    ratio = round(int(currentRenderWindowX)/int(currentRenderWindowY), 2)
    ratioX = 1
    ratioY = 1
    if currentRenderWindowX > currentRenderWindowY:
        ratioY = currentRenderWindowY/currentRenderWindowX
    elif currentRenderWindowY > currentRenderWindowX:
        ratioX = currentRenderWindowX/currentRenderWindowY
    ratioStr = str(round(ratioX, 2)) + ":" + str(round(ratioY, 2))
    
    ratio169 = round(16/9, 2)
    ratio32 = round(3/2, 2)
    ratio43 = round(4/3, 2)
    ratioA = round(297/210, 2)
    ratio169V = round(9/16, 2)
    ratio32V = round(2/3, 2)
    ratio43V = round(3/4, 2)
    ratioAV = round(210/297, 2)
    # print(str(ratio))
    if ratio == ratio169:
        ratioStr = "16/9 Orizontal"
    elif ratio == ratio32:
        ratioStr = "3/2 Orizontal"
    elif ratio == ratio43:
        ratioStr = "4/3 Orizontal"
    elif ratio == ratioA:
        ratioStr = "Ax Orizontal"
    elif ratio == ratio169V:
        ratioStr = "16/9 Vertical"
    elif ratio == ratio32V:
        ratioStr = "3/2 Vertical"
    elif ratio == ratio43V:
        ratioStr = "4/3 Vertical"
    elif ratio == ratioAV:
        ratioStr = "Ax Vertical"

    strSizeInfo = str(currentRenderWindowX) + "x" + str(currentRenderWindowY) + " - " + ratioStr       
    # print("Current Render Window Size: " + strSizeInfo)
    return strSizeInfo

#################################################################
# Libs
from PySide2 import QtCore, QtGui, QtWidgets

importError = False
try:
    import vrOSGWidget
except ImportError:
    importError = True
    pass

import uiTools

#################################################################
# Build Menu
vrManageWS_form, vrManageWS_base = uiTools.loadUiType('SetRenderWindowSizeUI.ui')

class vrManageWS(vrManageWS_form, vrManageWS_base):
    def __init__(self, parent=None):
        super(vrManageWS, self).__init__(parent)
        parent.layout().addWidget(self)
        self.parent = parent
        self.setupUi(self)

        # add resize grip in bottom right corner.
        self.sizeGrip = QtWidgets.QSizeGrip(parent);
        self.sizeGrip.setFixedSize(16, 16)
        self.sizeGrip.move(parent.rect().bottomRight() - self.sizeGrip.rect().bottomRight())
        self.sizeGrip.raise_()
        self.sizeGrip.show()
        
        self._SIZUPD_.clicked.connect(self._SIZUPD)
        
        self._1080O_.clicked.connect(self._1080O)
        self._1080O_.clicked.connect(self._SIZUPD)
        self._1080V_.clicked.connect(self._1080V)
        self._1080V_.clicked.connect(self._SIZUPD)
        self._720O_.clicked.connect(self._720O)
        self._720O_.clicked.connect(self._SIZUPD)
        self._720V_.clicked.connect(self._720V)
        self._720V_.clicked.connect(self._SIZUPD)
        
        self._D169O_.clicked.connect(self._D169O)
        self._D169O_.clicked.connect(self._SIZUPD)
        self._D169V_.clicked.connect(self._D169V)
        self._D169V_.clicked.connect(self._SIZUPD)
        self._D43O_.clicked.connect(self._D43O)
        self._D43O_.clicked.connect(self._SIZUPD)
        self._D43V_.clicked.connect(self._D43V)
        self._D43V_.clicked.connect(self._SIZUPD)
        self._D32O_.clicked.connect(self._D32O)
        self._D32O_.clicked.connect(self._SIZUPD)
        self._D32V_.clicked.connect(self._D32V)
        self._D32V_.clicked.connect(self._SIZUPD)
        self._DAXO_.clicked.connect(self._DAXO)
        self._DAXO_.clicked.connect(self._SIZUPD)
        self._DAXV_.clicked.connect(self._DAXV)
        self._DAXV_.clicked.connect(self._SIZUPD)
        self._D11_.clicked.connect(self._D11)
        self._D11_.clicked.connect(self._SIZUPD)
        
        self._DYNA_.clicked.connect(self._DYNA)
        self._UNDOCKRW_.clicked.connect(self._UNDOCKRW)
        self._DOCKRW_.clicked.connect(self._DOCKRW)
        self._TOGFULLRW_.clicked.connect(self._TOGFULLRW)

    def resizeEvent(self, event):
        # move resize grip to bottom right corner.
        self.sizeGrip.move(self.parent.rect().bottomRight() - self.sizeGrip.rect().bottomRight())
        self.sizeGrip.raise_()
    
    def _SIZUPD(self):
        strSizeInfo = calcCurrentRenderSize()
        self.currentSizeLabel.setProperty("text", strSizeInfo)
    
    #fixed sizes
    def _1080O(self):
        SetRenderWindowSizeCustom(1920, 1080)
    
    def _1080V(self):
        SetRenderWindowSizeCustom(1080, 1920)
    
    def _720O(self):
        SetRenderWindowSizeCustom(1280, 720)
    
    def _720V(self):
        SetRenderWindowSizeCustom(720, 1280)
    
    # Dynamic Sizes
    def _DYNA(self):
        SetRenderWindowSizeCustom(0, 0)
        # print("Not Yet Implemented")
        
    def _D169O(self):
        ratiox = 16
        ratioy = 9
        SetRenderWindowSizeDynamic(ratiox, ratioy)
    
    def _D169V(self):
        ratiox = 9
        ratioy = 16
        SetRenderWindowSizeDynamic(ratiox, ratioy)
    
    def _D43O(self):
        ratiox = 4
        ratioy = 3
        SetRenderWindowSizeDynamic(ratiox, ratioy)
    
    def _D43V(self):
        ratiox = 3
        ratioy = 4
        SetRenderWindowSizeDynamic(ratiox, ratioy)
        
    def _D32O(self):
        ratiox = 3
        ratioy = 2
        SetRenderWindowSizeDynamic(ratiox, ratioy)
    
    def _D32V(self):
        ratiox = 2
        ratioy = 3
        SetRenderWindowSizeDynamic(ratiox, ratioy)
    
    def _DAXO(self):
        ratiox = 297
        ratioy = 210
        SetRenderWindowSizeDynamic(ratiox, ratioy)
    
    def _DAXV(self):
        ratiox = 210
        ratioy = 297
        SetRenderWindowSizeDynamic(ratiox, ratioy)
    
    def _D11(self):
        ratiox = 1
        ratioy = 1
        SetRenderWindowSizeDynamic(ratiox, ratioy)
    
    # def _DAXV(self):
        # ratiox = 210
        # ratioy = 297
        # SetRenderWindowSizeDynamic(ratiox, ratioy)
    
    # toggle Dock render window
    def _UNDOCKRW(self):
        vrOSGWidget.setRenderWindowDocked(0, False, 0)
    
    def _DOCKRW(self):
        vrOSGWidget.setRenderWindowDocked(0, True, 2)
    
    # toggle Fullscreen render window
    def _TOGFULLRW(self):
        vrOSGWidget.toggleFullscreen(0, False)
    
if not importError:
    manageWS = vrManageWS(VREDPluginWidget)
