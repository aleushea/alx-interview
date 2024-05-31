0x05. N Queens
The “0x05. N queens” project is a classic problem in computer science and mathematics, known for its application of the backtracking algorithm to place N non-attacking queens on an N×N chessboard. To successfully complete this project, you will need to understand several key concepts and have access to resources that will help you grasp the necessary algorithms and techniques.
Concepts Needed:
	Backtracking Algorithms:
    •	Understanding how backtracking algorithms work to explore all potential solutions to a problem and backtrack when a solution cannot be completed.
    •	Backtracking Introduction
	Recursion:
    o	Using recursive functions to implement backtracking algorithms.
    o	Recursion in Python
	List Manipulations in Python:
    o	Creating and manipulating lists, especially to store the positions of queens on the board.
    o	Python Lists
	Python Command Line Arguments:
    o	Handling command-line arguments with the sys module.
    o	Command Line Arguments in Python
By studying these concepts and utilizing the resources provided, you will be equipped with the knowledge required to implement an efficient solution to the N queens problem using Python. This project not only tests programming and problem-solving skills but also offers an excellent opportunity to learn about algorithmic thinking and optimization techniques.
Additional Resources
    o	Mock Interview
Repo:
    o	GitHub repository: alx-interview
    o	Directory: 0x05-nqueens
General Requirements
    o	Allowed editors: vi, vim, emacs
    o	All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
    o	All your files should end with a new line
    o	The first line of all your files should be exactly #!/usr/bin/python3
    o	A README.md file, at the root of the folder of the project, is mandatory
    o	Your code should use the PEP 8 style (version 1.7.*)
    o	All your files must be executable
Tasks
0. N queens
Chess grandmaster Judit Polgár, the strongest female chess player of all time
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.
    o	Usage: nqueens N
    o	If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1
    o	where N must be an integer greater or equal to 4
    o	If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
    o	If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
    o	The program should print every possible solution to the problem
    o	One solution per line
    o	Format: see example
    o	You don’t have to print the solutions in a specific order
    o	You are only allowed to import the sys module
•	File: 0-nqueens.py
