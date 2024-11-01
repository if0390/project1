# Advanced Python Calculator

Created as a midterm project in the Building Web Applications course, this advanced Python-based calculator application illustrates the professional software development with regards to structuring, data management with Pandas, and a REPL to allow real-time user interaction.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Usage Guide](#usage-guide)
- [Demonstration Video](#demonstration-video)

## Project Overview
The Advanced Python Calculator is equipped with support for simple arithmetic, history-tracking, and plugins loaded into a REPL interface. This project emphasizes fairly clean code, modular architecture, and an almost professional approach to software development. 

## Features
### Command-Line Interface (REPL)
- **Core Operations:** Supports standard arithmetic functions, including addition, subtraction, multiplication, and division.
- **History Management:** Users can save, load, clear, and delete calculation history, managed by Pandas.

### History Management with Pandas
Calculation history is efficiently managed using Pandas, allowing users to:
- Save and load history records to/from CSV files.
- Clear or delete history as needed.

### Professional Logging Practices
The project captures great detail when it comes to logging the operations of the application, error handling, etc. Log messages are divided, as per their seriousness, into categories denoted by probable names for them: INFO, WARNING, and ERROR. The severity level and output destinations are specified as environmental variables.

## Setup Instructions
To set up and run the application, follow these steps:
1. **Clone the Repository:** 
    ```bash
    git clone git@github.com:if0390/project1.git
    ```
2. **Install Dependencies:** Ensure you have Python installed and then run:
    ```bash
    pip install -r requirements.txt
    ```
3. **Set Up Environment Variables:** Use the `.env` file provided in the repository to configure logging and other settings.

## Usage Guide
1. **Running the Calculator:**
    Launch the REPL by running:
    ```bash
    python main.py
    ```
2. **Available Commands:** Type `Menu` in the REPL to view all available commands, including core operations, history management, and additional plugin commands.
3. **Example Commands:**
    - **Add Numbers:** `Add 5 8`
    - **View History:** `History`
    - **CLear History:** `Clear`


## Demonstration Video
A [3-5 minute video demonstration](https://drive.google.com/file/d/1n4IJi9JYTemU_H33DP_iZC_xHdedbOOX/view?usp=sharing) of the calculator’s key functionalities is provided to guide users through its usage.