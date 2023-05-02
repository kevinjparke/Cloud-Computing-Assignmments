#Checksum Calculator Application
This application consists of two Flask microservices (App 1 and App 2) that work together to calculate the checksum of a file.

##How it works
When a user sends a request to /checksum endpoint of App 1, it first checks whether the request contains a JSON object with a file name. If the file name is not present or is empty, it returns an error response with a message "Invalid JSON input" and HTTP status code 400.

If the file name is present, App 1 checks whether the file exists in the mounted volume. If the file does not exist, it returns an error response with a message "File not found" and HTTP status code 400.

If the file exists, App 1 sends a GET request to the / endpoint of App 2 with the JSON object containing the file name. App 2 calculates the MD5 checksum of the file and returns the response with the file name and checksum as a JSON object.

Finally, App 1 returns the response it received from App 2 back to the user who made the initial request to /checksum.

##Requirements
The following Python packages are required to run this application:

- Flask
- requests
- hashlib
- json

##How to run the application
To run the application, follow these steps:

Make sure you have all the required packages installed.
Copy the code for App 1 and App 2 into separate Python files on your local machine.
Run App 2 by executing python app2.py in your terminal.
Run App 1 by executing python app1.py in another terminal window.
Send a POST or GET request to the /checksum endpoint of App 1 with a JSON object containing a file name.
Future Improvements
Add error handling for unexpected issues, such as network or server failures.
Implement a better way of handling file paths and file validation.
