import requests
import json
import base64
from cryptography.fernet import Fernet

key = Fernet.generate_key()
encrypt_type = Fernet(key)
data1 = input("Do you want to open a connection? [y/n]> ")
if data1.lower() == "y":
    with open("~data/key.txt", "w") as f:
        f.write(str(key))
        f.close()


    githubAPIURL = "https://api.github.com/repos/no1638/IMCchatAppENCRYPTED/contents/~data/key.txt"
    # Replace "bracketcounters" with your username, replace "test-repo" with your repository name and replace "new-image.png" with the filename you want to upload from local to GitHub.

    # Paste your API token here
    githubToken = "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"
    response = requests.get(githubAPIURL)
    response = response.json()
    sha_value = response["sha"]
    print(sha_value)
    headers = {
        "Authorization": f'''Bearer {githubToken}''',
        "Accept": "application/vnd.github+json"
    }
    with open("~data/key.txt", "rb") as f:
        # Encoding "my-local-image.jpg" to base64 format
        encodedData = base64.b64encode(f.read())

        headers = {
            "Authorization": f'''Bearer {githubToken}''',
            "Content-type": "application/vnd.github+json",
            "sha": f"{sha_value}"
        }
        data = {
            "message": "EMERGENCY USE ONLY", # Put your commit message here.
            "content": encodedData.decode("utf-8"),
            "sha": f"{sha_value}"
        }

        r = requests.put(githubAPIURL, headers=headers, json=data)
        #print(r.text) # Printing the response
        f.close()
    
    
    
    
    
    
    with open("~data/message.txt", "w") as f:
        f.write("WELCOME")
        f.close()


    githubAPIURL = "https://api.github.com/repos/no1638/IMCchatAppENCRYPTED/contents/~data/message.txt"
    # Replace "bracketcounters" with your username, replace "test-repo" with your repository name and replace "new-image.png" with the filename you want to upload from local to GitHub.

    # Paste your API token here
    githubToken = "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"
    response = requests.get(githubAPIURL)
    response = response.json()
    sha_value = response["sha"]
    print(sha_value)
    headers = {
        "Authorization": f'''Bearer {githubToken}''',
        "Accept": "application/vnd.github+json"
    }
    with open("~data/message.txt", "rb") as f:
        # Encoding "my-local-image.jpg" to base64 format
        encodedData = base64.b64encode(f.read())

        headers = {
            "Authorization": f'''Bearer {githubToken}''',
            "Content-type": "application/vnd.github+json",
            "sha": f"{sha_value}"
        }
        data = {
            "message": "EMERGENCY USE ONLY", # Put your commit message here.
            "content": encodedData.decode("utf-8"),
            "sha": f"{sha_value}"
        }

        r = requests.put(githubAPIURL, headers=headers, json=data)
        #print(r.text) # Printing the response
        f.close()
    
    
input("press enter when connection is terminated...")
with open("~data/key.txt", "w") as f:
    f.write(str(" "))
    f.close()


githubAPIURL = "https://api.github.com/repos/no1638/IMCchatAppENCRYPTED/contents/~data/key.txt"
# Replace "bracketcounters" with your username, replace "test-repo" with your repository name and replace "new-image.png" with the filename you want to upload from local to GitHub.

# Paste your API token here
githubToken = "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"
response = requests.get(githubAPIURL)
response = response.json()
sha_value = response["sha"]
print(sha_value)
headers = {
    "Authorization": f'''Bearer {githubToken}''',
    "Accept": "application/vnd.github+json"
}
with open("~data/key.txt", "rb") as f:
    # Encoding "my-local-image.jpg" to base64 format
    encodedData = base64.b64encode(f.read())

    headers = {
        "Authorization": f'''Bearer {githubToken}''',
        "Content-type": "application/vnd.github+json",
        "sha": f"{sha_value}"
    }
    data = {
        "message": "EMERGENCY USE ONLY", # Put your commit message here.
        "content": encodedData.decode("utf-8"),
        "sha": f"{sha_value}"
    }

    r = requests.put(githubAPIURL, headers=headers, json=data)
    #print(r.text) # Printing the response
    f.close()
