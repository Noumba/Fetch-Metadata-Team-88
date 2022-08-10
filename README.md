# Fetch-Metadata-Team-88

Team link
https://github.com/orgs/zuri-training/teams/fetch-metadata-team-88

### This team is building a web app that extracts metadata of files

---

In this project we used Django to build a web based metadata extraction web app, for any kind of a file. You upload a file, and the web app extracts the metadata, saves it as a json file, and you can download, and share the metadata and file.

---

Tools used
Figma

Google Docs

Figjam

Python

___

**Our Project Documentation:**

- [Research Document](https://docs.google.com/document/d/1V-CsWNocUllupPYLu3KicmMY2abUbJ4wbuCy5uT--h8/edit?usp=sharing)

- [User Research](https://www.figma.com/file/7dUOOrIWE8Ts7bBna4mRUd/user-research-fetch-metadata--proto?node-id=0%3A1)
- [Final Design](https://www.figma.com/file/R6dseaUIzRUSh4YP09cT7d/Team_88_Fetch-Metadata?node-id=3%3A5)
- [Slides ]
- [Database Schema]

---

### Getting Started

---

**Clone Project**
To use the project you need to clone the repo on to your computer.
`git clone https://github.com/zuri-training/Fetch-Metadata-Team-88.git`

**Create A virtual Environment**
You need to create a virtual environment to run the project in it. And Make sure you have `Python 3` before you proceed.
run `python3 -m venv env` in the terminal
The name of the environment here is `env`

Next you **activate** the virtual environment using the following command

> Mac User

run `source env/bin/activate`

> Windows User

run `./env/Scripts/activate`
make sure you using Command-line not Powershell

**Requirements**
To work with the project well, you need to install the package dependencies.Make sure your environment is active.

> Install requirements

run `pip install -r requirements.txt`

and wait for all the packages to be installed before you start using the django project.

---

**Project Initialization**
To start working with the project after installing the dependencies you need to first initialize your django project.

run `python manage.py makemigrations`
and then
run `python manage.py migrate`

---

**Execution**
Now after successfull execution of the commands above you can run your django server and view the web app

run `python manage.py runserver`

---

App Pass: bsdhjmxkwlysgrjt
