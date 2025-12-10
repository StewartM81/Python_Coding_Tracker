# Coding logger

A simple coding session logger CLI application built in Python using SQLite3 and PeeWee ORM.

---

## Purpose

This project is a learning exercise to practice working with SQLite databases and ORM in Python.  
It demonstrates creating, reading, updating, and deleting records (CRUD) in a local SQLite database through a command-line interface.
A databaseController class has been made, this would allow the use of other databases with the whole program needing to be rewritten

---

## Features

- Create, view, update, and delete coding session records
- Stores user name, coding language, start time, end time and end time of coding session
- Basic input validation class
- DataBase controller class
- Controller class for interacing main program with database controller
- Simple menu-driven CLI 

---

## Getting Started

### Prerequisites

- Python 3.10 or newer (for `match-case` support)
- External Library required for PeeWee ORM (included in requirements.txt)

### How to Run

1. Clone or download the repository

```bash
   git clone https://github.com/StewartM81/Python_Coding_Tracker.git
   cd your-repo-name 
```

2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
```

3. Install dependenceies from requirements.txt

```bash
pip install -r requirements.txt
```

4. Run the script:

```bash
python main.py
```

## Usage

After running the app, you’ll see a menu with options to:

View existing sessions

Add a new coding session

Update a session

Delete a session

Exit the program

Follow the prompts to input details like username, programming language, and start/end times.

## Project Structure

main.py - Entry point and CLI interface

database.py - Database abstraction layer using PeeWee ORM

input.py - Helper for validating user input

controller.py - Class responsible for processing user commands and interacting with the database layer

requirements.txt — List of Python dependencies

