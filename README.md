# 👹 VizDoom Combat Predictor 🏆

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.20+-red.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-orange.svg)
![Reinforcement Learning](https://img.shields.io/badge/Reinforcement%20Learning-PPO-brightgreen.svg)

## 📌 Overview
The **VizDoom Combat Predictor** is an end-to-end Machine Learning web application that analyzes an AI agent's combat tier and training hours to predict its probability of surviving a match in the game VizDoom. 

Beyond simple predictions, this project features actual gameplay footage of a custom **Deep Reinforcement Learning (PPO) agent** navigating the VizDoom environment using raw pixel data, alongside interactive data visualizations plotting the model's decision boundaries.

**🔴 Live Demo:** [Check out the live web app here!](https://vizdoom-predictor.streamlit.app/)

---

## 🛠️ Tech Stack
* **Machine Learning:** `scikit-learn` (Random Forest Classifier)
* **Reinforcement Learning:** Proximal Policy Optimization (PPO), Convolutional Neural Networks (CNN)
* **Frontend:** `Streamlit`
* **Data Manipulation:** `pandas`, `numpy`
* **Deployment & CI/CD:** GitHub, Streamlit Community Cloud

---

## 📊 Features
1. **Survival Probability Calculator:** Uses a trained Random Forest model to predict match outcomes based on training hours and combat levels.
2. **AI Confidence Tracker:** Displays the exact mathematical probability (confidence score) of the AI's prediction.
3. **The Victory Zone Graph:** A dynamic data visualization plotting the decision boundary for guaranteed agent survival.
4. **Agent Gameplay Showcase:** Embedded video playback of the custom PPO agent successfully clearing the VizDoom environment.

---

## 🚀 How to Run Locally

To run this project on your own machine, follow these steps:

**1. Clone the repository**
```bash
git clone [https://github.com/kushagra2503-del/ai_server.git](https://github.com/kushagra2503-del/ai_server.git)
cd ai_server
'''



**2. Install dependencies**
Make sure you have Python installed, then run:
 ```bash
  pip install pandas scikit-learn numpy streamlit joblib
  ```

**3. Train the Model**
  ```bash
  python train.py
  ```