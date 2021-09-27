import smtplib
from time import sleep

import requests
from bs4 import BeautifulSoup

URL = 'https://www.bikecenter.bg/komponenti/spirachki/spirachka-diskova-predna/spirachka-diskova-predna-shimano-bl-m4100-deore-res/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}



def check_price():
    page = requests.get( URL, headers=headers )

    soup = BeautifulSoup( page.content, 'html.parser' )

    title = soup.find( itemprop='name' ).get_text()

    #method 1
    price = soup.findAll( class_='price' ).pop()
    converted_price = int( str( price )[20:22] )

    #method 2
    #price2 = soup.findAll('span', {'class': 'price'})[-1].get_text()
    #print(price2)


    if converted_price < 69:
        print('GO GO GO')
    else:
        print('not yet')



def send_email():
    server = smtplib.SMTP('.............', 111)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('...................', '..................')

    subject = 'Price fell down!'

    body = 'Check the link: https://www.bikecenter.bg/komponenti/spirachki/spirachka-diskova-predna/spirachka-diskova-predna-shimano-bl-m4100-deore-res/'

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'from',
        'to',
        msg
    )
    print('Email has been sent!')

    server.quit()

while True:
    check_price()
    sleep(5)


