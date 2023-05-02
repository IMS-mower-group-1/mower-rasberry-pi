import requests

mowerId = "aBPovOQznCxzNHE0Uo97"

def start_mow_session(api_key):
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key
    }

    url = f"https://tgin13-1-q1387758.deta.app/mow-session/start-session/{mowerId}"
    response = requests.post(url, headers=headers)

    if response.status_code == 201:
        print("Mow session started successfully")
        return response.json()
    else:
        print(response.json()['error'])
        return None

def end_mow_session(api_key):
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key
    }

    url = f"https://tgin13-1-q1387758.deta.app/mow-session/end-session/{mowerId}"
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        print("Mow session ended successfully")
        return response.json()
    else:
        print(response.json()['error'])
        return None
        
def update_mower_position(api_key, xPos, yPos):
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key
    }

    url = f"https://tgin13-1-q1387758.deta.app/position/update/{mowerId}"
    response = requests.post(url, headers=headers, json={"position": { "x": xPos, "y": yPos }})

    if response.status_code == 200:
        print("Mower position updated successfully")
        return response.json()
    else:
        print(response.json()['error'])
        return None
    
def upload_avoided_collision(api_key, image_data):
    headers = {
        "Content-Type": "application/octet-stream",
        "x-api-key": api_key
    }

    url = f"https://tgin13-1-q1387758.deta.app/image/upload/{mowerId}"
    response = requests.post(url, headers=headers, data=image_data)

    if response.status_code == 200:
        print("Avoided collision uploaded successfully")
    else:
        print(response.json()['error'])
