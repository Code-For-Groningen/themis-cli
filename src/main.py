#!/bin/python3
from .classes import login

def main():
    # Legit does nothing rn
    username = input("Username: ")
    password = input("Password: ")
    course = input("Course: ")
    tutorial = input("Tutorial: ")
    t = login.Themis(course, tutorial, username, password)
    t.formatExercises()