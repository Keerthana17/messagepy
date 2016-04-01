import xmpp

username = raw_input(" Enter username : ")
passwd = raw_input(" Enter the password : ")
msg  = raw_input(" Enter a message  : ")
to = raw_input(" Enter the sender's address : ")

client = xmpp.Client('gmail.com')
client.connect(server=('talk.google.com',5223))
client.auth(username, passwd, 'botty')
client.sendInitPresence()
message = xmpp.Message(to, msg)
message.setAttr('type', 'chat')
client.send(message)

#You may need to change gmail's privacy settings for this to work.
#If XMPP is not installed, please do so using 'sudo apt-get install python-xmpp'for debian/ubuntu systems (Package may vary for other linux distros)
