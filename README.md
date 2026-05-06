# 🎨 Poster Analysis System  
### Automated Visual Analysis of Poster Designs using Computer Vision

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Interactive%20UI-red)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📌 Overview

This project presents an **automated poster analysis system** built using image processing and computer vision techniques.  

The system analyzes visual characteristics of poster designs including:

- 🎨 Dominant color extraction  
- ⚖️ Visual balance analysis  
- 🧠 Saliency (focal point) detection  
- 📊 Structural and edge complexity analysis  

The application provides an interactive web interface powered by **Streamlit**, allowing users to upload posters and instantly receive analytical insights.

---

## 🚀 Features

✅ Extract dominant colors using **K-Means clustering**  
✅ Analyze brightness distribution for visual balance  
✅ Compute edge density for structural complexity  
✅ Generate saliency maps using **Spectral Residual method**  
✅ Interactive UI with real-time visualization  
✅ Persian (RTL) interface support  

---

## 🛠 Technologies Used

- Python  
- OpenCV  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Streamlit  

---

## 🧠 System Architecture

The system consists of three main analytical modules:

### 1️⃣ Color Analysis Module
- Converts image to HSV color space
- Applies K-Means clustering
- Extracts dominant color palette

### 2️⃣ Composition & Structure Module
- Edge detection (Canny)
- Brightness distribution analysis
- Complexity estimation

### 3️⃣ Saliency Detection Module
- Spectral Residual approach
- Generates visual attention heatmap
- Identifies focal regions

---

## 📷 How It Works

1. Upload a poster image  
2. The system processes the image  
3. Visual metrics are computed  
4. Analytical results and visualizations are displayed  

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/poster-analysis.git
cd poster-analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📊 Example Output

- Dominant Color Palette  
- Saliency Heatmap  
- Edge Density Visualization  
- Visual Balance Score  

---

## 🎓 Academic Context

This project was developed as part of a bachelor's thesis in the field of:

> Computer Engineering / Computer Vision / Image Processing

The goal is to bridge the gap between **graphic design principles** and **automated visual analysis**.

---

## 🔮 Future Improvements

- Deep learning-based aesthetic scoring  
- Typography detection  
- Layout structure recognition  
- Dataset-based comparative evaluation  

---

## 🤝 Contribution

Contributions, suggestions, and improvements are welcome!  
Feel free to fork this repository and submit pull requests.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

- Armin Abdollahi
- Sarina Kasaiyan

---

⭐ If you find this project useful, consider giving it a star!
```
