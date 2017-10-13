# Aidan's JCR Website
[![Build Status](https://travis-ci.org/AidansJCR/aidans-jcr.svg?branch=master)](https://travis-ci.org/AidansJCR/aidans-jcr)
[![Updates](https://pyup.io/repos/github/AidansJCR/aidans-jcr/shield.svg)](https://pyup.io/repos/github/AidansJCR/aidans-jcr/)
## Introduction
This is the start of something new... the creation of a website designed BY students, FOR students. Rather than being a site dedicated entirely to selling the college to external students, it should provide a balance between selling the college and helping the college members settle in, making their lives that little bit easier.

That's the mentaility I have when creating this site.

## Getting Started
### 1. Clone the repository
You can either use a GitHub desktop client, or in the terminal:

```bash
git clone https://GitHub.com/AidansJCR/aidans-jcr.git
```

### 2. Download Vagrant
We use Vagrant in order to avoid polluting your system with all the dependencies.
This is useful if you do other Python work, and want different versions of libraries.

[Click here to download it.](https://www.vagrantup.com/downloads.html)

### 3. Provision your Vagrant Machine.

In the command line, run:

```bash
vagrant up
```

This will set up your virtual machine and download all the needed files.

### 4. Run the Vagrant Machine

Do this in the command line. Run:

```bash
vagrant ssh
```

You will now be dropped in a terminal session on the Vagrant Machine, which means
everything is now installed.

### 5. Run the test server

To test changes to your code, you need to run a local version of the site. This
can be done easily by running the following command:

```bash
python3 manage.py runserver 0.0.0.0:8000
```

Then go to your normal web browser, and navigate to ```localhost:8000``` and
you should see the debug version of the site!

### 6. Get Developing!
That's it, you can now write code using any text editor of your choice. Just modify the code,
and then check back to the web browser session on the localhost version (be sure you aren't looking
at the live website). When you are ready, commit your changes and push them (after creating a pull request).
