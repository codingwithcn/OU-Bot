from flask import Flask, request, render_template, jsonify

import random, chatbot

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

chatbots = chatbot.ChatBot()

@app.route('/', methods=['GET'])
def index():
  try:
    stuff = chatbots.messages[request.remote_addr]
  except KeyError:
    chatbots.add_new_ip(request.remote_addr)
  return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
  data = request.get_json()
  try:
    stuff = chatbots.messages[request.remote_addr]
  except KeyError:
    chatbots.add_new_ip(request.remote_addr)

  return {'messages': chatbots.send_message(request.remote_addr,data['message'])}

@app.route('/get/mes', methods=['POST'])
def get_mes():
  try:
    try:
      stuff = chatbots.messages[request.remote_addr]
    except KeyError:
      chatbots.add_new_ip(request.remote_addr)
    return {'messages': chatbots.get_message(request.remote_addr)}
  except Exception as e:
    print(e)
    return 'Issue'

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=random.randint(2000, 9000))