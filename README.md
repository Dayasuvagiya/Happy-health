# Kyros Employee Management

![Website responsiveness on multiple screen sizes](documentation/images/kyros.png)

Welcome to Kyros! This website has been built using Django, incorporating custom Python, HTML, and CSS elements. Our platform caters to both small and large organizations, providing a seamless and paperless solution for effortlessly inputting employee information. Users have the ability to create profiles, enabling them to efficiently manage and add employee details to their database.

[Live link to Kyros](https://kyros-emp-mgt-c05d2ad42403.herokuapp.com/)

<br>

# Table of Contents

1. [UX](#ux)

2. [The Strategy Plane](#the-strategy-plane)
    * [Targeted Users](#targeted-users)
    * [Site Goals](#site-goals)
    * [Project Goals](#project-goals)
3. [Agile Planning](#agile-planning)
    * [User Stories](#user-stories)
    * [Epic Breakdowns](#epic-breakdowns)
        * [Initial Installation](#initial-installation)
        * [Initial Deployment](#initial-deployment)
        * [Databases](#databases)
        * [Employee App](#employee-app)
        * [Contact Form](#contact-form)
        * [Front End Design](#front-end-design)
        * [Error Pages](#error-pages)
        * [Create Documentation](#create-documentation)
4. [Skeleton Plane](#skeleton-plane)
    * [Wireframes](#wireframes)  
5. [Technologies Used](#technologies-used)
    * [Languages & Frameworks](#languages--frameworks)
    * [Libraries & Tools](#libraries--tools)
6. [Design](#design)
    * [Colors](#colours)
    * [Fonts](#fonts)
7. [Project Structure](#project-structure)
    * [Features](#features)
        * [Home Page](#home-page)
        * [About Page](#about-page)
        * [Register Pages](#register-page)
        * [Login page](#login-page)
        * [Add Employee Page](#add-employee-page)
        * [List Of Employee Page](#list-of-employee-page)
        * [Update Page](#update-page)
        * [Contact Page](#contact-page)
        * [Logout](#logout)
        * [Navbar](#navbar)
        * [Footer](#footer)
    [Future Features](#feature-features)




# UX

## The Strategy Plane

### Targeted Users

- HR Professionals: HR professionals use the app to manage employee information efficiently.
- Business Owners and Managers: Business owners and managers rely on it for overseeing their workforce.
- Administrative Staff: Administrative personnel value its user-friendly interface for record-keeping.
- Startups and Growing Companies: Emerging businesses use it to scale their HR operations effectively.
- Training and Development Specialists: Specialists use it for tailored employee training.

### Site Goals

- User Account Creation: Enable HR professionals and authorized personnel to effortlessly create accounts, granting them access to manage employee data efficiently.
- Account Editing for Employee Management: Allow users to edit their account information, ensuring the accuracy of employee records and data.
- Employee Data Management: Provide users with the capability to easily add, edit, or delete employee details through the online platform, streamlining HR processes.
- Business Contact form: Users can contact for support and inquiries related to the employee management platform.

### Project Goals

- Develope a website for a company, and I believe it offers utility to both small and large organizations for effective employee management and data handling.

- Acquire the skills to design an application with complete CRUD functionality.

<br>

[Back to Top](#table-of-contents)

<br>

## **Agile Planning**

I utilized agile planning in the development of my project. This involved breaking down each feature into User Stories, outlining user expectations for the website. Each User Story was carefully considered and planned, leading to the creation of multiple tasks for implementing specific features.

To ensure effective prioritization, I categorized everything as Must Have, Should Have, Could Have, or Won't Have. This helped determine which aspects were of the highest importance for implementation.

As the primary focus of the website, I initially dedicated significant time to developing the data-adding system. Subsequently, as the project progressed, I made adjustments and added or updated tasks in response to evolving user needs within the website.

The Project board (documentation/images/agile2.png)

[Back to Top](#table-of-contents)

<br>

## User Stories

* Users will:

  * Find information about a company sservices and contact option.
  * Be able to use the website across all devices with responsive design.
  * Be able to create, update and delete Employe details.

* Users expect:

  * A website that looks well across all devices.
  * A website that works well, with minimum errors encountered.

## Epic Breakdowns

### Initial Installation 

> Install: Django, gunicorn, dj-database, psycopg2.
> Hide sensitive information by creating an env.py file.
> Create Employee management app.

### Initial Deployment

> First deployment to the Heroku app once basic framework for the project is in place.
> Create App in Heroku, Create Config Var files, Deploy from main branch.
> Create Database URL in Elephant SQL, Add the Database URL to env.py and Heroku Config Vars.

### Databases

> Create database models in project app and migrate them.
> Create and Migrate Database.
  - The database model has everything needed to add new employee and details.
  - For Home, a database model was created for the contact form.

### Employee App

> Create an app to allow users to add employee informations.
  - Create an app inside the Django project to allow users to add employee details.
  - Create form which will allow site users to add new employee.
  - Allow users to update any information added for an employee.
  - Allow users to delete perticuler employee.

### Contact Form

> Create a Contact Form and associated model to store contact submissions to the admin panel.
  - Create a contact form to insert into a template to allow users to send messages to the site admin
  - Create a model for the Contact form which will allow all submitted forms to be stored on the admin panel.

### Front End Design

> Create templates, a colour scheme, navigation and responsiveness for the website
  - Create templates for each page needed within the site, including the home page, a Add Employee page, a login/register page and pages for further information.
  - Design a website fitting of the theme with appropriate colours, easy to navigate, easily accessible information and has full screen reader capabilities.

An essential aspect of a website's success lies in its appearance and user-friendly design. It was crucial for the website to maintain a clean and professional layout, aligning seamlessly with the business's theme. To achieve this, we carefully selected a color scheme, images, and a logo that harmonized with the overall aesthetics. Furthermore, the website's responsiveness underwent rigorous testing, as detailed in the testing section.

## Error Pages

> Create custom error page templates for 404, 403 and 500 errors.
  - Add a custom 404 Page to show the user which error they encountered while keeping the base template and css of the website.


### Create Documentation

> Create both a README.md file and a Testing.md file to show the process of creating the project

[Back to Top](#table-of-contents)

<br>

## Skeleton Plane

### Wireframes

- I began this project by selecting a layout design using a wireframe. For the homepage, I opted for a Hero Image to instantly convey the business's purpose to users upon their initial view.

- This was done in Balsamiq Wireframes. 

<details><summary>Home Page</summary>
<img src="documentation/images/home_ui.png">
</details>

<details><summary>About Page</summary>
<img src="documentation/images/about_ui.png">
</details>

<details><summary>Login Page</summary>
<img src="documentation/images/login_ui.png">
</details>

<details><summary>Register Page</summary>
<img src="documentation/images/register_ui.png">
</details>

<details><summary>Login Page</summary>
<img src="documentation/images/login_ui.png">
</details>

<details><summary>Add Employee Page</summary>
<img src="documentation/images/add_emp_ui.png">
</details>

<details><summary>Employee List page</summary>
<img src="documentation/images/emp_list_ui.png">
</details>

<details><summary>Contact Page</summary>
<img src="documentation/images/contact_ui.png">
</details>

[Back to Top](#table-of-contents)

<br>

## Technologies Used

### Languages & Frameworks

- HTML
- CSS
- Javascript
- Boostrap 5
- Python
- Django

### Libraries & Tools

- [Am I Responsive](http://ami.responsivedesign.is/) was usedfor creating the multi-device mock-up at the top of this README.md file
- [Balsamiq](https://balsamiq.com/) to create the projects wireframes
- [Bootstrap 5](https://getbootstrap.com/). This project uses the Bootstrap library for UI components (Buttons, Card, Footer, Pagination, Navbar)
- [Favicon.io](https://favicon.io) for making the site favicon
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/) was used for debugging of the code and checking site for responsiveness
- [Boostrap icons](https://fontawesome.com/) - Icons from Boostrap icons were used throughout the site
- [CodeAnyWhere](https://app.codeanywhere.com/) was IDE used for writing code and to push the code to GitHub
- [Visualstudio](https://code.visualstudio.com/) was the IDE also used for writing code and to push the code to GitHub.
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [Google Fonts](https://fonts.google.com/) - for typography in project
- [Google Maps](https://maps.google.com/) - for sample location of the company

[Back to Top](#table-of-contents)

<br>

## Design

### Colours

Web app is utilizing bootstrap inbuilt dark background, which looks professional for business website and other colors were selected by site owner. It's a self custom design as per wish of Site Owner.

### Fonts

Google fonts were used for this project as it offers clean and legible design, which makes it easy to read on screens of different sizes and resolutions. It has a neutral appearance and doesn't have any distracting features that can make it difficult to read.


## Project Structure

# Features 

## Existing Features

### Home Page

![Hero Image](documentation/images/home.png)
- The home page features a hero image, with some text explaining the main purpose of the website.

![Customize Option Info](documentation/images/customize.png)

- The index page is split into multiple sections, with the information easy to read and eye catching to a visitor.

![Testimonial Section](documentation/images/testimonial.png)

- The index page is split into multiple sections, with the information easy to read and eye catching to a visitor.


<br>

[Back to Top](#table-of-contents)

<br>

### About Page
![About Page Image](documentation/images/about1.png)

- The "About Us" page serves as a source of essential information about company. Here, you'll discover why choosing our company is a wise decision and gain insight into identity and values.

![About Page Image](documentation/images/about2.png)

- The "About Us" page provides in-depth insights into our company's history, mission, and core values. It elucidates the compelling reasons for selecting our services and introduces you to the individuals who comprise our dedicated team. 

<br>

[Back to Top](#table-of-contents)

<br>

### Register Pages

![Register form](documentation/images/register.png)

- This feature is presenting registreation by user
- For registering User must provide a username password adn email ID.

### Login page

![Login form](documentation/images/login.png)

- Returning users with created account can get back and use the web app
- user must provide valid username and password


<br>

[Back to Top](#table-of-contents)

<br>

### Add Employee Page

![Add Employee Page](documentation/images/add_emp.png)

- "Add Employee" page is designed to facilitate the inclusion of new employees' information into system. This page typically allows HR professionals or authorized personnel to input essential details about a new employee, such as their name, ID, contact information, department, and current employment status. 

### List Of Employee Page

![List of Employee Page](documentation/images/list_emp.png)

- "List of Employee" page offers a concise, organized view of all employees' essential details, simplifying workforce management and access to crucial employee information.

### Update Page

![update Employee Page](documentation/images/update_emp.png)

- The "Update" page in the app allows authorized users to modify or edit existing employee information, ensuring that employee records remain accurate and up-to-date.

<br>

[Back to Top](#table-of-contents)

<br>

### Contact Page

![Contact Page](documentation/images/contact.png)

- The "Contact" page in the app provides a means for users to easily get in touch with the app's support or team.

### Logout

![Logout](documentation/images/logout_popup.png)

- When a user decides to log out from the app, a confirmation popup button will appear, seeking their final confirmation before logging out.

<br>

[Back to Top](#table-of-contents)

<br>

### Navbar

![Navbar Before](documentation/images/nav1.png)

![Navbar After](documentation/images/nav2.png)

- Our website's navigation menu offers a straightforward experience. Visitors can explore the "Home" and "About Us" pages. Registered users gain access to additional features, like "Add Employee," streamlining employee data management and enhancing their interaction with our platform.

### Footer

![Footer](documentation/images/footer.png)

Added simple footer to the website, including links to our social media profiles.

### Admin Page

![Admin Employee Details](documentation/images/admin_emp.png)

![Admin User Login Details ](documentation/images/user_login.png)

![Admin Contact](documentation/images/admin_contact.png)
- The Contact form submissions are saved to the admin panel. The name, email and message from the contact form is shown to the admin, to allow them to reply to the User easily.


[Back to Top](#table-of-contents)

<br>

## Future Features

- I have plans to enhance the website with improved features for registered users. Currently, there's no option to reset passwords or update email addresses. Additionally, I had intended to create individual employee cards with CRUD functionality and images, but time constraints have delayed this feature implementation on the already extensive project.

# Testing 
### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/)
  - The only warnings that were given were because of the nature of Django Template Syntax.
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/)
- Python
  - No errors were returned when passing through [CI Python Linter](https://pep8ci.herokuapp.com/)
  - The only error is showing for long line

### Lighthouse Testing
![Lighthouse Metrics](documentation/images/lighthouse.png)
  - Testing on Desktop has given a variety of scores, going from a score between 85 and 98 for Performance and a score between 83 to 92 for Best Practices. The last tests before submissions are posted below.
  - When tested on desktop, the website score 98 on performance.
  - An accessibility score is 96
  - The best practices score is 92 and SEO score is 100

<br>

 [Back to Top](#table-of-contents)

<br>

### Automated Testing

- I wrote some tests for the app, covering view.py, model.py, and form.py. However, the tests aren't as thorough as I'd prefer, mainly because I faced challenges in grasping how to write tests for specific aspects of my forms and views. Nevertheless, I acknowledge the significance of comprehensive testing within a project and intend to delve deeper into this area in the future, as I recognize its value.

### Manual Testing
- Manual testing has been done extensively and has been shown in separate file, located [here.](documentation/test.md)

### Other Testing
 - The website has been tested across various screen sizes, using the Chrome DevTools responsive device section, [Responsive Design Checker](https://responsivedesignchecker.com/) and by opening the website on Firefox, Chrome, 3 various sized Android phones.

<br>

[Back to Top](#table-of-contents)

<br>

# Bugs

#### Issue: Validation for adding phone number

##### Fix:

 - I previously addressed an issue where users were encountering errors when entering letters or non-numeric characters as phone numbers. To resolve this, I implemented an if statement that now prompts users to input a valid phone digit when non-numeric characters are detected, providing a more user-friendly experience.
 - I took support from slack family and google to resolve this issue.
 

#### Issue: login, registration

 - Previously, users were able to freely add, delete, and update data without the need for logging in or registering.

##### Fix:

 - I have now implemented a security measure. If a user attempts to access the data by copying and pasting the URL without being logged in or signed up, they will be automatically redirected to the login page. After successfully logging in, they will gain the necessary access to modify or add information.


# Bugs Not Fixed

#### Issue: User Personal profile

I developed the login and registration functionalities in my Django project without utilizing the Allauth library. Initially, I embarked on this path to deepen my understanding of Django's native methods. However, during the project's course, I encountered an issue where user registration resulted in data from another user being saved unintentionally. This occurred due to the absence of individual admin panels for users within my app.

To address this issue effectively, I would need to either implement the Allauth method or establish a more robust connection between user data and the database. However, given time constraints, I decided to leave the issue as is, with the intention of revisiting it in the future to implement a lasting solution. I recognize the importance of ensuring data integrity and individual user experiences and remain committed to addressing this concern comprehensively in due course.

<br>

[Back to Top](#table-of-contents)

<br>

# Credits and Sources

### Employee menagement app
- The Employee management app was based on reading and watching multiple walkthroughs of Django functionality.
- [Code Institute](https://learn.codeinstitute.net/)
- [Django](https://www.djangoproject.com/)
- [Youtube](https://www.youtube.com/)
- [Stackoverflow](https://stackoverflow.com/)
- [Freecodecamp](https://www.freecodecamp.org/news/tag/programming/)
- Mentor sessions have proven to be invaluable in aiding me and resolving any queries I encounter.

# Deployment

The following are the steps I went through to deploy my live site:

- The site was deployed using Heroku. The steps to deploy are as follows: 
1. Go to [Heroku](https://dashboard.heroku.com/apps)
2. Go to 'New' and select 'Create a new app'
3. Input your app name and create app.
4. Navigate to 'Settings'
5. On the Config Vars section, enter the following values:
    - SECRET_KEY: The Secret Key for your project
    - DATABASE_URL: The URL from your ElephantSQL dashboard
    - CLOUNDINARY_URL: The URL from your Cloudinary dashboard
    - PORT: 8000
6. Navigate to the 'Deploy' section. 
7. Connect to GitHub, search for your repo and confirm. 
8. Choose branch to deploy.
9. Your app should now be available to see. You can choose whether to have your app automatically redeploy with every push or to keep it manual. 

- To Fork the repository:
  - On GitHub.com, navigate to the repository.
  - In the top-right corner of the page, click Fork.
  - Select an owner for the forked repository.
  - By default, forks are named the same as their parent repositories. You can change the name of the fork to distinguish it further.
  - Optionally, add a description of your fork.
  - Choose whether to copy only the default branch or all branches to the new fork.
  - Click Create fork.

- To Clone the repository:
  - On GitHub.com, navigate to the repository.
  - Above the list of files, click the Code button.
  - Copy the URL for the repository.
  - Open Git Bash.
  - Change the current working directory to the location where you want the cloned directory.
  - Type git clone, and then paste the URL you copied earlier.
  - Press Enter. Your local clone will be created.
 
 <br>

Live link: [Kyros](https://kyros-emp-mgt-c05d2ad42403.herokuapp.com/)

<br>

<br>

[Back to Top](#table-of-contents)