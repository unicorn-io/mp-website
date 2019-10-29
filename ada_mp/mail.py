import smtplib
def Mail(email, name, r_dict):
    gmail_user = 'visheshsciensism@gmail.com'
    gmail_password = 'ohyeah!!!!'

    sent_from = gmail_user
    to = email
    email_text = """\
    From: %s
    To: %s
    
    Subject: Payment Confirmation: Sherlock Ada

    Dear %s
        Your order was success please find the order details below.
        %s
        

        See You on 2nd November
    Ada Dramatics
    """ % (sent_from, ", ".join(to), name, str(r_dict))


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')

param_dict = {
            'MID':'KcuTvw62377761596842',
            'TXN_AMOUNT':'180',
            'CUST_ID':'acfff@paytm.com',
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'wWEBSTAGING',
            'CHANNEL_ID':'WEB',
            'CALLBACK_URL':'http://127.0.0.1:5000/handlepayment',
        }
Mail('tayalvishesh83@gmail.com', 'Vishesh Tayal', str(param_dict))