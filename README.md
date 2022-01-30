# **MILESTONE PROJECT 4 – GALLERY FIVE** 

## CONTENT
- [Overview](#overview)
- [User Experience](#user-experience)
    * [User stories](#user-stories)
- [The 5 Planes](#the-5-planes)
    * [Strategy](#strategy)
    * [Scope](#scope)
    * [Structure](#structure)
    * [Skeleton](#skeleton)
    * [Surface](#surface)
- [Technologies used](#technologies-used)
- [Testing](#testing)
    * [HTML testing](#html-testing)
    * [CSS testing](#css-testing)
    * [PEP8 testing](#pep8-testing)
    * [User stories testing](#user-stories-testing)
    * [Cross platform testing](#cross-platform-testing)
    * [Bugs and fixes](#bugs-and-fixes)
- [Deployment](#deployment)
- [Credits](#credits)
    * [Credits](#credits)
    * [Conent](#content)
    * [Media](#media)
- [Acknowledgement](#acknowledgement)
- [Disclaimer](#disclaimer)

## **OVERVIEW** 

Gallery Five (TF) is a charity that helps support children from disadvantaged backgrounds to achieve their artistic potentials and dreams. It is mainly financed by taking a cut from the selling of donated art work from their London based gallery. Due to the current world pandemic, T5 have asked me to create a full-stack website where people can purchase the donated art works from the comfort of their own home. 

## **USER EXPERIENCE** 
### **User stories**: 
- As a first time visitor to the website, I would like to 
    * Be able to browse through all the art work available for purchase 
    * Search for specific art work 
    * Know basic information of the art work easily such as price, name etc 
    * Sorting of products on to make it easier for what I want 
    * Read about the company of the website 
    <!-- * Know how delivery and returns work  -->
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
    <!-- * Receive emails regarding news about the website -->
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
    <!-- * Have enough time for my items to be in the basket before it is taken off  -->
    * Edit my basket such as deleting an item, changing the quantity etc 
    * Have a confirmation message

## **THE 5 PLANES** 
### **Strategy** 
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

### **Scope** 
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

### **Structure** 
Database - [image](readme/images/database_schema.png)

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

### **Skeleton** 

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

### **Surface** 
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
- Lucid chart - website where I made the database schema
- W3C Markup Validator - detects any errors in .html files
- W3C CSS Validator - detects any errors in .css files


## **TESTING**
### **HTML Testing**
Using - W3C Markup Validator
Errors and Warnings in the .html files have been attended with the help of W3 .html Validator. After alterations, no major errors were found in the .html files; Most were related to the django templates. The few slightly concerning errors have been documented below
| FILE | Result | Comment
--- | --- | --- |
checkout.html | [image](readme/images/w3_checkout.png) | could not resolve error 7
footer.html | [image](readme/images/w3_footer.png) | do not believe a title element is needed regarding error 2 and 3
navigation.html | [image](readme/images/w3_navigation.png) | did not want to alter with error 12 and 13 as it is from Bootstrap and changing of any id names most likely will interfere with the builtin in bootstrap jquery/js

### **CSS Testing**
| FILE | Result | Notes
base.css | [image](readme/images/w3_base_css.png) | 2 warnings were related to the colours of the background and border of a class element being the same

### **PEP8 Testing**
* I used pep8online to check whether my .py file codes were PEP8 compliant. I made the changes needed for an All right pass for all .py files.
* After changes were made, an internal server error occured. I had to revert some line of codes back to its original state for the website to work. More details can be found in 'Bugs and Fixes' section

### **User Stories Testing**
| AIM | Achieved | Comment |
--- | --- | --- | 
**As a first time visitor to the website, I would like to..** 
Be able to browse through all the art work available for purchase | yes | |
Search for specific art work | yes | |
Know basic information of the art work easily such as price, name etc | yes | |
Sorting of products on to make it easier for what I want | yes | |
Purchase with ease and confidence | yes | |
Read about the company of the website | yes | |
Be able to communicate with the website as in email, contact number etc | yes | |
Register to the website | yes | |
Read reviews of the art works | yes | | 
Read articles/blogs related to art and the charity sector | yes | |
**As a registered member to the website, I would like to..** 
Purchase with ease and confidence | yes | |
View and edit my shopping basket | yes | |
Have quick purchasing procedures in the form of saved bank details | yes | |
Know about my previous purchases/orders | yes | |
Have a page with my information given such as name, address, email etc | yes | | 
Reset my password | yes | |
Delete my account 
Create a favourite/likes list | yes | |
Post reviews of the art works | yes | |
Post articles/blogs related to art and the charity sector | yes | |
**As a site owner/admin user, I would like to..**
Remove and ban accounts | yes | |
Edit products on the websites for reasons such as typo errors, pricing etc | yes | |
Add and remove products | yes | |
Add and remove reviews | yes | |
Approve and then post of blogs by users/member | yes | |
**As a user in the process of purchasing, I would like to..** 
A secured payment system | yes | |
Be acknowledged of how secure the process is for peace of mind | yes | |
An email once payment has gone through 
Edit my basket such as deleting an item, changing the quantity etc | yes | |
Have a confirmation message | yes | |

### **Cross Platfrom Testing**
#### CRUD (create, read, update, delete) TESTING
| AIM | admin | registered user | non-registered user |
--- | --- | --- | --- |
**Products/art works - from products app**
CREATE a product to add to the database | yes | no | no
READ/see a product from the database on the website | yes | yes | yes
UPDATE a product | yes | no | no
DELETE a product | yes | no | no
**Blogs - from blogs app**
CREATE a blog post to add to the database | yes | yes | no
READ a blog from the website on the website | yes | yes | yes
UPDATE a blog | no | no | no
DELETE a blog | yes | no | no
**Reviews - from products app**
CREATE a review | yes | yes | no
READ a review | yes | yes | yes
UPDATE a review | no | no | no
DELETE a review | yes | yes | no
**Crate - from crate app**
CREATE a crate | yes | yes | yes
READ a crate | yes | yes | yes
UPDATE a crate | yes | yes | yes
DELETE a crat | yes | yes | yes
**Wishlist - from wishlist app**
CREATE a wishlist | yes | yes | no
READ a wishlist | yes | yes | no
UPDATE a wishlist | yes | yes | no
DELETE from wishlist | yes | yes | no

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
**Contact us - index.html**
'Name' field will accept upto 100 characters | yes | yes | yes
'E-mail' field must have follow the pattern of have a '@' and a '.' in the email | yes | yes | yes

### Lighthouse testing
I used Google Chrom Lighthouse testing to find out the quality of the website. Here are my results: [image](readme/images/lighthouse_testing.png)

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

### Bugs and Fixes
ISSUE | Solved? | How? | link
--- | --- | --- | --- | 
It was not possible to NOT save the changes made in teh checkout form in checkout.html | Yes | Thanks to helpful student peers (Phillip and Luke) from the Slack community, they posted the required code needed for the checkbox to work with the .js, .html, and .py files. | (https://code-institute-room.slack.com/archives/C7HS3U3AP/p1605302104469800?thread_ts=1605222094.452700&cid=C7HS3U3AP) and (https://code-institute-room.slack.com/archives/C7HS3U3AP/p1621881386435800?thread_ts=1605222094.452700&cid=C7HS3U3AP) 
inernal server occured after PEP8 chnages | yes | Gitpod terminal told me whre the errors were occuring. Reverted the codes back to its state before the PEP8 changes | [image](readme/images/bugs_and_fixes_pep8.png)

## **DEPLOYMENT**
### Making a local clone
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

### Working with a local clone
1. Install all the requirements from requirements.txt by typing in 'pip3 install -r requirements.txt' into your terminal
2. Create a .gitignore from the root of your project
3. Create a env.py from the root of your project and have it look like this: [image](readme/images/env_py_file.png)
4. Include env.py into .gitignore
5. Create a Stripe account
    * Under the 'Developers' tab, click on 'Webhooks'
    * Click on '+ Add endpoint' and enter in the your URL followed by 'checkout/wh/', and check recieve all events
6. In your env.py file, fill out the second parameter of every os.environ line with the following:
    * "SECRET_KEY" can be anything you want
    * "STRIPE_PUBLIC_KEY" can be found from your Stripe account under the name of 'Publish key'
    * "STRIPE_SECRET_KEY" can be found in your Stripe account under the name of 'Secret key'
    * "STRIPE_WH_SECRET" can be found in your 'endpoint' tab from your Strip account under the name of 'signing secret'
7. An admin/super_user will need to be created. To do so, type in 'python3 manage.py createsuperuser'; and follow the instructions
8. Now it is time load up your django with the initial files/data and databases. You can do so by tyoing into your terminal the following:
    * python3 manage.py makemigrations
    * python3 manage.py migrate
    * python3 manage.py loaddata categories
    python3 manage.py loaddata products
9. You are now done. To get access to your admin, run the server ('python3 manage.py runserver') and type in'/admin' at teh end of your url

### Deploying to Heroku
1. Install all the requirements from requirements.txt by typing in 'pip3 install -r requirements.txt' into your terminal
2. Create a Heroku account
    * Under 'Add-ons', find Heroku-Postgress and provision  it
3. Follow step 8 and 7 from the previous sub title(Working wiht a local clone)
4. In settings.py, replace and/or add the url of your Heroku app in teh variable 'ALLOWED_HOSTS'
5. If you would like quick deployment to Heroku, add your repository to Heroku under Deploy > Connect to Github > Enable automatic deploys

### Hosting files with AWS
1. Create and AWS account
2. Under S3 services, create a new bucket
    * Uncheck 'Block all public access'
3. In your newly created bucket, enable Static Web Hosting from the tab Properties
4. Under the 'Permissions' tab, make the following changes:
    * 'Bucket policy' > policy generator
        * Select Type of Policy = select 'S3 Bucket Policy'
        * Principle: type in '*'
        * Actions: select 'GetObject'
        * Amazon Resource Name(ARN): you should find this from the previus windown under the 'Bucket policy' tab
        * Add statement > Generaate policy. Copy given code
        * Paste the code in the editor under the 'Bucket policy tab and add '/*' at the end of "Resource" image
        * Click save
5. Under IAM services, create a new 'user group'
6. Access management > Policies > Create policy
    * Under JSON tab, click on 'Import Managed policy' and import 'AmazonS3FullAccess'
    * Now under the JSON tab, include your ARN twice in the 'Resources' with the second follewed by '/*'
    * Click on 'Review policy', fill out the name and description, and finally click on 'Create policy'
7. Go to the page of the group you created
    * Under 'Permissions' > Attach Policy, select for the policy you have just created and click 'Attach policy'
8. Access management > Users > Add user. Give it a name and check 'Access type'
    * Progress on to last step without changes and click 'Create user'
    * Download the .csv file and save it somewhere secure as you will NOT be able to download it again once you naviate away from this page
9. In settings.py, change the AWS_STORAGE_BUCKET_NAME to the name of your AWS bucket and AWS_S3_REGION_NAME to your region which you can find in your AWS account
10. In teh S3 services, add a new colder named 'media'
    * Upload your images, Select 'Grant public read access to this objects(s)' and finally 'upload'
11. From your Stripe account, click '+ Add endpoint' and enter in the your Heroku URL followed by 'checkout/wh/', and check recieve all events
12. Your 'Config Vars' from your Heroku account (under Settings) should look like this: [image](readme/images/heroku_config_look.png)
    * AWS_ACCESS_KEY_ID can be found from your AWS account
    * AWS_SECRET_ACCESS_KEY can be found from your AWS account

### Setting up a real active email service
1. Create a Gmail account
2. go to Settings > Accounts and Import > Other Google account settings
    * Click on 'Security' tab and enable 2-step verification
3. Back to 'Security' tab, click on 'App passwords'
    * for 'Select app', select 'Mail'
    * for 'Select device', select 'other'
    * Name your app password and click 'GENERATE'; You will then be given a password
    * Copy and paste the password and add it to your Heroku config variable under the name of 'EMAIL_HOST_PASS'
4. Whilst on the config variable, add another under the name of 'EMAIL_HOST_USER' with its value being your email address

## **CREDITS**
### References
* REF001 - 'profile' app was heavily copied/slightly adapted from Code Insitute Full Stack Frameworks with Django module (https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/4201818c00aa4ba3a0dae243725f6e32/2c1b98a8efb748009445d5056c97483b/)
* REF002 - 'checkout' app was heavily copied/slightly adapted from Code Insitute Full Stack Frameworks with Django module (https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/4201818c00aa4ba3a0dae243725f6e32/326f171b831446588d33c0333eb4caaa/)
* REF003 - 'crate' app was heavily copied/slightly adapted from Code Insitute Full Stack Frameworks with Django module (was heavily copied/slightly adapted from Code Insitute Full Stack Frameworks with Django module)

### Content
* I copied and pasted [lorem ipsum](https://www.lipsum.com/) texts into the products details due to the nature of the project
* About us written content was written by me

### Media
* [Jeremy Bezanger](https://unsplash.com/photos/NsdNBQxb-8s)
* [Antonino Cicero](https://unsplash.com/photos/_5puSofcfOs)
* [Pascal Bernardon](https://unsplash.com/photos/1wOv0s1oR4A)
* [Nick Kwan](https://unsplash.com/photos/FeBoOVQv0sQ)
* [Jeremy Bezanger](https://unsplash.com/photos/rCefTI3jS2Y)
* [Bees And Green Tea](https://unsplash.com/photos/WqjW5em9S5o)
* [Jeremy Bezanger](https://unsplash.com/photos/7vGDT1Ygbl4)
* [Jorge Zapata](https://unsplash.com/photos/TPPzDKIvROw)
* [Timothy Dykes](https://unsplash.com/photos/KTYSVnv6lUw)
* [Pegah Mostafavi Zade](https://unsplash.com/photos/w-ImBSMvpZM)
* [Trude Jonsson Stangel](https://unsplash.com/photos/TO_h3akXWf0)
* [Vika Wendish](https://unsplash.com/photos/h4PSY635040)
* [Matt Seymour](https://unsplash.com/photos/rSKjPA41H2Q)
* [Vika Wendish](https://unsplash.com/photos/PFmk0-yVKzI)
* [adr sree](https://unsplash.com/photos/sWvbhOTl09o)
* [Earl Wilcox](https://unsplash.com/photos/j_9wznLtfKk)
* [Misael Moreno](https://unsplash.com/photos/14HNtFPbKbs)
* [Kevin Bluer](https://unsplash.com/photos/e6XqFP4kCxM)
* [Mattias Russo-Larsson](https://unsplash.com/photos/GQ8JIFHHmCg)
* [denis pan](https://unsplash.com/photos/FnNIDG9k8Ag)
* [Stavrialena Gontzou](https://unsplash.com/photos/jyE-TqbRy3Y)
* [Casey Horner](https://unsplash.com/photos/Ms77GfPPT48)
* [Jan Gottweiss](https://unsplash.com/photos/SCTALD23uXA)
* [Oneisha Lee](https://unsplash.com/photos/r3WFKMR9zzI)
* [Mika](https://unsplash.com/photos/y-RjWd6Ol7A)
* [Matteo Vistocco](https://unsplash.com/photos/mJUpopBUGsg)
* [Matt Moloney](https://unsplash.com/photos/tKB1GDJUq9c)
* [Jen Theodore](https://unsplash.com/photos/PU4sOcNnYj8)
* [Katie Rainbow](https://unsplash.com/photos/DjGHuzUh_84)
* [Karim MANJRA](https://unsplash.com/photos/fm9wqDNXyQ0)
* [Avinash Kumar](https://unsplash.com/photos/u3B4oNyXYXE)
* [Tim Hufner](https://unsplash.com/photos/QtL46PrOg9E)
* [Oscar Helgstrand](https://unsplash.com/photos/HPwbniZ9g6Q)
* [Matt Moloney](https://unsplash.com/photos/lYENI1CYeP0)
* [Matt Moloney](https://unsplash.com/photos/cJL2LuBTu0A)
* [Anil Kumar](https://unsplash.com/photos/dBkT44qZD6M)
* [Ezi](https://unsplash.com/photos/ZcY6QeXg_J4)
* [Alexander Shatov](https://unsplash.com/photos/DHl49oyrn7Y)
* [Benjamin henon](https://unsplash.com/photos/2JlLdOm1xIs)
* [Mingwei Lim](https://unsplash.com/photos/Q1Us6ITDPeo)
* [Fakurian Design](https://unsplash.com/photos/nNpLEEdmUj0)
* [KOBU Agency](https://unsplash.com/photos/csJt89dL9pE)
* [Pink flip](https://unsplash.com/photos/1BcfKfeavVA)
* [ueberform](https://unsplash.com/photos/eejq0xM2RTk)
* [Europeana](https://unsplash.com/photos/6c43FgRt0Dw)
* [Vojtech Bruzek](https://unsplash.com/photos/mCjA1I8SlS8)
* [Europeana](https://unsplash.com/photos/TjegK_z-0j8)
* [Matthew Brindle](https://unsplash.com/photos/p7ILrZmhHHc)
* [Federico Di Dio](https://unsplash.com/photos/XVOBr3F95RY)
* [Adrianna Geo](https://unsplash.com/photos/1rBg5YSi00c)
* [Europeana](https://unsplash.com/photos/Wiad3DQxUho)
* [Steve Johnson](https://unsplash.com/photos/iBlW9tjiyqw)
* [Paul Blenkhorn](https://unsplash.com/photos/PkDnu0lImv4)
* [Sir Edward Burne-Jones](https://unsplash.com/photos/tV02AFxvRJg)
* [David Roberts](https://unsplash.com/photos/sJr8LDyEf7k)
* [Frederick Sandys Greek](https://unsplash.com/photos/aE0-ZJb2VTQ)
* [Michael Angelo](https://unsplash.com/photos/1rBg5YSi00c)
* [Fuu J](https://unsplash.com/photos/KRztl5I6xac)
* [McGill Library](https://unsplash.com/photos/eMw-fVXNpME)
* [Sir David Wilkie](https://unsplash.com/photos/XSMTwl7n3p4)
* [Francis Towne](https://unsplash.com/photos/5ruS8plfbvM)
* [Robert Hills](https://unsplash.com/photos/6fv0MEf3FUE)

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