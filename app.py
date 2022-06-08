from flask import render_template, request, Flask
import numpy as np
import pickle

app = Flask(__name__)

def load_object(filename):
    with open(''+filename ,'rb') as f:
        loaded = pickle.load(f)
    return loaded

model = load_object(r'model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods =['POST'])
def predict():
    '''
    For rendering results on HTML GUI

    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    return render_template('index.html', predict_text='Tip should be {} $ '.format(output))

# if __name__ == "__main__":
#     # app.run(debug=True, )
#     app.run(debug = True)