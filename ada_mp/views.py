from ada_mp import app
from flask import render_template
from flask import Flask
from flask import request
import requests
from flask import jsonify
from ada_mp.checksum import generate_checksum
from ada_mp.checksum import verify_checksum
import smtplib
from ada_mp.mail import Mail

email = ""
name = ""
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/purchase')
def contact():
    return render_template('contact.html')


@app.route('/handlepayment', methods = ['POST'])
def handle_payment():
    data = request.form
    response_dict = {}
    for i in data.keys():
        response_dict[i] = data[i]
        if i == 'CHECKSUMHASH':
            checksum = data[i]
    
    verify = verify_checksum(response_dict, 'wEits@QnXrF9QGJQ', checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            Mail(email, name, response_dict)
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render_template('paymentstatus.html', response = response_dict)

@app.route('/payment', methods = ['POST', 'GET'])
def pay():
    first_name = request.args.get('fname')
    last_name = request.args.get('lname')
    name = first_name + " " + last_name
    email =  request.args.get('email')
    reg_no = request.args.get('rnum')
    college_name = request.args.get('clgname')
    phone_number = request.args.get('pnum')
    address = request.args.get('addr')
    
    param_dict = {
            'MID':'KcuTvw62377761596842',
            'ORDER_ID': str(int(phone_number) + 123456789),
            'TXN_AMOUNT':'180',
            'CUST_ID':'acfff@paytm.com',
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'wWEBSTAGING',
            'CHANNEL_ID':'WEB',
            'CALLBACK_URL':'http://127.0.0.1:5000/handlepayment',
        }
    checksumq = generate_checksum(param_dict, 'wEits@QnXrF9QGJQ')
  
    param_dict.update({'CHECKSUMHASH': checksumq})
    return render_template('paytm.html', param_dict = param_dict)
   
