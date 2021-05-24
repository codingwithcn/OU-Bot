class ChatBot:
  def __init__(self):
    self.messages = {}
    
  def get_message(self, ip):
    return self.messages[ip]
  
  def add_new_ip(self, ip):
    self.messages[ip]=[]

  def delete_ip(self, ip):
    self.messages.pop(ip)

  def get_bot_reply(self, ip, message):
    # Feel free to change
    return "hello" 
    
  def send_message(self,ip,  message):
    try:
      repl = {'User': message, 'Bot': self.get_bot_reply(ip, message)}
      self.messages[ip].append(repl)
      return self.get_message(ip)
    except Exception as e:
      print(e)
      return "Problem saving chat"