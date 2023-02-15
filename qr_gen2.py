from segno import helpers
import segno


def qrgen2(data):

    name = data['first_name'] + ';' + data['last_name']
    company = data['company']
    phone = data['phone']
    email = data['email']
    url = data['url']
    note = data['note']
    street = data['street']
    city = data['city']
    zipcode = data['zipcode']
    region = data['region']

    qrcode = helpers.make_vcard(
        displayname=name,
        name=name,
        email=email,
        phone=phone,
        org=company,
        url=url,
        memo=note,
        street=street,
        city=city,
        zipcode=zipcode,
        region=region
    )

    qrcode.save('static/img/mecard.svg', scale=7)
    return 'static/img/mecard.svg'
