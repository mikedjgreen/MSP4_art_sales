- [Testing](#testing)
  * [Feature testing](#feature-testing)
  * [Bug testing](#bug-testing)
  * [User Story testing](#user-story-testing)

[TOC](http://ecotrust-canada.github.io/markdown-toc/)

## Testing

[Return to Readme](../../README.md#testing)

### Feature testing

#### 1  a remote API to recieve a patron's payments by credit card, securely [STRIPE](https://stripe.com/gb).

#### 2  using the same payment feature, allow club members to pay their annual subscription easily.

#### 3  a query and classification of artworks that allows easy browsing of selected images and their details.

#### 4  an email confirmation of sale and paid subscription.

#### 5  a secure login to allow a logged in member or patron to view their previous orders, paid subscriptions, and a club member's sold works.

#### 6  a shopping basket of selected works with a running total of price, VAT and commision due.


### Bug testing

#### 1. Artworks programming error

![Artworks Error](heroku_artworks_debug_error1.jpg)

Model migration changes had not been implemented on Heroku server.

[Heroku Migrations](heroku_artworks_debug_error.txt)

![Artworks error fixed](heroku_artworks_fixed.jpg)

#### 2. Server Error (500) upon login

![Server 500 Error](server_500_login_error.jpg)

This was caused by a wayward migration to update production models.
It cleared the profiles table 'Patron' that had a foreign key relation to alluath's user.

Temporarily set the Patron to be created upon login, regardless.

Then logged in as admin and entered Patron details for  the superuser 'mdjg' to be able to login.

Rolled back the code changes to enable this, and then logged in successfully.


### User Story testing

#### 1 As a visitor to the site I would like to view art works for sale
    If I see something I like, I would like to know the price, what it's made of and size of it ( will it 'fit' on my wall or shelf ), as well as it's title and who made it.

#### 2 As a patron I would like to buy artworks within my price range and likes

#### 3 As a frequent patron I would like to keep a record of my purchases with the club

#### 4 As a patron I would like to keep a running total of incomplete orders,
            including V.A.T.,
            delivery charges (if not collecting)
            and potential commission to the club.

#### 5 As a club member I would like to purchase my year's club membership subscription remotely

#### 6 As a member of the art club, I may like to have a record of my work that sold via the club's site

#### 7 As a club administrator I would like to enter new works of art as images with details such as price, media and dimensions of the piece

#### 8 As a club administrator I would like an idea of sales commissions in order to distribute funds to activities that will benefit the club
