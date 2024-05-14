import requests

# API endpoint URL
url = "https://random-word-api.herokuapp.com/word"

try:
    # Send a GET request to the API endpoint
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the JSON data from the response
        data = response.json()
        
        # The response is a list, so we extract the first element (random word)
        random_word = data[0]

        print("Random word:", random_word)
    else:
        print("Failed to fetch data. Status code:", response.status_code)

except Exception as e:
    print("An error occurred:", e)
