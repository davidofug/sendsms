'''
Import the package
e.g: python pip -m africastalking
'''
import africastalking
# TODO: Initialize Africa's Talking

africastalking.initialize(
    username='Ablestatestudents',
    api_key='238d21b78efe51c5ac7263acf4c2ca903546cd770d9da840ccdbec51abc6db15'
)

sms = africastalking.SMS

class send_sms():
    
    def send(self):
        #TODO: Send message
        recipients = [] #Put phone numbers as strings separated by commas
        
        '''
          Message length must be equal or less than 160 characters.
          Special symbols are allow but might result in a bigger message. So you maybe charged for more than one message.
          If you don't have senderID, an arbitray senderID will be sent.
        '''  
        message = "Message here." 
  
        try:
            response = sms.send(message, recipients)
            
            print(response)
            
        except Exception as e:
            print(f'We have a problem: {e}')

send_sms().send()
