# WD Buzzwords
___
___
WD Buzzwords is a crowdsourced dictionary where users can look up explanations to some of the most important terms and abbreviations they will come accross when working in web development and contribute to the dictionary to benefit others staring out in the industry. The live website can be found [here]().

## Table of Contents
___


## UX
___
### Strategy

**Project Goals**
* To create an easy to access platform which contains key web development buzzwords, ranging from most basic to the more technical.
* To provide users with an introduction to the most common terms in web development with clear and comprehensive definitions. 
* To allow users to quickly look up words in the dictionary and for registered users to add new terms as well as modify and delete their previous entries. 

#### User Stories
**Guest user**
* As a guest user of WD Buzzwords, I want to browse all web development terms and jargons and familiarize myself with their exact meanings without needing to register to the website. 
* As a guest user of WD Buzzwords, I want to be able to easily access all available website features from different screen size devices.
* As a guest user of WD Buzzwords, I want to be able to use the searchbox to search for terms that I would like to find out more about.
* As a guest user of WD Buzzwords, I want to be able to display the selected term and its description. 
* As a guest user of WD Buzzwords, I want to be able to browse terms alphabetically using the alphabet filter buttons. 
* As a guest user of WD Buzzwords, I want to be able to learn one of the latest entries to the website.
* As a guest user of WD Buzzwords, I want to be able to register to the website.

**Registered user**
* As a guest user of WD Buzzwords, I want to be able to log in to the website using my username and password. 
* As a registered user of WD Buzzwords, I want to be able to contribute to the dictionary by adding new terms and their description to the glossary.
* As a guest user of WD Buzzwords, I want to be able to edit the entries contributed by myself as well as their description.
* As a guest user of WD Buzzwords, I want to be able to view all my stored entries in my Account page.
* As a guest user of WD Buzzwords, I want to be able to delete the entries contributed by myself if necessary.
* As a guest user of WD Buzzwords, I want to be able to get a delete confirmation message before deleting my entries.

**Site owner / admin**
* * As a site owner of WD Buzzwords, I want to create an online educational resource, to promote understanding of web development terms and abbreviations, as well as crowdsource new terms and definitions to benefit users who are new to the sector.
* As a site owner of WD Buzzwords, I want to be able to monitor and regularly update the website to keep up-to-date and to meet users' expectations.
* As a site owner of WD Buzzwords, I want to be able to delete entries contributed by users if necessary.


### Scope
* To create a user friendly website using HTML, CSS, JavaScript, Python, Flask and MongoDB that ensures continuous, intuitive and fluid experience for the users. 
* To provide a learning aid that promotes understanding of web development terms and abbreviations and stimulates a desire to learn independently.
                                                                                              
### Structure
This website offers users the option to choose between the following two to accomodate their individual preferences:
* **Guest users** - (unauthenticated site visitors) can access selected functions in the navigation panel: Home, Glossary, Log In and Sign Up Pages.
* **Registered users** - once users decide to register to the website, they will be able to access full functionality and additionally access Account, Add Term and Log Out pages. 


### Skeleton
* [Desktop wireframes]()
* [Tablet and Mobile wireframes]()
* The wireframes have been changed quite a bit:

* Database Diagram

