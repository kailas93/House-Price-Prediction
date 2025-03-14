# California House Price Prediction Flask App

This is a Flask-based web application that predicts house prices in California based on various input features such as median income, house age, average rooms, etc. The app uses a pre-trained linear regression model to make predictions.

---

## Table of Contents
1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Running the App](#running-the-app)
5. [API Usage](#api-usage)
6. [Deployment](#deployment)
7. [Contributing](#contributing)
8. [License](#license)

---

## Features
- Predict house prices using a pre-trained machine learning model.
- Simple web interface for inputting features and viewing predictions.
- REST API endpoint (`/predict`) for programmatic access.

---

## Prerequisites
Before running the app, ensure you have the following installed:
- Python 3.7 or higher
- pip (Python package manager)

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/california-house-price-prediction.git
   cd california-house-price-prediction
   # Clone the repository
git clone https://github.com/your-username/california-house-price-prediction.git
cd california-house-price-prediction

# Create and activate virtual environment
- python -m venv venv
- .\venv\Scripts\activate  # Windows
- source venv/bin/activate # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# Deactivate virtual environment (when done)
deactivate
