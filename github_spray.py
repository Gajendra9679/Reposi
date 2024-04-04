import os
import subprocess
from datetime import datetime, timedelta

# Set start date to one year ago
start_date = datetime.today() - timedelta(days=365)

# Create or move into the repo
if not os.path.exists(".git"):
    subprocess.run(["git", "init"])

# Generate commits for each day in the past year
for i in range(365):
    date = start_date + timedelta(days=i)
    with open("commit.txt", "a") as file:
        file.write(f"Commit on {date.strftime('%Y-%m-%d')}\n")

    subprocess.run(["git", "add", "commit.txt"])
    subprocess.run(["git", "commit", "--date", date.strftime("%Y-%m-%dT12:00:00"), "-m", f"Commit on {date.strftime('%Y-%m-%d')}"])

# Push all commits to GitHub
subprocess.run(["git", "branch", "-M", "main"])
subprocess.run(["git", "remote", "add", "origin", "https://github.com/Gajendra9679/Repo.git"])
subprocess.run(["git", "push", "-u", "origin", "main"])
