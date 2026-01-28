# ollama-proxy-litellm

# How to Create a LiteLLM Key with Priority Reservation

This guide outlines the steps to generate a new API key in the LiteLLM UI and configure it with specific priority reservations.

## Prerequisites
* Access to the LiteLLM Admin UI.
* Admin privileges to create and edit Virtual Keys.

---

## Step-by-Step Instructions

### 1. Access the LiteLLM UI
Navigate to your LiteLLM dashboard. Locate and click on the **"Virtual Keys"** (or **"Keys"**) section in the sidebar.

### 2. Add a New Key
Click the **"+ Create New Key"** button (usually located in the top right corner of the table).

### 3. Configure Basic Settings
* **Key Name:** Enter a descriptive name (e.g., `production-app-key`).
* **Models:** Select specific models if needed, or leave blank to allow all.
* **Budget (Optional):** Set a max budget if required.

### 4. Set Metadata & Priority Reservation
To enforce the priority reservation, you must add the configuration to the **Metadata** field.

1.  Locate the **Metadata** input field.
2.  Paste the following JSON object exactly as shown:

```json
{
  "priority": "realtime" // avaliable are realtime, realtime-dev, extract-spo
}
```