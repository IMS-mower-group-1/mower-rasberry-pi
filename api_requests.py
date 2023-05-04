import requests
from config import *

def start_mow_session():
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key
    }

    url = f"https://tgin13-1-q1387758.deta.app/mow-session/start-session/{mowerId}"
    response = requests.post(url, headers=headers)

    if response.status_code == 201:
        print("Mow session started successfully")
        return response.status_code
    else:
        return response.status_code

def end_mow_session():
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key
    }

    url = f"https://tgin13-1-q1387758.deta.app/mow-session/end-session/{mowerId}"
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        print("Mow session ended successfully")
        return response.status_code
    else:
        return response.status_code
        
def update_mower_position(xPos, yPos):
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key
    }

    url = f"https://tgin13-1-q1387758.deta.app/position/update/{mowerId}"
    response = requests.post(url, headers=headers, json={"position": { "x": xPos, "y": yPos }})

    if response.status_code == 200:
        print("Mower position updated successfully")
        return response.status_code
    else:
        print("Mower position not updated")
        return response.status_code
    
def upload_avoided_collision(image_data):
    headers = {
        "Content-Type": "application/octet-stream",
        "x-api-key": api_key
    }

    url = f"https://tgin13-1-q1387758.deta.app/image/upload/{mowerId}"
    response = requests.post(url, headers=headers, data=image_data)

    if response.status_code == 200:
        print("Avoided collision uploaded successfully")
        return response.status_code
    else:
        return response.status_code
        
def active_session_exists():
    headers = {
        "Content-Type": "application/octet-stream",
        "x-api-key": api_key
    }
    url = f"https://tgin13-1-q1387758.deta.app/mow-session/mower/{mowerId}/active"
    response = requests.get(url, headers=headers)
    
    if response.json() != None:
        print("Active mow session exists")
        return True
    else:
        print("No active mow session found or an error occured")
        return False
