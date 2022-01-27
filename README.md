# **MILESTONE PROJECT 4 – GALLERY FIVE** 

## **OVERVIEW** 

Gallery Five (TF) is a charity that helps support children from disadvantaged backgrounds to achieve their artistic potentials and dreams. It is mainly financed by taking a cut from the selling of donated art work from their London based gallery. Due to the current world pandemic, T5 have asked me to create a full-stack website where people can purchase the donated art works from the comfort of their own home. 

## **USER EXPERIENCE** 

### User stories: 
- As a first time visitor to the website, I would like to 
    * Be able to browse through all the art work available for purchase 
    * Search for specific art work 
    * Know basic information of the art work easily such as price, name etc 
    * Sorting of products on to make it easier for what I want 
    * Read about the company of the website 
    * Know how delivery and returns work 
    * Be able to communicate with the website as in email, contact number etc 
    * Register to the website 
    * Read reviews of the art works 
    * Read articles/blogs related to art and the charity sector 

- As a registered member to the website, I would like to 
    * Purchase with ease and confidence 
    * View and edit my shopping basket 
    * Have quick purchasing procedures in the form of saved bank details 
    * Know about my previous purchases/orders 
    * Have a page with my information given such as name, address, email etc 
    * Reset my password 
    * Delete my account 
    * Receive emails regarding news about the website
    * Create a favourite/likes list 
    * Post reviews of the art works 
    * Post articles/blogs related to art and the charity sector  

- As a site owner/admin user, I would like to 
    * Remove and ban accounts 
    * Edit products on the websites for reasons such as typo errors, pricing etc 
    * Add and Remove products 
    * Approve and then post of blogs by users/members 

- As a user in the process of purchasing, I would like to 
    * A secured payment system 
    * Be acknowledged of how secure the process is for peace of mind 
    * An email once payment has gone through 
    * Have enough time for my items to be in the basket before it is taken off 
    * Edit my basket such as deleting an item, changing the quantity etc 
    * Have a double confirmation process 

## **THE 5 PLANES** 
### Strategy 
- Purpose of the website? To be able to purchase art works to raise money for the charity 

- Target audience? Art enthusiasts who also care about social disadvantages from around the world 

- Value to the user? Have a great selection of art works to choose from whist also knowing their money will go to a good cause 

- What makes a good experience? 
    * An easy to navigate website where they will never be more than a few clicks away to the important destinations 
    * A non-cluttered appearance to avoid over irritable stimulation 
    * An easy purchasing process 
    * A consistent theme to the website 
    * Sufficient information regarding the directly to the product and non direct information of the product such as delivery and what the company is about 

- How are we different? No other website has part of the financial part of the purchases go to a charity 

- What we shouldn’t do? 
    * Make purchasing difficult as purchasing will be the main source of income 
    * Not registering should not have the same experience as registered users’ registered user should have a better experience in the form of offers, convenience etc 

### Scope 
Intended features: 
- Purchasing of art works 
- Secured 
- Assurance of purchases 
- Necessary requested information 
- Easy to explore art works 
- Organise products into categories 
    * Paintings 
    * Graphics
    * Sculptures 
- Ordering products 
    * Release date 
    * Price 
- Searchable products 
- Detailed art work information 
    * Price 
    * About the art work 
- Registration/membership 
    * Save personal information for quick future purchases 
    * Purchasing and viewing history 
    * Note/mark products for later viewing/purchasing 

Future features:
- Stock check
- Tags for better search experience
- Promotion of certain artworks based upon release date, popularity etc

Content requirements: 
- Text  
    * Information regarding the art work such as the artist and the piece itself 
    * Based on the previous point, some text must also be informative to help the users final decision 
- Image 
    * Sufficient images should be available for every product 
    * Images of product should be consistent in terms of size and layout 
    * Website logo should be appropriate 
- Video 
    * A video describing the objective of the charity and the website 
- Audio 
    * No audio as it can be more of an annoyance than an entertaining feature of the site 

### Structure 
Database 
- Database model for each art work: 
    * Id 
    * Name 
    * Artist 
    * Type 
    * Work description 
    * Creation date 
    * Image 
    * Price 
    * Purchasers
    * Sold
    * Likes

