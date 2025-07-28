import json
import os
import matplotlib.pyplot as plt

DATA_FILE = "progress_data.json"

# load or initialize data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        progress_data = json.load(f)
else:
    progress_data = {}

def add_daily_progress():
    date = input("Enter date (DD/MM/YY): ")
    topics = {}
    while True:
        topic_name = input("Enter topic name (or 'done' to finish): ")
        if topic_name.lower() == "done":
            break
        status = input(f"Status for {topic_name} (done/somewhat/not done): ")
        topics[topic_name] = status
    progress_data[date] = topics
    with open(DATA_FILE, "w") as f:
        json.dump(progress_data, f, indent=4)
    print(f"Progress saved for {date}!")

def analyze_week():
    topic_scores = {}
    for day, tasks in progress_data.items():
        for topic, status in tasks.items():
            score = 0
            if "done" in status.lower():
                score = 1
            elif "somewhat" in status.lower():
                score = 0.5
            else:
                score = 0
            topic_scores[topic] = topic_scores.get(topic, 0) + score
    
    # show results
    print("\nWeekly Analysis:")
    for topic, score in topic_scores.items():
        print(f"{topic}: {score} / {len(progress_data)} days")
    
    # plot
    plt.bar(topic_scores.keys(), topic_scores.values(), color="skyblue")
    plt.ylabel("Score")
    plt.title("Weekly Progress Summary")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def menu():
    while True:
        print("\n--- Progress Tracker ---")
        print("1. Add today's progress")
        print("2. Analyze weekly progress")
        print("3. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            add_daily_progress()
        elif choice == "2":
            analyze_week()
        elif choice == "3":
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()
