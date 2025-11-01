College ChatBot
Project Overview

The College ChatBot is a simple Python-based program that can answer frequently asked questions about the college. It uses a dataset of predefined questions and answers stored in a CSV file. When a user asks a question, the chatbot finds the most similar question in the dataset and responds with the corresponding answer.

Objective

To develop a basic chatbot system that can assist students, parents, and visitors by providing instant answers to common queries related to the college.

Features

Reads a dataset of college-related questions and answers.

Matches user queries with similar questions using text similarity.

Provides appropriate responses from the dataset.

Easy to update by adding new Q&A pairs in the CSV file.

Works on the command line or Jupyter Notebook.

Technologies Used
Component	Technology
Programming Language	Python
Libraries	pandas, difflib
Dataset Format	CSV
Platform	Jupyter Notebook / VS Code
Dataset Information

File name: college_chatbot_dataset.csv

The dataset contains two columns:

Question – a common question related to the college.

Answer – the chatbot’s response to that question.

Question	Answer
What courses are offered?	Our college offers B.Tech in CSE, IT, and ECE programs.
What are the library hours?	The library is open from 9 AM to 6 PM, Monday to Saturday.
