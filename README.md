# Parkinson-s-Disease-Prediction_
AI-powered Parkinson's Disease Prediction web app using voice features, Streamlit interface, SVM model, real-time prediction, and interactive visual feedback.

# 🧠 Parkinson's Disease Prediction 🍁
**Made by Priyam Parashar**

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.45.1-orange)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 🌟 Project Overview

This AI-powered web application predicts the likelihood of **Parkinson's Disease** using clinical voice features. Built with **Python**, **Streamlit**, **scikit-learn**, and **NumPy**, it offers a simple and interactive interface for medical and research purposes.

- Real-time predictions based on voice features
- Confidence score displayed
- Interactive and responsive UI
- Custom background with autumn theme 🍁

---

## 🎬 Demo

Watch the app in action:  

![Dashboard](images/Prkinson's_Dashboard.png)
![Dashboard](images/High_Chance.png)
![Dashboard](images/Low_chance.png)

Or try it locally:

```bash
python -m streamlit run "D:\ML Projects\app.py"

Access URL in browser: http://localhost:8501

🖼 Screenshots

Home Page

<img width="1917" height="915" alt="Screenshot 2025-08-20 032454" src="https://github.com/user-attachments/assets/22013db9-6956-407c-b5a3-2c4b7c1a73c0" />

<img width="1912" height="930" alt="Screenshot 2025-08-20 032507" src="https://github.com/user-attachments/assets/be7a7945-2bcf-494a-8dcd-fee289ea71b8" />


Sidebar Input Features

<img width="1908" height="928" alt="Screenshot 2025-08-20 032520" src="https://github.com/user-attachments/assets/97d371eb-d05b-42d6-babe-59a9014d2cb0" />

Prediction Result

<img width="1909" height="915" alt="Screenshot 2025-08-20 032538" src="https://github.com/user-attachments/assets/b3506184-65f4-4903-8e15-c8f7549122e1" />

```

📊 Features

Input 22 clinical voice features via the sidebar

Predict likelihood of Parkinson's Disease

Confidence score displayed as progress bar

Responsive design and custom theme colors

Background image changes based on seasonal theme (fall)

Made with ❤️ by Priyam Parashar


⚙️ Installation

Make sure Python 3.9+ is installed.

Install required packages:

``` bash

pip install streamlit numpy scikit-learn pillow

python -m streamlit run "D:\ML Projects\app.py"

```

🗂 File Structure

```
D:\ML Projects\
├── app.py              # Main Streamlit application
├── svm_model.pkl       # Pre-trained SVM model
├── scaler.pkl          # Pre-trained feature scaler
├── fall_bg.jpg         # Background image for the app
├── README.md           # This file
├── LICENSE             # MIT License

```

🧩 How it Works

Enter the voice features in the sidebar.

Click Predict Parkinson's.

View prediction results and confidence score.

📌 License

This project is licensed under the MIT License – see the LICENSE
 file for details.
