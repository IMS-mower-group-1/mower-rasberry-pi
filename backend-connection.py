import requests

# Set the API endpoint
url = 'https://example.com/api/data'

# Set the data to be sent in the POST request

def sendMowSession(id,start,end,path,collisionAvoidance):
    data = {
        'id': id,
        'start': start,
        'end': end,
        'path' : path,
        'collisionAvoidance': collisionAvoidance
    }
    # Send the POST request with the data
    response = requests.post(url, data=data)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print('POST request successful!')
    else:
        print(f'Error: {response.status_code} - {response.reason}')




