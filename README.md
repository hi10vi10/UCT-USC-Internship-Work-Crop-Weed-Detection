# UCT-USC-Internship-Work-Crop-Weed-Detection

Overview<br>
This project involves the development of a real-time crop and weed detection system using the YOLOv5x model. The system is designed to assist farmers by accurately identifying crops and weeds, enhancing agricultural productivity. The project includes dataset preparation, model training, and deployment in a mobile application.<br>

Features<br>
Real-Time Detection: Utilizes YOLOv5x for high-speed, accurate detection of crops and weeds.<br>
Mobile App Integration: Includes an Android app for easy access and use in the field.<br>
Model Conversion: The trained model is converted to TensorFlow Lite and ONNX formats for efficient deployment.<br>

Project Structure<br>
crop-weed-detection.ipynb: Contains the datasets used for training and testing.<br>
Crop_Weed_Detection_App/android_app/android_app/: Source code for the Android application.<br>
datasets/internship.v2i.yolov8/: Sample images showing the detection results and app interface.<br>

Setup and Installation<br>
Clone the Repository:<br>

bash<br>
Copy code<br>
git clone https://github.com/yourusername/crop-weed-detection.git<br>
cd crop-weed-detection<br>

Download Additional Files:<br>
Due to size constraints, some files are hosted on Google Drive:<br>

Model Weights (YOLOv5x) : https://drive.google.com/drive/folders/1fb0BziWaCyPvI0_b2PqjPYsfNrkaJzpa?usp=sharing<br>
android app model : https://drive.google.com/drive/folders/1WyMmVxhhNJ2GzHhOb5rv0eUNgMFLZ3MS?usp=sharing<br>
Download these files and place them in the appropriate directories as indicated.<br>

Usage<br>
Training the Model:<br>
Follow the instructions in the model/README.md to train the model on your dataset.<br>

Running the Android App:<br>
The Android app can be installed on your device. It utilizes the TensorFlow Lite model for real-time detection.<br>

Results<br>
Detection Accuracy: Achieved over 90% accuracy in detecting various crops and weeds.<br>

## Images
![confusion_matrix](https://github.com/user-attachments/assets/4aacbe8a-c2cf-4301-bcfd-323074d61203)<br>
<p align="center">[ Confusion Matrix ]</p><br>

![agri_0_151_jpeg rf cab5779323e091caf55f52d7bd75be73](https://github.com/user-attachments/assets/469269ed-41c9-48aa-8262-94577f6b94a8)<br>
<p align="center">[ Weed Detection ]</p><br>

![agri_0_164_jpeg rf 9582ee2bad95cad403da1a75444ca6cc](https://github.com/user-attachments/assets/469a3353-6f45-4d98-8130-84360f41ec8d)<br>
<p align="center">[ Crop Detection ]</p><br>

![Result Set](https://github.com/user-attachments/assets/d1938337-3cba-4a4a-8ea9-bc06236b62e3)<br>
<p align="center">[ Result Set ]</p><br>

![YOLO Evaluation Metrics](https://github.com/user-attachments/assets/bf6ae5f6-07af-41fc-ad22-d8459841d621)<br>
<p align="center">[ YOLO Evaluation Metrics ]</p><br>

![Precision, Recall, and F1 Scores](https://github.com/user-attachments/assets/f72fef5c-00fc-4504-8da2-3779003445b2)<br>
<p align="center">[ Precision, Recall, and F1 Scores ]</p><br>

![Testing](https://github.com/user-attachments/assets/76294e70-4137-4f9a-8ab5-830bfeb3b0d2)<br>
<p align="center">[ Testing ]</p><br>

![Screenshot_2024-07-25-18-55-50-082_com surendramaran yolov8tflite](https://github.com/user-attachments/assets/164b6260-e4dc-4fe7-abdf-8b0a82fa5e44)<br>
<p align="center">[ Android Application ]</p><br>

![Screenshot_2024-07-25-18-58-46-982_com surendramaran yolov8tflite](https://github.com/user-attachments/assets/03eecbea-6ea2-43a8-b7dd-0f0b1ee480cf)<br>
<p align="center">[ Android Application Test ]</p><br>


Contact<br>
For any inquiries or contributions, please contact patelhiten1789@gmail.com.<br>

