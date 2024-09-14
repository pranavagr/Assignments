# Image to Pixel Conversion

## Description
This Python script converts an image to a representation of its constituent pixels. The script supports both direct pixel extraction for grayscale and color images. It reads an image file, converts it into a numpy array of pixel values, and provides a visualization of the pixel matrix with the pixel values overlaid on the image.

## Approach
- **Direct Pixel Extraction**: This approach involves reading the image and extracting its pixel values (RGB values for color images). The output is a numpy array containing the pixel information. The script also visualizes the pixel matrix and overlays the pixel values on the image.

## Libraries Used
- **OpenCV**: Used for reading and processing the image files.
- **NumPy**: Used for handling the image data as numpy arrays.
- **Matplotlib**: Used for visualizing the pixel matrix and overlaying the pixel values on the image.

## Output Format
- The script outputs a numpy array containing the pixel values of the image in RGB format.
- The pixel matrix is visualized as an image with the pixel values overlaid on it for better understanding.

## Files
- `direct_pixel_extraction.py`: The main script that performs the image to pixel conversion and visualization.
- `README.md`: This file, explaining the approach, libraries used, and output format.

## How to Run
1. Ensure you have the required libraries installed:
   ```sh
   pip install opencv-python-headless numpy matplotlib
   
2. Place the image you want to convert in the same directory as the script or provide the correct path to the image file.

3. Run the script:
   python direct_pixel_extraction.py