import requests
import threading
import time
import datetime

# ⚠️ PASTE YOUR KEY HERE
SPO_KEY = "sk-..." 

URL = "http://localhost:4000/v1/chat/completions"
TOTAL_REQUESTS = 10  # Enough to fill the queue (since RPM is 10)
TOTAL_THREADS = 10

def send_spo_request(i):
    for j in range(TOTAL_REQUESTS):
        start_time = time.time()
        try:
            payload = {
                "model": "deepseek-r1:1.5b",
                "messages": [{"role": "user", "content": f"Extract SPO from this sentence: request number {i}"}],
                "max_tokens": 10
            }
            headers = {"Authorization": f"Bearer {SPO_KEY}", "Content-Type": "application/json"}
            
            response = requests.post(URL, json=payload, headers=headers)
            
            elapsed = time.time() - start_time
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            
            if response.status_code == 200:
                print(f"[{timestamp}] SPO Req thread : {i} #{j}: Success ({elapsed:.2f}s)")
            else:
                print(f"[{timestamp}] SPO Reqthread : {i}  #{j}: Status {response.status_code} (Queued or Limited)")
                
        except Exception as e:
            print(f"SPO thread : {i} Req #{j} Error: {e}")

if __name__ == "__main__":
    print(f"--- STARTING SPO FLOOD thread ({TOTAL_THREADS} {TOTAL_REQUESTS} requests) ---")
    print("This will fill the traffic queue...")
    
    threads = []
    for i in range(TOTAL_THREADS):
        t = threading.Thread(target=send_spo_request, args=(i,))
        threads.append(t)
        t.start()
        time.sleep(0.05) # Fire rapidly
        
    for t in threads:
        t.join()