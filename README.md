Prerequisites

Before running this project, ensure you have the following installed on your local machine:
Python 3.8 or later
Django

Django Project Setup (Basic, No Database)

This is a simple Django project that doesn't require a database. The steps below will guide you through the installation process to get the project up and running.
Prerequisites

You need to have Python and Django installed on your system.
1. Install Python

First, install Python. It is recommended to use Python 3.8 or later.
Download Python from python.org and follow the installation instructions for your operating system (Windows, macOS, Linux).
During installation, make sure to add Python to your PATH.

2. Install Django

Once Python is installed, you need to install Django.
Using pip:
Open a terminal (or Command Prompt on Windows).
Install Django using pip, Python's package installer:
pip install Django
Project Setup

Clone the Repository
If you haven't already, clone the repository for your Django project:
git clone https://github.com/ramjancse/assignment1.git

Set up a Virtual Environment (Optional but Recommended)
It’s recommended to set up a virtual environment to avoid conflicts with other Python packages on your system. To do this:
Install virtualenv (if you don’t have it):
pip install virtualenv
Create and activate a virtual environment:

For macOS/Linux:
python3 -m venv venv
source venv/bin/activate

For Windows:
python -m venv venv
venv\Scripts\activate

Once activated, your terminal prompt should change to show the virtual environment's name.

Running the Project
Once the setup is done, you can start the Django development server.
1. Run the Development Server
To start the server, run:

Troubleshooting
If you encounter any issues, here are some things to check:
Ensure Python and Django are installed correctly. You can check the Python version with python --version and the Django version with django-admin --version.
Make sure your virtual environment is activated before installing dependencies.
If you get permission errors when running commands, try running with sudo (on Linux/macOS) or ensure you have the correct permissions on your system.
python manage.py runserver

By default, this will start the development server at http://127.0.0.1:8000. Open that URL in your web browser to view the project.
By default, this will start the development server at http://127.0.0.1:8000. Open that URL in your web browser to view the project.
