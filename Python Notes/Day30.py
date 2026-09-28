#Example Code
import re

text = "Contact me at raj@gmail.com or support@gmail.com"

emails = re.findall(r'\w+@\w+\.\w+', text)

print("Emails found:")
print(emails)

'''Output:

Emails found:
['raj@gmail.com', 'support@gmail.com']'''

#Phone Number Example
import re

text = "My phone number is 9876543210"

pattern = r'\b[6-9]\d{9}\b'

result = re.findall(pattern, text)

print(result)