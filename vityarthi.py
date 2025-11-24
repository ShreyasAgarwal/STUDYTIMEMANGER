import json
import datetime
import os

class StudyManager:
    def __init__(self, filename="study_data.json"):
        self.filename = filename
        self.subjects = self.load_data()
    
    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {}
    
    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.subjects, file, indent=4)
    
    def add_study_session(self, subject, duration, topic=""):
        today = str(datetime.date.today())
        
        if subject not in self.subjects:
            self.subjects[subject] = {}
        
        if today not in self.subjects[subject]:
            self.subjects[subject][today] = []
        
        session = {
            "duration": duration,
            "topic": topic,
            "timestamp": datetime.datetime.now().strftime("%H:%M:%S")
        }
        
        self.subjects[subject][today].append(session)
        self.save_data()
    
    def view_study_sessions(self, subject=None):
        if not self.subjects:
            print("No study sessions recorded yet.")
            return
        
        if subject:
            if subject in self.subjects:
                print(f"\nStudy sessions for {subject}:")
                for date, sessions in self.subjects[subject].items():
                    print(f"  {date}:")
                    for session in sessions:
                        print(f"    - {session['duration']} min on '{session['topic']}' at {session['timestamp']}")
            else:
                print(f"No sessions found for {subject}")
        else:
            print("\nAll study sessions:")
            for subject_name, dates in self.subjects.items():
                total_time = 0
                for date_sessions in dates.values():
                    for session in date_sessions:
                        total_time += session['duration']
                print(f"{subject_name}: {total_time} total minutes")
    
    def get_today_stats(self):
        today = str(datetime.date.today())
        total_today = 0
        subjects_today = []
        
        for subject, dates in self.subjects.items():
            if today in dates:
                day_total = sum(session['duration'] for session in dates[today])
                total_today += day_total
                subjects_today.append((subject, day_total))
        
        print(f"\nToday's Study Summary ({today}):")
        print(f"Total study time: {total_today} minutes")
        for subject, time in subjects_today:
            print(f"  {subject}: {time} minutes")
    
    def get_weekly_report(self):
        today = datetime.date.today()
        week_ago = today - datetime.timedelta(days=7)
        weekly_data = {}
        
        for subject, dates in self.subjects.items():
            for date_str, sessions in dates.items():
                session_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                if week_ago <= session_date <= today:
                    day_total = sum(session['duration'] for session in sessions)
                    if subject not in weekly_data:
                        weekly_data[subject] = 0
                    weekly_data[subject] += day_total
        
        print("\nWeekly Study Report:")
        if weekly_data:
            for subject, total_time in weekly_data.items():
                print(f"  {subject}: {total_time} minutes")
        else:
            print("  No study sessions in the past week")

def main():
    manager = StudyManager()
    
    while True:
        print("\nStudy Time Manager")
        print("1. Add study session")
        print("2. View study sessions")
        print("3. Today's statistics")
        print("4. Weekly report")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            subject = input("Enter subject name: ")
            try:
                duration = int(input("Enter study duration (minutes): "))
                topic = input("Enter topic studied: ")
                manager.add_study_session(subject, duration, topic)
                print("Study session added successfully!")
            except ValueError:
                print("Please enter a valid number for duration.")
        
        elif choice == '2':
            subject = input("Enter subject name (or press enter for all): ")
            if subject.strip():
                manager.view_study_sessions(subject)
            else:
                manager.view_study_sessions()
        
        elif choice == '3':
            manager.get_today_stats()
        
        elif choice == '4':
            manager.get_weekly_report()
        
        elif choice == '5':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()