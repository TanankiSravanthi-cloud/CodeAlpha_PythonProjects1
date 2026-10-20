# CodeAlpha Python Programming Internship Projects

This repository contains four beginner-friendly Python projects based on the task list:
1. Hangman Game
2. Stock Portfolio Tracker
3. Task Automation Scripts
4. Basic Rule-Based Chatbot

## Requirements
- Python 3.9 or newer
- Tasks 1, 2 and 4 use only Python's standard library.
- Task 3 uses only Python's standard library for the included file automation and email extraction options.
- The webpage-title option in Task 3 requires `requests` and `beautifulsoup4`.

Install optional dependencies for webpage-title scraping:
```bash
python -m pip install requests beautifulsoup4
```

## Run a project
Open a terminal in this repository folder and run one of:
```bash
python hangman_game.py
python stock_portfolio_tracker.py
python task_automation.py
python basic_chatbot.py
```

## Task 3 options
Run `python task_automation.py`, then choose:
1. Move `.jpg` files from one folder to another
2. Extract email addresses from a text file
3. Save the title of a webpage (requires optional packages)

Use these scripts only on files and websites you are authorized to access. Make a backup before moving files.

## GitHub upload
1. Create a new GitHub repository named `CodeAlpha_PythonProjects` (or the exact name required by your internship).
2. Do not initialize it with a README if you plan to push this folder as-is.
3. Open a terminal in this project folder.
4. Run:
```bash
git init
git add .
git commit -m "Add CodeAlpha Python internship projects"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/CodeAlpha_PythonProjects.git
git push -u origin main
```
Replace `YOUR-USERNAME` with your GitHub username and use the repository URL shown by GitHub.

## Before submitting
- Run each script and test its main features.
- Upload the repository link using the official submission form shared by CodeAlpha.
- Follow your internship instructions for LinkedIn posts and video explanation.
- Submit only work you understand and can explain. Customize and test these starter projects before submission.
