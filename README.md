# [ProFit-PT](https://pro-fit-pt-dcb56d3b7224.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/DavidFB94/pro-fit-pt)](https://github.com/DavidFB94/pro-fit-pt/commits/main)

[![GitHub last commit](https://img.shields.io/github/last-commit/DavidFB94/pro-fit-pt)](https://github.com/DavidFB94/pro-fit-pt/commits/main)

[![GitHub repo size](https://img.shields.io/github/repo-size/DavidFB94/pro-fit-pt)](https://github.com/DavidFB94/pro-fit-pt)

## Overview

ProFit-PT is an e-commerce website where the customer can hire personal trainers for in person training, creating personalized workout plans, and fitness counseling.

This website was built as a project for the Diploma in Full Stack Software Development at Code Institute.

## Mockup

![screenshot](documentation/mockup.png)

## UX

I started out with Wireframes for both desktop and mobile.

The basic structure for services and service details was created. I did not have any wireframes for the profile/cart/checkout, so I used the CI Boutique Ado walk-through for those pages.

After the base structure for viewing and purchasing services was complete, I moved on the the about/faqs/contact pages. Originally, I had planned for separate pages for all of them, but as the pages started taking shape, I combined some of their functionalities to make related information easier to find.

### Colour Scheme

-  `##4C4C4C` used for primary text.

-  `#f5f5f5` used for primary highlights.

-  `#FFFFFF` used for secondary text.

-  `#4C4C4CBF` used for secondary highlights.

I used [coolors.co](https://coolors.co/ffffff-f5f5f5-4c4c4c) to generate my colour palette.

![screenshot](documentation/color-palette.png)

### Typography

- [Lato](https://fonts.google.com/specimen/Lato) was used for all text.

- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the search icon and tag icon for categories.

## User Stories

### Site Users

- As a customer I can register an account so that I can log in, and use the site in an authorized and secure way.

- As a customer I can  receive a email confirmation after account registration so that I know that my registration was successful.

- As a customer I can log in with my account information so that I can fully use the sites features.

- As a customer I can log out from my account so that I can avoid unauthorized access to my data.

- As a customer I can view services so that I can see the sites supply.

- As a customer I can view service details so that I can see detailed service information and make informed purchasing decisions.

- As a customer I can search for a service by name or description so that I can find a specific service I'd like to purchase.

- As a customer I can sort the list of services so that I can easily identify the product I might be interested in.

- As a customer I can add services to my shopping cart, view the contents of my cart and proceed to checkout, so that I can complete my purchase quickly and easily.

- As a customer I can proceed to checkout/payment so that I can pay for my services and enter my delivery information.

- As a customer I can receive a purchase confirmation e-mail so that I know that my order was successful.

- As a customer I can access my profile so that add/review information about my account.

- As a customer I can save my information so that I can have a faster checkout process when coming back to the site.

- As a customer I can view my order history so that I can track my purchases.

- As a customer I can fill out a contact form so that I can send messages to the site admin.

- As a customer I can find a FAQ section so that I can easily find answers to common questions regarding the site.

- (Future Feature) As a customer I can sign up for a newsletter so that I can receive the latest news and deals.

### Site Admin

- As a site admin I can moderate users and their data in the admin dashboard so that I can make changes when required.

- As a site admin I can receive a contact form so that I can have direct contact with the customers.

- As a site admin I can mark contact messages as "read" so that I can keep track on which messages I have reviewed.

- As a site admin I can add/edit/delete FAQs so that I can make the site easier to use for the customer.

- As a site admin I can add/edit/delete services so that I can manage my service inventory.

- (Future Feature) As a site admin I can send mass emails to users, if they have signed up for it, so that I can increase traffic and sales on the site.

## Wireframes
Wireframes were developed for mobile and desktop sizes.

I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

### Mobile Wireframes

<details>
<summary> Click here to see the Mobile Wireframes </summary>

Home
- ![screenshot](documentation/wireframes/mobile-home.png)

Services
- ![screenshot](documentation/wireframes/mobile-services.png)

Service Details
- ![screenshot](documentation/wireframes/mobile-service-details.png)

About
- ![screenshot](documentation/wireframes/mobile-about.png)

Contact
- ![screenshot](documentation/wireframes/mobile-contact.png)

FAQs
- ![screenshot](documentation/wireframes/mobile-faqs.png)

</details>

### Desktop Wireframes

<details>
<summary> Click here to see the Desktop Wireframes </summary>

Home
- ![screenshot](documentation/wireframes/desktop-home.png)

Services
- ![screenshot](documentation/wireframes/desktop-services.png)

Service Details
- ![screenshot](documentation/wireframes/desktop-service-details.png)

About
- ![screenshot](documentation/wireframes/desktop-about.png)

Contact
- ![screenshot](documentation/wireframes/desktop-contact.png)

FAQs
- ![screenshot](documentation/wireframes/desktop-faqs.png)

</details>

## Features

### Existing Features

 **#1 Header with Logo home redirect**

- Adds maneuverability to the site.

![screenshot](documentation/features/feature-01.png)

**#2 Navbar links to "Our Services"  in drop-down menu**

-  Includes links to all services and service categories. Adds maneuverability to the site.

![screenshot](documentation/features/feature-02.png)

**#3 Navbar links to About/FAQs and Contact section**

- Adds maneuverability to the site.

![screenshot](documentation/features/feature-03.png)

**#4 Search field**

- For search queries. Adds maneuverability to the site. Makes it easier for the user to find what they are looking for.

![screenshot](documentation/features/feature-04.png)

**#5 "My Account" drop-down menu**

- Includes link to register/login/logout, profile page (registered users), and "Add Services" (for admin users only). Adds maneuverability to the site.

![screenshot](documentation/features/feature-05.1.png)
![screenshot](documentation/features/feature-05.2.png)
![screenshot](documentation/features/feature-05.3.png)

**#6 Cart display**

- Updates with cart content being added. Displays total cost. Link to "Shopping cart". Adds maneuverability to the site. Provides visual feedback for the user. Displays a cart preview when an item is added, with link to shopping cart.

![screenshot](documentation/features/feature-06-1.png)
![screenshot](documentation/features/feature-06-2.png)
![screenshot](documentation/features/feature-06-3.png)

**#7 Site Banner**

- Highlights the sites deal to get price reduction for buying more services at once. Will encourage users to buy more.

![screenshot](documentation/features/feature-07.png)

**#8 Feedback messages**

- Toast messages are displayed on user action. Message: Success, Error and Info. Provides instant feedback to the user.

![screenshot](documentation/features/feature-08-1.png)
![screenshot](documentation/features/feature-08-2.png)
![screenshot](documentation/features/feature-08-3.png)

**#9 Landing page**

- Includes inspiring message for the sites services and link to Personal Training category. Adds maneuverability to the site. Makes it easy for the user to find the sites main service.

![screenshot](documentation/features/feature-09.png)

**#10 Our services cards**

- Services display with all services, shown in a paginated list. Includes "Services home" link, number of found services, sorting and current category (if selected). Displays service name, image, category tag, description and starting price.

![screenshot](documentation/features/feature-10.1.png)
![screenshot](documentation/features/feature-10.2.png)
![screenshot](documentation/features/feature-10.2.png)

**#11 Service cards edit/delete links (ADMIN ONLY)**

-  Links to edit/delete a service (ADMIN ONLY). Includes a delete confirmation popup modal.

![screenshot](documentation/features/feature-11.1.png)
![screenshot](documentation/features/feature-11.2.png)
![screenshot](documentation/features/feature-11.3.png)

**#12 Service cards Read More link**

- "Read More" link to service details.

![screenshot](documentation/features/feature-12.png)

**#13 Service details**

- Display service details. Displays service name, image, category tag, full description. Includes "Buy sessions" section, with quantity selection drop-down, price per unit + total price, and "Add to cart" link. Also includes edit/delete links (ADMIN ONLY).

![screenshot](documentation/features/feature-13.png)

**#14 Shopping Cart**

- Displays items in the cart with service info and grand total. Includes links to keep shopping, remove an item and checkout.

![screenshot](documentation/features/feature-14.1.png)
![screenshot](documentation/features/feature-14.2.png)

**#15 Checkout**

- Checkout form with order summery. Includes option to save customer information to their profile (if registered user), card payments with Stripe, link back to current cart, total charge amount, and complete order button.

![screenshot](documentation/features/feature-15.png)

**#16 User registration**

- Sign Up form for user registration. Includes links to home page, and sign up button for completing the form. User verification
by email.

![screenshot](documentation/features/feature-16.1.png)
![screenshot](documentation/features/feature-16.2.png)
![screenshot](documentation/features/feature-16.3.png)
![screenshot](documentation/features/feature-16.4.png)

**#17 User Sign in**

- Sign in form for user login. Includes links to home page, and confirmation button for signing in. 

![screenshot](documentation/features/feature-17.png)

**#18 User Log out**

- Log out screen with log out confirmation. 

![screenshot](documentation/features/feature-18.png)

**#19 User Profile**

- Default User Information form and order history. Includes option to save/update customer information to their profile (if registered user), which will be used in the next checkout. Order history includes links to the order summary on previous orders.

![screenshot](documentation/features/feature-19.png)

**#20 About/FAQs page**

- About us section with site description, links to partners, facebook and privacy statement. FAQs section with accordion to save screen space (FAQs can be added/edited/removed in admin dashboard).

![screenshot](documentation/features/feature-20.png)

**21 Contact page**

- Includes contact form to send a message to the admin (can be read in the contacs tab in the dashboard) and a section for phone contact and phone-line operating hours. 

![screenshot](documentation/features/feature-21.png)

### Future Features

 **#1 Newsletter signup**

- Newsletter signup form, to add the email address to the database for newsletter emails.

 **#2 Sending mass emails**

- Sending emails to all users that has signed up for the newsletter.

 **#3 Front end pricing tier creation**

- Allowing for new pricing tiers to be created in the front end for admins

## Tools & Technologies Used

- [![Markdown Builder](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://tim.2bn.dev/markdown-builder) used to generate README and TESTING templates.

- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)

- [![GitHub](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage.

- [![Gitpod](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) used as a cloud-based IDE for development.

- [![HTML](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) used for the main site content.

- [![CSS](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.

- [![JavaScript](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) used for user interaction on the site.

- [![jQuery](https://img.shields.io/badge/jQuery-grey?logo=jquery&logoColor=0769AD)](https://jquery.com) used for user interaction on the site.

- [![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language.

- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) used for hosting the deployed back-end site.

- [![Bootstrap](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.

- [![Django](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) used as the Python framework for the site.

- [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) used as the relational database management.

- [![PostgreSQL by Code Institute](https://img.shields.io/badge/PostgreSQL_by_Code_Institute-grey?logo=okta&logoColor=F05223)](https://dbs.ci-dbs.net) used as the Postgres database from Code Institute.

- [![Cloudinary](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) used for online static file storage.

- [![WhiteNoise](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) used for serving static files with Heroku.

- [![Stripe](https://img.shields.io/badge/Stripe-grey?logo=stripe&logoColor=008CDD)](https://stripe.com) used for online secure payments of ecommerce products/services.

- [![Gmail API](https://img.shields.io/badge/Gmail_API-grey?logo=gmail&logoColor=EA4335)](https://mail.google.com) used for sending emails in my application.

- [![Balsamiq](https://img.shields.io/badge/Balsamiq-grey?logo=barmenia&logoColor=CE0908)](https://balsamiq.com/wireframes) used for creating wireframes.

- [![Font Awesome](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) used for the icons.

- [![ChatGPT](https://img.shields.io/badge/ChatGPT-grey?logo=chromatic&logoColor=75A99C)](https://chat.openai.com) used to help debug, troubleshoot, code suggestions and explain things.

## Database Design

Initial ERD:

![screenshot](documentation/initial-erd.png)

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models.

Understanding the relationships between different tables can save time later in the project.

I have used `pygraphviz` and `django-extensions` to auto-generate an ERD.

The steps taken were as follows:

- In the terminal: `sudo apt update`

- then: `sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config`

- then type `Y` to proceed

- then: `pip3 install django-extensions pygraphviz`

- in my `settings.py` file, I added the following to my `INSTALLED_APPS`:

```python

INSTALLED_APPS = [

...

'django_extensions',

...

]

```

- back in the terminal: `python3 manage.py graph_models -a -o erd.png`

- dragged the new `erd.png` file into my `documentation/` folder

- removed `'django_extensions',` from my `INSTALLED_APPS`

- finally, in the terminal: `pip3 uninstall django-extensions pygraphviz -y`

  
![erd](documentation/erd.png)

source: [medium.com](https://medium.com/@yathomasi1/1-using-django-extensions-to-visualize-the-database-diagram-in-django-application-c5fa7e710e16)

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://github.com/DavidFB94/pro-fit-pt/projects) served as an Agile tool for this project.

It isn't a specialized tool, but with the right tags and project creation/issue assignments, it can be made to work.

Through it, user stories, issues, and milestone tasks were planned, then tracked on a weekly basis using the basic Kanban board.

![screenshot](documentation/gh-kanban-1.png)

### GitHub Issues

[GitHub Issues](https://github.com/DavidFB94/pro-fit-pt/issues) served as an another Agile tool.

There, I used my own **User Story Template** to manage user stories.

It also helped with milestone iterations on a weekly basis.

![screenshot](documentation/gh-milestones.png)

- [Open Issues](https://github.com/DavidFB94/pro-fit-pt/issues) [![GitHub issues](https://img.shields.io/github/issues/DavidFB94/pro-fit-pt)](https://github.com/DavidFB94/pro-fit-pt/issues)

![screenshot](documentation/gh-issues-open.png)

- [Closed Issues](https://github.com/DavidFB94/pro-fit-pt/issues?q=is%3Aissue+is%3Aclosed) [![GitHub closed issues](https://img.shields.io/github/issues-closed/DavidFB94/pro-fit-pt)](https://github.com/DavidFB94/pro-fit-pt/issues?q=is%3Aissue+is%3Aclosed)

![screenshot](documentation/gh-issues-closed-1.png)
![screenshot](documentation/gh-issues-closed-2.png)

### MoSCoW Prioritization

I've decomposed my Epics into stories prior to prioritizing and implementing them.

Using this approach, I was able to apply the MoSCow prioritization and labels to my user stories within the Issues tab.

-  **Must Have**: guaranteed to be delivered (*max 60% of stories*)

-  **Should Have**: adds significant value, but not vital (*the rest ~20% of stories*)

-  **Could Have**: has small impact if left out (*20% of stories*)

-  **Won't Have**: not a priority for this iteration