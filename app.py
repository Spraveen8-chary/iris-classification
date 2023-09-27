import pickle
import numpy as np
from flask import render_template, Flask, request

app = Flask(__name__)

with open('iris_model.pickle', 'rb') as f:
    model = pickle.load(f)
result_images = {
    'Setosa': 'Setosa.jpeg',
    'Versicolor': 'Versicolor.jpeg',
    'Virginica': 'Virginica.jpeg',
}
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input1 = float(request.form['input1'])
        input2 = float(request.form['input2'])
        input3 = float(request.form['input3'])
        input4 = float(request.form['input4'])
        
        X_new = np.array([[input1, input2, input3, input4]])
        class_names = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
        predictions = model.predict(X_new)
        result = class_names.get(predictions[0], 'Unknown')
        result_image = result_images[result]
         
        return render_template('index.html', result=result , result_image=result_image)
    
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
