import pyautogui as pag
from typing import Union
import collections
Box = collections.namedtuple('Box', 'left, top, width, height')

import time

class ATEMSoftwareController:
    """Holds properties for connecting to ATEM Software Control."""
    PIP_Source: int = None
    KEY_ON_AIR: bool = None
    KEY_ON_PREV: bool = None

    def __init__(self):
        self.sidebar_pip_settings: Box = None
        self.next_transition: Box = None
        
        if not self.check_PIP_Source(): print("ERROR: PIP Source detection failed during initialization.")
        if not self.check_ADV_KEY(): print("ERROR: ADV KEY detection failed during initialization.")

    # ================================================================================
    # CHECK METHODS
    # ================================================================================

    def check_PIP_Source(self) -> bool:
        # Detect and Switch to Upstream Key 1 on side bar
        try:
            self.sidebar_pip_settings = pag.locateOnScreen("./detect resources/Sidebar KEY 1 Settings.png", grayscale=True, confidence=0.5)
            print(f"Sidebar KEY 1 Settings found at: {self.sidebar_pip_settings}")
        except pag.ImageNotFoundException:
            self.sidebar_pip_settings = self.switch_UP_KEY1_Sidebar()
            if self.sidebar_pip_settings == False: 
                print("False to check PIP Source Settings")
                return False
        
        sources = []
        try: 
            pag.locateOnScreen("./detect resources/Sidebar PIP Source1.png", region=self.sidebar_pip_settings, grayscale=True, confidence=0.85)
            sources.append(True)
        except pag.ImageNotFoundException: sources.append(False)
        try: 
            pag.locateOnScreen("./detect resources/Sidebar PIP Source2.png", region=self.sidebar_pip_settings, grayscale=True, confidence=0.9)
            sources.append(True)
        except pag.ImageNotFoundException: sources.append(False)
        try: 
            pag.locateOnScreen("./detect resources/Sidebar PIP Source3.png", region=self.sidebar_pip_settings, grayscale=True, confidence=0.9)
            sources.append(True)
        except pag.ImageNotFoundException: sources.append(False)
        try: 
            pag.locateOnScreen("./detect resources/Sidebar PIP Source4.png", region=self.sidebar_pip_settings, grayscale=True, confidence=0.85)
            sources.append(True)
        except pag.ImageNotFoundException: sources.append(False)

        if sum(sources) != 1:
            print(f"Error detecting PIP Source, multiple or no sources detected, RAW: {sources}")
            return False
        else:
            self.PIP_Source = sources.index(True) + 1
            print(f"PIP Source detected: Source {self.PIP_Source}")
            return True

    def check_ADV_KEY(self) -> bool:
        try:
            self.next_transition = pag.locateOnScreen("./detect resources/Next Transition.png", grayscale=True, confidence=0.7)
            print(f"Next Transition found at: {self.next_transition}")
        except pag.ImageNotFoundException:
            print(f"Error locating Next Transition")
            return False
        
        try:
            if pag.locateOnScreen("./detect resources/ADV_KEY1_ONAIR_ON.png", region=self.next_transition, grayscale=False, confidence=0.8):
                self.KEY_ON_AIR = True
        except pag.ImageNotFoundException:
            self.KEY_ON_AIR = False
        try:
            if pag.locateOnScreen("./detect resources/ADV_KEY1_PREV_ON.png", region=self.next_transition, grayscale=False, confidence=0.8):
                self.KEY_ON_PREV = True
        except pag.ImageNotFoundException:
            self.KEY_ON_PREV = False
        
        print(f"ADV KEY Status - ON AIR: {self.KEY_ON_AIR}, PREV: {self.KEY_ON_PREV}")
        return True

    # ================================================================================
    # ACTION METHODS
    # ================================================================================

    def switch_UP_KEY1_Sidebar(self) -> Union[bool, Box]:
        """Switches to Upstream Key 1 on the sidebar."""
        try: 
            sidebar_palettes = pag.locateCenterOnScreen("./detect resources/Sidebar Palettes.png", grayscale=True, confidence=0.7)
            print(f"Sidebar Palettes found at: {sidebar_palettes}")
        
            pag.click(sidebar_palettes)
            print("Clicked on Sidebar Palettes")
        except pag.ImageNotFoundException:
            print(f"Error locating Sidebar Palettes")
            return False
        
        pag.move(20, 100)
        for i in range(3): pag.scroll(1000)

        try:
            sidebar_dve_btn = pag.locateCenterOnScreen("./detect resources/Sidebar DVE BTN.png", grayscale=True, confidence=0.7)
            print(f"Sidebar DVE Button found at: {sidebar_dve_btn}")
            
            pag.click(sidebar_dve_btn)
            print("Clicked on Sidebar DVE Button")
        except pag.ImageNotFoundException:
            print(f"Error locating Sidebar DVE Button, Switching to KEY 1 Button")

            try:
                sidebar_key1_btn = pag.locateCenterOnScreen("./detect resources/Sidebar KEY 1 BTN.png", grayscale=True, confidence=0.7)
                print(f"Sidebar KEY 1 Button found at: {sidebar_key1_btn}")

                pag.click(sidebar_key1_btn)
                print("Clicked on Sidebar KEY 1 Button")
            except pag.ImageNotFoundException:
                print(f"Error locating Sidebar KEY 1 Button")
                return False
            
            try:
                sidebar_dve_btn = pag.locateCenterOnScreen("./detect resources/Sidebar DVE BTN.png", grayscale=True, confidence=0.7)
                print(f"Sidebar DVE Button found at: {sidebar_dve_btn}")
                
                pag.click(sidebar_dve_btn)
                print("Clicked on Sidebar DVE Button")
            except pag.ImageNotFoundException:
                print(f"Error locating Sidebar DVE Button")
                return False
        
        try:
            sidebar_pip_settings = pag.locateOnScreen("./detect resources/Sidebar KEY 1 Settings.png", grayscale=True, confidence=0.5)
            print(f"Sidebar KEY 1 Settings found at: {sidebar_pip_settings}")
            print("Successfully switched to Upstream Key 1 [UP] on Sidebar")
            return sidebar_pip_settings
        except pag.ImageNotFoundException:
            print(f"Error locating Sidebar KEY 1 Settings")
            return False

    def switch_PIP_Source(self, source_number: int) -> bool:
        try:
            self.sidebar_pip_settings = pag.locateOnScreen("./detect resources/Sidebar KEY 1 Settings.png", grayscale=True, confidence=0.5)
            print(f"Sidebar KEY 1 Settings found at: {self.sidebar_pip_settings}")
        except pag.ImageNotFoundException:
            self.sidebar_pip_settings = self.switch_UP_KEY1_Sidebar()
            if self.sidebar_pip_settings == False: 
                print("False to check PIP Source Settings")
                return False
        
        try:
            if self.PIP_Source == 1:
                pag.click(pag.locateCenterOnScreen("./detect resources/Sidebar PIP Source1.png", region=self.sidebar_pip_settings, grayscale=True, confidence=0.85))
            elif self.PIP_Source == 2:
                pag.click(pag.locateCenterOnScreen("./detect resources/Sidebar PIP Source2.png", region=self.sidebar_pip_settings, grayscale=True, confidence=0.9))
            elif self.PIP_Source == 3:
                pag.click(pag.locateCenterOnScreen("./detect resources/Sidebar PIP Source3.png", region=self.sidebar_pip_settings, grayscale=True, confidence=0.9))
            elif self.PIP_Source == 4:
                pag.click(pag.locateCenterOnScreen("./detect resources/Sidebar PIP Source4.png", region=self.sidebar_pip_settings, grayscale=True, confidence=0.85))
        except pag.ImageNotFoundException:
            print(f"Error locating current PIP Source Button, Switching to Check PIP Source")
            try: self.check_PIP_Source()
            except: return False

        try:
            if source_number == 1:
                pag.click(pag.locateCenterOnScreen("./detect resources/Sidebar PIP Source1.png", region=self.sidebar_pip_settings, grayscale=True, confidence=0.85))
            elif source_number == 2:
                pag.click(pag.locateCenterOnScreen("./detect resources/Sidebar PIP Source2.png", region=self.sidebar_pip_settings, grayscale=True, confidence=0.9))
            elif source_number == 3:
                pag.click(pag.locateCenterOnScreen("./detect resources/Sidebar PIP Source3.png", region=self.sidebar_pip_settings, grayscale=True, confidence=0.9))
            elif source_number == 4:
                pag.click(pag.locateCenterOnScreen("./detect resources/Sidebar PIP Source4.png", region=self.sidebar_pip_settings, grayscale=True, confidence=0.85))
        except:
            return False

main = ATEMSoftwareController()
start_time = time.time()
main.check_ADV_KEY()
print(time.time() - start_time)