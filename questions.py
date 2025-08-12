import json

# class TaskQuery:
#     def __init__ (self):

def retrieve_query(i):
    with open('query.json', 'r') as file:
        data = json.load(file)
    instructions = data["format"]
    question = data["questions"][i]["question"]
    choices = data["questions"][i]["choices"]

    choices = ", ".join([f"{key}: {value}" for key, value in choices.items()])
    prompt = f"{instructions} {question} {choices}"
    return prompt
    
def main():
    from start import CallingModels
    api_key = "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"
    api_url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
             "Authorization": f"Bearer {api_key}",
             "Content-Type": "application/json"
         }
    query = retrieve_query(0)
    fred = CallingModels(api_key, api_url, headers)
    response = fred.call_model(model_name= 'google/gemini-2.5-flash-lite', prompt= query)
    print(response)

if __name__ == "__main__":
    main()