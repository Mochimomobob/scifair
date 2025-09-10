import json
import re

class AskingQuestions:
    def __init__(self):
        pass
   
    def count_questions(self, q_file):
        file_length = len(q_file["questions"])
        return file_length

    def retrieve_query(self, q_file,i):
        instructions = q_file["format"]
        question = q_file["questions"][i]["question"]
        choices = q_file["questions"][i]["choices"]
        answer = q_file["questions"][i]["answer"]

        choices = ", ".join([f"{key}: {value}" for key, value in choices.items()])
        prompt = f"{instructions} {question} {choices}"
        return {
        "prompt": prompt,
        "answer": answer,
        "raw_question": question,
        "choices": choices
        }
    
    
    def check_final_answer(self, response: str, correct_answer: str) -> bool:
    # Use regex to find text after "final:"
        match = re.search(r"final:\s*([A-Za-z])", response, re.IGNORECASE)
        
        if not match:
            print("No final answer found in response.")
            return False
        
        final_answer = match.group(1).upper()
        correct_answer = correct_answer.upper()
        
        print(f"Model answered: {final_answer}, Correct answer: {correct_answer}")
        
        return final_answer == correct_answer

# def main():
#     api_key = "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"
#     api_url = "https://openrouter.ai/api/v1/chat/completions"
#     headers = {
#              "Authorization": f"Bearer {api_key}",
#              "Content-Type": "application/json"
#          }
#     with open('query.json', 'r') as file:
#         data = json.load(file)
#     aq = AskingQuestions()
#     file_length = aq.count_questions(data)
#     from start import CallingModels
#     fred = CallingModels(api_key, api_url, headers)

#     for i in range(file_length):
#         query = aq.retrieve_query(data, i)
#         response = fred.call_model(model_name='google/gemini-2.5-flash-lite', prompt=query)
#         print(f"Response for question {i+1}: {response}")


# if __name__ == "__main__":
#     main()