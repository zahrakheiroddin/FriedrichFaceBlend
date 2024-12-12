# FriedrichFaceBlend

Here's a more detailed and comprehensive `README.md` for your project:

```markdown
# Face Blending into Friedrich's Painting

This Python program enables the user to capture their face using a webcam and blend it into a classical painting of Friedrich II. The program applies artistic effects to the captured face and seamlessly integrates it into the painting. This is achieved using OpenCV for face detection and image manipulation, as well as PIL (Pillow) for applying artistic filters.

## Features

- **Real-time face detection** using OpenCV's Haar Cascade Classifier.
- **Artistic effects** applied to the captured face, including smoothing, edge enhancement, and color desaturation to create a painted look.
- **Seamless blending** of the detected face with a designated region of Friedrich's painting.
- **Circular alpha mask** applied to ensure smooth blending between the face and the painting.
- **Save the output** as a new image file with the face blended into the painting.
- **Webcam interface** allowing the user to interact and capture their face at any moment.

## Requirements

This program requires Python 3.x and several external libraries. You can install all the required libraries using `pip`:

- **Python 3.x** (preferably Python 3.6 or later)
- **OpenCV** for real-time face detection and image manipulation
- **NumPy** for array manipulation
- **Pillow (PIL)** for applying artistic filters to the image

To install these dependencies, use the following commands:

```bash
pip install opencv-python-headless numpy pillow
```

### Optional (for image display):
```bash
pip install opencv-python
```

## Installation

1. Clone the repository or download the code:
    ```bash
    git clone https://github.com/your-username/face-blending-painting.git
    cd face-blending-painting
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Place the painting image (`friedrich_ii.jpg`) in the directory where the script is located.

## Usage

### Running the Script

1. **Run the script**:
    In your terminal or command prompt, navigate to the folder where the script is located and run:
    ```bash
    python blend_face_into_painting.py
    ```

2. **Webcam feed**:
    The program will launch a webcam feed window. You can press the **'s'** key to capture your face and blend it into the painting, or **'q'** to quit the program.

3. **Capture the face**:
    When you press the **'s'** key:
    - The program will automatically detect faces in the webcam feed.
    - If at least one face is detected, the program will apply artistic effects to the first detected face.
    - The processed face will then be blended into the designated region of the painting (Friedrich II’s face region).
    - The final blended image will be saved as `painting_with_blended_face.jpg`.

4. **Save the output**:
    Once the blending is complete, the program will save the output as `painting_with_blended_face.jpg` in the same directory.

### Keys:
- **'s'**: Capture the face from the webcam and blend it into the painting.
- **'q'**: Quit the program.

### Example of Use:

1. Start the program by running the script.
2. You will see the webcam feed. Press **'s'** when you're ready to capture your face.
3. The program will detect the face, apply artistic effects, and blend it into Friedrich's painting.
4. The final result will be saved, and the blended painting will be displayed for 3 seconds.

## How It Works

### 1. **Face Detection**:
   The program uses OpenCV's **Haar Cascade Classifier** to detect faces in the webcam feed. This allows it to locate and extract the user's face for blending.

### 2. **Face Transformation**:
   Once a face is detected, it is resized to fit into a predefined region on Friedrich's painting. The following artistic filters are applied using Pillow (PIL):
   - **Smoothing**: Using `ImageFilter.SMOOTH_MORE` to make the face appear soft and painterly.
   - **Detail enhancement**: Using `ImageFilter.DETAIL` to sharpen the edges and add texture.
   - **Color desaturation**: Using `ImageEnhance.Color` to reduce the color saturation for a more muted, painting-like appearance.
   - **Blur**: A slight **Gaussian Blur** is applied using `ImageFilter.GaussianBlur` for a softer, painted effect.

### 3. **Seamless Blending**:
   The processed face is then blended into the painting using OpenCV’s `cv2.seamlessClone`, which is a technique that creates a smooth transition between the face and the painting. This function helps avoid harsh lines or edges that might otherwise make the blending look unnatural.

### 4. **Alpha Mask**:
   A circular **alpha mask** is applied to fade the edges of the detected face, ensuring that the blending with the painting is smooth and realistic.

### 5. **Saving the Result**:
   After blending the face, the final image is saved as `painting_with_blended_face.jpg`. It is also briefly displayed for 3 seconds so you can see the result before closing the program.

## Example Output

After blending, the result will look like this:

![Blended Painting](painting_with_blended_face.jpg)

## Contributing

Feel free to fork the repository and contribute by making improvements or submitting pull requests. You can help by:
- Adding new artistic effects or filters.
- Improving the face detection accuracy.
- Supporting other input methods for capturing faces (such as from an image or video).
- Enhancing the blending functionality.

### Guidelines for Contributing:
1. Fork the repository.
2. Make your changes or improvements.
3. Open a pull request with a clear description of your changes.

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- **Friedrich II's painting**: Public domain image of the famous painting, used for artistic blending.
- **OpenCV**: Used for face detection and image manipulation.
- **Pillow (PIL)**: Used for applying artistic filters and effects to the face.
- **Haar Cascade Classifier**: Used for real-time face detection from the webcam feed.

