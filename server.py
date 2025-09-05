from flask import Flask, render_template, url_for, request, redirect

import csv
import os

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template("index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


<<<<<<< HEAD
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONTACTS_FILE = os.path.join(BASE_DIR, "database.csv")
print("Using database file at:", CONTACTS_FILE)


=======
>>>>>>> 0493dcb22c0a3da2e1a5c06bcf03fc05ca4a17f5
def write_to_csv(data):
    with open(CONTACTS_FILE, mode='a') as database2:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            print(data)
            return redirect('/thankyou.html')
        except:
            return 'Unable to save to database'
    else:
        return 'Error in Sending. Please try again.'
