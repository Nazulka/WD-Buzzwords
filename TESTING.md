## **Testing**
___
___
### Table of Contents

  * [Code Validity](#code-validity)
  * [Testing User Stories](#testing-user-stories)
  * [Functionality Testing](#functionality-testing)
  * [Defensive Design Testing](#defensive-design-testing)
  * [Responsiveness](#responsiveness)
  * [Usability Testing](#usability-testing)
  * [Performance Testing](#performance-testing)
  * [Browser Compatibility Testing](#browser-compatibility-testing)


### Code Validity
___

- HTML Markup Validation - [pass](https://validator.w3.org/nu/)
  * All pages passed the validator except for errors and warnings due HTML validator not being able to recognize Jinja.
- CSS Validation - [pass](https://jigsaw.w3.org/css-validator/)
- JavaScript Code Quality Tool JSHint - [pass](https://jshint.com/)
- PEP8 - [pass](http://pep8online.com/)


### Testing User Stories
___

- [x] **Guest user**

* As a guest user of WD Buzzwords, who is visiting the site for the first time, I want to understand easily what the site is about.
  * The Home page features a 'Welcome' section to offer new visitors more information on what this site is about. It also contains two sections with call to action buttons that aim
   to spark curiosity and lead visitors to the other pages of the website. The parallax image visually supports the content and adds interactivity to the page.
* As a guest user of WD Buzzwords, I want to be able to use the searchbox to search for terms that I would like to find out more about.
  - The search box is clearly labelled and easily accessible from the Home Page.
* As a guest user of WD Buzzwords, I want to browse web development terms and jargons and look up meanings without needing to register to the website.
  - The Glossary Page contains all the terms and is visible to all visitors to the website, whether they are registered or not.
* As a guest user of WD Buzzwords, I want to be able to easily access all available website features from different screen size devices.
  - The website is fully responsive and designed to provide an optimal user experience, no matter what device users are accessing it from.
* As a guest user of WD Buzzwords, I want to be able to filter terms by letters of the alphabet.
  - The Alphabet Filter buttons are accessible to all users and allow them to narrow down the results displayed on the Glossary page.
* As a guest user of WD Buzzwords, I want to be able to easily register to the website.
  - The Welcome section on the Home page has got a call to action button to prompt guest users to sign up to access full features of the site.

- [x] **Registered user**

* As a registered user of WD Buzzwords, I want to be able to log in to the website using my username and password.
  - Log in page is easily accessible from the navbar and allows registered users to easily log in to their account.
* As a registered user of WD Buzzwords, I want to be able to contribute to the dictionary by adding new terms and their description.
  - When logged in, registered users are able to access Add Term page, which allows them to add a new term and it's description to the glossary.
* As a registered user of WD Buzzwords, I want to be able to view all my added entries on my Account page and update or delete them if necessary.
  - Logged in registered users can view all their added terms in their Account page. There are Edit and Delete buttons below each displayed term.
* As a registered user of WD Buzzwords, I want to be able to confirm deletion before deleting my entries.
  - If users wish to delete the term they've added previously, they have to confirm deletion by clicking on Delete button again on a pop-up modal.
    This was designed to avoid accidental deletion from the glossary.

- [x] **Site owner / admin**

* As a site owner of WD Buzzwords, I want to be able to monitor and regularly update the website.
  - The admin user is responsible for researching the newest terms and keeping the glossary up to date.
* As a site owner of WD Buzzwords, I want to be able to delete entries contributed by registered users if necessary.
  - The admin user is authorised to remove any content that is deemed irrelevant or inapropriate.

**[back to top](#testing)**

### Functionality Testing
___

- [x] **Home Page**

**Navigation Bar**

  - The Materialize navbar is fixed and is visible across all pages and on all screen size devices. The `.hide-on-med-and-down` class is working as expected and it collapses into a hamburger menu on Tablets and smaller devices.
  - The sidenav, which was used in conjunction with the fullscreen navigation is working as desired and is visible on screen sizes =< 992px.
  - All the links on both, navbar and a sidenav were checked by clicking and are working as intended, allowing users to jump to the linked page.
  - The brand logo link was also tested by clicking and is working correctly, as it takes users back to the Home page from anywhere on the site.

**Parallax**

* The parallax effect was tested by scrolling down the page. It is working as it should and the image moves slower than the rest of the page, creating a 3D effect and giving the page a very unique feel and look.


**Search box**

The input field was tested by:
* Entering terms that exist in the glossary and clicking the _Search button_ - the selected term is displayed in the Glossary Page
* Typing words that are not in the dictionary and clicking the Search button - _No matching results found_ message is displayed on the Glossary Page.

In both cases users see _Browse Terms_ button that refreshes the page and displays all the words contained in the glossary.
* Clicking on the _Search button_ without entering any value - _Please fill in this field_ message is displayed, prompting users to enter a value. All above described features are working as intended.


**Icon Boxes Section**

* All three links on these sections were clicked to test and are working as intended.
    * The first two buttons contain links to redirect users to the _Sign Up_ and _Browse All_ pages accordingly.
    * The link on the last section opens up a third-party website in a new tab.
* On small screen sizes each section takes up the full width of the screen.


**Footer**

* Materialize Sticky Footer is responsive and stays on the bottom of the page. It is visible on all pages and gets pushed down when there is a lot of content. This have been tested by reducing / increasing the screen width and is working as intended. 
* Change of colour and transition effects on hovering over Social Icons are working as intended. Social icons were tested by clicking on them, all links to the external websites are functioning as intended and open in new tabs.
* Copyright section is center-aligned and located directly below the Footer as intended.


- [x] **Glossary Page**

**Filter Results Buttons**

  * Verified that by default the Glossary page displays all existing terms (including ones contributed by the users) in alphabetical order. 
  * The _Back to top_ Materialize FAB is working as intended, it floats on right bottom corner of the page and when clicked takes users to the top of the page. 
  * In an unfortunate event of dictionary being empty, it displays a message: "No results found" and a _ADD TERM_ button to encourage users to make contributions.
  * The _Filter Results Buttons_ are functioning as expected. When clicked by the user it renders the results for the button clicked on the _Filtered Results_ page. If there are no terms in the dictionary starting with the letter displayed on the button, the page displays a message: "No results found for the letter _(clicked by the user)_" along with the _Browse Terms_ button to redirect users back to the Glossary Page. 

- [x] **Log In Page**

* The page only appears when the user is not logged in.
* Verified, the Flash message always pops up when users successfully log in to the website. 
* Link below the card was clicked to test and is functioning as it should, redirecting users to the _Sign Up_ page.


- [x] **Sign Up Page**

* Sign Up page only appears when the user is not logged in.
* Flash message pops up to confirm the successul registration.
* The link below the card is fully functional, redirects users to the _Log In_ page.


- [x] **Account Page**

* The page is only accessible after user logs in to the website.
* The _Add Term_ button is verified to redirect users to the Add Term page.
* The Account holder's contributed words displayed on the page in an alphabetical order.
* _Edit_ button is functioning as desired, allowing users to update the terms they contributed previuosly.
* _Delete_ button is working as intended and triggers _Confirm deletion_ pop up modal when clicked. Clicking on the _Delete_ button again on the modal will result in removal of the term from the glossary. Alternatively, if users clicked on it by accident or changed mind, they can click on the _Cancel_ button. 


- [x] **Add Term Page**

* The page is available for logged in users only.
* The image is rendered correctly.
* The form was tested by:
  * Entering a unique new term and description, it was verified that the form is working as intended allowing users to make a contribution to the dictionary. The flash message is correctly displayed after every successful contribution to the dictionary.
  * Entering a non-unique term: a warning flash message is displayed, informing the user that _This term already exist in the dictionary_. The entry is not added to the dictionary.


- [x] **Log Out Page**

* The page is visible for logged in users only.
* The _Log Out_ link on the navbar (sidenav on smaller screens) is working as expected and logs users out of their account when clicked.
* Further tests verified that users are then redirected to the _Log In_ page where a flash message pops up to confirm they've been logged out. 

- [x] **404 Error Page**

* Confirmed that the page is displayed as expected if users navigate to the broken or dead links.
* _Return to Home page_ link is working as intended and takes users back to the Home page. 


- [x] **500 Error Page**

* Confirmed that the page is rendered correctly if something has gone wrong on the web site's server.
* _Return to Home Page_ link is functioning properly and redirects users back to the Home page. 

**[back to top](#testing)**


### Defensive Design Testing
___
* **Registration attempt with an existing Username**

  :ballot_box_with_check: Returns flash message "Username already exists".
  ![username exists](static/img/img_test/test2.png)

* **Registration attempt with an unmatching Password and Confirm Passwors fields**

  :ballot_box_with_check: Returns flash message "Passwords don't match!".
  ![passwords don't match](static/img/img_test/test3.png)

* **Registration attempt with a Username and/or Password containing special charachters**

  :ballot_box_with_check: Displays form validation error message.
  ![passwords don't match](static/img/img_test/test5.png)

* **Log In attempt with an incorrect Username and/or Password**

  :ballot_box_with_check: Returns flash message "Incorrect Username and/or Password" to deter users from trying to guess either one of the fields.
  ![incorrect username and/or password](static/img/img_test/test4.png)

* **Attempts by user to delete terms not contributed by them**

  :ballot_box_with_check: Verified users are able to view their entries in their Account Page and only edit and delete the terms contributed by themselves. Only Admin user is authorised to delete other users' entries.
  ![account page](static/img/img_test/test6.png)

  :ballot_box_with_check: Confirmation delete modal pops up when users attempt to delete the term from the dictionary to avoid accidental deletion. 

  ![delete modal](static/img/img_test/test8.png)

* **Attempts to contribute a term that already exists in the dictionary**

  :ballot_box_with_check: Returns flash message "This term already exists in the dictionary!"  
  ![add term](static/img/img_test/test7.png)


**[back to top](#testing)**


### Responsiveness
___
The responsiveness of the website was tested on all popular devices, including iPhone 5/SE Android Pixel 2, Samgung Galaxy S5, iPhone 6/7/8, iPad, iPad Pro, etc using [Responsinator](https://www.responsinator.com/), [Am I Responsive](http://ami.responsivedesign.is/) as well as Google Dev Tools Device Mode. 

It was tested on physical devices including iPhone XR and iPad. All tests have shown that site is fully responsive and fits and adapts well to the different viewport size devices.


### Usability Testing
___
This website was tested for usability by my family and friends. They didn't experience any issues during the testing process and it was confirmed that the website was easy to use and navigate. They were able to intuitively use the interactive elements of the website, find the information they were looking for and easily understand the purpose of the website.


### Performance Testing
___
Performance testing was carried out using Lighthouse in Chrome Developer Tools. The tests had shown an excellent performance and accessibility results for desktop devices. 
Steps taken to improve performance for the mobile devices following the initial tests:
* Added ```aria-label="search"``` attribute to a search button.
* Used darker background-color for the navbar to improve legibility and increase contrast with the foreground **text.


### Browser Compatibility Testing
___
Device/Browser | Google Chrome    | Microsoft Edge   | Firefox          | Safari           | Internet Explorer |
-------------- | :---------------:|:----------------:| :---------------:| :---------------:| :----------------:|
Mobile Phone   |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| n/a               |
Tablet         |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| n/a               |
Desktop        |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| n/a               |


**[back to top](#testing)**