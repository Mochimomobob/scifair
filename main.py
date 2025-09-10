import json
import re
from start import CallingModels
from questions import AskingQuestions

def main():
    api_key = "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"
    api_url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
             "Authorization": f"Bearer {api_key}",
             "Content-Type": "application/json"
         }
    fred = CallingModels(api_key, api_url, headers)
    models = ['google/gemini-2.5-flash-lite', 'deepseek/deepseek-chat-v3.1:free']

    with open('query.json', 'r') as file:
        data = json.load(file)

    aq = AskingQuestions()
    file_length = aq.count_questions(data)
    accuracy = {}

    for model in models:
        correct_count = 0

        for i in range(file_length):
            query = aq.retrieve_query(data, i)
            response = fred.call_model(model_name=model, prompt=query['prompt'])

            correct_count += int(aq.check_final_answer(response[-1]['content'], query["answer"]))

            # with open("response.json", "w") as outfile:
            #     json.dump(response, outfile, indent=2)
            
            print(f"Response from {model}: {response}")
        accuracy[model] = correct_count / file_length * 100

    print(accuracy)
    
        

if __name__ == "__main__":
    main()

