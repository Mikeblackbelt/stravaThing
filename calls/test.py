import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import os
import dotenv

dotenv.load_dotenv()
    
# Configure OAuth2 access token for authorization: strava_oauth
swagger_client.configuration.access_token = os.getenv("token")

# create an instance of the API class
api_instance = swagger_client.AthletesApi()

try: 
    # Get Authenticated Athlete
    api_response = api_instance.getLoggedInAthlete()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AthletesApi->getLoggedInAthlete: %s\n" % e)