- Database model for each category: 
    * Id 
    * Name of category 

- Database model for each member: 
    * Id 
    * First name 
    * Last name 
    * Email 
    * Home address 
    * Contact number 
    * Registration date 

- Database model for each Review 
    * Id 
    * Review title 
    * Reviewer
    * Product - Art work database  
    * Reviewer - Member database  
    * Review date 

- Database for each blog: 
    * Id 
    * Blog title 
    * Blog 
    * Auther 
    * Blog date 
    * Image 
    * Publish 

Page details: 
- Header section – This will be on top of every page. It should consist of: 
    * Company logo 
    * Search panel 
    * Login link 
    * Shopping basket link 

- Footer section – This will be at the bottom of every page. IT should consist of: 
    * Company logo 
    * Social media links 
    * Links/information of contacting the charity 

- Navigation section – This will be near the top of every page. It should consist of: 
    * Links to art works organised by its main category. The main categories and its sub-categories will be:  
        * Paintings - water colour, acrylic, oil, and tempera
        * Graphicss - digital, and handmade  
        * Physical - wood, clay, and stone

- Home page – First page user will encounter. It should consist of: 
    * Company logo dominating the page 
    * Below should lead to section containing promotions 
    * A section explaining the purpose of the charity 

- Art works page – Will be the basic template of the pages containing the art works on sale 
    * No more than three or four art works on each row 
    * Each art work should have a: 
        * Picture
        * Name of art work 
        * Name of artist 
        * Price 
        * Option to like
    * Organising button should be at a sensible position. The button should have be able to sort the art works by: 
        * Name of art work 
        * Price 
    * A button leading user back to the top of the page 

- Selected art work page – This will be the basic template of the page containing the selected art work. It should consist of: 
    * Large picture of the art work 
    * Name of art work 
    * Name of artist 
    * Price 
    * Description of art work 
    * Description of artist 
    * Add to basket button 
    * Wish list button 
    * A link asking whether the user would like to register 
    * A link asking whether the user would like to login 

- Shopping cart page – The screen where the user can see what they have added to their basket for purchasing intentions. This page will consist of: 
    * Art work with details of: 
        * Name of art work 
        * Name of artist 
        * Price 
        * Quantity
    * Option to delete selected art work 
    * Information regarding how much of the sale will go to the charity
    * Button to proceed purchasing which will be the purchasing page 

- Purchasing page – This is where the user will be entering their banking information for purchasing of the art work: 
    * Form should be centre of page 
    * A message asking whether the user is sure that they want to purchase should appear before confirmation 
    * Once order has been confirmed, a dominating message should appear on screen letting the user know that the transaction has been successful 

- Login/Registration page – A page containing the form for the view to either register or login. It should consist of: 
    * The form asking for: 
        * First name 
        * Last name 
        * Home address 
        * Email 
        * Contact number 

- Favourites page - a page containing all the art works the user has favourited. It will consist of: 
    * Same layout as the Products page 
    * Also with the same functionalities as the Products page 

- Create a blog page. It should have a form consisting of:  
    * Name of the article 
    * The actual article 
    * Option to add an image 

- Selected blog page – a page containing the selected blog from the Blog page. It should consist of: 
    * An image of the article near the top left of page 
    * Title and auther of the article next to the image 
    * Actual article starts from under the auther text 
    * Option to delete/edit art work if user is an admin 

- Blogs page – A page containing blogs posted by users. It should consist of: 
    * A card containing an 
        * Image 
        * Title 
        * Auther 
        * Snippet of the article 
        * Button to read more of the article(selected blog page) 
    * A button leading user to a page where they can submit their blog 

- Profile page – a page containing the basic information regarding the current user. IT should consist of: 
    * A welcoming/knowledgment message of the user (ie. Welcome user100 etc) 
    * Order history 
    * Review history 
    * Blog history 
    * Option to edit basic information such as name, email etc 

- Contacts page - a page containing information regarding how to get in touch with teh charity. It should consist of:
    * Ability to send a message/email
    * Phone number
    * Office address

- About us page - a page with information about the website and charity. It should consist of:
    * Story about the charity
    * Images of the team behind the website and the children they are/have helped

### Skeleton 

