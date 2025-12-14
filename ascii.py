# Portions of this code were generated using
# ChatGPT and GigaCode.


import sys
import os
import cv2
import numpy as np

"""
High‑detail image rendering in ANSI terminal.
Goal: increase real visual detail WITHOUT breaking colors.
Method:
- truecolor (24‑bit)
- upper half block '▀'
- 2 vertical pixels per character
- high‑quality resize (LANCZOS)
- NO destructive color quantization
"""


def convert_image_to_terminal(image_path, width=120):
    """
    Convert an image to a high-detail ANSI terminal output using upper half blocks.
    
    Args:
        image_path (str): Path to the input image file.
        width (int): Target width in characters (default is 120).
    """
    if not os.path.exists(image_path):
        print("File not found")
        return

    img = cv2.imread(image_path)
    if img is None:
        print("Failed to load image")
        return

    # Convert from BGR (OpenCV default) to RGB color space
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    src_h, src_w, _ = img.shape
    aspect = src_h / src_w

    # Calculate target dimensions
    # Use 2 vertical pixels per character row
    target_width = width
    target_height = int(target_width * aspect * 0.9)

    # Ensure height is even (required for pairing pixels with '▀' block)
    if target_height % 2 != 0:
        target_height += 1

    # Resize image using high-quality LANCZOS interpolation
    img = cv2.resize(
        img,
        (target_width, target_height),
        interpolation=cv2.INTER_LANCZOS4
    )

    # Clear the terminal screen
    print("\033[2J\033[H", end="")

    # Render the image using upper half block characters
    for y in range(0, target_height, 2):
        line = []
        for x in range(target_width):
            # Get RGB values for upper and lower pixels
            r1, g1, b1 = img[y, x]       # upper pixel
            r2, g2, b2 = img[y + 1, x]   # lower pixel

            # Create ANSI escape codes for foreground and background colors
            # and use '▀' to display two vertical pixels in one character
            line.append(
                f"\033[38;2;{r1};{g1};{b1}m"
                f"\033[48;2;{r2};{g2};{b2}m▀"
            )

        # Reset formatting at the end of the line
        line.append("\033[0m")
        print("".join(line))


def main():
    """
    Main function to parse command-line arguments and initiate image conversion.
    """
    if len(sys.argv) < 2:
        print("Usage: python convert_terminal_hires.py <image> [width]")
        return

    image_path = sys.argv[1]
    width = int(sys.argv[2]) if len(sys.argv) > 2 else 120

    convert_image_to_terminal(image_path, width)


if __name__ == "__main__":
    main()
