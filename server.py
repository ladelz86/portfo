
import os
import csv
from flask import Flask, render_template, send_from_directory, url_for, request, redirect
app = Flask(__name__)
print(__name__)


pages = ('/', '/works', '/work', '/about', '/contact')

# for i, page in enumerate(pages):
#     funct_name = f'page{i}'


@app.route('/')
def home():
    return render_template('./index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(f'./{page_name}.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            if data['email'] and data['subject'] and data['message']:
                write_to_csv(data)
            else:
                print("No data")
            print(data)
            return redirect('./thankyou')
        except:
            return 'Did not save to database'
    else:
        return 'something went wrong'


def write_to_file(data):
    with open('./database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f"{email},{subject},{message}\n")


def write_to_csv(data):
    with open('./database.csv', newline='', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        if os.stat('./database.csv').st_size == 0:
            csv_writer.writerow(['email', 'subject', 'message'])
        file = csv_writer.writerow([email, subject, message])


# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')
