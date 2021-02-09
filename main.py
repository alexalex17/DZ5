import csv
import base58
import requests
from faker import Faker
from flask import Flask
from flask import send_file

fake = Faker()

app = Flask(__name__)


# 1
@app.route('/requirements/')
def requirements():
    return send_file('requirements.txt')


# 2
@app.route('/generate-users/<int:post_id>')
def generate(post_id):
    q = ''
    for i in range(0, post_id):
        q += fake.name() + ' ' + fake.email() + '<br>'
        i += 1
    return str(q)


# 3
@app.route('/mean/')
def mean():
    with open("hw05.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        count = 0
        a = 0
        b = 0
        for row in file_reader:
            if count == 0:
                a = 0
            else:
                a = a + 2.54 * float(row[1])
                b = b + 0.45359237 * float(row[2])
            count += 1
        prints = f'Parsed file: hw05.csv<br>' \
                 f'Total values in file (strings of data): {str(count - 1)}<br>' \
                 f'Average height: {round(a / (count - 1))} cm <br>' \
                 f'Average weight: {round(b / (count - 1))}   kg '
    return prints


# 4
@app.route('/space/')
def space():
    r = requests.get('http://api.open-notify.org/astros.json')
    return str(len(r.json()["people"]))


# 5
@app.route('/base58encode/<text>')
def base58encode(text):
    return base58.b58encode(text)


# 6
@app.route('/base58decode/<text>')
def base58decode(text):
    return base58.b58decode(text)


@app.errorhandler(404)
def internal_server_error(error):
    print("caught internal server error")
    return "<h1 align='center'>This page does not exist<h1><br><big><big><big><h1 " \
           "align='center'>404<h1></big></big></big> "


app.debug = True
app.run(port=5000)
