import os
import json
import requests
import numpy as np

from dotenv import load_dotenv
load_dotenv()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)


maze = np.load('sample_maze.npy')
agent_id = os.environ.get("AGENT_ID")

# the ip below should be modified by you according to the server IP communicated with you
# students track --> 16.170.85.45
# working professionals track --> 13.49.133.141
response = requests.post(
    'http://16.170.85.45:5000/submitMaze',
    json={"agentId": agent_id, "submittedMaze": json.dumps(maze.tolist())}
)
print(response.text, response.status_code)
