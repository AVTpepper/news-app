# **TaleTell**

![am-i-responsive](/documents/readme_images/am_i_responsive.png)

**TaleTell is a an app for those interested in reading, sharing and/or creating posts to share with others.**

This application was built using [GitHub](https://github.com/) and deployed to [Heroku](https://id.heroku.com/login).

<u>Required technologies:</u>

Python (+Django Framework), JavaScript, HTML5 and CSS3.

Deployed version of this project can be found [here](https://news-app-avtpepper.herokuapp.com/).
 
## **Table of content**

* [Project Purpose](#project-purpose)
* [UX](#ux)
    * [Project Scope](#project-scope)
    * [User Stories](#user-stories)
* [Design](#design)
    * [Website Structure](#website-structure)
    * [Relational Database Diagram](#relational-database-diagram)
    * [Design Diagram](#design-diagram)
    * [Colour Design](#colour-design)
    * [Fonts](#fonts)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [CRUD Operations](#crud-operations)
    * [Defense Design](#defense-design)
    * [Features Left to Implement](#features-left-to-implement)
* [Data Validation](#data-validation)
* [Technologies and libraries used](#technologies-and-libraries-used)
    * [Languages](#languages)
    * [Database Platform and Cloud Storage](#database-platform-and-cloud-storage)
    * [Libraries and other resources](#libraries-and-other-resources)
* [Testing](#testing)
    * [Introduction](#introduction)
    * [Testing User Stories](#testing-user-stories)
    * [Automated Testing](#automated-testing)
    * [Testing Accessibility and Performance](#testing-accessibility-and-performance)
    * [Code Validation](#code-validation)
* [Bugs during development](#bugs-during-development)
    * [Fixed Bugs and Solutions](#fixed-bugs-and-solutions)
* [Development and Deployment](#development-and-deployment)
    * [Local Deployment](#local-deployment)
    * [Deployment to Heroku](#deployment-to-heroku)
* [Credits](#credits)
    * [Code](#code)
    * [Acknowledgments](#acknowledgments)


# **Project Purpose**

TaleTell is a website application designed specifically for people who have an interest in sharing and reading stories or news created by others on the platform. 

Target Audience: People looking for a community to share stories with others.

# **UX** 

## **Project Scope**

* **Functionality**

    * To be able to sign-up using a username, email address and secure password.
    * To be able to login and logout of an account
    * To be able to create/view/edit/delete as site admin
    * To be able to create/view/edit/delete user profile information as a user
    * To be able to store and retrieve profile image
    * To handle errors: 404 page 'Not Found'

* **Content Requirements**

    * Clear, unambiguous and concise information on how to use the website
    * Forms where user input is required
    * Responsive and interactive website that responds to user
    * Images across website to provide visually appealing content

* **Site-owner goal** 

    * To provide a platform for users who are looking to share stories
    * To provide a platform that allows users to create a profile
    * To create a viable product that can be further developed with additional features

* **User goals**

    * To access a user-friendly application across multiple devices
    * To read and learn from other users

## **User Stories**

I initially used githubs project board (dont know how to link it, but its set to public access, so should be able to be viewed [project-board](https://github.com/users/AVTpepper/projects/4/views/1)) to help me stay on track with features I wanted to implement. Some of the user stories below are ones I thought of on the go during the project.

* As an **admin**, I can **access an admin profile** so that I can **create, edit and delete posts.**

* As an **admin**, I can **view user profile information** so that I can **modify any particular user detail or delete users.**

* As a **first-time site visitor**, I can **sign-up** so that I can **create an account to access user features.**

* As a **user**, I can **sign-in and out of an account** so that I can **log-in and out of user account.**

* As a **user**, I can **view posts** so that I can **read and learn from others.**

* As a **user**, I can **add comments** so that I can **share my thoughts on a post.**

* As a **user**, I can **like a post** so that I can **tell the author I liked their content.**

* As a **user**, I can **unlike a post** so that I can **change my mind if I dont like a post anymore.**

* As a **user**, I can **create a post** so that I can **share my stories and news.**

* As a **user**, I can **update my post** so that I can **modify my stories/news.**

* As a **user**, I can **delete my post** so that I can **remove it from the website.**

* As a **user**, I can **search for a post** so that I can **select the post I am looking.**

* As a **user**, I can **get to a user profile** so that I can **see my account profile.**

* As a **user**, I can **update my profile information** so that I can **modify user profile dashboard information.**


# **Design**

## **Website Structure**

* Website is structured into 11 principal pages
* All pages extend the same base therefore producing a consistent style across the application
* Pages are the following:

| Page | Description |
| --- | --- |
| **Header** | Navbar header with site logo and collapsable links for media query sizes |
| **Home** | A page consisting of a posts created by users |
| **Post Creation** | A page to create a post |
| **Post View** | View a specific article, update, delete, like, unlike, comment. |
| **Sign Up** | Where users can create an account |
| **Login** | Where users can login with an account |
| **Logout** | Where users logged out of an account |
| **User Profile** | A profile dashboard displaying user information |
| **Profile Settings** | An input page where users can modify their existing information |
| **Footer** | Displays social media links, and a home button. |

* **Interactive Design**

    * Collapsable navbar menu for smaller media query screens

    ![responsive-toggle-example](/documents/readme_images/responsive-toggle-example.png)

    * All buttons, icons and links respond to hovering

    ![responsive-link-example](/documents/readme_images/responsive-link-example.png)


## **Relational Database Diagram**

* The project uses a relational database (PostgreSQL)

* The following diagram represents the relational database model design for this website. It was made using Quick Database Diagrams:

![relational-database-diagram](/documents/readme_images/relational-database-diagram.png)

**Models**

* **User**
    * The User model contains information about each user that registers an account
    * The fields used for this project are: *username*, *email*, *password*

* **Post**
    * The Post model is the principal model
    * Any user can create a post
    * All users can interact with Post with limiting features depending on who created it.
    * The model contains the following fields: *id*, *title*, *content*, *date_posted*, *author_id*, *image*.

* **Like**
    * Has an id to keep track if a post is liked or not.
    * ForeignKey relationship with both Post and User
    * Contains the following fields: *id*, *user_id*, *post_id*.

* **Profile**
    * The Profile model is used to store information regarding any registered user.
    * Users can create posts.
    * Users can modify profile information at any time.
    * An admin can also create, modify and delete profile objects
    * ForeignKey relationship with User
    * Contains the following fields: *id*, *user_id*, *image*, *email*.
    
## **Design Diagram**

Intial ideas were far more challenging to implement than what I first had intended. Below I will share the first few Wireframes created for this project.
* **Wireframes**
 
    * Design for home page can be seen [here](/documents/readme_images/Landing%20Page.png).
    * Design for sign up page can be seen [here](/documents/readme_images/sign-up-wireframe.png.png).
    * Design for login can be seen [here](/documents/readme_images/actual-login-page.png).
    * Design for article view page can be seen [here](/documents/readme_images/single-article-view.png).
    * Design for post creation can be seen [here](/documents/readme_images/Post%20Creation%20Page.png).
    * Design for view all posts page can be seen [here](/documents/readme_images/View%20All%20Stories.png).
    * Design for Site Map can be seen [here](/documents/readme_images/Site%20Map.png).

The rest of the pages were created without a design in mind but followed the general structure of those already created.

## **Color Design**

This color palette was made using [Coolers](https://coolors.co/).

![color-palette](/documents/readme_images/color-palette-p4.png)

This colour palette has been the basis for colour which has been applied throughout the website in this general order: 

* Navbar color: #000080 (Navy-Blue)
* Body : #FAFAFF ('Ghost' white)
* Nav-Links : #FFD700 (Gold)
* Principal font colour : #000000 (black)

## **Fonts**

Font application in this website at the moment is the standard fonts provided; **sans-serif**.


# **Features**

## **Existing features**

Information on existing features can be found on [this page](/documents/features/existing_features.md).

## **CRUD Operations**

| **Operations** |  First Time Visitor |  Auth. Users | Superusers |
|  --- | --- | --- | --- |
| **View Home Page** | No | Yes | Yes |
| **View Posts** | No | Yes | Yes |
| **Create Posts** | No | Yes | Yes |
| **Update Posts** | No | Yes | Yes |
| **Delete Posts** | No | Yes | Yes |
| **Like / Unlike Posts** | No | Yes | Yes |
| **Comment On Posts** | No | Yes | Yes |
| **Update / Delete Profile** | No | Yes | Yes |
| **Login** | No | Yes | Yes |
| **Register New user** | Yes | No | Yes |


## **Defense Design**

* Delete operations

    * Delete button brings you to a post deletion confirmation page:

        * Which asks the user if they are sure to delete their post.
        * Which also gives them the option to return back.

    ![delete-page](/documents/readme_images/delete-post-page.png)

    * Updating

        * Similar to the delete page, you need to click the **post** button after making the wanted changes to the post.
        * There is also a button that will bring you back to the article view page.


## **Features left to implement**

* Ability to delete / update / like and unlike comments.
* Ability to connect different profiles so that users can directly "Add friend" or "Connect" with another user.
* Ability to allow different users to privately message each other.
* Font Selection.
* Modified buttons to be more inlign with the color-scheme.
* Password Reset interface that successfully sends an e-mail to user to change password.
* Crispy Forms for better forms.
* More success messages.

# **Data Validation**

* **Post Creation**

    * Title is limited to 100 characters.
    * textfield cannot exceed any more than >500 characters.
    * Image has a defualt if nothing is uploaded.


* **Registering An Account**

    * All fields must be filled.
    * System will not allow non-registered users to create an account with a conflictive username.


* **Sign In Page**

    * System does not accept any username or password that is non-existent or incorrect.



# **Technologies and libraries used**

## **Languages**

The languages used are:

* [HTML](https://html.spec.whatwg.org/multipage/)
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
* [Python](https://www.python.org/)

## **Database Platform and Cloud Storage**

* [ElephantSQL Postgres](https://www.elephantsql.com/): SQL database service provided by ElephantSQL for data storage.
* [SQLite](https://www.sqlite.org/index.html): SQL database engine used by default as part of Django Framework and used during development.
* [Cloudinary](https://cloudinary.com/home-102622): to store images and static files.
* [Heroku](https://id.heroku.com/login): to deploy and run the application.

## **Libraries and other resources**

This project contains the following resources:

* [Django](https://www.djangoproject.com/): Python-based framework for rapid website development. 
* [Bootstrap](https://getbootstrap.com/): CSS and JavaScript library.
* [HTML Markup Validation](https://validator.w3.org/): used to validate HTML code syntax.
* [CSS Validation Service](https://jigsaw.w3.org/css-validator/): used to validate CSS code syntax.
* [PEP8 Validation](http://pep8online.com/): used to validate Python code syntax.
* [Chrome DevTools](https://developer.chrome.com/docs/devtools/): development tool supplied by Google Chrome browser to test responsive design during development.
* [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/): used to access website performance.
* [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/index.html): used for user account registration and user authentication.
* [Font Awesome](https://fontawesome.com/): used for icons across website.
* [Icons8](https://icons8.com/): used for favicon.
* [GitHub](https://github.com/): used to store, develop and maintain project code.


# **Testing**

## **Introduction**

* Site has been continuously tested throughout development stages using the following features:
    * Python terminal for backend functionalities
    * Google Developer Tools 
    * Manual Testing


## **Testing User Stories**

| **User Stories** |  Tested |  Works As Intended |
|  --- | --- | --- |
| As an **admin**, I can **access an admin profile** | ✅ | ✅
| As an **admin**, I can **view / edit / delete user profile information** |✅ | ✅
| As a **first-time site visitor** I can **sign-up** |✅ | ✅
| As a **user**, I can **sign-in and out of an account** |✅ | ✅
| As a **user**, I can **view posts** |✅ | ✅
| As a **user**, I can **add comments** |✅ | ✅
| As a **user**, I can **like a post** |✅ | ✅
| As a **user**, I can **unlike a post** |✅ | ✅
| As a **user**, I can **create a post** |✅ | ✅
| As a **user**, I can **update my post** |✅ | ✅
| As a **user**, I can **delete my post** |✅ | ✅
| As a **user**, I can **search for a post** |✅ | ✅
| As a **user**, I can **get to my user profile** |✅ | ✅
| As a **user**, I can **update my profile information** |✅ | ✅

## **Automated Testing**

* I have not used any Automated Testing, but I hope to learn more about this functionality for my next project.

## **Testing Accessibility and Performance**

* Testing for accessibility and performance is managed using the Lighthouse tool in Chrome extension:

These results are **before improvements**:

    * For Desktop:

    | Section | Performance | Accessibility | Best Practices | SEO |
    | --- | --- | --- | --- | --- |
    | Index | 76 | 91 | 92 | 82 |
    | All Posts | 75 | 94 | 92 | 90 |
    | Login | 100 | 94 | 92 | 90 |
    | Profile Dashboard | 88 | 94 | 83 | 91 |
    | Article View | 83 | 93 | 92 | 91 |
    | Post Creation | 98 | 94 | 92 | 90 |

    * For Mobile devices:

    | Section | Performance | Accessibility | Best Practices | SEO |
    | --- | --- | --- | --- | --- |
    | Index | 66 | 93 | 92 | 85 |
    | All Posts | 64 | 93 | 92 | 92 |
    | Login | 99 | 95 | 92 | 92 |
    | Profile Dashboard | 92 | 94 | 83 | 92 |
    | Article View | 94 | 94 | 92 | 92 |
    | Post Creation | 97 | 95 | 92 | 92 |

## **Code Validation**

* **W3C HTML Code Validator**

    * Each page of the deployed website was run through the [HTML Markup Validation Service](https://validator.w3.org/) and returned only a few errors, most of them which were complaining about the static urls. 1 or two warnings / erros about wrapping a tags within buttons. That was a quick fix by just removing the button element and gave the a tag bootstrap classes.

* **W3C CSS Jigsaw Validator**

    * CSS code was tested with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) via direct input and returned no errors.

* **JSHint validator**

    * No custom JavaScript code has been written for this project, only what is included with Bootstrap4. 

* **Python Validator**

    * The only problem I am getting are lines too long. All the problems are now solved after going through all the documents (28.02.23).

    ** <u>**NOTE**</u> **

    * At the time of testing (27/02/2023), the [PEP8 Online Service](http://pep8online.com/) has been down for a while.
    * In order to carry out effective validation of standardised Python, the following was done in the GitPod terminal:
        * Run the command `pip3 install pycodestyle`. It may be that this is already installed by default, that being the case, the requirement is met and nothing will happen.
        * Press CTRL+Shift+P (or Cmd+Shift+P on Mac) and type `linter` into the search tab that appears.
        * Click on `Python: Select Linter` from the filtered results.
        * Select `pycodestyle` from the list.
        * PEP8 errors will now be underlined in red and shall also appear in the `PROBLEMS` part of the terminal.


# **Bugs during development**

## **Fixed bugs and solutions:**

* Static Files failed to load when running the server

    * _Solution: '/' was incorrectly placed before the file path._

* When using smaller screens, the navigation bar felt quite chunky and took up a lot of the screen.

    * _Solution: Modified navbar position to static and created a toggle button for the navbar links for screens tablet size or smaller using Bootstrap._

* Text Field for post-creation, comments, post-updates were challenging to make responsive. 

    * _Solution: Discovered that I could target the specifc fields through parent-child relationships with other elements around._


# **Development and deployment**

The development environment used for this project was GitPod. Regular commits and pushes to Github have been employed to be able to track and trace the development process of the website. The Gitpod environment for this particular project was created using a template provided by Code Institute.

For local deployments instructions shall be written below, along with instructions with deployment to Heroku, the hosting service used to deploy this particular website. Heroku was chosen as the hosting service due to its database maintenance capabilities. 

## **Local Deployment**

This repository can be cloned and run locally with the following steps:

1. Login to [GitHub](https://www.github.com).
2. Select repository named: [keironchaudhry/p4-lingomeets](https://github.com/AVTpepper/news-app).
3. Click code toggle button and copy the url (i.e., https://github.com/AVTpepper/news-app.git).
4. In your IDE, open terminal and run the git clone command (i.e., git clone https://github.com/AVTpepper/news-app.git).
5. The repository will now be cloned in your workspace.
6. Create an [env.py file](https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1) (this file should normally be included in .gitignore, therefore it'll not be committed publicly in the root folder of your project) and add in the following code with the relevant key, value pairs, and ensure you enter the correct key values. For example:

`import os`

`os.environ['SECRET_KEY'] = 'ADDED_BY_YOU'`

`os.environ['DATABASE_URL'] = 'ADDED_BY_YOU'`

`os.environ['CLOUDINARY_URL'] = 'ADDED_BY_YOU'`

7. Install the relevant packages as per the requirements.txt file
8. In `settings.py` file, ensure the connection is set to either the Heroku Postgres Database or the local SQLite database
9. Ensure debug is set to true in the `settings.py` file for local development
10. Add 'localhost', to the ALLOWED_HOSTS variable in `settings.py`
11. Run `python3 manage.py showmigrations` to check the status of the migrations
12. Run `python3 manage.py migrate` to migrate the database
14. Start the application by running `python3 manage.py runserver`

## **Deployment to Heroku**

Deployment to Heroku can be done with the following guideline:

1. Create an account on Heroku
2. Create an app and give it the desired name and select a region
3. Create an account on ElephantSQL.
4. Click on 'Create an instance'
5. Give your app a Name, select the appropriate Plan and then select a region and data-center closest to your location.
6. Once details are completed, click 'Create instance'. 
7. Copy and paste the dashboard `DATABASE_URL` and paste it into Heroku Config Vars in Settings, and be sure to set your `env.py` in your project IDE to the same URL. 
8. The `DATABASE_URL` needs to be set as an environment variable in both Heroku and in the IDE local environment variables
9. Create a `Procfile` with the following text: `web: gunicorn project_name.wsgi`
10. Make sure you add your environment variables (env.py) to Heroku's Config Vars
11. Ensure `Debug` is set to `False` in the settings.py file
12. Add 'localhost', and 'project_name.herokuapp.com' to the `ALLOWED_HOSTS` variable in `settings.py`
13. Run `python3 manage.py showmigrations` to check the status of the migrations
14. Run `python3 manage.py migrate` to migrate any necessary data to the database
15. Run `python3 manage.py createsuperuser` to create an admin user
16. Connect the app to GitHub, and enable automatic deploys from main (or you can manually deploy).
17. Click 'deploy' to deploy your application to Heroku for the first time


# **Credits**

## **Code**

The following websites proved to be both insightful and helpful during development of this project:

* [Stack Overflow](https://stackoverflow.com/)
* [W3School](https://www.w3schools.com/)
* [GeeksForGeeks](https://www.geeksforgeeks.org/)
* [YouTube](https://www.youtube.com/) - [Desphixs](https://www.youtube.com/watch?v=OBsLgCm-Ayo&list=PL_KegS2ON4s580mS3nPt5x_eu6kO2cvOc&ab_channel=Desphixs)

# **Acknowledgments**

For inspiration, guidance and inputs, thank you to:

* Maranatha Ilesanmi

    My mentor from Code Institute.
    
* Keiron Liam Chaudhry

    Code Institute Hackathon buddy providing troublshooting help and a wonderful README.md template!

* Iuliia Konovalova

    Another Code Institute Hackathon buddy taking time out of her day just to have a look at my project! Always nice with another set of eyes, thanks!

* Code Institute Tutors

    Thanks for being available for questions when I was in dire need!
