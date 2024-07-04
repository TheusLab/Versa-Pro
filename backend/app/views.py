# backend/app/views.py
from flask import request, jsonify
from . import app, db
from .models import Project

@app.route('/api/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    return jsonify([project.to_dict() for project in projects])
