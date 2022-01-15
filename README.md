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

Wireframe 
Home page: [wireframe image](readme/images/home.png)
Browsing/Products page: [wireframe image](readme/images/products.png)
Login/registration page: [wireframe image](readme/images/login_and_registration_page.png) 
Payment processing page: [wireframe image](readme/images/payment_process.png)
Selected product page: [wireframe image](readme/images/selected_product.png)
Shopping basket page: [wireframe image](readme/images/shopping_basket.png)
Contact us page: [wireframe image](readme/images/contact_us.png)
Blogs page: [wireframe image](readme/images/blogs.png)
Selected blog page: [wireframe image](readme/images/selected_blog.png)
 

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