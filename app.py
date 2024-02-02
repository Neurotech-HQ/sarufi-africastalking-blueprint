import os 
import logging
import africastalking
from sarufi import Sarufi
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from starlette.datastructures import FormData

load_dotenv()

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize SDK
africastalking.initialize(
    username=os.getenv('AT_USERNAME'),
    api_key=os.getenv('AT_API_KEY_SECRET')
)
sarufi = Sarufi(os.getenv('SARUFI_API_KEY'))
sms = africastalking.SMS

app = FastAPI()

@app.post("/")
async def form_data_endpoint(request: Request):
    form_data: FormData = await request.form()
    text = form_data.get('text')
    to = form_data.get('to')
    from_number = form_data.get('from')
    logging.info(f"Message received from {from_number}")
    
    # Integrate Sarufi with sarufi here  and send the response to the user
    response = sarufi.chat(
        bot_id=os.getenv('SARUFI_BOT_ID'),
        chat_id=from_number,
        message=text,
        message_type='text',
        channel='general'
    )
    
    if response:
        logging.info(response)
        message = response.get('message', 'Sorry, I did not understand that')
        sms.send(message = message, recipients=[from_number], sender_id=to)
        logging.info(f"Message sent to {from_number}")
    return {"status": "data received"}
    