### Surface
#### Design
**Color Scheme**
* The color palette has been created using [Coolors](https://coolors.co/4db6ac-ffc400-c2185b-e0e0e0-eeeeee) and materialize color classes have been used in this project.
* I have chosen a base color of teal and a complimentary color orange to create contrast to the site and add depth. By using this bold combination, I aimed to create an inviting and relaxing design for the users. A splash of pink has been added for a contrast and light grey has been used to display the flash messages. 
![color palette](static/img/color-palette.jpg)

**Typography**
* Google Fonts *Special Elite* used to give a vintage style typewriter feel to the website logo.
* *Monserrat* used for headings to give the site less formal feel.
* *Average* for the all other elements as I found it complemented well the above two fonts. 

**Imagery**
* The Home page supporting image added to enchance the overall experience and is from [Unsplash](https://unsplash.com/photos/T6fDN60bMWY).


## Technologies Used
___
### Languages Used
* HTML5
* CSS3
* JavaScript
* Python

### Languages, Frameworks, Libraries and tools Used
#### Front-end
* **[Materialize CSS v1.0.0]**(https://materializecss.com/) - a front-end framework, used to create sleek, consistent, functional and responsive website. I wanted to familiarize myself better with Materialize as my previous two projects used Bootstrap. 
The main components used: navbar, sidenav, parallax, cards, modal, footer, etc.  
* **jQuery** - required to ensure proper rendering of the Materialize components listed above.
* **[Google Fonts]**(https://fonts.google.com/) for typography. 
* **[Font Awesome v5.15.3]**(https://fontawesome.com/icons?d=gallery&p=2) for icons in icons section, social icons and some of the buttons.
* **[Tinypng.com]**(https://tinypng.com/) - to reduce size and compress the images used in this project.
* **[RandomKeygen]**(https://randomkeygen.com/) - to create Fort Knox Password.
* **[Balsamiq]**(https://balsamiq.com/wireframes/desktop/) - to generate digital sketches for the project concept for better planning of the layout of the website.

#### Back-end
* **Flask** - a lightweight micro web framework written in Python used to create a simple, clean code and to reduce development time.
* **[MongoDB]**(https://www.mongodb.com/2) - non-relational database, used to store, manipulate and retrieve data.
* **[Werkzeug]**(https://werkzeug.palletsprojects.com/en/1.0.x/) - used with Flask to securely store passwords with salted hashes and verify user passwords to authenticate users.
* **Flask Jinja** - used as it's a part of a Flask package and to allow template inheritance.


#### Deployment
* **Git** - used for version control and to keep track of the changes made to the repository.
* **Gitpod** - open source development platform, allowed me to add, commit and push files to GitHub. 
* **GitHub** - used as a hosting service for version control and future collaborations.
* **Heroku** - my GitHub repo for this project had been connected to Heroku app to enable management and deployment of this app.


## Features
___

### Implemented Features

##### Features accessible for all users and admin
###### Home Page
**Navigation Bar** 
* Responsive Navigation Bar is created using Materialize Navbar class. It displays the website's logo on the left and on the right navigation links to the "Home", "Glossary", "Log In" and "Sign Up" Pages when the user is not logged in. 
* Brand Logo also serves Home Page link, which is particularly convenient when accessing the site on smaller screen size devices. 
* On screen sizes below 992px navbar is hidden and slide out menu comes into effect, which collapses into a hamburger menu bar when closed. 

**Parallax**
* A Materialize parallax image has been added to visually support the content and for added user interactivity.  

**Search WD Buzzwords** 
* The Search box's design has been inspired by this YouTube tutorial video by [Traversy Media](https://www.youtube.com/watch?v=MaP3vO-vEsg&t=2677s). However, the code has been modified and adapted to the site's needs. I also have modified classes and added "Search" and "Refresh" buttons. 

**Welcome Section**
* This section consists of a title and a paragraph text that explains the concept of the website. 

**Icon Boxes Section** 
* This section is made of two Materialize card-panels, with added Font Awesome Icons and call to action buttons. The first panel invites users to sign-up to the website and the second one guides users to the Glossary Page to browsw all terms. 
* The bottom part of the section is for users who would like to purchase a Glossary in a book form and includes a link to an external third-party site that opens up in a new tab. 

**Footer**
* Designed using Materialize Sticky Footer component, it's responsive and always stays on the bottom the page unless there is a lot of content, when it gets pushed down. Contains hoverable Social Media icons to let users know they are clickable. Icons are linked to the external websites and open in new tabs when clicked. 
* Copyright section is directly below the Footer and contains Copyright information.


###### Glossary Page
**Filter Results Section**
* Contains letters of the alphabet so users can click and select


#### CRUD Functionality




### Future Features 


## Testing
___
### Create Testing.md


### Issues and Solutions

## Deployment
___



## Credits
___

### Media 
* A parallax image for the Home Page is taken from [Unsplash](https://unsplash.com/photos/T6fDN60bMWY)
* A new entry submission chart is taken from [Macmillian Dictionary](https://www.macmillandictionary.com/open-dictionary/submit.html) 
* Favicon icon made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com


### Code

## Acknowledgements
___

