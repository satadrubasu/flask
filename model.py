"""
model.py
  just a simulator to db , which loads records from a db.
  In this case a flat json file : flashcards_db.json
"""

import json

def load_db():
    with open("flashcards_db.json") as f:
        return json.load(f)

db = load_db()