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
ZOOM_STEP = 1.1                     # Zoom in/out multiplier (10% per step)

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
    default: str
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
    
    PIP_SOURCE1_BTN: ResourceSpec = {'default': "./resources/PIP Source1 W.png",
        'WHITE': "./resources/PIP Source1 W.png",
        'GREEN': "./resources/PIP Source1 G.png",
        'RED': "./resources/PIP Source1 R.png",
        'x': 58, 'y': 788, 'w': 233}
    PIP_SOURCE2_BTN: ResourceSpec = {'default': "./resources/PIP Source2 W.png",
        'WHITE': "./resources/PIP Source2 W.png",
        'GREEN': "./resources/PIP Source2 G.png",
        'RED': "./resources/PIP Source2 R.png",
        'x': 311, 'y': 788, 'w': 233}
    PIP_SOURCE3_BTN: ResourceSpec = {'default': "./resources/PIP Source3 W.png",
        'WHITE': "./resources/PIP Source3 W.png",
        'GREEN': "./resources/PIP Source3 G.png",
        'RED': "./resources/PIP Source3 R.png", 
        'x': 564, 'y': 788, 'w': 233}
    PIP_SOURCE4_BTN: ResourceSpec = {'default': "./resources/PIP Source4 W.png",
        'WHITE': "./resources/PIP Source4 W.png",
        'GREEN': "./resources/PIP Source4 G.png",
        'RED': "./resources/PIP Source4 R.png",
        'x': 817, 'y': 788, 'w': 233}
    PIP_SOURCE_ON_BTN: ResourceSpec = {'default': "./resources/PIP Source ON W.png",
        'WHITE': "./resources/PIP Source ON W.png",
        'GREEN': "./resources/PIP Source ON G.png",
        'RED': "./resources/PIP Source ON R.png",
        'x': 1070, 'y': 788, 'w': 127}
    PIP_SOURCE_OFF_BTN: ResourceSpec = {'default': "./resources/PIP Source OFF W.png",
        'WHITE': "./resources/PIP Source OFF W.png",
        'GREEN': "./resources/PIP Source OFF G.png",
        'RED': "./resources/PIP Source OFF R.png",
        'x': 1070, 'y': 876, 'w': 127}
    
    PIP_LEFT_UP_BTN: ResourceSpec = {'default': "./resources/PIP Left Up W.png",
        'DISABLED': "./resources/PIP Left Up D.png",
        'WHITE': "./resources/PIP Left Up W.png",
        'GREEN': "./resources/PIP Left Up G.png",
        'RED': "./resources/PIP Left Up R.png",
        'x': 57, 'y': 532, 'w': 147}
    PIP_RIGHT_UP_BTN: ResourceSpec = {'default': "./resources/PIP Right Up W.png",
        'DISABLED': "./resources/PIP Right Up D.png",
        'WHITE': "./resources/PIP Right Up W.png",
        'GREEN': "./resources/PIP Right Up G.png",
        'RED': "./resources/PIP Right Up R.png",
        'x': 207, 'y': 532, 'w': 147}
    PIP_LEFT_DOWN_BTN: ResourceSpec = {'default': "./resources/PIP Left Down W.png",
        'DISABLED': "./resources/PIP Left Down D.png",
        'WHITE': "./resources/PIP Left Down W.png",
        'GREEN': "./resources/PIP Left Down G.png",
        'RED': "./resources/PIP Left Down R.png",
        'x': 57, 'y': 630, 'w': 147}
    PIP_RIGHT_DOWN_BTN: ResourceSpec = {'default': "./resources/PIP Right Down W.png",
        'DISABLED': "./resources/PIP Right Down D.png",
        'WHITE': "./resources/PIP Right Down W.png",
        'GREEN': "./resources/PIP Right Down G.png",
        'RED': "./resources/PIP Right Down R.png",
        'x': 207, 'y': 630, 'w': 147}

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
        Load image from file path and ensure RGBA format for transparency.
        Converts to premultiplied ARGB32 if alpha channel is missing.
        """
        self.original_pixmap = QtGui.QPixmap(image_path)
        if self.original_pixmap.isNull():
            print(f"Warning: Failed to load image: {image_path}")
        else:
            # Ensure alpha channel exists for transparency
            if not self.original_pixmap.hasAlphaChannel():
                self.original_pixmap = self.original_pixmap.convertToFormat(
                    QtGui.QImage.Format.Format_ARGB32_Premultiplied
                )
    
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
        """
        Calculate widget position with support for negative coordinates.
        Negative x/y values are measured from right/bottom edges respectively.
        """
        x = self.resource_spec["x"]
        y = self.resource_spec["y"]
        
        # Handle negative coordinates (measured from opposite edge)
        if x < 0:
            x = window_width + int(x * scale_factor)
        else:
            x = int(x * scale_factor)
        
        if y < 0:
            y = window_height + int(y * scale_factor)
        else:
            y = int(y * scale_factor)
        
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
            self.pip_right_down_btn
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
    
    def resizeEvent(self, event):
        """Handle window resize events"""
        super().resizeEvent(event)
        self.update_positions()


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
        self.resize_edge = None  # Current resize edge: 'left', 'right', 'top', 'bottom', 'topleft', etc.
        self.drag_position = QtCore.QPoint()
        self.resize_start_width = None  # Content width at resize start
        self.button_press_position = None  # Track where button press started
        self.button_press_widget = None  # Track which button was pressed
        
        # Calculate scale-aware margins (scales with content size)
        # Base margins are defined at BKGD_IMG w=2100, corner at x<50, y<50
        self.resize_margin = int(BASE_EDGE_MARGIN * self.scale_factor)
        self.corner_margin = int(BASE_CORNER_MARGIN * self.scale_factor)
        
        self.setMouseTracking(True)
        # Enable mouse tracking on central widget as well
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
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            # Check if mouse is within BKGD_IMG area
            bkgd_rect = self.get_bkgd_rect()
            if not bkgd_rect.contains(event.pos()):
                # Outside background - ignore event (let it pass through)
                event.ignore()
                return
            
            # Convert to position relative to background
            rel_pos = event.pos() - bkgd_rect.topLeft()
            
            # Check if pressing on any interactive button
            for button in self.interactive_buttons:
                if self.is_point_in_widget(event.pos(), button):
                    # Track button press but don't trigger yet (trigger on release)
                    self.button_press_position = event.pos()
                    self.button_press_widget = button
                    return
            
            # Not on button - check if mouse is on resize edge/corner (relative to BKGD)
            # Only allow resize if not over any button
            if not self.is_mouse_over_button(event.pos()):
                edge = self.get_resize_edge(rel_pos, bkgd_rect.width(), bkgd_rect.height())
                if edge:
                    self.resizing = True
                    self.resize_edge = edge
                    self.drag_position = event.globalPosition().toPoint()
                    self.resize_start_width = int(self.scale_factor * self.base_width)
                else:
                    # Start dragging mode if not on edge or button
                    self.dragging = True
                    self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
    
    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        """Handle mouse movement for resizing and dragging"""
        bkgd_rect = self.get_bkgd_rect()
        
        # Check if mouse is within BKGD_IMG area for event handling
        if not bkgd_rect.contains(event.pos()) and not self.resizing and not self.dragging:
            # Outside background - ignore event (let it pass through)
            event.ignore()
            self.setCursor(QtCore.Qt.CursorShape.ArrowCursor)
            return
        
        if self.resizing and self.resize_edge:
            delta = event.globalPosition().toPoint() - self.drag_position
            
            # Calculate new width based on resize edge
            if self.resize_edge in ['right', 'bottomright', 'topright']:
                new_width = self.resize_start_width + delta.x()
            elif self.resize_edge in ['left', 'bottomleft', 'topleft']:
                new_width = self.resize_start_width - delta.x()
            else:  # top or bottom - maintain aspect ratio
                new_height = int(self.resize_start_width * self.aspect_ratio) + (delta.y() if self.resize_edge == 'bottom' else -delta.y())
                new_width = int(new_height / self.aspect_ratio)
            
            # Clamp width to allowed range
            new_width = max(MIN_WINDOW_WIDTH, min(MAX_WINDOW_WIDTH, new_width))
            
            # Check for meaningful change
            current_width = int(self.scale_factor * self.base_width)
            if abs(new_width - current_width) < 2:
                return
            
            # Apply content resize (window position and size stay fixed)
            self.resize_content(new_width)
            
        elif self.dragging:
            # Cancel dragging if mouse moves over a button
            if self.is_mouse_over_button(event.pos()):
                self.dragging = False
            else:
                # Move window while dragging
                self.move(event.globalPosition().toPoint() - self.drag_position)
        else:
            # Update cursor based on mouse position relative to background
            rel_pos = event.pos() - bkgd_rect.topLeft()
            self.update_cursor(rel_pos, bkgd_rect.width(), bkgd_rect.height())
    
    def mouseReleaseEvent(self, event: QtGui.QMouseEvent):
        """Handle mouse button release and button click triggers"""
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            # Check if this was a button press and release on the same button
            if self.button_press_widget and self.button_press_position:
                # Only trigger if mouse is still over the same button on release
                if self.is_point_in_widget(event.pos(), self.button_press_widget):
                    # Trigger button action based on which button was pressed
                    if self.button_press_widget == self.exit_btn:
                        QtWidgets.QApplication.quit()
                    elif self.button_press_widget == self.min_btn:
                        self.showMinimized()
                    # Add more button handlers here as needed
                    # elif self.button_press_widget == self.pip_source1_btn:
                    #     self.handle_pip_source1()
                
                # Reset button press tracking
                self.button_press_widget = None
                self.button_press_position = None
            
            # Reset drag/resize state
            self.dragging = False
            self.resizing = False
            self.resize_edge = None
            self.resize_start_width = None
    
    def get_resize_edge(self, pos: QtCore.QPoint, bkgd_width: int, bkgd_height: int) -> Optional[str]:
        """
        Detect which edge or corner the mouse is on relative to BKGD_IMG.
        Uses scale-aware margins for consistent detection at any scale.
        """
        x = pos.x()
        y = pos.y()
        
        # Update margins based on current scale
        self.resize_margin = int(BASE_EDGE_MARGIN * self.scale_factor)
        self.corner_margin = int(BASE_CORNER_MARGIN * self.scale_factor)
        
        # Check if near each edge
        on_left = x <= self.resize_margin
        on_right = x >= bkgd_width - self.resize_margin
        on_top = y <= self.resize_margin
        on_bottom = y >= bkgd_height - self.resize_margin
        
        # Check corners first (higher priority than edges)
        if x <= self.corner_margin and y <= self.corner_margin:
            return 'topleft'
        elif x >= bkgd_width - self.corner_margin and y <= self.corner_margin:
            return 'topright'
        elif x <= self.corner_margin and y >= bkgd_height - self.corner_margin:
            return 'bottomleft'
        elif x >= bkgd_width - self.corner_margin and y >= bkgd_height - self.corner_margin:
            return 'bottomright'
        
        # Check edges
        elif on_left:
            return 'left'
        elif on_right:
            return 'right'
        elif on_top:
            return 'top'
        elif on_bottom:
            return 'bottom'
        
        return None
    
    def update_cursor(self, rel_pos: QtCore.QPoint, bkgd_width: int, bkgd_height: int):
        """
        Update cursor icon based on mouse position relative to BKGD_IMG.
        Shows appropriate resize cursor or pointer cursor for buttons.
        """
        # Convert relative position back to absolute for button checking
        bkgd_rect = self.get_bkgd_rect()
        abs_pos = rel_pos + bkgd_rect.topLeft()
        
        # Check if hovering over any interactive button
        if self.is_mouse_over_button(abs_pos):
            self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
            return
        
        # Otherwise show resize cursor based on edge
        edge = self.get_resize_edge(rel_pos, bkgd_width, bkgd_height)
        
        if edge in ['left', 'right']:
            self.setCursor(QtCore.Qt.CursorShape.SizeHorCursor)
        elif edge in ['top', 'bottom']:
            self.setCursor(QtCore.Qt.CursorShape.SizeVerCursor)
        elif edge in ['topleft', 'bottomright']:
            self.setCursor(QtCore.Qt.CursorShape.SizeFDiagCursor)
        elif edge in ['topright', 'bottomleft']:
            self.setCursor(QtCore.Qt.CursorShape.SizeBDiagCursor)
        else:
            self.setCursor(QtCore.Qt.CursorShape.ArrowCursor)
    
    def is_point_in_widget(self, pos: QtCore.QPoint, widget: QtWidgets.QWidget) -> bool:
        """Check if a point is within a widget's bounds"""
        widget_rect = QtCore.QRect(widget.pos(), widget.size())
        return widget_rect.contains(pos)


