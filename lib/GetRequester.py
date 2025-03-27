
# A tool that helps Python fetch data from websites.import requests
import requests

# A tool to turn website data into something we can read (like lists and dictionaries)
import json




class GetRequester:
    def __init__(self, url):
        self.url = url



    def get_response_body(self):
        response = requests.get(self.url)#It grabs the data and stores it in response
        return response.content# returns the raw data

#the function below turns the raw data into something we can read easily (a Python list or dictionary).

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)




if __name__ == "__main__":
    url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    requester = GetRequester(url)#It creates a GetRequester robot with a real website link.
    data = requester.load_json()#It fetches and converts the data into a readable format
    print(data)#It prints the data to the screen

