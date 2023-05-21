# Emoji Creator 

This is a Python project that uses machine learning to generate emojis based on input text. Given a text input, the model predicts and generates an emoji that represents the input.

## Prerequisites

- Python 3.6 or higher
- TensorFlow 2.x
- NumPy
- PIL (Python Imaging Library)
- scikit-learn

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/fti-sfuke/emoji_creator
   
2. Install the required dependencies using pip:

    ``` bash
   pip install -r requirements.txt
   
3. If the faced error: Could not find a version that satisfies the requirements, Then install the latest available versions for all packages. 

   ```
   pip3 install tensorflow numpy pillow scikit-learn
   ```

## Usage

 1. Prepare the emoji dataset:
   - In the `emoji_dataset` folder, you need to have image files representing the emojis you want to train the model on. The images should follow the following guidelines:

   1. Image Format: The images should be in a common image format such as PNG or JPEG.
   2. Image Size: It's recommended to resize the images to a consistent size for easier processing. In the provided code, the   
   3. images are resized to (64, 64) pixels. You can adjust the resizing dimensions based on your requirements.
   4. Image Content: Each image should represent a single emoji. The content of the image should be a clear representation of the       emoji it represents.

   For example, if you want to train the model to generate emojis for emotions like happy, sad, and angry, you can have image    
   files in the `emoji_dataset` folder named `happy.png`, `sad.png`, `angry.png`, and so on. Each image should contain a visual 
   representation of the corresponding emotion.
   
   - Add image files to the ```emoji_dataset``` folder Each image should represent a single emoji.

 ## Train the model:
 1. Run the following command to train the model on the emoji dataset:

    ```bash
    python3 emoji_creator.py train

  The model will be trained on the dataset, and the training progress will be displayed.

## Generate an emoji:

 1. To generate an emoji based on input text, run the following command:

    ``` bash
        python3 emoji_creator.py generate
   Enter your desired text when prompted.
   The model will process the input text and generate an emoji based on its learned associations.
   
   Example : 
``` Enter your text: "happy"
    1/1 [==============================] - 0s 48ms/step
    Generated Emoji: happy

    root@samadhan_hp:/home/samadhan/emoji_creator/emoji_dataset# ls
    angry.png  disgusted.png  fearful.png  happy.png  neutral.png  sad.png  surpriced.png
    root@samadhan_hp:/home/samadhan/emoji_creator/emoji_dataset#
 ``` 
    
## Customization

   If you want to modify the model architecture or experiment with different hyperparameters, you can edit the ```build_model()``` function in ```emoji_creator.py.```
    For customizing the image preprocessing logic, update the ```preprocess_input_text()``` function in ```emoji_creator.py``` to convert the input text into a processed image.

## Contributing

Contributions are welcome! If you have suggestions or improvements for the project, feel free to open issues or submit pull requests.
License

This project is licensed under the MIT License. See the LICENSE file for more details.

Feel free to modify the README file to include additional information specific to your project, such as installation instructions, usage examples, and any other relevant details.

## Copyrights
- Samadhan Fuke
- https://www.linkedin.com/in/samadhanfuke/
