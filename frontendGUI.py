import sys
import os
from typing import Optional, TypedDict

from PyQt6 import QtCore, QtGui, QtWidgets

# ================================================================================
# Global Configuration Variables
# ================================================================================
# Window scaling parameters
DEFAULT_WINDOW_WIDTH = 1600         # Initial window width in pixels
MIN_WINDOW_WIDTH = 400              # Minimum allowed window width
MAX_WINDOW_WIDTH = 2800             # Maximum allowed window width

# Mouse interaction parameters (base values at original BKGD_IMG size w=2100)
BASE_EDGE_MARGIN = 20               # Margin for edge detection at base scale
BASE_CORNER_MARGIN = 50             # Margin for corner detection at base scale (x<50, y<50)

# High DPI settings for Windows Qt6
# Reference: https://zhuanlan.zhihu.com/p/9871635469
if sys.platform == 'win32':
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
    QtWidgets.QApplication.setHighDpiScaleFactorRoundingPolicy(
        QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )

# ================================================================================
# Type Definitions
# ================================================================================
class ResourceSpec(TypedDict):
    """Type definition for resource specifications with position and state variants"""
    name: str                       # Resource name identifier
    default: str                    # Default image path
    WHITE: Optional[str]
    YELLOW: Optional[str]
    GREEN: Optional[str]
    DISABLED: Optional[str]
    RED: Optional[str]
    x: int                          # X position (negative = from right edge)
    y: int                          # Y position (negative = from bottom edge)
    w: int                          # Width at base scale

