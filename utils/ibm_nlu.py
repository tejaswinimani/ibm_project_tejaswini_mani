from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, ConceptsOptions, KeywordsOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

API_KEY = "your_api_key_here"
SERVICE_URL = "your_service_url_here"

def analyze_text_ibm(text):
    authenticator = IAMAuthenticator(API_KEY)
    nlu = NaturalLanguageUnderstandingV1(
        version='2021-08-01',
        authenticator=authenticator
    )
    nlu.set_service_url(SERVICE_URL)

    try:
        response = nlu.analyze(
            text=text,
            features=Features(
                concepts=ConceptsOptions(limit=5),
                keywords=KeywordsOptions(limit=5)
            )
        ).get_result()
        return response
    except Exception as e:
        return {"error": str(e)}


{
  "apikey": "awEnZNlvTpJ7nFuEuQIu5ExNdLE3eyfOYeNpOgwUueuC",
  "iam_apikey_description": "Auto-generated for key crn:v1:bluemix:public:natural-language-understanding:eu-gb:a/8b13bcfbeb3c436a8bbb563d93f695fa:0fdd6f74-7c55-4e83-af40-0fd2c2d079f0:resource-key:437735de-515c-45d6-bac7-9a8b5d450de6",
  "iam_apikey_id": "ApiKey-f68b9cc7-e9ca-4f33-afd2-d2bcba7d3ab7",
  "iam_apikey_name": "Auto-generated service credentials",
  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Manager",
  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/8b13bcfbeb3c436a8bbb563d93f695fa::serviceid:ServiceId-6bd25afc-2496-45a8-9f2f-2999dab5ec7b",
  "url": "https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/0fdd6f74-7c55-4e83-af40-0fd2c2d079f0"
}
