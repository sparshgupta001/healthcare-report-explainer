import requests

url = "http://127.0.0.1:5000/analyze"

# Change "sample.pdf" to your actual test file name
with open("sample.pdf", "rb") as f:
    files = {"file": f}
    response = requests.post(url, files=files)

print("Status Code:", response.status_code)
print("Response:", response.json())
