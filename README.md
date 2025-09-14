# RecycleVision

## Description
RecycleVision is a machine learning and computer vision application that classifies waste items as recyclable or non-recyclable. The project is trained on a custom dataset and deployed using Streamlit for a user-friendly web interface.

## Features
- Classifies waste images into recyclable and non-recyclable.

- Upload images directly through the Streamlit web app.

- Provides real-time predictions.

- Built with Python libraries: scikit-learn, OpenCV, scikit-image, joblib, etc.

## Technologies used
- Technologies Used

- Python

- Streamlit

- OpenCV (cv2)

- scikit-image (skimage)

- scikit-learn (sklearn)

- joblib

## Usage

Follow these steps to run and use the RecycleVision web app:

1. **Clone the repository** 

```bash
git clone <your-repo-url>
cd RecycleVision
```

2. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**
   ```
   python -m streamlit run recyclevision_app.py
   ```
4. **Open the app in a browser**:

   Use the Local URL provided by Streamlit (usually http://localhost:8501).

   If using the Network URL, you can access it from other devices on the same network.

5. **Upload an image of waste**:

   Use the upload button in the web interface to select an image from your computer.

6. **View the prediction**:

   The app will display whether the uploaded item is recyclable or non-recyclable.

