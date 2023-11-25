# activity_tracker.py
import datetime
import json

class ActivityTracker:
    def __init__(self):
        self.activities = []

    def log_activity(self, activity, category, tags=None):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.activities.append({"timestamp": timestamp, "activity": activity, "category": category, "tags": tags})

    def export_activities(self, filename="activity_data.json"):
        with open(filename, "w") as file:
            json.dump(self.activities, file)
