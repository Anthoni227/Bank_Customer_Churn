from flask import Flask, render_template, request
import numpy as np
import pickle
import mysql.connector
import pandas as pd


app = Flask(__name__)

# Load the trained model
model = pickle.load(open('saved_model.pkl','rb'))

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="newdata"
)


@app.route('/')
def index():
    return render_template("loginpage.html")

@app.route('/mainpage')
def mainpage():
    return render_template("mainpage.html")
# Function to retrieve customer data from MySQL
def retrieve_customer_data(customer_id):
    cursor = conn.cursor(dictionary=False)
    query = "SELECT CreditScore,Age, Balance, IsActiveMember,EstimatedSalary, Complain,SatisfactionScore FROM newone WHERE CustomerId = %s"
    cursor.execute(query, (customer_id,))
    customer_data = cursor.fetchone()
    cursor.close()
    return customer_data

@app.route('/predict', methods=['GET','POST'])

def predict():

    # Retrieve CustomerId from the form
    customer_id = int(request.form['customer_id'])
    
    # Retrieve customer data from the database
    customer_data = retrieve_customer_data(customer_id)
    

    # Extract features
    variable = np.array(customer_data)
    preprocess=pickle.load(open("preprocessing_model.pkl","rb"))
    new_var=pd.DataFrame(variable).T
    cols=['CreditScore','Age', 'Balance', 'IsActiveMember',
        'EstimatedSalary', 'Complain','SatisfactionScore']
    new_var.columns=cols
    processed_features=(preprocess.transform(new_var))
    


   
    # Make prediction
    
    prediction = model.predict(processed_features)
    if prediction==1:
        return render_template("true.html",prediction=prediction)
        
    else:
        
        return render_template("false.html",prediction=prediction)
       

if __name__ == '__main__':
    app.run(debug=True)