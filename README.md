# Python Crash Course — Learning Journey & Projects

A structured collection of Python exercises, practice programs, and projects developed while working through *Python Crash Course* by Eric Matthes. This repository documents my progression from Python fundamentals to object-oriented programming, testing, data visualization, game development, and web development.

The goal is to build a strong foundation in Python through consistent practice, hands-on implementation, debugging, and project development.

## Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Topics Covered](#topics-covered)
- [Projects](#projects)
- [Technologies and Tools](#technologies-and-tools)
- [Getting Started](#getting-started)
- [Running the Code](#running-the-code)
- [Development Workflow](#development-workflow)
- [Learning Objectives](#learning-objectives)
- [Future Improvements](#future-improvements)

## Overview

This repository contains my solutions, exercises, experiments, and projects developed while studying Python using *Python Crash Course*.

Rather than treating the book as a purely theoretical resource, I use the exercises and projects to practise writing, running, debugging, testing, and organizing Python code.

The repository is organized into two main sections:

1. **Chapter exercises:** Focused practice covering Python syntax, data structures, functions, classes, file handling, and testing.
2. **Projects:** Practical applications of Python in data visualization, game development, and web development.

The code represents an ongoing learning process. As I revise previous chapters and complete additional projects, I continue updating the repository.

## Repository Structure

```text
Crash-Course/
│
├── Chapter_2-Variables/
├── Chapter_3-Lists/
├── Chapter_4-Working_on_lists/
├── Chapter_5-If_statements/
├── Chapter_6-Dictionaries/
├── Chapter_7-User_Input_&_while_loops/
├── Chapter_8-Functions/
├── Chapter_9-Classes/
├── Chapter_10-Files_&_exceptions/
├── Chapter_11-Testing_your_code/
│
├── Projects/
│   │
│   ├── Data_Visualization/
│   │   ├── Downloading_Data/
│   │   ├── Generating_Data/
│   │   └── Working_with_APIs/
│   │
│   ├── Game_Development/
│   │   └── Alien_Invasion/
│   │
│   └── Web_Development/
│       ├── learning_log/
│       └── spec.txt
│
├── hello_world.py
├── .gitignore
└── README.md
```

*Note: This is a guide to the repository's current organization. Individual project directories may contain additional files, images, configuration files, and subdirectories.*

## Topics Covered

### 1. Python Fundamentals

**Variables and basic data types**

- Variables and assignment
- Strings and string manipulation
- Numbers and basic arithmetic
- Naming conventions and readable code

**Lists**

- Creating and accessing lists
- Indexing and slicing
- Modifying lists
- Sorting and organizing data
- Iteration and list operations

**Control flow**

- Conditional statements
- `if`, `elif`, and `else`
- Boolean expressions
- User input
- `while` loops and repeated execution

**Dictionaries**

- Key-value pairs
- Accessing and modifying dictionary entries
- Iterating through dictionaries
- Representing structured information

### 2. Functions and Code Organization

- Defining and calling functions
- Parameters and return values
- Positional and keyword arguments
- Working with lists and dictionaries in functions
- Organizing reusable functionality

### 3. Object-Oriented Programming

- Defining classes and creating objects
- Attributes and methods
- Constructors and instance initialization
- Inheritance and code reuse
- Modeling real-world entities in Python

### 4. Files, Exceptions, and Testing

- Reading and writing files
- Handling file paths and file operations
- Working with exceptions
- Managing errors and unexpected input
- Writing tests for functions and classes
- Improving code reliability through testing

### 5. Applied Python Development

The project directories extend the chapter exercises into practical applications involving data, graphical games, APIs, and web applications.

## Projects

### Data Visualization

Location: `Projects/Data_Visualization/`

This section contains exercises and projects involving data generation, downloading datasets, and interacting with APIs.

**Subdirectories**

- `Downloading_Data/` — exercises involving obtaining and working with data.
- `Generating_Data/` — exercises involving the generation of data for analysis and visualization.
- `Working_with_APIs/` — exercises involving APIs and retrieving information from external services.

These projects provide practical experience with data acquisition, data representation, and the Python tools used in data-oriented applications.

### Game Development — Alien Invasion

Location: `Projects/Game_Development/Alien_Invasion/`

Alien Invasion is a Python game project built while studying game development concepts.

The current project contains modules including:

- `alien_invasion.py` — the main game entry point.
- `alien.py` — alien-related game logic.
- `ship.py` — player ship logic.
- `bullet.py` — bullet-related logic.
- `settings.py` — game configuration.
- `game_stats.py` — game statistics and state.
- `scoreboard.py` — scoreboard functionality.
- `button.py` — button functionality.
- `images/` — image assets used by the game.

The project is organized into separate modules to keep related responsibilities together.

**Running the game**

1. Ensure Python and the required game dependencies are installed.
2. Open a terminal in the `Alien_Invasion` directory.
3. Run:

   ```bash
   python alien_invasion.py
   ```

The command assumes the required dependencies are installed and `python` points to the appropriate Python interpreter on your system.

### Web Development — Learning Log

Location: `Projects/Web_Development/learning_log/`

Learning Log is a Django web application developed while learning Python web development.

The project provides practical experience with organizing a web application, working with Django, and developing a web-based learning log.

The application is maintained in its own directory so that it can be managed and deployed independently of the other projects in this repository.

**Running the application locally**

The following is a general Django development workflow. The exact commands depend on the project's installed dependencies and configuration.

1. Navigate to the project directory.
2. Create and activate a Python virtual environment.
3. Install the project's dependencies from its `requirements.txt`, if provided.
4. Apply database migrations.
5. Start the development server.

Example commands for Windows Git Bash:

```bash
cd Projects/Web_Development/learning_log

python -m venv .venv
source .venv/Scripts/activate

python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

If the project does not yet contain a `requirements.txt`, install its actual dependencies before running the application. The commands above assume that `manage.py` and `requirements.txt` are located in the `learning_log` directory.

Once the server starts successfully, Django normally makes the local application available at:

`http://127.0.0.1:8000/`

For deployment, refer to the project's actual Django settings, dependency list, database configuration, and hosting requirements.

## Technologies and Tools

The repository primarily focuses on Python development and the tools used to write, test, and manage Python projects.

| Technology or tool | Purpose |
|---|---|
| Python | Main programming language |
| PyCharm | Code editing and development environment |
| Git | Version control |
| GitHub | Source-code hosting and project history |
| Django | Web application development |
| APIs | Retrieving data from external services |
| Data visualization libraries | Generating and displaying visual representations of data |
| Game development libraries | Supporting the Alien Invasion game |

Specific libraries and versions vary between projects. Refer to the relevant project files for their actual dependencies.

## Getting Started

### Prerequisites

Before working with the repository, ensure that you have:

- Python installed.
- Git installed and configured.
- A code editor such as PyCharm.
- A terminal for executing Python and Git commands.
- Internet access when a project requires downloading datasets or accessing external APIs.

Some projects may require additional dependencies.

### Clone the Repository

To obtain a local copy of the repository:

```bash
git clone https://github.com/Peter-Muigai/Crash-Course.git
cd Crash-Course
```

Replace the repository URL if your GitHub username or repository name differs.

### Run a Chapter Exercise

Navigate to the relevant chapter directory and execute the Python file you want to practise.

For example:

```bash
cd Chapter_3-Lists
python example.py
```

Replace `example.py` with the actual filename in that directory.

Chapter exercises are independent learning activities, so there is no single command that runs the entire repository.

## Development Workflow

This repository is maintained incrementally as chapters are revised and projects are completed.

The typical workflow is:

1. Work on a chapter or project locally.
2. Test the code and review the changes.
3. Stage only the files intended for the next commit.
4. Commit the changes with a descriptive message.
5. Push the commit to GitHub.

Example:

```bash
git status

git add "Projects/Game_Development/Alien_Invasion"

git diff --staged

git commit -m "Update Alien Invasion game project"

git push
```

When working on a different project, replace the path with the relevant directory.

This approach keeps changes organized and helps prevent unrelated projects from being included in the same commit.

### Version Control Practices

- Use descriptive commit messages.
- Check staged files before committing.
- Keep virtual environments and generated Python cache files out of version control.
- Never commit passwords, API keys, Django secret keys, or other sensitive credentials.
- Keep project-specific dependencies documented.
- Preserve a clear directory structure as new projects are added.

## Learning Objectives

The main objectives of this repository are to:

- Develop a strong understanding of Python fundamentals.
- Improve problem-solving and debugging skills.
- Practise writing modular and maintainable code.
- Understand object-oriented programming.
- Learn how to test code and handle errors.
- Apply Python to practical engineering and software projects.
- Gain experience with version control and collaborative development workflows.
- Build a portfolio that demonstrates continued learning and practical implementation.

## Future Improvements

As the learning journey continues, planned improvements may include:

- Completing and refining the remaining chapter exercises.
- Expanding existing projects with additional functionality.
- Improving documentation for individual projects.
- Adding tests where appropriate.
- Documenting project-specific dependencies and setup instructions.
- Exploring more advanced Python applications.
- Continuing to develop practical skills in software engineering, data processing, and web development.

## Acknowledgements

This repository is inspired by *Python Crash Course* by Eric Matthes, a hands-on introduction to programming with Python.

The exercises and projects are part of my independent learning and practical implementation journey.

---

**Maintained by:** Peter Muigai Ng'ang'a

**GitHub:** [Peter-Muigai](https://github.com/Peter-Muigai)

*This repository is a work in progress and will continue to evolve as I learn, practise, and build more Python projects.*
