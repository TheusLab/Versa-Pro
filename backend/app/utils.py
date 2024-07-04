# backend/app/utils.py
import os
import json

def save_project(project_data):
    with open(f'projects/{project_data["name"]}.vpp', 'w') as f:
        json.dump(project_data, f)
