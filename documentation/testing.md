## Manual Testing 

Testing has taken place continuously throughout the development of the project. Each view was tested regularly. When the outcome was not as expected, debugging took place at that point.

### W3C Html Validator

- No bug was found during Html validation
-- The only warnings that were given were because of the nature of Django Template Syntax.

### W3C CSS Validator

- No bug was found during CSS Validation

### CI Python Linter

- No bug was found during Python Validation
- The only error is showing for long line

### Heroku Deployment

- Error was shown while deploying in Heroku.
- The same was resolved updating requirements.txt file after trying again it works proprely. 
- Maybe the error was because of diffrent version of Django.

This table shows all the manual testing done for the website, and whether it worked as expected or not.

### Features

Feature Tested | Expected Result | Actual Result
---------------|-----------------|---------------
NavBar responsiveness | NavBar becomes hamburger menu on below mediam screen | As expected
Images resize on mobile | Images resize on mobile | As expected
Layout becomes linear on mobile | Layout becomes linear on mobile | As expected |
Form Buttons transparent coour on hover | Form Buttons transparent coour on hover | As expected
Messages are displayed for user action | All messages shown as expected | As expected
Footer links all work when clicked | Footer links all work when clicked | As expected
Button on home page for users not logged in | button redirects to Register Page | As expected
Other URLs without login | page redirects to login | As expected
Contact form renders on Contact button | contact.html renders | As expected 
Contact form saves to admin panel | admin panel shows message, name and email | As expected
User gets feedback on contact form submission | Message "Thank you for connecting us!" displays | As expected
Registration page validates each required input| message appear to fill the field | As expected
Add employee, list of employee and contact links are hidden until a user is logged in | Only show when logged in | As expected
User gets feedback message on Adding new employee confirmation | message "You added new employee successfully" displays | As expected
Page redirects to list of employee | renders on list of employee page | As expected
User added employee shown on list of employee page(home_emp.html) | User added employee shown on list of employee page | As expected
Curruntly working checkbox true if employee working | Pass true on select | As expected
Update button brings user to update any details of employee | update emp page render renders | As expected
update button on update emp page redirects back to list of employee page | home_emp.html renders | As expected
Delete button delete emoloyee details| delete emoloyee details | As expected
Confirmation message on user_delete shows | message "Successfully deleted an employee details" shown | As expected
User redirected to logout confirmation popup when Logout is clicked | Option to logout or close | As expected
User redirected to Profile Logout is cancelled | Back to current page  | As expected
User redirected to login page when logged out | login.html renderes | As expected
User shown log out message feedback | message "Successfully signed out, see you next time!" shown | As expected
User tried to render user_profile URL when not logged in | user redirected to log in page | As expected