class StaticResources:
    """Resource paths and specifications for all UI elements"""
    BKGD_IMG: ResourceSpec = {"default": "./resources/BKGD.png", "x": 0, "y": 0, "w": 2100}
    EXIT_BTN: ResourceSpec = {"default": "./resources/EXIT.png", "x": -117, "y": 78, "w": 39}
    MIN_BTN: ResourceSpec = {"default": "./resources/Minimize.png", "x": -172, "y": 78, "w": 39}
    
    PIP_SOURCE1_BTN: ResourceSpec = {"default": "./resources/PIP Source1 W.png",
        'WHITE': "./resources/PIP Source1 W.png",
        'GREEN': "./resources/PIP Source1 G.png",
        'RED': "./resources/PIP Source1 R.png",
        'x': 58, 'y': 788, 'w': 233}
    PIP_SOURCE2_BTN: ResourceSpec = {"default": "./resources/PIP Source2 W.png",
        'WHITE': "./resources/PIP Source2 W.png",
        'GREEN': "./resources/PIP Source2 G.png",
        'RED': "./resources/PIP Source2 R.png",
        'x': 311, 'y': 788, 'w': 233}
    PIP_SOURCE3_BTN: ResourceSpec = {"default": "./resources/PIP Source3 W.png",
        'WHITE': "./resources/PIP Source3 W.png",
        'GREEN': "./resources/PIP Source3 G.png",
        'RED': "./resources/PIP Source3 R.png", 
        'x': 564, 'y': 788, 'w': 233}
    PIP_SOURCE4_BTN: ResourceSpec = {"default": "./resources/PIP Source4 W.png",
        'WHITE': "./resources/PIP Source4 W.png",
        'GREEN': "./resources/PIP Source4 G.png",
        'RED': "./resources/PIP Source4 R.png",
        'x': 817, 'y': 788, 'w': 233}
    PIP_SOURCE_ON_BTN: ResourceSpec = {"default": "./resources/PIP Source ON W.png",
        'WHITE': "./resources/PIP Source ON W.png",
        'GREEN': "./resources/PIP Source ON G.png",
        'RED': "./resources/PIP Source ON R.png",
        'x': 1070, 'y': 788, 'w': 127}
    PIP_SOURCE_OFF_BTN: ResourceSpec = {"default": "./resources/PIP Source OFF W.png",
        'WHITE': "./resources/PIP Source OFF W.png",
        'GREEN': "./resources/PIP Source OFF G.png",
        'RED': "./resources/PIP Source OFF R.png",
        'x': 1070, 'y': 876, 'w': 127}
    
    PIP_LEFT_UP_BTN: ResourceSpec = {"default": "./resources/PIP Left Up W.png",
        'DISABLED': "./resources/PIP Left Up D.png",
        'WHITE': "./resources/PIP Left Up W.png",
        'GREEN': "./resources/PIP Left Up G.png",
        'RED': "./resources/PIP Left Up R.png",
        'x': 57, 'y': 530, 'w': 147}
    PIP_RIGHT_UP_BTN: ResourceSpec = {"default": "./resources/PIP Right Up W.png",
        'DISABLED': "./resources/PIP Right Up D.png",
        'WHITE': "./resources/PIP Right Up W.png",
        'GREEN': "./resources/PIP Right Up G.png",
        'RED': "./resources/PIP Right Up R.png",
        'x': 207, 'y': 530, 'w': 147}
    PIP_LEFT_DOWN_BTN: ResourceSpec = {"default": "./resources/PIP Left Down W.png",
        'DISABLED': "./resources/PIP Left Down D.png",
        'WHITE': "./resources/PIP Left Down W.png",
        'GREEN': "./resources/PIP Left Down G.png",
        'RED': "./resources/PIP Left Down R.png",
        'x': 57, 'y': 630, 'w': 147}
    PIP_RIGHT_DOWN_BTN: ResourceSpec = {"default": "./resources/PIP Right Down W.png",
        'DISABLED': "./resources/PIP Right Down D.png",
        'WHITE': "./resources/PIP Right Down W.png",
        'GREEN': "./resources/PIP Right Down G.png",
        'RED': "./resources/PIP Right Down R.png",
        'x': 207, 'y': 630, 'w': 147}
    
    PIP_MINIMIZE_BTN: ResourceSpec = {"default": "./resources/PIP Minimize W.png",
        'WHITE': "./resources/PIP Minimize W.png",
        'GREEN': "./resources/PIP Minimize G.png",
        'RED': "./resources/PIP Minimize R.png",
        'x': 407, 'y': 630, 'w': 147}
    PIP_FULL_BTN: ResourceSpec = {"default": "./resources/PIP Full W.png",
        'WHITE': "./resources/PIP Full W.png",
        'GREEN': "./resources/PIP Full G.png",
        'RED': "./resources/PIP Full R.png",
        'x': 407, 'y': 530, 'w': 147}
    
    PIP_MINI_LEFT_UP_BTN: ResourceSpec = {"default": "./resources/PIP Mini Left Up W.png",
        'YELLOW': "./resources/PIP Mini Left Up Y.png",
        'WHITE': "./resources/PIP Mini Left Up W.png",
        'GREEN': "./resources/PIP Mini Left Up G.png",
        'RED': "./resources/PIP Mini Left Up R.png",
        'x': 607, 'y': 430, 'w': 147}
    PIP_MINI_UP_BTN: ResourceSpec = {"default": "./resources/PIP Mini Up W.png",
        'YELLOW': "./resources/PIP Mini Up Y.png",
        'WHITE': "./resources/PIP Mini Up W.png",
        'GREEN': "./resources/PIP Mini Up G.png",
        'RED': "./resources/PIP Mini Up R.png",
        'x': 754, 'y': 430, 'w': 147}
    PIP_MINI_RIGHT_UP_BTN: ResourceSpec = {"default": "./resources/PIP Mini Right Up W.png",
        'YELLOW': "./resources/PIP Mini Right Up Y.png",
        'WHITE': "./resources/PIP Mini Right Up W.png",
        'GREEN': "./resources/PIP Mini Right Up G.png",
        'RED': "./resources/PIP Mini Right Up R.png",
        'x': 901, 'y': 430, 'w': 147}
    PIP_MINI_LEFT_MID_BTN: ResourceSpec = {"default": "./resources/PIP Mini Left Mid W.png",
        'YELLOW': "./resources/PIP Mini Left Mid Y.png",
        'WHITE': "./resources/PIP Mini Left Mid W.png",
        'GREEN': "./resources/PIP Mini Left Mid G.png",
        'RED': "./resources/PIP Mini Left Mid R.png",
        'x': 607, 'y': 530, 'w': 147}
    PIP_MINI_MIDDLE_BTN: ResourceSpec = {"default": "./resources/PIP Mini Middle W.png",
        'YELLOW': "./resources/PIP Mini Middle Y.png",
        'WHITE': "./resources/PIP Mini Middle W.png",
        'GREEN': "./resources/PIP Mini Middle G.png",
        'RED': "./resources/PIP Mini Middle R.png",
        'x': 754, 'y': 530, 'w': 147}
    PIP_MINI_RIGHT_MID_BTN: ResourceSpec = {"default": "./resources/PIP Mini Right Mid W.png",
        'YELLOW': "./resources/PIP Mini Right Mid Y.png",
        'WHITE': "./resources/PIP Mini Right Mid W.png",
        'GREEN': "./resources/PIP Mini Right Mid G.png",
        'RED': "./resources/PIP Mini Right Mid R.png",
        'x': 901, 'y': 530, 'w': 147}
    PIP_MINI_LEFT_DOWN_BTN: ResourceSpec = {"default": "./resources/PIP Mini Left Down W.png",
        'YELLOW': "./resources/PIP Mini Left Down Y.png",
        'WHITE': "./resources/PIP Mini Left Down W.png",
        'GREEN': "./resources/PIP Mini Left Down G.png",
        'RED': "./resources/PIP Mini Left Down R.png",
        'x': 607, 'y': 630, 'w': 147}
    PIP_MINI_DOWN_BTN: ResourceSpec = {"default": "./resources/PIP Mini Down W.png",
        'YELLOW': "./resources/PIP Mini Down Y.png",
        'WHITE': "./resources/PIP Mini Down W.png",
        'GREEN': "./resources/PIP Mini Down G.png",
        'RED': "./resources/PIP Mini Down R.png",
        'x': 754, 'y': 630, 'w': 147}
    PIP_MINI_RIGHT_DOWN_BTN: ResourceSpec = {"default": "./resources/PIP Mini Right Down W.png",
        'YELLOW': "./resources/PIP Mini Right Down Y.png",
        'WHITE': "./resources/PIP Mini Right Down W.png",
        'GREEN': "./resources/PIP Mini Right Down G.png",
        'RED': "./resources/PIP Mini Right Down R.png",
        'x': 901, 'y': 630, 'w': 147}
    
    ADV_KEY_BTN: ResourceSpec = {"default": "./resources/ADV KEY W.png",
        'WHITE': "./resources/ADV KEY W.png",
        'YELLOW': "./resources/ADV KEY Y.png",
        'x': 1237, 'y': 143, 'w': 233}
    ADV_BKGD_BTN: ResourceSpec = {"default": "./resources/ADV BKGD W.png",
        'WHITE': "./resources/ADV BKGD W.png",
        'YELLOW': "./resources/ADV BKGD Y.png",
        'x': 1494, 'y': 143, 'w': 233}
    ADV_ON_AIR_BTN: ResourceSpec = {"default": "./resources/ADV ON AIR W.png",
        'WHITE': "./resources/ADV ON AIR W.png",
        'RED': "./resources/ADV ON AIR R.png",
        'x': 1750, 'y': 143, 'w': 233}
    
    BKGD_TRANS_CUT_BTN: ResourceSpec = {"default": "./resources/Trans CUT W.png",
        'WHITE': "./resources/Trans CUT W.png",
        'RED': "./resources/Trans CUT R.png",
        'x': 1237, 'y': 355, 'w': 233}
    BKGD_TRANS_AUTO_BTN: ResourceSpec = {"default": "./resources/Trans AUTO W.png",
        'WHITE': "./resources/Trans AUTO W.png",
        'RED': "./resources/Trans AUTO R.png",
        'x': 1494, 'y': 355, 'w': 233}
    
    PIP_TRANS_CUT_BTN: ResourceSpec = {"default": "./resources/Trans CUT W.png",
        'WHITE': "./resources/Trans CUT W.png",
        'RED': "./resources/Trans CUT R.png",
        'x': 1237, 'y': 571, 'w': 233}
    PIP_TRANS_AUTO_BTN: ResourceSpec = {"default": "./resources/Trans AUTO W.png",
        'WHITE': "./resources/Trans AUTO W.png",
        'RED': "./resources/Trans AUTO R.png",
        'x': 1494, 'y': 571, 'w': 233}
    
    DUR_0_5_BTN: ResourceSpec = {"default": "./resources/DUR 0.5 W.png",
        'WHITE': "./resources/DUR 0.5 W.png",
        'RED': "./resources/DUR 0.5 R.png",
        'x': 1750, 'y': 571, 'w': 112}
    DUR_1_0_BTN: ResourceSpec = {"default": "./resources/DUR 1.0 W.png",
        'WHITE': "./resources/DUR 1.0 W.png",
        'RED': "./resources/DUR 1.0 R.png",
        'x': 1870, 'y': 571, 'w': 112}
    DUR_1_5_BTN: ResourceSpec = {"default": "./resources/DUR 1.5 W.png",
        'WHITE': "./resources/DUR 1.5 W.png",
        'RED': "./resources/DUR 1.5 R.png",
        'x': 1750, 'y': 651, 'w': 112}
    DUR_2_0_BTN: ResourceSpec = {"default": "./resources/DUR 2.0 W.png",
        'WHITE': "./resources/DUR 2.0 W.png",
        'RED': "./resources/DUR 2.0 R.png",
        'x': 1870, 'y': 651, 'w': 112}
    
    VIEW_TRANS_CUT_BTN: ResourceSpec = {"default": "./resources/Trans CUT W.png",
        'WHITE': "./resources/Trans CUT W.png",
        'RED': "./resources/Trans CUT R.png",
        'x': 1237, 'y': 788, 'w': 233}
    VIEW_TRANS_AUTO_BTN: ResourceSpec = {"default": "./resources/Trans AUTO W.png",
        'WHITE': "./resources/Trans AUTO W.png",
        'RED': "./resources/Trans AUTO R.png",
        'x': 1494, 'y': 788, 'w': 233}
    VIEW_TRANS_FTB_BTN: ResourceSpec = {"default": "./resources/Trans FTB W.png",
        'WHITE': "./resources/Trans FTB W.png",
        'RED': "./resources/Trans FTB R.png",
        'x': 1750, 'y': 788, 'w': 233}

