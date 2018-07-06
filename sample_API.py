import requests
import json

URL_suffix = '/v0.1'
url = 'https://henryyang.herokuapp.com' + URL_suffix
# url = 'http://127.0.0.1:5000' + URL_suffix
# url = 'http://e6dfec2a.ngrok.io' + URL_suffix


# def get_response_example_new(userInput):
#     # print('userInput in Tomo_API.py')
#     # print(userInput)
#     headers = {'Authorization': '',
#                'Accept': 'application/json',
#                'Content-Type': 'application/json'}

#     response = requests.post(url, data=userInput, headers=headers)
#     return response.text


def get_response_example_json(userInput):
    print(userInput)
    headers = {'Authorization': '',
               'Accept': 'application/json',
               'Content-Type': 'application/json'}

    response = requests.post(url, data=json.dumps(userInput), headers=headers)
    response_dict = json.loads(response.text)
    ans_text = response_dict['response']['answer']
    return ans_text

userInput = {"question": "message_input"}
response = get_response_example_json(userInput)
print(response)
    
