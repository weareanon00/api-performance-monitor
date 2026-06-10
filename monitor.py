import requests
import pandas as pd
from datetime import datetime

websites = [
    "https://github.com",
    "https://google.com",
    "https://openai.com"
]

results = []

for site in websites:

    try:

        response = requests.get(site)

        results.append({
            "Website": site,
            "Status Code": response.status_code,
            "Response Time": response.elapsed.total_seconds(),
            "Checked At": datetime.now()
        })

        print(f"{site} is UP")

    except:

        results.append({
            "Website": site,
            "Status Code": "DOWN",
            "Response Time": "N/A",
            "Checked At": datetime.now()
        })

        print(f"{site} is DOWN")

df = pd.DataFrame(results)

df.to_csv("api_results.csv", index=False)

print("Monitoring completed!")