# ================================================================================
# PART I: UI Rendering
# ================================================================================
class ImageWidget(QtWidgets.QWidget):
    """
    Custom widget for rendering image elements with high quality scaling.
    Uses QPainter for direct pixmap rendering to maintain sharp edges.
    """
    
    def __init__(self, resource_spec: ResourceSpec, base_width: int, parent=None):
        super().__init__(parent)
        self.resource_spec = resource_spec
        self.base_width = base_width
        self.original_pixmap = None
        self.scaled_pixmap = None
        self.current_scale = 1.0
        
        # Load the image from resource specification
        self.load_image(resource_spec["default"])
        
        # Enable transparency for rounded corners and alpha channel
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_OpaquePaintEvent, False)
        # Initially don't pass through mouse events (will be configured per widget)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
    
    def load_image(self, image_path: str):
        """
        Load image directly as QPixmap from file path.
        QPixmap automatically handles transparency and format conversion.
        """
        self.original_pixmap = QtGui.QPixmap(image_path)
        if self.original_pixmap.isNull():
            print(f"Warning: Failed to load image: {image_path}")
    
    def update_scale(self, scale_factor: float):
        """
        Update widget scale using high-quality smooth transformation.
        Recalculates scaled pixmap and adjusts widget size accordingly.
        """
        if self.original_pixmap and not self.original_pixmap.isNull():
            self.current_scale = scale_factor
            # Calculate scaled width based on resource spec and scale factor
            scaled_w = int(self.resource_spec["w"] * scale_factor)
            
            # Use SmoothTransformation for high quality anti-aliased scaling
            self.scaled_pixmap = self.original_pixmap.scaled(
                scaled_w, scaled_w,
                QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                QtCore.Qt.TransformationMode.SmoothTransformation
            )
            
            # Resize widget to match scaled pixmap dimensions
            self.setFixedSize(self.scaled_pixmap.size())
            self.update()  # Trigger repaint
    
    def paintEvent(self, event: QtGui.QPaintEvent):
        """
        Custom paint event using QPainter for maximum quality.
        Enables antialiasing and smooth pixmap transform for sharp rendering.
        """
        if self.scaled_pixmap and not self.scaled_pixmap.isNull():
            painter = QtGui.QPainter(self)
            # Enable antialiasing for smooth edges
            painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing, True)
            # Enable smooth pixmap transform for better quality
            painter.setRenderHint(QtGui.QPainter.RenderHint.SmoothPixmapTransform, True)
            
            # Draw the pre-scaled pixmap directly without additional transforms
            painter.drawPixmap(0, 0, self.scaled_pixmap)
            painter.end()
    
    def sizeHint(self):
        """Return the recommended size for this widget"""
        if self.scaled_pixmap and not self.scaled_pixmap.isNull():
            return self.scaled_pixmap.size()
        return QtCore.QSize(100, 100)
    
    def get_position(self, scale_factor: float, window_width: int, window_height: int) -> tuple[int, int]:
        """Compute widget position; negative coords measured from right/bottom edges."""
        rx, ry = self.resource_spec["x"], self.resource_spec["y"]
        x = window_width + int(rx * scale_factor) if rx < 0 else int(rx * scale_factor)
        y = window_height + int(ry * scale_factor) if ry < 0 else int(ry * scale_factor)
        return x, y

