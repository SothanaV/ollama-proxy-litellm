import requests
import json

# Configuration
API_URL = "http://localhost:4000/key/generate"
MASTER_KEY = "sk-..." # Must match your docker-compose LITELLM_MASTER_KEY

def generate_key(priority_level):
    headers = {
        "Authorization": f"Bearer {MASTER_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "models": ["deepseek-r1:1.5b"],
        "metadata": {
            "priority": priority_level,
            "test_label": f"test-{priority_level}"
        },
        "duration": "1h" # Temporary key for testing
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        key_info = response.json()
        return key_info['key']
    except Exception as e:
        print(f"Error creating key: {e}")
        return None

if __name__ == "__main__":
    print("--- Generating Test Keys ---")
    
    # 1. Create Realtime Key (High Priority)
    realtime_key = generate_key("realtime")
    print(f"\n✅ REALTIME KEY (Priority 3):")
    print(f"Key: {realtime_key}")
    
    # 2. Create SPO Key (Low Priority)
    spo_key = generate_key("extract-spo")
    print(f"\n✅ EXTRACT SPO KEY (Priority 1):")
    print(f"Key: {spo_key}")

    print("\n--- SAVE THESE KEYS for the next scripts ---")