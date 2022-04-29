#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Project Name: Computational Intelligence
# File Name: Computational-Intelligence.py
# Author: Erik Nahmad
# Date: August 04 2021
# Purpose: To demonstrate a basic example of using Wolfram Alpha's Computational Knowledge Engine

import wolframalpha

API = "API_KEY"
client = wolframalpha.Client(API)  # API Key

while True:
  try:
    Answers = []  # List used to store WolframAlpha.Pod results
    userInput = input("Ask me a question: ")  # Store user input
    question = client.query(userInput).pods  # Request to Wolfram Alpha

    for result in question:  # For each result
      Answers.append(result)  # Append result to the list

    Input = f"{Answers[0].title}: {Answers[0].text}"  # Input Interpretation
    Res = f"{Answers[1].title}: {Answers[1].text}"  # Result
    print(Input + "\n" + Res + "\n")  # Output separated by new line
    
  except IndexError:  # Error Handler
    print("No Result.\n")
  except Exception:
    pass
