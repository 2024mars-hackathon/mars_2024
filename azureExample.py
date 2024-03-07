import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
from azure.search.documents import SearchClient
from azure.storage.blob import BlobServiceClient

key=""
endpoint="https://textanalysticsskillextraction.cognitiveservices.azure.com/"
client=TextAnalyticsClient(endpoint=endpoint,credential = AzureKeyCredential(key))

document=[
"""
Review diagnostics and assess the functionality and efficiency of systems
Implement security measures
Monitor security certificates and company compliance of requirements
Offer technical support to company staff and troubleshoot computer problems
Install and update company software and hardware as needed
Anticipate and report the cost of replacing or updating computer items
John Doe
john.doe@email.com
AI 
ML 
Java developer
"""]

result=client.recognize_entities(document)

for idx,review in enumerate(result): 
    for entity in review.entities:
        print(f"text: {entity.text}, category: {entity.category}, subcategory: {entity.subcategory}")

service_endpoint = "https://calazuresearchservice.search.windows.net"
index_name = "resume-index2"
key = ""


search_client = SearchClient(service_endpoint, index_name, AzureKeyCredential(key))

results = search_client.search(search_text="HTML")

for result in results:
    #print("{}: {})".format(result["content"], result["people"]))
    print("{})".format(result["skills"]))