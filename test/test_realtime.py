import requests
import time
import datetime

# ⚠️ PASTE YOUR KEY HERE
REALTIME_KEY = "sk-..." 

URL = "http://localhost:4000/v1/chat/completions"

def send_realtime_request():
    print("\n🚀 SENDING REALTIME REQUEST (High Priority)...")
    start_time = time.time()
    
    payload = {
        "model": "deepseek-r1:1.5b",
        "messages": [{"role": "user", "content": "What is the capital of France?"}],
        "max_tokens": 10
    }
    headers = {"Authorization": f"Bearer {REALTIME_KEY}", "Content-Type": "application/json"}
    
    try:
        response = requests.post(URL, json=payload, headers=headers)
        elapsed = time.time() - start_time
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        
        if response.status_code == 200:
            print(f"✅ [{timestamp}] REALTIME SUCCESS!")
            print(f"⏱️  Time taken: {elapsed:.2f} seconds")
            print(f"📄 Response: {response.json()['choices'][0]['message']['content']}")
        else:
            print(f"❌ Failed: {response.status_code} - {response.text}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_realtime_request()