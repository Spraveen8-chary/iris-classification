# Iris Flower Classification Web App
This is a simple web application built using Flask for Iris flower classification. Users can input the measurements of an Iris flower, and the application will predict the species of the flower (Setosa, Versicolor, or Virginica) and display an image corresponding to the predicted species.

# Prerequisites
Before you begin, ensure you have the following requirements installed:

- Python (3.6 or higher)
- Flask
- scikit-learn (for the machine learning model)
- Bootstrap (for styling)
- A web browser


## Clone this repository to your local machine:

- git clone https://github.com/yourusername/iris-classification-web-app.git

## Change the current directory to the project folder:

- cd iris-classification-web-app

## Install the required Python packages:

- pip install Flask scikit-learn

# Run the Flask application:

- python app.py
- Open your web browser and navigate to http://localhost:5000/ to access the application.

# Usage
- Enter the measurements of the Iris flower in centimeters (Sepal Length, Sepal Width, Petal Length, and Petal Width) in the input fields.

- Click the "Submit" button to classify the Iris flower.

- The application will display the predicted species of the Iris flower along with an image of the predicted species.

# Project Structure

- app.py: The Flask application that handles web requests and predictions.
- iris_model.pickle: A pre-trained machine learning model for Iris flower classification.
- templates/index.html: The HTML template for the web page.
- static/images/: Contains images of Iris species for display.

# Output 
![image](https://github.com/Spraveen8-chary/iris-classification/assets/108536707/20369e4e-d941-48a3-9728-6246d8db2bf0)
