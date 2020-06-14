import requests
import pandas as pd
import csv
import json
import re

zoom_base_url = 'https://api.zoom.us/v2'
zoom_meeting_id = '86941866544'
zoom_api_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOm51bGwsImlzcyI6Imt1Y3p4a3l0UmhxY2pJYzBVRTJrZVEiLCJleHAiOjE1OTI3MDg0NjAsImlhdCI6MTU5MTA2NjkzNn0.tHPiWm2tG6rAuGV3BForxLUwLmOLwHOnsyAJjQbkUYs'
zoom_api_key = 'kuczxkytRhqcjIc0UE2keQ'
zoom_api_secret = 'FaGg3z0xiaztCXHfge6frv2COkX2Lj3tQw4B'

credentials = {'api_key': zoom_api_key, 'api_secret': zoom_api_secret}
meeting_data = {'type': 2, 'topic': 'QFL', 'option_jbh': True, 'option_registration': True}
registrant_data = {'email': 'test@gmail.com', 'first_name': 'Alex ', 'last_name': 'Zhang', 'group': '1'} # empty dict for registering users to zoom

def register_xlsx_users(path):
    data = pd.read_excel(path)
    df = pd.DataFrame(data)
    df.columns = ['Group', 'Email', 'CName', 'EName', 'Church'] # rename columns
    for index in range(len(df)):
        group = str(df['Group'].iloc[index])
        church = df['Church'].iloc[index]
        church = church[0:7] # update later to remove all chinese characters at any position
        registrant_data['email'] = df['Email'].iloc[index]
        registrant_data['group'] = group
        registrant_data['first_name'] = 'G' + group + ' ' + df['EName'].iloc[index]
        registrant_data['last_name'] = church
        response = register_user(registrant_data)
        response_dict = json.loads(response.text) # json format is very fragile; be careful for chinese characters
        print(response_dict)
        save_links(group, df['Email'].iloc[index], df['CName'].iloc[index], df['EName'].iloc[index], df['Church'].iloc[index], response_dict['join_url'])
       

def register_user(data):
    register_url = zoom_base_url + '/meetings/' + zoom_meeting_id + "/registrants"
    # register user to meeting
    headers = {'authorization': f'Bearer {zoom_api_token}',
               'content-type': 'application/json'}
    msg_body = dict_to_json(data)
    response = requests.request("POST", register_url, data=msg_body, headers=headers)
    print(response.text)
    return response

def save_links(group, email, cname, ename, church, link):
    with open('join_links.csv', mode='a') as join_links:
        writer = csv.writer(join_links, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([group, email, cname, ename, church, link])

def check_user(query_string):
    user_url = zoom_base_url + '/users/email'
    headers = {'authorization': 'Bearer ' + zoom_api_token}
    response = requests.request("GET", user_url, headers=headers, params=query_string)
    print(response.text)

def dict_to_json(dict_object):
    message = "{"
    for key in dict_object.keys():
        message = message + f'\"{key}\":\"{dict_object[key]}\",'
    message = message[:-1] + '}'
    print(message)
    return message

def main():
    register_xlsx_users (r'/home/alex/projects/playground/zoom_api/registration_june_13.xlsx')

if __name__ == "__main__":
    main()

