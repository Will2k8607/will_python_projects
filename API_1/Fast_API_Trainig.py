#training using fastAPI
#I need to install the package 'FastAPI' and 'Uvicorn' (last one is used for the web interface)

from fastapi import FastAPI
from fastapi import Path #this will help us to put comments in some of the processes
from typing import Optional

#GET -> get information
#POST -> Create something new

#PUT -> Update the information
#DELETE -> delete something

app = FastAPI() #This will create your app, you can call it with whatever name you want, this will call later in the server

@app.get('/') #this is always called for actions in the app, the information inside () is the home page
def index(): #this can be called whatever you want
    return {'name': 'Second Data'}

#next steps are in termial, we need to go to the folder where your API is located like below
#"uvicorn Fast_API_Training:app --reload"
#uvicorn is the tool to run the API is the local server
#Fast_API_Training is the python file created, do not put the file extenstion!!
#app: is the name of the variable assaigned to FastAPI
#--reload: this is SUPER IMPORTANT as it's the option to update the website with any change done in the code
#this will generate a http, example: http://127.0.0.1:8000
#if you type in the browser after the http.../docs you will see a really cool UI to see all the documentation for you API

#Now creating a mos complex get request

#Creating a Json file:

students = {
    1:{
        'Name': 'John',
        'Age' : 17,
        'Class' : 'Year 12'
    }
    }

#Example of how the below funtions looks in a internet page: google.com/get-student/1
#creating a new end point
@app.get('/get-student/{student_id}') #It is like creating a dinamic variable, it will change depending of the value inserted
#now create the function
def get_student(student_id:int = Path(description = "The ID of the student you want to view"),gt=0, lt=3):#Path help to add a description
    return students[student_id] #we are looking into the dictionary using a dinamic variable
    #when you don't have the variable inserted, the server will show an error...
    #you can add more details in the path, for example gt (greater than) ,lt (less than), ge (greater or equal) ,le --this is not working for me
    #now you can go to the website and put the end point to get the information, for example in our case is: http://127.0.0.1:8000/get-student/1 (use the app.get path created)

#now we are going to test the query parameter, which is different from the previous one which was a path parameter, an example is google.com/results?search=Python
@app.get('/get-by-name')## Important!!! don't forget to put the '/' if not, is not going to work!!
def get_student(name:Optional[str] = None): #When you put None it makes the value optional, however the recomend to do it using 'Optional[str]', how ever you will need to import the package typing -> Optional
    for student_id in students:
        if students[student_id]['Name'] == name:
            return students[student_id]
    return{'Data': 'Not Found'}



