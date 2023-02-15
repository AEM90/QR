from flask import Flask, render_template, request
import pyqrcode
from qr_gen2 import qrgen2


app = Flask(__name__)


#https://www.youtube.com/watch?v=zt1YbpnBkQU&ab_channel=CodeWithPrince
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/vcard', methods=['GET', 'POST'])
def vcard():
    if request.method == 'POST':

        filename = qrgen2(request.form)

        return render_template('vcard.html', qr_code_image=filename)
    else:
        return render_template('vcard.html')


@app.route('/webadress', methods=['GET', 'POST'])
def instagram():
    if request.method == 'POST':

        # Get form data
        url = request.form['url']

        # generate url and local path
        url = pyqrcode.create(url)
        path = "static/img/myqr.svg"

        # create svg file
        url.svg(path, scale=8)

        return render_template('webadress.html', qrcode_socialmedia='img/myqr.svg')
    else:
        return render_template('webadress.html')


if __name__ == '__main__':
    app.run(debug=True)