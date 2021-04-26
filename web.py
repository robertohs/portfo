from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def hello(name=None):
    return render_template('index.html', name=name)


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        name = data['name']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n {name},{subject},{email},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        name = data['name']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, subject, email, message])
        print(data)


@app.route('/p_data', methods=['GET', 'POST'])
def parse_request():
    if request.method == 'POST':

        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('/')
        except :
            return 'did not save to database'
    else:
        return 'something went wrong'
