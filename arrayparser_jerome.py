import re

# This object can be used to store info in a more readable way 
# Data can be access using objectname.data 

class Message(object):
    # The class "constructor" - It's actually an initializer 
    def __init__(self, index, status, sender, something, date, hour):
        self.index = index
	self.status = status
	self.sender = sender
	self.something = something
	self.date = date
	self.hour = hour
	self.content = '' 

    def combineText(self, text):
	if self.content != '':
		self.content += '\r\n'
	self.content += text

    def get(self):
	return (self.index, self.status, self.sender, self.something, self.date, self.hour, self.content)

### Cleaning and parsing

raw=['\r\n', '+CMGL: 31,"REC UNREAD","+33637165118"," ","17/12/03,17:58:13+04"\r\n', 'Text Message Contents\r\n', '\r\n', '+CMGL: 32,"REC UNREAD","+33637165118"," ","17/12/03,17:58:13+04"\r\n', 'Text Message Contents\r\n', '\r\n', '+CMGL: 33,"REC UNREAD","+33637165118"," ","17/12/03,17:58:13+04"\r\n', 'Text Message Contents\r\n', '\r\n', 'OK\r\n']

# Remove lines containing only '\r\n' or 'Text Message Contents\r\n'
raw = list(filter(lambda x : x != '\r\n' and x != 'Text Message Contents\r\n', raw))

# Remove end of line carriage returns
raw = [s.replace('\r\n', '') for s in raw]

# Initialize an array to receive the messages
messages = []

for line in raw:
	if re.match('^\+CMGL', line): # Regular expression for line staring with CMGL
		line = line.replace('"', '') # Remove unneeded "
		data = re.split(',', line) # Split info based on , separators
		messages.append(Message(data[0], data[1], data[2], data[3], data[4], data[5])) # Append a new Message object to the array
	else:
		messages[len(messages)-1].combineText(line) # Else append text line to the last message from the messages array

# Access your date
print messages[0].sender
print messages[0].date
print messages[0].hour
print messages[2].content

