import requests
import json

def query_ollama(user_prompt):
    url = "http://localhost:11434/api/generate"
    
    payload = {
        "prompt": user_prompt,
        "model": 'qwen2.5:0.5b' , 
        "sys_prompt":"answer only questions related to india"
    }
    try:
        response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
        
        if response.status_code == 200:
            response_text = response.text
            lines = response_text.strip().split("\n")
            full_response = "".join(json.loads(line)["response"] for line in lines)
            print(full_response)
    except Exception as e:
        print(str(e))
query_ollama("onion is heat")
