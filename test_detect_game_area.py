import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Wnck', '3.0')
from gi.repository import Gtk, Gdk, GdkX11, Wnck
from Xlib import display, Xatom
from PIL import Image
import pyautogui
import time

disp = display.Display()
root = disp.screen().root
NET_FRAME_EXTENTS = disp.intern_atom('_NET_FRAME_EXTENTS')

def get_game_window_list():
    game_window_list = {}
    try:
        screen = Wnck.Screen.get_default()
        screen.force_update()
        window_list = screen.get_windows()
        for window in window_list:
            window_name = window.get_name()
            instance_name = window.get_class_instance_name()
            if instance_name == 'dofus.exe' or instance_name == 'scrcpy':
                game_window_list[window_name] = window.get_xid()
    except Exception as ex:
        print(ex)
    return game_window_list

def get_game_window(window_xid):
    gdk_display = GdkX11.X11Display.get_default()
    game_window = GdkX11.X11Window.foreign_new_for_display(gdk_display, window_xid)
    return game_window

def get_game_window_decoration_height(window_xid):
    window = disp.create_resource_object('window', window_xid)
    window_decoration_property = window.get_full_property(NET_FRAME_EXTENTS, Xatom.CARDINAL).value
    window_decoration_height = int(window_decoration_property[2]) + int(window_decoration_property[3])
    return window_decoration_height

def detect_game_display_area():
    game_windows = get_game_window_list()
    if not game_windows:
        print("No game windows found.")
        return None
    
    for window_name, window_xid in game_windows.items():
        game_window = get_game_window(window_xid)
        decoration_height = get_game_window_decoration_height(window_xid)
        
        size = game_window.get_geometry()
        width, height = size.width, size.height
        
        # Adjust for window decoration
        game_area = (0, decoration_height, width, height - decoration_height)
        
        # Take a screenshot and analyze the edges for black spots
        pb = Gdk.pixbuf_get_from_window(game_window, 0, 0, width, height)
        pb.savev("game_screenshot.png", "png", (), ())
        
        image = Image.open("game_screenshot.png")
        pixels = image.load()
        
        # Analyze edges (top, bottom, left, right) for black spots
        edge_threshold = 10  # Number of pixels to analyze from the edge
        for x in range(width):
            for y in range(edge_threshold):
                if pixels[x, y] != (0, 0, 0) or pixels[x, height - y - 1] != (0, 0, 0):
                    game_area = (game_area[0], y, game_area[2], height - y * 2)
                    break
        
        for y in range(height):
            for x in range(edge_threshold):
                if pixels[x, y] != (0, 0, 0) or pixels[width - x - 1, y] != (0, 0, 0):
                    game_area = (x, game_area[1], width - x * 2, game_area[3])
                    break
        
        return game_area

game_display_area = detect_game_display_area()
if game_display_area:
    print("Game display area detected:", game_display_area)
else:
    print("Failed to detect game display area.")