Wireframes for laptop/computer screens
* Home page: [wireframe image](readme/images/home.png)
* Products page: [wireframe image](readme/images/products.png)
* Product detail page: [wireframe image](readme/images/product_detail.png)
* Login/registration page: [wireframe image](readme/images/login_and_registration.png) 
* Crate(shopping basket) page: [wireframe image](readme/images/crate.png)
* Checkout page: [wireframe image](readme/images/checkout.png)
<!-- Contact us page: [wireframe image](readme/images/contact_us.png) -->
* Blogs page: [wireframe image](readme/images/blogs.png)
* Selected blog page: [wireframe image](readme/images/read_blog.png)

Wireframes for mobile/tablet screens
* Home page: [wireframe image](readme/images/mobile_home.png)
* Products page: [wireframe image](readme/images/mobile_products.png)
* Product detail page: [wireframe image](readme/images/mobile_product_detail.png)
* Login/registration page: [wireframe image](readme/images/mobile_login_and_registration.png) 
* Crate(shopping basket) page: [wireframe image](readme/images/mobile_crate.png)
* Checkout page: [wireframe image](readme/images/mobile_checkout.png)
<!-- Contact us page: [wireframe image](readme/images/contact_us.png) -->
* Blogs page: [wireframe image](readme/images/mobile_blogs.png)
* Selected blog page: [wireframe image](readme/images/mobile_read_blog.png)
 

### Surface 
- Font: 
    * Noto Sans Display - https://fonts.google.com/noto/specimen/Noto+Sans+Display 
    * Ubuntu - https://fonts.google.com/specimen/Ubuntu 

- Colour scheme: 
    * Found from the website - https://99designs.co.uk/blog/creative-inspiration/color-combinations/, design 8 
        * Off-white - #f5f0e1 
        * Navy - #1e3d59 
        * Pale orange - #ff6e40 
        * Yellow - #ffc13b 

## **TECHNOLOGIES USED**
- HTML
- CSS
- Jquery - a lightweight JavaScript library
- Python - back-end programming language
- Bootstrap 4 - a .css library which also includes use of .js
- Bootstrap 5 - a .css library which also includes use of .js
- Django - Cloud based service focused on database management
- Heroku - Web hosting service
- Stripe - Card payment service for websites
- Font awesome - a catalogue of icons for .html files
- Django templates - a template for use of python with Django in .html
- Jquery - A convenient JS library
- Github - Save and deploy projects useing this
- Git pod - Platform to write code
- Balsamiq - software for use fo making skeleton sketches
- Paint 3D - an app I used to help resize and edit images; It is available on Windows 10
<!-- Lucid chart - website where you can make flowcharts -->
- W3C Markup Validator - detects any errors in .html files
- W3C CSS Validator - detects any errors in .css files


## **TESTING**
### HTML Testing
Using - W3C Markup Validator
| FILE | Result 1 | Correction (if needed) | Notes
--- | --- | --- | --- |

### User Stories Testing
| AIM | Achieved | Comment |
--- | --- | --- | 
**As a first time visitor to the website, I would like to..** 
Be able to browse through all the art work available for purchase | yes | 
Search for specific art work | yes | 
Know basic information of the art work easily such as price, name etc | yes | 
Sorting of products on to make it easier for what I want | yes | 
Purchase with ease and confidence | yes | 
Read about the company of the website 
Know how delivery and returns work 
Be able to communicate with the website as in email, contact number etc 
Register to the website | yes | 
Read reviews of the art works | yes | 
Read articles/blogs related to art and the charity sector | yes | 
**As a registered member to the website, I would like to..** 
Purchase with ease and confidence | yes | 
View and edit my shopping basket | yes | 
Have quick purchasing procedures in the form of saved bank details | yes | 
Know about my previous purchases/orders | yes | 
Have a page with my information given such as name, address, email etc | yes | 
Reset my password | yes | 
Delete my account 
Receive emails regarding news about the website
Create a favourite/likes list | yes | 
Post reviews of the art works | yes | 
Post articles/blogs related to art and the charity sector | yes |
**As a site owner/admin user, I would like to..**
Remove and ban accounts | yes |
Edit products on the websites for reasons such as typo errors, pricing etc | yes | 
Add and remove products | yes |
Add and remove reviews | yes | 
Approve and then post of blogs by users/member | yes |
**As a user in the process of purchasing, I would like to..** 
A secured payment system | yes | 
Be acknowledged of how secure the process is for peace of mind 
An email once payment has gone through 
Have enough time for my items to be in the basket before it is taken off 
Edit my basket such as deleting an item, changing the quantity etc | yes | 
Have a double confirmation process  

