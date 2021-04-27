## Testing

---

---

### Code Validity

- HTML Markup Validation
- CSS Validation
- JavaScript Code Quality Tool JSHint
- PEP8

### Testing User Stories

- [x] **Guest user**

* As a guest user of WD Buzzwords, who is visiting the site for the first time, I want to understand easily what the site is about.
  - The Home page has a 'Welcome' section to offer new visitors more information on what this site is about. It also contains two sections with
    call to action buttons to spark curiosity and lead visitors to the other pages of the website. The parallax image visually supports the content and adds interactivity to the page.
* As a guest user of WD Buzzwords, I want to be able to use the searchbox to search for terms that I would like to find out more about.
  - The search box is clearly labelled and easily accessible from the Home Page.
* As a guest user of WD Buzzwords, I want to browse web development terms and jargons and look up meanings without needing to register to the website.
  - The Glossary Page contains all the terms and is visible to all visitors to the website, whether they are registered or not.
* As a guest user of WD Buzzwords, I want to be able to easily access all available website features from different screen size devices.
  - The website is fully responsive and designed to provide an optimal user experience, no matter what device users are accessing it from.
* As a guest user of WD Buzzwords, I want to be able to filter terms by letters of the alphabet.
  - The alphabet filter buttons are accessible to all users and allow them to narrow down the results dispalyed on the Glossary page.
* As a guest user of WD Buzzwords, I want to be able to easily register to the website.
  - The Welcome section on the Home page has got a call to action button to prompt guest users to sign up to access full features of the site.

- [x] **Registered user**

* As a registered user of WD Buzzwords, I want to be able to log in to the website using my username and password.
  - Log in page is easily accessible from the navbar and allows registered users to easily log in to their account.
* As a registered user of WD Buzzwords, I want to be able to contribute to the dictionary by adding new terms and their description.
  - When logged in, registered users are able to access Add Term page, which allows them to add a new term and it's description to the glossary.
* As a registered user of WD Buzzwords, I want to be able to view all my added entries in my Account page and update or delete them if necessary.
  - Logged in registered users can view all their added terms in their Account page. There are Edit and Delete buttons below each displayed term.
* As a registered user of WD Buzzwords, I want to be able to confirm deletion before deleting my entries.
  - If users wish to delete the term they've added previously, they have to confirm deletion by clicking on Delete button again on a pop-up modal.
    This was designed to avoid accidental deletion from the glossary.

- [x] **Site owner / admin**

* As a site owner of WD Buzzwords, I want to be able to monitor and regularly update the website.
  - The admin user is responsible for researching the newest terms and keeping the glossary up to date.
* As a site owner of WD Buzzwords, I want to be able to delete entries contributed by registered users if necessary.
  - The admin user is authorised to remove any content that is irrelevant or inapropriate.

### Functionality Testing

- [x] **Navigation Bar**

  - The Materialize navbar is fixed and is visible on all screen size devices. The included `.hide-on-med-and-down` class is working as expected and collapses into a hamburger menu on Tablets and smaller devices.
  - The sidenav which is used in conjunction with the fullscreen navigation is working as desired and is visible on screen sizes =< 992px.
  - All the links on both, navbar and a sidenav were checked by clicking and are working as intended, allowing users to jump to the linked page.
  - The brand logo link was also tested by clicking and is working correctly, as it takes users back to the Home page from anywhere on the site.

- [x] **Parallax**

  - The parallax effect was tested by scrolling down the page. It is working as it should and the image moves slower than the rest of the page making the page more engaging.

- [x] **Search box**

The input field was tested by:
* Entering terms that exist in the glossary and clicking the _Search button_ - the selected term is displayed in the Glossary Page
* Typing words that are not in the dictionary and clicking the Search button - users see the message _"No matching results found!"_ on the Glossary Page.

In both cases users see _Browse Terms_ button that refreshes the page and displays all the words contained in the glossary.
* Clicking on the _Search button_ without entering any value - _Please fill in this field_ message is displayed, prompting users to enter a value. All above described features work as intended.

- [x] **Icon Boxes Section**
* All three links on these sections were clicked to test and are working as intended.
    * The first two buttons contain links to redirect users to the _Sign Up_ and _Browse All_ pages accordingly.
    * The link on the last section opens up a third-party website in a new tab.
* On small screen sizes each section takes up the full width of the scree.


- [x] **Footer**
* Visible on all pages.
* Materialize Sticky Footer is responsive and stays on the bottom of the page. It gets pushed down when there is a lot of content. This have been tested by reducing / increasing the screen width and is working as intended. 
* Change of colour and transition effects on hovering over Social Icons have been tested and working as intended.
Social icons were tested by clicking on them, all links to the external websites are functioning as intended and open in new tabs.
* Copyright section is center-aligned and located directly below the Footer as intended.

- [x] **Filter Results Buttons**
* Verified that by default the Glossary page displays all existing terms (including ones contributed by the users) in alphabetical order. 
* The _Back to top_ Materialize FAB is working as intended, it floats on right bottom corner of the page and when clicked takes users to the top of the page. 
* The _Filter Results Buttons_ 

+++++++++++++++++++
+++++++++++++++++++++


- [x] **Log In Page**
* Verified, the Flash message always pops up when users successfully log in to the website. 
* Link below the card was clicked to test and is functioning as it should, redirecting users to the _Sign Up_ page.

- [x] **Sign Up Page**
* Flash message pops up to confirm the successul registration.
* The link below th ecard is fully functional, redirects users to the _Log In_ page.

- [x] **Account Page**
* The user's contributed words displayed on the page in an alphabetical order.
* _Edit_ button is functioning as desired, allowing users to update the terms they contributed previuosly.
* _Delete_ button is working as intended and _Confirm deletion_ modal pops up if users click on it. Clicking on the _Delete_ button again on the pop up modal will result in removal of the term from the glossary. Alternatively, if users clicked on it by mistake or changed mind, they can click on the _Cancel_ button. 

- [x] **Add Term Page**
* The image is rendered correctly.
* The form was tested by entering a new term and description and is working as intended.
* The flash message is correctly displayed after every successful contribution to the dictionary.

- [x] **Log Out Page**
* The _Log Out_ link on the navbar (sidenav on smaller screens) is working as expected and logs users out of their account when clicked.
* Further tests verified that users then redirected to the _Log In_ page where a flash message pops up to confirm they've been logged out. 


### Usability Testing

### Performance Testing

### Compatibility Testing

### Defensive Design Testing
