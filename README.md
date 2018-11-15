# Aidan's JCR Website
[![Build Status](https://travis-ci.org/AidansJCR/aidans-jcr.svg?branch=master)](https://travis-ci.org/AidansJCR/aidans-jcr)
[![Updates](https://pyup.io/repos/github/AidansJCR/aidans-jcr/shield.svg)](https://pyup.io/repos/github/AidansJCR/aidans-jcr/)
## Introduction
This is the start of something new... the creation of a website designed BY students, FOR students. Rather than being a site dedicated entirely to selling the college to external students, it should provide a balance between selling the college and helping the college members settle in, making their lives that little bit easier.

That's the mentality I have when creating this site.

## Getting Started
### 1. Clone the repository
You can either use a GitHub desktop client, or in the terminal:

```bash
git clone https://GitHub.com/AidansJCR/aidans-jcr.git
```

### 2. Install Pip
Pip is a program that requires Python but it will allow you to easily download many other packages too.
This is useful if you decide to take part in other Python projects.

[Click here to get it.](https://pip.pypa.io/en/stable/installing/)

### 2. Install Pipenv
Run the following command in your terminal:

```bash
pip install pipenv
```

### 3. Installing the packages and loading into the environment

In the terminal navigate to the directory of the website (where you have manage.py).
Once you're there, run:

```bash
pipenv install
pipenv shell
```

You are now in the environment that is needed to run the website.

### 4. Run the server

Do this in the command line. Run:

```bash
python manage.py runserver
```

If you then navigate to 127.0.0.1 in your browser the debug version of the Website should be available.

### 5. Get Developing!
That's it, you can now write code using any text editor of your choice. Just modify the code,
and then check back to the web browser session on the localhost version (be sure you aren't looking
at the live website). When you are ready, commit your changes and push them (after creating a pull request).
