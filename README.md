# 🚀 FalconVision - Space Station Object Detector

- [FULL VIDEO OF WEB APP](https://drive.google.com/file/d/1OYh0UVd2NxdRsCHFWq8Sl42oquVV4l11/view?usp=sharing)

 
A web-based object detection application built with YOLOv8 and Falcon AI platform for detecting safety-critical objects in space station environments.

## 📋 Project Overview

FalconVision is an intelligent object detection system designed to help astronauts and ground control quickly identify and locate critical safety equipment in space stations. The application uses advanced computer vision to detect FireExtinguishers, ToolBoxes, and OxygenTanks from uploaded images.

### 🎯 Key Features

- **Real-time Object Detection**: Upload images and get instant detection results with bounding boxes and class labels
- **Multi-class Detection**: Detects three critical object types: FireExtinguisher, ToolBox, OxygenTank
- **Web-based Interface**: Accessible from any modern browser on computer or mobile devices
- **Download Results**: Save annotated images with detection overlays
- **Model Maintenance**: Built-in support for continuous model updates and improvements

## 🏗️ Architecture

- **Frontend**: HTML5, CSS3avaScript (Vanilla)
- **Backend**: Python Flask
- **AI Model**: YOLOv8 (Ultralytics) with custom training
- **Platform**: Falcon AI by Duality AI

## 📦 Installation

### Prerequisites

- Python 30.9gher
- pip package manager
- Modern web browser

### Setup Instructions

1. **Clone or download the project files**
   ```bash
   # Ensure all files are in the Falcon directory
   # - app.py
   # - index.html
   # - best.pt (YOLOv8 model)
   # - requirements.txt
   ```

2. **Install Python dependencies**
   ```bash
   cd Falcon
   pip install -r requirements.txt
   ```
3*Verify model file**
   - Ensure `best.pt` (5.9 is present in the project directory
   - This is the trained YOLOv8 model for space station object detection

## 🚀 Usage

### Starting the Application

1. **Start the Flask backend**
   ```bash
   cd Falcon
   python app.py
   ```

2. **Access the web application**
   - Open your browser and navigate to: `http://12700.1 - The application will load with a modern, space-themed interface

### Using the Application

1. **Upload an Image**
   - ClickChoose Image" to select a `.jpg`, `.jpeg`, or `.png` file
   - The file name will be displayed below the button

2. **Detect Objects**
   - Click "Detect Objects to run the YOLOv8 model
   - Wait for the Detecting objects..." message to complete
3 **View Results**
   - Original and detected images will be displayed
   - Bounding boxes show detected objects with class labels
   - Click "Download Annotated Image" to save the result4Learn About Falcon**
   - ClickAbout Falcon" in the navigation to learn about the platform
   - Access official documentation and understand model maintenance

## 📊 Model Performance

### Metrics (mAP@00.5916)
- **Precision**: 0.943 **Recall**: 0.881- **mAP50*: **0.916**
- **mAP50: 0.83s-wise Performance
| Class | Precision | Recall | mAP50 |
|-------|-----------|--------|-------|
| FireExtinguisher | 0.987|0.9400.952
| ToolBox | 0.963|0.867|0900 |
| OxygenTank | 0.88000.8376 Project Structure

```
Falcon/
├── app.py                 # Flask backend server
├── index.html            # Web application frontend
├── best.pt               # Trained YOLOv8 model (5.9MB)
├── requirements.txt      # Python dependencies
├── Project_Report.md     # Detailed project report
└── README.md            # This file
```

## 🌟 About Falcon AI Platform

Falcon is an advanced AI platform by Duality AI, designed for rapid development, deployment, and maintenance of computer vision models in real-world environments. It supports multiclass object detection, continuous learning, and seamless integration with applications.

### Model Maintenance with Falcon

The application demonstrates how Falcon can maintain and update models as real-world environments change:

- **Continuous Updates**: Users can flag incorrect detections or upload new images where the model fails
- **Automated Retraining**: New annotated images are added to the training dataset, triggering automated model retraining
- **Adaptation**: The model adapts to new objects or changes in appearance (e.g., new FireExtinguisher colors)
- **Deployment**: Improved models are automatically deployed to the application

### Official Documentation
- [Falcon Object Detection Multiclass Documentation](https://falcon.duality.ai/secure/documentation/ex3-objdetection-multiclass?sidebarMode=learn&utm_source=hackathon&utm_medium=instructions&utm_campaign=algoverse)

## 🎯 Use Cases

### Space Station Safety
- Quick verification of safety equipment presence and location
- Emergency response support for locating critical items
- Automated inventory management

### Real-world Applications
- Industrial safety monitoring
- Equipment tracking in controlled environments
- Automated safety compliance checking

## 🔄 Continuous Improvement

The system is designed for continuous improvement:

1. **Feedback Collection**: Users can report detection errors
2. **Data Augmentation**: New images are collected and annotated
3. **Model Retraining**: Falcon platform handles automated retraining
4loyment**: Updated models are seamlessly deployed

## 📝 Technical Details

### Training Configuration
- **Model**: YOLOv8(Ultralytics)
- **Epochs**:50
- **Batch Size**:16
- **Image Size**:640x640
- **Early Stopping**: Patience = 3

### Dataset
- **Format**: YOLO format
- **Classes**: 3 (FireExtinguisher, ToolBox, OxygenTank)
- **Split**: Train/Val/Test with proper distribution

## 🚨 Troubleshooting

### Common Issues

1. **Detection failed" error**
   - Ensure the Flask backend is running (`python app.py`)
   - Check that `best.pt` is in the correct directory
   - Verify image format (.jpg, .jpeg, .png)2. **CORS errors**
   - Access the app via `http://12700.1/` (not by opening index.html directly)
   - The backend includes CORS support for cross-origin requests

3del loading issues**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Check that the `best.pt` file is not corrupted

## 📄 License

This project is developed for the Falcon AI hackathon and uses the Falcon platform by Duality AI.

## 👥 Team

- **Platform**: Falcon AI by Duality AI
- **Model**: YOLOv8 (Ultralytics)
- **Framework**: Flask, HTML5, CSS3, JavaScript

---

**Built using Falcon synthetic data by Duality AI**

For more information about the Falcon platform, visit the [official documentation](https://falcon.duality.ai/secure/documentation/ex3-objdetection-multiclass?sidebarMode=learn&utm_source=hackathon&utm_medium=instructions&utm_campaign=algoverse). 
