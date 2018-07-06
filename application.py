from flask import Flask, jsonify
from flask import request
from flask import abort
from flask import Response
import json
import ast
import pprint
import re
import requests
from urllib.parse import unquote_plus
import telepot
import time

stopwatch = {'01 init': time.clock()}


# For telegram message monitoring
bbmousetoken='293749176:AAFUwX1PMi-FtFnorDJga3l3vKRcCBuwHTo'
bot = telepot.Bot(bbmousetoken)

# For Slack message monitorying
slack_webhook_url = 'https://hooks.slack.com/services/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'

stopwatch['02 end_of_setting'] = time.clock()

# print a nice greeting.
def say_hello(username="World"):
    return '<p>Hello %s!</p>\n' % username  


# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>20180201 EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text + say_hello() + instructions + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', 'hello', (lambda username: header_text + say_hello(username) + home_link + footer_text))


@application.route('/v0.1', methods=['POST'])
def get_response():
    print(request)

    if not request.json:
        try:
            bot.sendMessage(271383530, u"henryyangbot 進來了一筆不是json的request: \n" + str(request))
        except:
            pass
        abort(400)
    try:
        bot.sendMessage(271383530, "henryyangbot 進來了一筆request:")
        bot.sendMessage(271383530, pprint.pformat(request.json, indent=2))
    except:
        pass
    if not request.json:
        abort(400)

    print('request.json:')
    print(json.dumps(request.json, indent=4, sort_keys=True))

    response = request.json
    response['answer'] = 'a' + request.json['question']
    return jsonify({'response': response})


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
