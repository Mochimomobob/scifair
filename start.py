import requests
import json
import copy

class CallingModels:
    def __init__(self,api_key,api_url,headers):
        self.api_key = api_key
        self.api_url = api_url
        self.headers = headers
       
    def call_model(self,model_name, prompt, messages: list = None):
        if messages == None:
            temp = [{
            "role": "user",
            "content": prompt
            },]
        else:
            temp = copy.deepcopy(messages)
            temp.append({"role": "user", "content": prompt})
        data = {
            "model": model_name,
            "messages": temp,
            "max_tokens": 100,
        }
        response = requests.post(url=self.api_url, headers=self.headers, json=data)
        response_json = response.json()
        assistant_reply = response_json['choices'][0]['message']['content']
        temp.append({"role": "assistant", "content": assistant_reply})

        return temp
    
    def get_answer(self, response : json): #extract answer from json and return it
        answer_dict = response.json()
        return answer_dict['choices'][0]['message']['content'] #How to get any answer from json?
    
# def main():
#     api_key = "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"
#     api_url = "https://openrouter.ai/api/v1/chat/completions"
#     headers = {
#              "Authorization": f"Bearer {api_key}",
#              "Content-Type": "application/json"
#          }
#     fred = CallingModels(api_key, api_url, headers)
#     response0 = fred.call_model(model_name= 'google/gemini-2.5-flash-lite', 
#                                prompt="What is the capital of France?")
#     response1 = fred.call_model('google/gemini-2.5-flash-lite', "Who's the president of that country?", response0)
#     print(response0)
#     print('-=-=-=-=-')
#     print(response1)
#     # output = response.json()
#     # with open("data.json", "w") as outfile:
#     #     json.dump(output, outfile, indent=2)
#     # print(fred.get_answer(response))
#     # print(fred.get_answer(response1))


# if __name__ == "__main__":
#     main()

