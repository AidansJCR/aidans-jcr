# JCR Website Apps
The website itself consists of several Django apps. This document outlines what each of them do.

## aidansadmintheme
This simply customises the Wagtail CMS admin to be themed around aidan's. This includes using the custom svg logo on the backend, custom login text, and custom welcome text to make the site more Aidan's themed.

## cisauth
This is a login driver for CIS. It currently runs using the ITS validator and an API to get college information. It would be best if we can replace this with something more secure (like Shibboleth), but it's all we have for now.

All accounts are given no privileges at all, but you should be able to give a specific user some privileges later on.

### TODO:
+ Store a person's name, so we can address them nicely.

## home
This contains the home page themes for wagtail.

## search
This deals with website search.


