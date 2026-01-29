# Recursion_TextWise_Solution

This repository contains my implementation of a recursive string reversal function for the ContentOptimizer project at TextWise Solutions. The goal of this task is to demonstrate understanding of recursion, algorithmic reasoning, clean code practices, and professional documentation.
## Project Overview
TextWise Solutions is enhancing their ContentOptimizer tool with advanced text‑manipulation features. One of the required components is a recursive string reversal function, which supports deeper text analysis and stylistic evaluation.
This project includes:
- A Java implementation of the recursive string reversal function
- Clarifying questions
- Flowchart diagram of the recursive process
- Unit tests (normal + edge cases)
- Time and space complexity analysis

## Clarifying Questions
Before implementing the solution, these are the questions I would ask to ensure alignment with requirements:
- What should the function return if the input is null?
- Should whitespace be preserved exactly as provided?
- Should the function reverse the entire string or reverse each word individually?
- Are there any performance constraints or maximum input sizes we should consider?

## Recursive Approach Explanation
The recursive strategy is based on two key ideas:
Base Case
If the string is empty or has one character, it is already reversed.
Recursive Case
Take the last character of the string and append it to the result of reversing the rest of the string.
This naturally breaks the problem into smaller subproblems until the base case is reached.




## Flowchart (Recursive Logic)
                            
                              
rverseString(s) -> is length <= 1? -> Yes? -> Return s
                      |
                      -> No?  Return last char + reverse(s without last) 

## Time Complexity
O(n)
The function makes one recursive call per character.
Each call processes one character, so total work grows linearly with input size.

## Space Complexity
O(n)
Each recursive call adds a new frame to the call stack.
For a string of length n, the deepest recursion level is n.






