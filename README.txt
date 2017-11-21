The cloud-based patient care application is an M-Health app designed to improve and simplify communication between patients and medical professionals. 

The proof of concept consists of two components: a website, and a dedicated Android application which uses all the features of the site, as well as utilising google cloud messenger to send notifications to the user. 
The site was built using the python Django framework and is currently deployed on pythonanywhere.com, while the code base is version controlled using git and hosted on GitHub. Django, like most web frameworks, uses a model-view-controller architecture but divides the site into several discrete units called ‘Apps’ which handle each distinct feature of the site. 

With the cloud-based patient care application there are 6 different apps:
•	Home – a simple landing page with little functionality.
•	Form – which handles submitting and reviewing forms.
•	Messaging – which handles sending messages between patients and doctors etc.
•	Analyse – which demonstrates how data can be reviewed and visualised.
•	UserAdmin – which handles things like login, patient creation etc.
Each app has a urls.py file which is consulted by Django when a URL is requested. Usually these URLs are pointed to functions in the apps views.py file which handle the request.
The database which powers the site is currently an SQLite3 database also hosted on Python Anywhere. SQLite3 was chosen simply for ease of development and is not suitable for use in a large application. Django provides simple migration tools which will make it straightforward to convert to a more robust DBMS. 
User Authentication is provided by the Django framework. Passwords are all hashed and salted in the database and things like sessions and cookies are handled automatically. Django has an Admin role which gives the user permission to access the Admin page of the site. Here they can manually add and edit records and create new users. The application has three other types of user which aren’t covered by Django’s generic ‘User’ role. These roles are implemented by piggybacking on the existing user authentication infrastructure and creating new database models which require a foreign key pointing to a unique User. The new custom roles are:
•	Administrator – Creates Patients and may schedule reminders to be sent out.
•	Patient – May add and review form submissions and can send and receive messages with doctors and Administrators.
•	Doctor – May browse submitted forms, message patients and colleagues and visit the analysis page to view visualisations of submitted data.

The Android application was build using Android Studio. Its operation relies heavily on the Android WebView to access and display the websites content. Superficially, the apps functionality resembles that of a web browser which only visits one site however it performs a very useful task in the background. When the user first logs in the app registers with google cloud messenger and receives a token. This token is then passed to the Web application and is stored in the database in the users record. The web application knows which user to store the token under because the Android app includes in the request the cookies it pulls from the WebView. This way the web application can associate the token with a session ID and hence, a user.  Once the Android app is registered to a specific user the Web Application can forward push notifications to the user using Google Cloud Messenger. Currently there are two kinds of notification the user may receive: form submission reminders and message notifications. Because of the Applications’ reliance on Google Cloud messenger, any environment intended to deploy the Django application must have the python GCM library installed.

