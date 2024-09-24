from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the machine learning model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        age = int(request.form['age'])
        
        # Prepare input data for the model (modify as needed)
        input_features = [[age]]  # Update this based on your model's input requirements
        
        # Make prediction
        prediction = model.predict(input_features)[0]  # Assuming the model returns a single value
        
        # Render the same index page with results
        return render_template('index.html', name=name, email=email, age=age, prediction=prediction)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
