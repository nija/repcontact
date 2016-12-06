#!/usr/bin/env python
'''Let's contact our Congress critters!'''
# pylint: disable=I0011,C0103

# ====== Imports ======
# Standard imports
import bleach
import json
import os
import pprint
# import requests
# import urllib
import urllib2

# Third-party APIs
from twilio.rest import TwilioRestClient


pp = pprint.PrettyPrinter(indent=2)

# Use Twilio; pull from the environment vars 
user_data = {
    'first_name': os.environ['USER_FIRST_NAME'],
    'last_name': os.environ['USER_LAST_NAME'],
    'phone': os.environ['USER_PHONE'],
    'email': os.environ['USER_EMAIL']
}

def get_congress_critter_data(zipcode=94301):
    '''
        Get a json representation of Congress critters from the backend API.
        This is by definition imprecise because zipcodes usually, but not always, correspond to
        voting districts.
    '''
    # Don't currently need an APIKey but will in the future; grab it from the env when I do need it
    # apikey = ''
    base_url = 'https://congress.api.sunlightfoundation.com'
    path = '/legislators/locate'
    request = base_url + path + "?zip=" + str(zipcode)
    # print request
    response = urllib2.urlopen(request)
    the_json = json.loads(response.read())
    critter_data_long = the_json.get('results')

    critter_data = [{
        'first_name': critter.get('first_name'),
        'last_name': critter.get('last_name'),
        'phone': critter.get('phone'),
        'oc_email': critter.get('oc_email'),
        'chamber': critter.get('chamber')} for critter in critter_data_long]

    pp.pprint(critter_data)
    return critter_data


def call_a_number(critter):
    '''Call out'''
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_ACUTH_TOKEN']
    client = TwilioRestClient(account_sid, auth_token)

    # TODO: massage phone number to be in the correct format
    critter_phone = '+1' + critter.get('phone')
    user_phone = user_data.get('phone')
    call = client.calls.create(to=str(critter_phone), from_=str(user_phone), url='http://demo.twilio.com/docs/voice.xml')
    print call.sid


if __name__ == '__main__':
    critters = get_congress_critter_data()
    for critter in critters:
        call_a_number(critter)