### Cross Platfrom Testing
#### CRUD (create, read, update, delete) TESTING
| AIM | SM | MD | LG |
--- | --- | --- | --- |
Is it possible to create an art work to add the database? | yes | yes | yes
Is it possible to read/see the created art work? | yes | yes | yes
Is it possible to update the art work from the database? | yes | yes | yes
Is it possible to delete the art work from the database? | yes | yes | yes
Is it possible to create a blog to add the database? | yes | yes | yes
Is it possible to read/see the created a blog? | yes | yes | yes
Is it possible to update the blog from the database? | yes | yes | yes
Is it possible to delete the blog from the database? | yes | yes | yes
Is it possible to create a review for an art work? | yes | yes | yes
Is it possible to read/see the review created? | yes | yes | yes
Is it possible to update the review from the database? | yes | yes | yes
Is it possible to delete the review from the database? | yes | yes | yes

### FORM VALIDATION TESTING
| AIM | SM | MD | LG |
--- | --- | --- | --- |
**Register** 
'E-mail' field must have follow the pattern of have a '@' and a '.' in the email. It won't accept if it does not | yes | yes | yes
Both 'E-mail' fields must match | yes | yes | yes
'Username' field must only contain letters, numbers, and @/./+/-/_ characters | yes | yes | yes
Both 'Password' fields must match | yes | yes | yes
**Login**
'Login' field must match with user from the database | yes | yes | yes
'Password' field must match with the password made for user entered in the 'Login' field | yes | yes | yes
**Checkout - checkout.html**
'Full Name' field will only accept upto 50 characters | yes | yes | yes
'E-mail' field must have follow the pattern of have a '@' and a '.' in the email | yes | yes | yes
'Phone Number' field will only accept numbers and a maximum of 20 numbers | yes | yes | yes
'Street Address 1' field will only accept upto 80 characters | yes | yes | yes
'Street Address 2' field will only accept upto 80 characters | yes | yes | yes
'Town or City' field will only accept upto 40 characters | yes | yes | yes
'County, State, or Locality' field will only accept upto 80 characters | yes | yes | yes
'Postcode' field will only accept upto 20 characters | yes | yes | yes
'Card number' field will only accept numbers | yes | yes | yes
**Add product - add_product.html**
'Category' will have a drop down containing options from the Category database | yes | yes | yes
'Name' will allow upto 80 characters | yes | yes | yes
'Artist name' will only allow upto 80 characters | yes | yes | yes
'Description' will allow upto 500 characters | yes | yes | yes
'Price' will only accept numbers. It will take a numbers upto 4 digits in length | yes | yes | yes
'Price' will not go lower than 0 | yes | yes | yes
'Image url' field will accept only urls | yes | yes | yes
'Image' will only let image files to be uploaded | yes | yes | yes
**Create Blog - create_blog.html**
'Title' field will accept upto 100 characters | yes | yes | yes
'Article' field has no limits to ammount of characters | yes | yes | yes
'Image' field will only accept image files | yes | yes | yes
**Reviews - product_detail.html**
'Title' field will accept upto 100 characters | yes | yes | yes
'Review' field will accept upto 1000 characters | yes | yes | yes

