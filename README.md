🚢 Titanic Survival Prediction

A Machine Learning web application that predicts whether a Titanic passenger is likely to survive based on passenger information.

📌 Project Overview

The Titanic Survival Prediction project is a Machine Learning classification application built using Python and FastAPI.

The application takes passenger details such as age, gender, fare, passenger class, family information, and embarkation point, and uses a trained Machine Learning model to generate a survival prediction.

This project demonstrates how a Machine Learning model can be integrated with a web application using FastAPI.

✨ Features

🚢 Titanic passenger survival prediction

🤖 Machine Learning classification model

⚡ FastAPI backend

🌐 HTML, CSS & JavaScript frontend

📊 Pandas for data processing

💾 Joblib for saving and loading the trained model

📱 Responsive and user-friendly interface

🎨 Modern lavender, rose and cream UI theme

🛠️ Technologies Used

Python

Pandas

Scikit-learn

FastAPI

Uvicorn

Joblib

Jinja2

HTML5

CSS3

JavaScript

📂 Project Structure

Titanic-Survival-Prediction/
│
├── titanic_dataset/
│   └── train_and_test2.csv
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── model.pkl
├── train.py
├── main.py
├── requirements.txt
└── README.md

📋 Input Features

The application uses the following passenger information:

Passenger ID

Age

Fare

Gender

Siblings / Spouses

Parents / Children

Passenger Class

Embarked From

⚙️ Installation

Clone the repository:

git clone https://github.com/NargisNizam/Titanic-Survival-Prediction.git

Open the project folder:

cd Titanic-Survival-Prediction

Install the required dependencies:

pip install -r requirements.txt

▶️ Run the Application

Start the FastAPI server:

uvicorn main:app --reload

Open your browser and visit:

http://127.0.0.1:8000/

🔮 How It Works

Titanic dataset is loaded using Pandas.

The data is prepared for Machine Learning.

A classification model is trained using train.py.

The trained model is saved as model.pkl.

FastAPI loads the trained model.

The user enters passenger information through the web interface.

The model processes the input data.

The application displays the predicted survival result.

🎯 Project Purpose

The main purpose of this project is to practice and demonstrate:

Machine Learning classification

Data preprocessing

Model training

Model persistence

FastAPI API development

Frontend and backend integration

Machine Learning model deployment

📸 Application Preview

Add your project screenshot here after uploading it to GitHub.

Example:

![Titanic Prediction Interface](docs/titanic-prediction.png)

🚀 Future Improvements

Add model accuracy and evaluation metrics

Add prediction probability

Improve data preprocessing

Add more visual analytics

Deploy the application online

Improve validation and error handling

⚠️ Disclaimer

This project is created for educational and demonstration purposes only. The predictions should not be considered historically accurate or used for any real-world decision-making.

👩‍💻 Author

Nargis Nizam

AI & Data Science | Machine Learning | Python | FastAPI

⭐ If you find this project useful, feel free to star the repository!