# ================================================================================
# PART III: Keyboard Shortcuts
# ================================================================================
class KeyBindingMixin:
    """Mixin class for handling keyboard shortcuts"""
    
    def setup_key_bindings(self):
        """Setup all keyboard shortcuts for window control"""
        # ESC key to quit application
        self.esc_shortcut = QtGui.QShortcut(QtGui.QKeySequence("Esc"), self)
        self.esc_shortcut.activated.connect(QtWidgets.QApplication.quit)
        
        # Ctrl+Q to quit application
        self.quit_shortcut = QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Q"), self)
        self.quit_shortcut.activated.connect(QtWidgets.QApplication.quit)
        
        # Ctrl+M to minimize window
        self.minimize_shortcut = QtGui.QShortcut(QtGui.QKeySequence("Ctrl+M"), self)
        self.minimize_shortcut.activated.connect(self.showMinimized)
        
        # Ctrl+Plus to zoom in
        self.zoom_in_shortcut = QtGui.QShortcut(QtGui.QKeySequence("Ctrl++"), self)
        self.zoom_in_shortcut.activated.connect(self.zoom_in)
        
        # Ctrl+Minus to zoom out
        self.zoom_out_shortcut = QtGui.QShortcut(QtGui.QKeySequence("Ctrl+-"), self)
        self.zoom_out_shortcut.activated.connect(self.zoom_out)
        
        # Ctrl+0 to reset to default size
        self.reset_size_shortcut = QtGui.QShortcut(QtGui.QKeySequence("Ctrl+0"), self)
        self.reset_size_shortcut.activated.connect(self.reset_size)
    
    def zoom_in(self):
        """Increase content size by ZOOM_STEP multiplier"""
        current_width = int(self.scale_factor * self.base_width)
        new_width = int(current_width * ZOOM_STEP)
        self.resize_content(new_width)
    
    def zoom_out(self):
        """Decrease content size by ZOOM_STEP divisor"""
        current_width = int(self.scale_factor * self.base_width)
        new_width = int(current_width / ZOOM_STEP)
        new_width = max(MIN_WINDOW_WIDTH, new_width)
        self.resize_content(new_width)
    
    def reset_size(self):
        """Reset content to default size"""
        self.resize_content(DEFAULT_WINDOW_WIDTH)


# ================================================================================
# PART IV: Main Application Class
# ================================================================================
class ATEMPIPController(MainWindow, MouseInteractionMixin, KeyBindingMixin):
    """
    Main application controller integrating all functionality.
    Combines window rendering, mouse interaction, and keyboard shortcuts.
    """
    
    def __init__(self):
        super().__init__()
        self.setup_mouse_interaction()
        self.setup_key_bindings()

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