# UCT-USC-Internship-Work-Crop-Weed-Detection

Overview
This project involves the development of a real-time crop and weed detection system using the YOLOv5x model. The system is designed to assist farmers by accurately identifying crops and weeds, enhancing agricultural productivity. The project includes dataset preparation, model training, and deployment in a mobile application.

Features
Real-Time Detection: Utilizes YOLOv5x for high-speed, accurate detection of crops and weeds.
Mobile App Integration: Includes an Android app for easy access and use in the field.
Model Conversion: The trained model is converted to TensorFlow Lite and ONNX formats for efficient deployment.

Project Structure
crop-weed-detection.ipynb: Contains the datasets used for training and testing.
aCrop_Weed_Detection_App/android_app/android_app/: Source code for the Android application.
datasets/internship.v2i.yolov8/: Sample images showing the detection results and app interface.

Setup and Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/crop-weed-detection.git
cd crop-weed-detection

Download Additional Files:
Due to size constraints, some files are hosted on Google Drive:

Model Weights (YOLOv5x) : https://drive.google.com/drive/folders/1fb0BziWaCyPvI0_b2PqjPYsfNrkaJzpa?usp=sharing<br>
android app model : https://drive.google.com/drive/folders/1WyMmVxhhNJ2GzHhOb5rv0eUNgMFLZ3MS?usp=sharing
Download these files and place them in the appropriate directories as indicated.

Usage
Training the Model:
Follow the instructions in the model/README.md to train the model on your dataset.

Running the Android App:
The Android app can be installed on your device. It utilizes the TensorFlow Lite model for real-time detection.

Results
Detection Accuracy: Achieved over 90% accuracy in detecting various crops and weeds.

Images
![confusion_matrix](https://github.com/user-attachments/assets/4aacbe8a-c2cf-4301-bcfd-323074d61203)
[ Confusion Matrix ]
![agri_0_151_jpeg rf cab5779323e091caf55f52d7bd75be73](https://github.com/user-attachments/assets/469269ed-41c9-48aa-8262-94577f6b94a8)
[ Weed Detection ]
![agri_0_164_jpeg rf 9582ee2bad95cad403da1a75444ca6cc](https://github.com/user-attachments/assets/469a3353-6f45-4d98-8130-84360f41ec8d)
[ Crop Detection ]
![Result Set](https://github.com/user-attachments/assets/d1938337-3cba-4a4a-8ea9-bc06236b62e3)
[ Result Set ]
![YOLO Evaluation Metrics](https://github.com/user-attachments/assets/bf6ae5f6-07af-41fc-ad22-d8459841d621)
[ YOLO Evaluation Metrics ]
![Precision, Recall, and F1 Scores](https://github.com/user-attachments/assets/f72fef5c-00fc-4504-8da2-3779003445b2)
[ Precision, Recall, and F1 Scores ]
![Testing](https://github.com/user-attachments/assets/76294e70-4137-4f9a-8ab5-830bfeb3b0d2)
[ Testing ]
![Screenshot_2024-07-25-18-55-50-082_com surendramaran yolov8tflite](https://github.com/user-attachments/assets/164b6260-e4dc-4fe7-abdf-8b0a82fa5e44)
[ Android Application ]
![Screenshot_2024-07-25-18-58-46-982_com surendramaran yolov8tflite](https://github.com/user-attachments/assets/03eecbea-6ea2-43a8-b7dd-0f0b1ee480cf)
[ Android Application Test ]


License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any inquiries or contributions, please contact patelhiten1789@gmail.com.

