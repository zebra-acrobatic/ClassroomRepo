# Classroom Repository

Welcome to the Classroom Repository! This repository is designed for teaching version control and collaborative coding in a classroom setting.

## Getting Started

Follow these steps to get started with the exercises:

### 1. Fork the Repository

- Click on the "Fork" button in the top right corner of this repository to create your own copy.

### 2. Clone Your Fork

Clone your forked repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/ClassroomRepo.git
```
### 3. Make changes

Inside the cloned repository, make changes to the sample_code.py file or add new files (try to use the command line where possible).

Make sure you use Git to confirm your changes:
```bash
git status
```

### 4. Commit and Push Changes
Commit your changes and push them to your forked repository:

```bash
git add .
```
```bash
git commit -m "Describe your changes here"
```
```bash
git push origin main
```
### 5. Create a Pull Request
On the GitHub page of your forked repository, click on the "New Pull Request" button.
Provide a meaningful title and description for your pull request.
Click "Create Pull Request."

### Conflicts
In some exercises, conflicts may intentionally be introduced. If conflicts occur, follow these steps:
1. Pull changes from the main repository:
```bash
git pull https://github.com/your-username/ClassroomRepo.git main
```
2. Resolve conflicts locally.
3. Commit and push the changes.
