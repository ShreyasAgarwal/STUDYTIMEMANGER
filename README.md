Study Time Manager
A Python application to help students track and manage their study time effectively.

Features
Add Study Sessions: Record study sessions with subject, duration, and topic

View Study History: Browse all study sessions or filter by subject

Daily Statistics: Get a summary of today's study progress

Weekly Reports: View study patterns over the past 7 days

Data Persistence: All data is automatically saved to a JSON file

Installation
Ensure you have Python 3.6 or higher installed

No additional packages required - uses only Python standard library

Usage
Run the program:

bash
python study_manager.py
Main Menu Options
Add Study Session

Enter subject name (e.g., "Mathematics", "Physics")

Enter study duration in minutes

Enter topic studied (optional)

View Study Sessions

View all subjects with total study time

Or enter a specific subject to see detailed sessions

Today's Statistics

Shows total study time for today

Breakdown by subject

Weekly Report

Summary of study time for each subject over the past 7 days

Exit

Safely exit the application

Data Storage
All study data is stored in study_data.json in the same directory. The file structure includes:

Subjects as top-level keys

Dates as nested keys

Individual sessions with duration, topic, and timestamp

Example Session Data
json
{
    "Mathematics": {
        "2024-01-15": [
            {
                "duration": 120,
                "topic": "Calculus",
                "timestamp": "14:30:00"
            }
        ]
    }
}
Benefits for Students
Track study habits and time allocation

Identify which subjects need more attention

Monitor daily and weekly progress

Maintain motivation through visible progress tracking

Technical Details
Built with Python standard library

Uses JSON for data storage

Implements object-oriented design with StudyManager class

Handles date/time operations with datetime module

Includes error handling for user input

Perfect for AB Tech students and anyone looking to improve their study organization and time management skills!