class MainWindow(QtWidgets.QMainWindow):
    """
    Main application window with frameless, transparent background and proportional scaling.
    Stays on top of other windows for easy access during live production.
    """
    
    def __init__(self):
        super().__init__()
        
        # Configure window properties
        self.setWindowTitle("ATEM PIP Controller")
        # Frameless window that stays on top
        self.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint |
            QtCore.Qt.WindowType.WindowStaysOnTopHint
        )
        # Enable transparency for rounded corners
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        
        # Initialize scaling variables
        self.base_width = StaticResources.BKGD_IMG["w"]
        self.scale_factor = 1.0
        self.image_widgets = {}
        
        # Calculate fixed window size based on MAX_WINDOW_WIDTH
        self.max_scale = MAX_WINDOW_WIDTH / self.base_width
        # Load background to get aspect ratio
        temp_pixmap = QtGui.QPixmap(StaticResources.BKGD_IMG["default"])
        self.aspect_ratio = temp_pixmap.height() / temp_pixmap.width()
        self.fixed_window_width = MAX_WINDOW_WIDTH
        self.fixed_window_height = int(MAX_WINDOW_WIDTH * self.aspect_ratio)
        
        # Setup central widget with transparency
        self.central_widget = QtWidgets.QWidget()
        self.central_widget.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        # Pass mouse events through central widget to main window
        self.central_widget.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        self.setCentralWidget(self.central_widget)
        
        # Set fixed window size
        self.setFixedSize(self.fixed_window_width, self.fixed_window_height)
        
        # Create all UI elements
        self.init_ui()
        
        # Set initial content size
        self.resize_content(DEFAULT_WINDOW_WIDTH)
    
    def init_ui(self):
        """Initialize all UI elements with proper mouse event handling"""
        # Create background image
        self.background = ImageWidget(StaticResources.BKGD_IMG, self.base_width, self.central_widget)
        self.image_widgets['background'] = self.background
        
        # Create exit button
        self.exit_btn = ImageWidget(StaticResources.EXIT_BTN, self.base_width, self.central_widget)
        self.image_widgets['exit_btn'] = self.exit_btn
        # Button needs to receive mouse events for click detection
        self.exit_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)

        # Create minimize button
        self.min_btn = ImageWidget(StaticResources.MIN_BTN, self.base_width, self.central_widget)
        self.image_widgets['min_btn'] = self.min_btn
        # Button needs to receive mouse events for click detection
        self.min_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        
        # Create PIP source buttons (functional placeholders for now)
        self.pip_source1_btn = ImageWidget(StaticResources.PIP_SOURCE1_BTN, self.base_width, self.central_widget)
        self.image_widgets['pip_source1_btn'] = self.pip_source1_btn
        self.pip_source1_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        
        self.pip_source2_btn = ImageWidget(StaticResources.PIP_SOURCE2_BTN, self.base_width, self.central_widget)
        self.image_widgets['pip_source2_btn'] = self.pip_source2_btn
        self.pip_source2_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.pip_source3_btn = ImageWidget(StaticResources.PIP_SOURCE3_BTN, self.base_width, self.central_widget)
        self.image_widgets['pip_source3_btn'] = self.pip_source3_btn
        self.pip_source3_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.pip_source4_btn = ImageWidget(StaticResources.PIP_SOURCE4_BTN, self.base_width, self.central_widget)
        self.image_widgets['pip_source4_btn'] = self.pip_source4_btn
        self.pip_source4_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)

        self.pip_source_on_btn = ImageWidget(StaticResources.PIP_SOURCE_ON_BTN, self.base_width, self.central_widget)
        self.image_widgets['pip_source_on_btn'] = self.pip_source_on_btn
        self.pip_source_on_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.pip_source_off_btn = ImageWidget(StaticResources.PIP_SOURCE_OFF_BTN, self.base_width, self.central_widget)
        self.image_widgets['pip_source_off_btn'] = self.pip_source_off_btn
        self.pip_source_off_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)

        # Create PIP Position Switcher Buttons
        self.pip_left_up_btn = ImageWidget(StaticResources.PIP_LEFT_UP_BTN, self.base_width, self.central_widget)
        self.image_widgets['pip_left_up_btn'] = self.pip_left_up_btn
        self.pip_left_up_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.pip_right_up_btn = ImageWidget(StaticResources.PIP_RIGHT_UP_BTN, self.base_width, self.central_widget)
        self.image_widgets['pip_right_up_btn'] = self.pip_right_up_btn
        self.pip_right_up_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.pip_left_down_btn = ImageWidget(StaticResources.PIP_LEFT_DOWN_BTN, self.base_width, self.central_widget)
        self.image_widgets['pip_left_down_btn'] = self.pip_left_down_btn
        self.pip_left_down_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.pip_right_down_btn = ImageWidget(StaticResources.PIP_RIGHT_DOWN_BTN, self.base_width, self.central_widget)
        self.image_widgets['pip_right_down_btn'] = self.pip_right_down_btn
        self.pip_right_down_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)

        self.pip_minimize_btn = ImageWidget(StaticResources.PIP_MINIMIZE_BTN, self.base_width, self.central_widget)
        self.image_widgets['pip_minimize_btn'] = self.pip_minimize_btn
        self.pip_minimize_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.pip_full_btn = ImageWidget(StaticResources.PIP_FULL_BTN, self.base_width, self.central_widget)
        self.image_widgets['pip_full_btn'] = self.pip_full_btn
        self.pip_full_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)

        self.pip_mini_left_up_btn = ImageWidget(StaticResources.PIP_MINI_LEFT_UP_BTN, self.base_width, self.central_widget)
        self.image_widgets['pip_mini_left_up_btn'] = self.pip_mini_left_up_btn
        self.pip_mini_left_up_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.pip_mini_up_btn = ImageWidget(StaticResources.PIP_MINI_UP_BTN, self.base_width, self.central_widget)
        self.image_widgets['pip_mini_up_btn'] = self.pip_mini_up_btn
        self.pip_mini_up_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.pip_mini_right_up_btn = ImageWidget(StaticResources.PIP_MINI_RIGHT_UP_BTN, self.base_width, self.central_widget)
        self.image_widgets['pip_mini_right_up_btn'] = self.pip_mini_right_up_btn
        self.pip_mini_right_up_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.pip_mini_left_mid_btn = ImageWidget(StaticResources.PIP_MINI_LEFT_MID_BTN, self.base_width, self.central_widget)
        self.image_widgets['pip_mini_left_mid_btn'] = self.pip_mini_left_mid_btn
        self.pip_mini_left_mid_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.pip_mini_middle_btn = ImageWidget(StaticResources.PIP_MINI_MIDDLE_BTN, self.base_width, self.central_widget)
        self.image_widgets['pip_mini_middle_btn'] = self.pip_mini_middle_btn
        self.pip_mini_middle_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.pip_mini_right_mid_btn = ImageWidget(StaticResources.PIP_MINI_RIGHT_MID_BTN, self.base_width, self.central_widget)
        self.image_widgets['pip_mini_right_mid_btn'] = self.pip_mini_right_mid_btn
        self.pip_mini_right_mid_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.pip_mini_left_down_btn = ImageWidget(StaticResources.PIP_MINI_LEFT_DOWN_BTN, self.base_width, self.central_widget)
        self.image_widgets['pip_mini_left_down_btn'] = self.pip_mini_left_down_btn
        self.pip_mini_left_down_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.pip_mini_down_btn = ImageWidget(StaticResources.PIP_MINI_DOWN_BTN, self.base_width, self.central_widget)
        self.image_widgets['pip_mini_down_btn'] = self.pip_mini_down_btn
        self.pip_mini_down_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.pip_mini_right_down_btn = ImageWidget(StaticResources.PIP_MINI_RIGHT_DOWN_BTN, self.base_width, self.central_widget)
        self.image_widgets['pip_mini_right_down_btn'] = self.pip_mini_right_down_btn
        self.pip_mini_right_down_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)

        self.adv_key_btn = ImageWidget(StaticResources.ADV_KEY_BTN, self.base_width, self.central_widget)
        self.image_widgets['adv_key_btn'] = self.adv_key_btn
        self.adv_key_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.adv_bkgd_btn = ImageWidget(StaticResources.ADV_BKGD_BTN, self.base_width, self.central_widget)
        self.image_widgets['adv_bkgd_btn'] = self.adv_bkgd_btn
        self.adv_bkgd_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.adv_on_air_btn = ImageWidget(StaticResources.ADV_ON_AIR_BTN, self.base_width, self.central_widget)
        self.image_widgets['adv_on_air_btn'] = self.adv_on_air_btn
        self.adv_on_air_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)

        self.bkgd_trans_cut_btn = ImageWidget(StaticResources.BKGD_TRANS_CUT_BTN, self.base_width, self.central_widget)
        self.image_widgets['bkgd_trans_cut_btn'] = self.bkgd_trans_cut_btn
        self.bkgd_trans_cut_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.bkgd_trans_auto_btn = ImageWidget(StaticResources.BKGD_TRANS_AUTO_BTN, self.base_width, self.central_widget)
        self.image_widgets['bkgd_trans_auto_btn'] = self.bkgd_trans_auto_btn
        self.bkgd_trans_auto_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        
        self.pip_trans_cut_btn = ImageWidget(StaticResources.PIP_TRANS_CUT_BTN, self.base_width, self.central_widget)
        self.image_widgets['pip_trans_cut_btn'] = self.pip_trans_cut_btn
        self.pip_trans_cut_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.pip_trans_auto_btn = ImageWidget(StaticResources.PIP_TRANS_AUTO_BTN, self.base_width, self.central_widget)
        self.image_widgets['pip_trans_auto_btn'] = self.pip_trans_auto_btn
        self.pip_trans_auto_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        
        self.dur_0_5_btn = ImageWidget(StaticResources.DUR_0_5_BTN, self.base_width, self.central_widget)
        self.image_widgets['dur_0_5_btn'] = self.dur_0_5_btn
        self.dur_0_5_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.dur_1_0_btn = ImageWidget(StaticResources.DUR_1_0_BTN, self.base_width, self.central_widget)
        self.image_widgets['dur_1_0_btn'] = self.dur_1_0_btn
        self.dur_1_0_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.dur_1_5_btn = ImageWidget(StaticResources.DUR_1_5_BTN, self.base_width, self.central_widget)
        self.image_widgets['dur_1_5_btn'] = self.dur_1_5_btn
        self.dur_1_5_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.dur_2_0_btn = ImageWidget(StaticResources.DUR_2_0_BTN, self.base_width, self.central_widget)
        self.image_widgets['dur_2_0_btn'] = self.dur_2_0_btn
        self.dur_2_0_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)

        self.view_trans_cut_btn = ImageWidget(StaticResources.VIEW_TRANS_CUT_BTN, self.base_width, self.central_widget)
        self.image_widgets['view_trans_cut_btn'] = self.view_trans_cut_btn
        self.view_trans_cut_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.view_trans_auto_btn = ImageWidget(StaticResources.VIEW_TRANS_AUTO_BTN, self.base_width, self.central_widget)
        self.image_widgets['view_trans_auto_btn'] = self.view_trans_auto_btn
        self.view_trans_auto_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.view_trans_ftb_btn = ImageWidget(StaticResources.VIEW_TRANS_FTB_BTN, self.base_width, self.central_widget)
        self.image_widgets['view_trans_ftb_btn'] = self.view_trans_ftb_btn
        self.view_trans_ftb_btn.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)

        # Background should pass through mouse events
        self.background.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        
        # Enable mouse tracking for hover effects on all buttons
        self.exit_btn.setMouseTracking(True)
        self.min_btn.setMouseTracking(True)
        self.pip_source1_btn.setMouseTracking(True)
        self.pip_source2_btn.setMouseTracking(True)
        self.pip_source3_btn.setMouseTracking(True)
        self.pip_source4_btn.setMouseTracking(True)
        self.pip_source_on_btn.setMouseTracking(True)
        self.pip_source_off_btn.setMouseTracking(True)
        self.pip_left_up_btn.setMouseTracking(True)
        self.pip_right_up_btn.setMouseTracking(True)
        self.pip_left_down_btn.setMouseTracking(True)
        self.pip_right_down_btn.setMouseTracking(True)
        self.pip_minimize_btn.setMouseTracking(True)
        self.pip_full_btn.setMouseTracking(True)
        self.pip_mini_left_up_btn.setMouseTracking(True)
        self.pip_mini_up_btn.setMouseTracking(True)
        self.pip_mini_right_up_btn.setMouseTracking(True)
        self.pip_mini_left_mid_btn.setMouseTracking(True)
        self.pip_mini_middle_btn.setMouseTracking(True)
        self.pip_mini_right_mid_btn.setMouseTracking(True)
        self.pip_mini_left_down_btn.setMouseTracking(True)
        self.pip_mini_down_btn.setMouseTracking(True)
        self.pip_mini_right_down_btn.setMouseTracking(True)
        self.view_trans_cut_btn.setMouseTracking(True)
        self.view_trans_auto_btn.setMouseTracking(True)
        self.view_trans_ftb_btn.setMouseTracking(True)
        self.adv_bkgd_btn.setMouseTracking(True)
        self.adv_key_btn.setMouseTracking(True)
        self.adv_on_air_btn.setMouseTracking(True)
        self.bkgd_trans_cut_btn.setMouseTracking(True)
        self.bkgd_trans_auto_btn.setMouseTracking(True)
        self.pip_trans_cut_btn.setMouseTracking(True)
        self.pip_trans_auto_btn.setMouseTracking(True)
        self.dur_0_5_btn.setMouseTracking(True)
        self.dur_1_0_btn.setMouseTracking(True)
        self.dur_1_5_btn.setMouseTracking(True)
        self.dur_2_0_btn.setMouseTracking(True)
        self.view_trans_cut_btn.setMouseTracking(True)
        self.view_trans_auto_btn.setMouseTracking(True)
        self.view_trans_ftb_btn.setMouseTracking(True)

        # List of all interactive buttons for easy checking
        self.interactive_buttons = [
            self.exit_btn, 
            self.min_btn,
            self.pip_source1_btn,
            self.pip_source2_btn,
            self.pip_source3_btn,
            self.pip_source4_btn,
            self.pip_source_on_btn,
            self.pip_source_off_btn,
            self.pip_left_up_btn,
            self.pip_right_up_btn,
            self.pip_left_down_btn,
            self.pip_right_down_btn,
            self.pip_minimize_btn,
            self.pip_full_btn,
            self.pip_mini_left_up_btn,
            self.pip_mini_up_btn,
            self.pip_mini_right_up_btn,
            self.pip_mini_left_mid_btn,
            self.pip_mini_middle_btn,
            self.pip_mini_right_mid_btn,
            self.pip_mini_left_down_btn,
            self.pip_mini_down_btn,
            self.pip_mini_right_down_btn,
            self.adv_key_btn,
            self.adv_bkgd_btn,
            self.adv_on_air_btn,
            self.bkgd_trans_cut_btn,
            self.bkgd_trans_auto_btn,
            self.pip_trans_cut_btn,
            self.pip_trans_auto_btn,
            self.dur_0_5_btn,
            self.dur_1_0_btn,
            self.dur_1_5_btn,
            self.dur_2_0_btn,
            self.view_trans_cut_btn,
            self.view_trans_auto_btn,
            self.view_trans_ftb_btn
        ]

    def resize_content(self, new_width: int):
        """
        Resize content (BKGD_IMG and elements) based on new width.
        Window size remains fixed. Only changes internal element scaling and positioning.
        """
        # Clamp width to allowed range
        new_width = max(MIN_WINDOW_WIDTH, min(MAX_WINDOW_WIDTH, new_width))
        # Calculate scale factor
        self.scale_factor = new_width / self.base_width
        
        # Update all image widgets with new scale
        for widget in self.image_widgets.values():
            widget.update_scale(self.scale_factor)
        
        # Reposition all elements within the fixed window
        self.update_positions()
    
    def get_bkgd_rect(self) -> QtCore.QRect:
        """Get the current rectangle of the background image within the window"""
        if self.background.scaled_pixmap and not self.background.scaled_pixmap.isNull():
            bkgd_width = self.background.scaled_pixmap.width()
            bkgd_height = self.background.scaled_pixmap.height()
            # Center the background in the fixed window
            x = (self.fixed_window_width - bkgd_width) // 2
            y = (self.fixed_window_height - bkgd_height) // 2
            return QtCore.QRect(x, y, bkgd_width, bkgd_height)
        return QtCore.QRect(0, 0, self.fixed_window_width, self.fixed_window_height)
    
    def update_positions(self):
        """Update positions of all UI elements based on current scale, centered in window"""
        bkgd_rect = self.get_bkgd_rect()
        bkgd_x = bkgd_rect.x()
        bkgd_y = bkgd_rect.y()
        bkgd_width = bkgd_rect.width()
        bkgd_height = bkgd_rect.height()
        
        # Position background centered in window
        self.background.move(bkgd_x, bkgd_y)
        
        # Calculate and apply new positions for all other widgets relative to background
        for name, widget in self.image_widgets.items():
            if name == 'background':
                continue
            x, y = widget.get_position(self.scale_factor, bkgd_width, bkgd_height)
            # Offset by background position
            widget.move(x + bkgd_x, y + bkgd_y)

