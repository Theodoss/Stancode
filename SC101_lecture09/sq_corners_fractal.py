"""
File: sq_corners_fractal.py
Name:
-----------------------------------
This program draws a fractal with GRect on GWindow.
Students will find it useful to understand the order
of each recursive calls.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GRect
from campy.gui.events.timer import pause

# Constants
SIZE = 50      # It controls the width and height of the GRect on canvas
LEVEL = 6       # It controls the recursive depth of fractal

# This is the canvas for GRect
window = GWindow(width=1000, height=600)


def main():
	center_x = window.width/2
	center_y = window.height/2
	draw_rect(LEVEL, 300, center_x, center_y)


def draw_rect(level, width, center_x, center_y):
	if level == 0:
		pass
	else:

		# Upper left
		draw_rect(level - 1, width / 2, center_x - width / 2, center_y - width / 2)
		# lower right
		draw_rect(level - 1, width / 2, center_x + width / 2, center_y + width / 2)
		rect = GRect(width, width, x= center_x-width/2, y= center_y-width/2)
		rect.filled = True
		rect.fill_color = 'snow'
		pause(50)
		window.add(rect)
		# lower left
		draw_rect(level - 1, width / 2, center_x - width / 2, center_y + width / 2)
		# Upper right
		draw_rect(level - 1, width / 2, center_x + width / 2, center_y - width / 2)


if __name__ == '__main__':
	main()
