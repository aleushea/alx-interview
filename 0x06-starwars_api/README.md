0x06. Star Wars API

AlgorithmAPIJavaScript

The “0. Star Wars Characters” project requires you to interact with an external API to fetch and display information about Star Wars characters based on the movie ID provided as an argument. To successfully complete this project, you need to be familiar with several key concepts related to web programming, API interaction, and asynchronous programming in JavaScript.

Concepts Needed:
    1.	HTTP Requests in JavaScript:
        o	Understanding how to make HTTP requests to external services using the request module or alternatives like fetch in Node.js.
        o	A Complete Guide to Making HTTP Requests in Node.js
    2.	Working with APIs:
        o	Understanding the basics of RESTful APIs and how to interact with them.
        o	Parsing JSON data returned by APIs.
        o	Working with APIs in JavaScript
    3.	Asynchronous Programming:
        o	Managing asynchronous operations with callbacks, promises, and async/await syntax.
        o	Handling API response data asynchronously.
        o	Asynchronous Programming in JavaScript
    4.	Command Line Arguments in Node.js:
        o	Using the process.argv array to access command-line arguments passed to a Node.js script.
        o	How to Parse Command Line Arguments in Node.js
    5.	Array Manipulation and Iteration:
        o	Iterating over arrays and manipulating data structures to format and display character names.
        o	JavaScript Array Methods
By familiarizing yourself with these concepts and resources, you will be able to efficiently retrieve, process, and display Star Wars characters from the specified movie using the Star Wars API, demonstrating your ability to work with external APIs and manage asynchronous code in JavaScript.
Additional Resources
    •	Mock Technical Interview
General Requirements
    •	Allowed editors: vi, vim, emacs
    •	All your files will be interpreted on Ubuntu 20.04 LTS using node (version 10.14.x)
    •	All your files should end with a new line
    •	The first line of all your files should be exactly #!/usr/bin/node
    •	A README.md file, at the root of the folder of the project, is mandatory
    •	Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
    •	All your files must be executable
    •	The length of your files will be tested using wc
    •	You are not allowed to use var
More Info
Install Node 10
    •	$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
    •	$ sudo apt-get install -y nodejs
    Install semi-standard Documentation
    •	$ sudo npm install semistandard --global
    Install request module and use it Documentation
    •	$ sudo npm install request --global
    •	$ export NODE_PATH=/usr/lib/node_modules
Tasks
Star Wars Characters
Write a script that prints all characters of a Star Wars movie:
    •	The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
    •	Display one character name per line in the same order as the “characters” list in the /films/ endpoint
    •	You must use the Star wars API
    •	You must use the request module
Repo:
    o	GitHub repository: alx-interview
    o	Directory: 0x06-starwars_api
    o	File: 0-starwars_characters.js
