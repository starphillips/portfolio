from flask import Flask, render_template, url_for, request, redirect

import csv

app = Flask(__name__)

# This says anything we run our server, this code will run
# python3 -m flask run
# server standard is http://127.0.0.1:5000


@app.route('/')
def my_home():  # this creates default when name isnt given
    # a second parameter is needed to print the name
    return render_template("index.html")

# We now are able to use URLs to communicate with the server and ask for specific data for it to receive our server based on what URL parameters we give it or end points


# @app.route('/generic.html')
# def generic():
#     return render_template('generic.html')


# @app.route('/elements.html')
# def elements():
#     return render_template('elements.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         name = data["name"]
#         email = data["email"]
#         message = data["message"]
#         file = database.write(f'\n{name}, {email}, {message}')


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
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
