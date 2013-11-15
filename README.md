3132GroupProject
================

Object Orientation and Generic Programming group project using Python

A simple python website using cgi

Installation:
Create your own branch using your cs login
Log on Bluenose and go into your public_html directory

and then use: 

git clone [the clone url on the right side of the page]

to pull the code into that directory

change the permissions

chmod -R 755 3132GroupProject

The .htaccess file is configured for bluenose and super simple routing

open the .htaccess file

and change the line:
RewriteBase /~pannell/3132GroupProject

to

RewriteBase /~yourcsusername/3132GroupProject

That should do it.

Now go to the url:
http://web.cs.dal.ca/~yourcslogin/3132GroupProject/

You should get the "Hello Design patterns!" mesage and some empty variable dumps.

To see how the .htaccess is handling the routing you can go to the URL:
http://web.cs.dal.ca/~yourcslogin/3132GroupProject/user/login

You can see in the message that it passes user as the class and login as the method.

Other paramaters are passed in the usual way.  Try:
http://web.cs.dal.ca/~yourcslogin/3132GroupProject/user/login?username=pannell&password=1234567

and you can see that username and password are passed into their own variables.

The main page also uses the HTML5 boilerplate so all of the standard web goodis like modernizer and jQuery are ready to go.