# ================================================================================
# PART II: Mouse Interaction Handling
# ================================================================================
class MouseInteractionMixin:
    """
    Mixin class for handling mouse-based window dragging and resizing.
    Supports 8-direction resizing with scale-aware detection thresholds.
    """
    
    def setup_mouse_interaction(self):
        """Initialize mouse interaction state variables"""
        self.dragging = False
        self.resizing = False
        self.resize_edge = None
        self.drag_position = QtCore.QPoint()
        self.resize_start_width = None
        self.button_press_position = None
        self.button_press_widget = None
        self.setMouseTracking(True)
        if hasattr(self, 'central_widget'):
            self.central_widget.setMouseTracking(True)
    
    def is_mouse_over_button(self, pos: QtCore.QPoint) -> bool:
        """Check if mouse position is over any interactive button"""
        for button in self.interactive_buttons:
            if self.is_point_in_widget(pos, button):
                return True
        return False
    
    def mousePressEvent(self, event: QtGui.QMouseEvent):
        """Handle mouse button press events"""
        if event.button() != QtCore.Qt.MouseButton.LeftButton:
            return
        
        bkgd_rect = self.get_bkgd_rect()

        # Check if pressing on any button
        for button in self.interactive_buttons:
            if self.is_point_in_widget(event.pos(), button):
                self.button_press_position = event.pos()
                self.button_press_widget = button
                return
        
        # Check for resize edge or start dragging
        rel_pos = event.pos() - bkgd_rect.topLeft()
        edge = self.get_resize_edge(rel_pos, bkgd_rect.width(), bkgd_rect.height())
        if edge:
            self.resizing = True
            self.resize_edge = edge
            self.drag_position = event.globalPosition().toPoint()
            self.resize_start_width = int(self.scale_factor * self.base_width)
        else:
            self.dragging = True
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
    
    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        """Handle mouse movement for resizing and dragging"""
        bkgd_rect = self.get_bkgd_rect()

        if self.resizing and self.resize_edge:
            delta = event.globalPosition().toPoint() - self.drag_position
            if self.resize_edge in ['right', 'bottomright', 'topright']:
                new_width = self.resize_start_width + delta.x()*2
            elif self.resize_edge in ['left', 'bottomleft', 'topleft']:
                new_width = self.resize_start_width - delta.x()*2
            else:
                dy = delta.y()*2 if self.resize_edge == 'bottom' else -delta.y()*2
                new_width = int((self.resize_start_width * self.aspect_ratio + dy) / self.aspect_ratio)
            
            new_width = max(MIN_WINDOW_WIDTH, min(MAX_WINDOW_WIDTH, new_width))
            self.resize_content(new_width)
        elif self.dragging:
            if self.is_mouse_over_button(event.pos()):
                self.dragging = False
            else:
                self.setCursor(QtCore.Qt.CursorShape.SizeAllCursor)
                self.move(event.globalPosition().toPoint() - self.drag_position)
        else:
            rel_pos = event.pos() - bkgd_rect.topLeft()
            self.update_cursor(rel_pos, bkgd_rect.width(), bkgd_rect.height())
    
    def mouseReleaseEvent(self, event: QtGui.QMouseEvent):
        """Handle mouse button release and button click triggers"""
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            if self.button_press_widget and self.is_point_in_widget(event.pos(), self.button_press_widget):
                if self.button_press_widget == self.exit_btn:
                    QtWidgets.QApplication.quit()
                elif self.button_press_widget == self.min_btn:
                    self.showMinimized()
                else:
                    print(f"Button clicked: {self.button_press_widget.resource_spec['default']}")
            if self.dragging:
                self.setCursor(QtCore.Qt.CursorShape.ArrowCursor)

            self.button_press_widget = None
            self.button_press_position = None
            self.dragging = False
            self.resizing = False
            self.resize_edge = None
            self.resize_start_width = None
    
    def get_resize_edge(self, pos: QtCore.QPoint, bkgd_width: int, bkgd_height: int) -> Optional[str]:
        """Detect resize edge/corner with scale-aware margins"""
        x, y = pos.x(), pos.y()
        margin = int(BASE_EDGE_MARGIN * self.scale_factor)
        corner = int(BASE_CORNER_MARGIN * self.scale_factor)
        
        # Check corners first
        if x <= corner and y <= corner: return 'topleft'
        if x >= bkgd_width - corner and y <= corner: return 'topright'
        if x <= corner and y >= bkgd_height - corner: return 'bottomleft'
        if x >= bkgd_width - corner and y >= bkgd_height - corner: return 'bottomright'
        
        # Check edges
        if x <= margin: return 'left'
        if x >= bkgd_width - margin: return 'right'
        if y <= margin: return 'top'
        if y >= bkgd_height - margin: return 'bottom'
        return None
    
    def update_cursor(self, rel_pos: QtCore.QPoint, bkgd_width: int, bkgd_height: int):
        """Update cursor based on mouse position"""
        if self.is_mouse_over_button(rel_pos + self.get_bkgd_rect().topLeft()):
            self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
            return
        
        edge = self.get_resize_edge(rel_pos, bkgd_width, bkgd_height)
        cursor_map = {
            'left': QtCore.Qt.CursorShape.SizeHorCursor,
            'right': QtCore.Qt.CursorShape.SizeHorCursor,
            'top': QtCore.Qt.CursorShape.SizeVerCursor,
            'bottom': QtCore.Qt.CursorShape.SizeVerCursor,
            'topleft': QtCore.Qt.CursorShape.SizeFDiagCursor,
            'bottomright': QtCore.Qt.CursorShape.SizeFDiagCursor,
            'topright': QtCore.Qt.CursorShape.SizeBDiagCursor,
            'bottomleft': QtCore.Qt.CursorShape.SizeBDiagCursor,
        }
        self.setCursor(cursor_map.get(edge, QtCore.Qt.CursorShape.ArrowCursor))
    
    def is_point_in_widget(self, pos: QtCore.QPoint, widget: QtWidgets.QWidget) -> bool:
        """Check if a point is within a widget's bounds"""
        widget_rect = QtCore.QRect(widget.pos(), widget.size())
        return widget_rect.contains(pos)

# ================================================================================
# PART III: Keyboard Shortcuts
# ================================================================================

# PLAN TO DEVELOP IN FUTURE UPDATES

# ================================================================================
# PART IV: Main Application Class
# ================================================================================
class ATEMPIPController(MainWindow, MouseInteractionMixin):
    """
    Main application controller integrating all functionality.
    Combines window rendering, mouse interaction, and keyboard shortcuts.
    """
    
    def __init__(self):
        super().__init__()
        self.setup_mouse_interaction()

# ================================================================================
# Application Entry Point
# ================================================================================
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # Use Fusion style for consistent cross-platform appearance
    app.setStyle('Fusion')
    
    # Create and show main window
    window = ATEMPIPController()
    window.show()
    
    sys.exit(app.exec())