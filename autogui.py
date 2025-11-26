import pyautogui as pag
import time

class ATEMSoftwareController:
    """Holds properties for connecting to ATEM Software Control."""
    DUR: int = None
    PIP_Source: int = None
    KEY_1: bool = None
    ON_AIR: bool = None
    

    # ================================================================================
    # CHECK METHODS
    # ================================================================================

    def check_PIP_Source(self):
        # Detect and Switch to Upstream Key 1 on side bar
        pass
    
    # ================================================================================
    # ACTION METHODS
    # ================================================================================

    def switch_UP_KEY1_Sidebar(self):
        """Switches to Upstream Key 1 on the sidebar."""
        try: 
            sidebar_palettes = pag.locateCenterOnScreen("./detect resources/Sidebar Palettes.png", grayscale=True, confidence=0.7)
            print(f"Sidebar Palettes found at: {sidebar_palettes}")
        
            pag.click(sidebar_palettes)
            print("Clicked on Sidebar Palettes")
        except pag.ImageNotFoundException:
            print(f"Error locating Sidebar Palettes")
            return False
        
        time.sleep(0.2)

        try:
            sidebar_dve_btn = pag.locateCenterOnScreen("./detect resources/Sidebar DVE BTN.png", grayscale=True, confidence=0.7)
            print(f"Sidebar DVE Button found at: {sidebar_dve_btn}")
            
            pag.click(sidebar_dve_btn)
            print("Clicked on Sidebar DVE Button")
        except pag.ImageNotFoundException:
            print(f"Error locating Sidebar DVE Button, Switching to KEY 1 Button")
            pag.move(20, 100)
            pag.scroll()

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

main = ATEMSoftwareController()