### Responsive Testing
AIM | SM | MD | LG |
--- | --- | --- | --- |
**HOME - index.html**
Links / URLs | yes | yes | yes
Images | yes | yes | yes
Renders as expected | yes | yes | yes
**PRODUCTS - products.html**
Links / URLs | yes | yes | yes
Images | yes | yes | yes
Renders as expected | yes | yes | yes
**PRODUCT DETAIL - product_detail.html**
Links / URLs | yes | yes | yes
Images | yes | yes | yes
Renders as expected | yes | yes | yes
Form validation | yes | yes | yes
**EDIT PRODUCT - edit_product.html**
Links / URLs | yes | yes | yes
Images | yes | yes | yes
Renders as expected | yes | yes | yes
Form validation | yes | yes | yes
**ADD PRODUCT - add_product.html**
Links / URLs | yes | yes | yes
Images | yes | yes | yes
Renders as expected | yes | yes | yes
Form validation | yes | yes | yes
**CRATE - crate.html**
Links / URLs | yes | yes | yes
Images | yes | yes | yes
Renders as expected | yes | yes | yes
**CHECKOUT - checkout.html**
Links / URLs | yes | yes | yes
Images | yes | yes | yes
Renders as expected | yes | yes | yes
**CHECKOUT SUCCESS - checkout_success.html**
Links / URLs | yes | yes | yes
Images | yes | yes | yes
Renders as expected | yes | yes | yes
**WISHLIST - wishlist.html**
Links / URLs | yes | yes | yes
Images | yes | yes | yes
Renders as expected | yes | yes | yes
**BLOGS - blogs.html**
Links / URLs | yes | yes | yes
Images | yes | yes | yes
Renders as expected | yes | yes | yes
**READ BLOG - read_blog.html**
Links / URLs | yes | yes | yes
Images | yes | yes | yes
Renders as expected | yes | yes | yes
**CREATE_BLOG - create_blog.hmtl**
Links / URLs | yes | yes | yes
Images | yes | yes | yes
Renders as expected | yes | yes | yes
Form validation | yes | yes | yes
**REQUESTED BLOG - requested_blog.html**
Links / URLs | yes | yes | yes
Images | yes | yes | yes
Renders as expected | yes | yes | yes
Form validation | yes | yes | yes
**PROFILE - profile.html**
Links / URLs | yes | yes | yes
Images | yes | yes | yes
Renders as expected | yes | yes | yes
**UPDATE PROFILE - update_profile.html**
Links / URLs | yes | yes | yes
Images | yes | yes | yes
Renders as expected | yes | yes | yes
Form validation | yes | yes | yes

## **DEPLOYMENT**
### Making A Local Clone
You may want to have access via a copy of the repository on your own device. There are three ways to do this: 
* Method 1
1. Login to your GitHub account and open up the repository you would like to copy 
2. Click on the button with a drop-down menu named ‘Code’ which will be placed next to the green ‘Gitpod’ button
3. You will then have the option to download it on to your system via the ‘Download ZIP’ option

* Method 2 
1. Open up your preferred IDE and open up the folder where you would the repository to be copied/cloned
2. In the terminal, type in ‘git clone’ ; do not press enter or anything else
3. Now login to your GitHub account and open up the repository you would like to copy
4. Click on the ‘Code’ button again and copy the text given under the subheading ‘HTTPS’. A button next to this text gives you an easier way of copying the text
5. Back to your IDE terminal, after the ‘git clone’, press the spacebar button and paste in the link you copied from the repository. Your entry in the terminal should look something like this: ‘gti clone https://github.com/shiba517/msp4_gallery_five.git’. Then press enter
6. Your terminal will let you know the repository has been cloned and saved to your preferred destination and will be evident when viewing files and folders from your preferred destination

## **CREDITS**
### References
* REF001 - 'Profile' app was heavily copied/slightly adapted from Code Insitute Full Stack Frameworks with Django module (https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/4201818c00aa4ba3a0dae243725f6e32/2c1b98a8efb748009445d5056c97483b/)
* REF002 - 'Checkout' app was heavily copied/slightly adapted from Code Insitute Full Stack Frameworks with Django module (https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/4201818c00aa4ba3a0dae243725f6e32/326f171b831446588d33c0333eb4caaa/)
### Content
### Media
### Acknowledgement 
* Code Institue course
* Course tutor Precious Ijege
* W3Schools
* Codemy
* Very Academy
* The Net Ninja 
* Cryce Truly

## **DISCLAIMER**
This webite was built for educational reasons for my coding course from Code Institute. No content, written(unless mentioned in CREDITS - Content of this document) and imagery, is of mine. No offense was intentionaly made with the pricing of the art works (I randomly made up the numbers), and any namings of art works. If there is anything you would like enquire, please do so via my email - shibacdeb@gmail.com


