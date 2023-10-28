# sarufi-africastalking-blueprint

Sarufi Blueprint to easier the integration between Sarufi and Africas talking 2 way SMS Platform 

It uses [africastalking](https://github.com/AfricasTalkingLtd/africastalking-python/) python SDK and FastAPI to implement a webhook that you're going to put on AT dashboard on a session of _incoming messages_. 


## Setting up 

To run this code, first install all the required libaries, which you can easily do by installing the _requirements.txt_

```bash
$ pip install -r requirements.txt
```

## Set up environment Variables

The next thing you need to do is setup the environment variables as shown below;

```bash 
AT_API_KEY_SECRET=Your AT Sarufi API key
AT_USERNAME=sandbox
SARUFI_API_KEY= Your Sarufi API Key
SARUFI_BOT_ID= Your Sarufi Bot ID
```

## Run the Webhook 

Once you do the above, you're now good to to start running the webhook, which you can easily do by using [uvicorn](https://www.uvicorn.org/). 

```bash
$ uvicorn app:app --reload
```

## You can then use Ngrok to expose it to the internet

Here how you link it with Ngrok, assumming your app run on port _8000_. 

```bash
$ ngrok http 8000
```

>After this, You can now just copy the HTTPS URL and then go put on your AT Portal and then you can use AT simulator to start testing your SMS based Chatbot. 


## Contribution ?

Got an idea on how to make it better or fix around this blueprint, All you need is a _pull request_. 

## Issues ?

Software are never complete by the way so incase of any issues, feel free to open one so we can fix as soon as we can. 


## Credits 

All the credit to all contributors. 