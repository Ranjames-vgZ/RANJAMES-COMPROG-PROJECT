# Student Record Management System

A comprehensive student record management system built with Python as a course project for
Computer Programming 2 (AY 2025–2026 2nd Sem) under Ms. Hasmin Cuevas at COMTEQ Computer and
Business College.

## Features (Part 1)
- Add new students with validation
- View all students
- Search students by ID
- Update student information
- Delete students
- Modular code organization

## Project Structure

student_record_system/
├── venv/                   # Virtual environment
├── src/
│   ├── utils/              # Utility modules
│   │   ├── validators.py   # Input validation
│   │   ├── formatters.py   # Display formatting
│   │   └── helpers.py      # Helper functions
│   ├── data/
│   │   └── student_data.py # Data management
│   └── main.py             # Main program
├── requirements.txt        # Dependencies
└── README.md               # This file

## Setup Instructions

1. Create virtual environment:
```bash
    python -m venv venv
```

2. Activate virtual environment:
-Windows:
```bash
    venv\Scripts\activate
```
-Mac/Linux:
```bash
    source venv/bin/activate
```
3.Install dependencies:
```bash
pip install -r requirements.txt
```