import tensorflow as tf
import numpy as np
from PIL import Image
import os
from sklearn.preprocessing import LabelEncoder

def load_dataset():
    emoji_images = []
    emoji_labels = []

    for emoji_file in os.listdir('emoji_dataset'):
        emoji_labels.append(emoji_file.split('.')[0])
        emoji_image = Image.open(os.path.join('emoji_dataset', emoji_file))

        # Convert RGBA images to RGB
        if emoji_image.mode == 'RGBA':
            emoji_image = emoji_image.convert('RGB')

        emoji_image = emoji_image.resize((64, 64))
        emoji_image = np.array(emoji_image) / 255.0
        emoji_images.append(emoji_image)

    emoji_images = np.array(emoji_images)
    emoji_labels = np.array(emoji_labels)

    return emoji_images, emoji_labels

def build_model(num_classes):
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(num_classes, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

# Load the dataset
emoji_images, emoji_labels = load_dataset()

# Convert string labels to integer labels
label_encoder = LabelEncoder()
emoji_labels_encoded = label_encoder.fit_transform(emoji_labels)

# Call the build_model() function and pass the number of classes as an argument
model = build_model(len(label_encoder.classes_))

# Train the model
model.fit(emoji_images, emoji_labels_encoded, epochs=10, batch_size=32)

# Function to generate emoji
def generate_emoji(input_text):
    input_image = preprocess_input_text(input_text)
    input_image = np.expand_dims(input_image, axis=0)
    predicted_label = model.predict(input_image)
    emoji_index = np.argmax(predicted_label)
    generated_emoji_encoded = emoji_index
    generated_emoji = label_encoder.inverse_transform([generated_emoji_encoded])[0]
    return generated_emoji

def preprocess_input_text(input_text):
    # Placeholder for image preprocessing logic
    # Convert text to image using libraries like PIL or OpenCV
    # Preprocess the image as per your requirements (resize, normalize, etc.)
    image = Image.new('RGB', (64, 64))
    # Add your image processing logic here to create the image based on the input text
    processed_image = np.array(image) / 255.0
    return processed_image


input_text = input("Enter your text: ")
generated_emoji = generate_emoji(input_text)
print("Generated Emoji:", generated_emoji)

