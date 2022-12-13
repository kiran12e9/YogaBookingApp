# YogaBookingApp

#Web application allows people of ages 18-65 to pay an amount at any time in the month ,choose their batch and can learn yoga till that end of that month,
they can only change their batch in the next subscription month.they have to pay on monthly basis.

--> This work is done as a part of Internship Assignment .


All about the application.






Title:   Yoga Class Booking - Web Application



Submission by:  Ravi Kiran Reddy. R
Mail: r.ravikiranreddy2409@gmail.com


 
Application Functionalities:
•	
User can register in the app by entering the details like his -

 1) First Name
 2) Last Name
 3) Email ID
 4) Password
 5) Date of birth

•	After registering, user can signup through his registered email address and password.


•	In case if the user forgets their password, they can click on forgot password, to which their password will be sent to their registered email address.
By using it, They can login into the app again. 

•	After Login:

	User can subscribe to the yoga classes, by clicking subscription details navigation bar in the header section of the application.

If a user is not subscribed, a message will be displayed as “please subscribe to see the subscription details and learn yoga” and prompt user to go the subscription page of the application where they can enter the bank details and pay amount of 500rs. and choose a batch and subscribe”.

=> If a user is already subscribed to the app, they will see their subscription details:
 1) their validity up to
 2) batch they chosen.
 3) amount paid.
 4) payment date.

	and prompts the user to go to my classes page of application where he can see his trainings (which are not available though).


After Payment:

If the payment is successful (in this case , always success, as we have not implemented the payment functionality in this app) , the web page containing his details , batch details, and amount paid and the validity along with the transaction successful message will be displayed.


Edit Details:

User at anytime can change his password and first name or last name and date of birth(functionality is given as user might entered wrong info).

Batch Change :

Once a user subscribed to the application, they cannot shift to another batch in the same month.

Example: If a user has chosen batch 6am-7am, paid the amount and subscribed. Then he or she cannot change his batch until the subscription of the month ends.

They can freely choose other or the same batch in their next subscription month while making the payment and submitting the subscription form on the subscribe page.
Validity and Duration:

No matter when the user has subscribed to the yoga application, their validity is up to the end of the payment month, but it soes not mean a compulsorily of 30days.

Example: User has subscribed by paying the required amount and subscribed on 15th January, his validity is up to 31st Jan of that year.
If they subscribed on 30th  January , their validity is till 31st January, if they have subscribed on 01st January , their subscription is still valid up to 31st January….




Technologies Used:

-HTML (for making the structure of the website).

-CSS (for styling the website in a basic way)

-Bootstrap( for making website styling and UI look good and also reduce CSS hardcoded- stylesheets and make use of already available styles for different elements present in our application).

-JavaScript ( For doing basic validations like checking if user entered the details in correct format , if they have entered the passwords and confirm password the same or not and basic validations are done on the client side itself before submitting the form).

-Python(Used for developing the application logic  for every functionality in the app)

-Django(python web framework , is used to build web application , deploy and run server locally or on remote , and also provides may functionalities to our project including a local database).

-MySQL( database query language used to do crud operations on database and stores data of users and their subscription details).








General flow of our Web Application:
















 
 



	
 


How overall software development was done? or to be done?

First, install python on your machine.

Go to python.org site and download the latest version of python
Install it, while installation it asks you to set the path of environment variable, make sure you tick mark it.

-To verify whether it is successfully installed or not,
Open command prompt, type python and press enter.

It shows the current installed version of python on your system if it is successfully installed, if not is shows command not recognised.

After installing python, open any code editor preferably visual studio code , you can work in command line also, but visual studio code makes it easier to run terminal and make git changes and deployment and other things easier for us.

Open visual studio code , Open a new terminal .

Make a folder in your desired directory, lets say on desktop, you make a folder yogatraining and open it in visual studio code.

To not make mess with the installed packages, dependencies and other software , we will use a virtual environment for our project, virtual environment makes us feel like we are working in an isolated environment, that means those packages, dependencies and frameworks we install in this environment is purely and only to this environment, they care not merged or accessible to the projects outside the environment.

After opening terminal, Create a virtual environment using 
command: virtualenv [environment name]

If virtualenv command is not recognised, it means virtualenv is not installed on your machine,
So to install virtualenv,
Command: pip install virtualenv

After installing virtualenv and creating the virtual environment as explained above, 
To activate it change the directory to environment you created 
  Command: cd [env_name] 
then, run Command: Scripts\activate to activate the virtual environment.


Now it’s time to install Django framework to manage our web application like running on the server, handling requests, providing ways to connect to a database and URL routing etc.. 
first change directory to the virtual environment you created, 
then, by using the 
command: pip install django

After successfully installing the django framework in our virtual environment,
To start our new project,

Command: django-admin startproject [project name]
then django setups a new project folder for us, in this case it is yogatraining, change the directory to project folder

Command: cd yogatraining

Inside the yogatraining project folder, you will see again an app called yogatraining,

django creates this by default and acts like a root app for the whole project .



APP vs PROJECT 

Django project is our complete web application, where is an app within the project is like a part of our web application, creating and separating different apps within the project helps us to debug, manage the entire application easily.

For example, Library management system has two types of users , one is student and the other is 
librarian , they have different functionalities, views, templates etc…so having two applications(apps) inside our project helps to maintain the code neat.

Hence, project is the complete package, app is the individual thing in django and 
Django creates a root app with some files and default settings .

To ensure that project is installed correctly, being in the project folder, got to terminal and 
run the server.

Command: python manage.py runserver

Then you will see something like this, 

Django version 3.2.16, using settings 'yogatraining.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

Open the URL in the browser to verify if the project is successfully running or not,

localhost:8000, we get a nice UI loaded page implying project is running on the local server successfully.


To create our own app other than the default one created by django,
Command: python manage.py startapp [app name]

In the below example, an app named mainapp is created.

Coming to folder structure that is created by Django, i.e., inside our yogatraining app,

Django App Folder Structure demystified:

=> 


 


As you can see inside our yogatraining project folder, we have another app as yogatraining which act as root application for our project and with default settings and installed apps information and also information and settings related to database.

Now, let us look at each file in detail , what it does.

1) __init__.py


2) settings.py


3) urls.py

4) manage.py

5) views.py

6) wsgi.py

7) models.py

8) migrations



 


database schema 
https://user-images.githubusercontent.com/98594066/207317745-a880fea5-e723-4685-b32c-94f3e061431e.png









  
 
