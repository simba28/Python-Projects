from twilio.rest import Client 
 
account_sid = 'twilio account id here' 
auth_token = '......'
client = Client(account_sid, auth_token) 

import sys

try:
    if sys.argv[1] == 'send':
        message = client.messages.create( 
                                    from_='number provided by twilio here',  
                                    body='this sms is sent through python using twilio communication api',      
                                    to='number----' 
                                ) 
        
        print(message.sid)
except:
    print('Not asked to send')