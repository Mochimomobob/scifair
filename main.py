import json
import time
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
    models = ['google/gemini-2.5-flash-lite', 'openai/gpt-oss-20b:free']

    with open('query.json', 'r') as file:
        data = json.load(file)
    aq = AskingQuestions()
    file_length = aq.count_questions(data)
    results = {model: {"correct": 0, "total": file_length} for model in models}
    for model in models:
        model_start = time.time()

        for i in range(file_length):
            query = aq.retrieve_query(data, i)
            response = fred.call_model(model_name=model, prompt=query)
            with open("response.json", "w") as outfile:
                json.dump(response, outfile, indent=2)
            answer = aq.retrieve_answer(data, i)
            if response[1]['content'] == answer:
                results[model]["correct"] += 1
            # else:
            #     print(f"Question {i+1} for {model} was answered incorrectly.")
            print(f"Response from {model}: {response}")
        model_end = time.time()
        total_elapsed = model_end - model_start
        print(f"Total time for {model}: {total_elapsed:.2f}s")
    accuracy = {model: results[model]["correct"] / results[model]["total"] * 100 for model in models}
    print(accuracy)
    
        

if __name__ == "__main__":
    main()

