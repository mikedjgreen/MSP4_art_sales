- [Testing](#testing)
  * [Feature testing](#feature-testing)
  * [Bug testing](#bug-testing)
  * [User Story testing](#user-story-testing)
  * [Responsiveness](#responsiveness)

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
---
#### 1. Artworks programming error
---
![Artworks Error](heroku_artworks_debug_error1.jpg)

Model migration changes had not been implemented on Heroku server.

[Heroku Migrations](heroku_artworks_debug_error.txt)

![Artworks error fixed](heroku_artworks_fixed.jpg)

#### 2. Server Error (500) upon login
---
![Server 500 Error](server_500_login_error.jpg)

This was caused by a wayward migration to update production models.
It cleared the profiles table 'Patron' that had a foreign key relation to alluath's user.

Temporarily set the Patron to be created upon login, regardless.

Then logged in as admin and entered Patron details for  the superuser 'mdjg' to be able to login.

Rolled back the code changes to enable this, and then logged in successfully.

#### 3. Server Error (500) upon adding artworks
---
Used Heroku CLI on Gitpod to access logs.

``` $heroku login -i```

Log showed 500 error

``` $heroku logs -tail --app msp4-art-sales ```

>> 2021-03-26T10:14:53.098938+00:00 heroku[router]: at=info method=POST path="/artworks/add/" host=msp4-art-sales.herokuapp.com request_id=85aef46d-ee34-495e-b48e-100db0362d1f fwd="86.16.134.162" dyno=web.1 connect=1ms service=1021ms status=**500** bytes=410 protocol=https
2021-03-26T10:14:53.101596+00:00 app[web.1]: 10.12.163.136 - - [26/Mar/2021:10:14:53 +0000] "POST /artworks/add/ HTTP/1.1"**500** 145 "https://msp4-art-sales.herokuapp.com/artworks/add/" "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
2021-03-26T10:14:53.482663+00:00 heroku[router]: at=info method=GET path="/favicon.ico" host=msp4-art-sales.herokuapp.com request_id=e2b1a32e-f9f9-47a9-a492-181d0e4960c4 fwd="86.16.134.162" dyno=web.1 connect=0ms service=44ms status=404 bytes=9845 protocol=https
<<

Checking that all database migrations have been enacted on production.

``` $heroku run python3 manage.py showmigrations --app msp4-art-sales```

No, one had not.


>artworks
>- [X] 0001_initial
>- [X] 0002_auto_20210313_1027
>- [X] 0003_auto_20210320_1623
>- [X] 0004_auto_20210321_1834
>- **[ ] 0005_auto_20210326_0846**

>auth

##### Resolution
``` $heroku run python3 manage.py migrate --app msp4-art-sales ```

>Running migrations:
  Applying artworks.0005_auto_20210326_0846... OK
  
``` $heroku logs -tail --app msp4-art-sales```

>2021-03-26T10:20:17.788918+00:00 app[web.1]: 10.11.223.86 - - [26/Mar/2021:10:20:17 +0000] "GET /artworks/29/ HTTP/1.1"**200** 13502 "https://msp4-art-sales.herokuapp.com/artworks/add/" "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"

#### 4. No order details displayed on order confirmation.
---

##### User Story 2 bug

![Order confirmed](user_story2_6.jpg)

##### Resolution

Amended code on checkout model to display order item default
and appropriate display line on checkout_success page.

![Checkout Success](bug_fix_userstory2.jpg)


### User Story testing
---
#### 1 As a visitor to the site I would like to view art works for sale
    If I see something I like, I would like to know the price, what it's made of and size of it ( will it 'fit' on my wall or shelf ), as well as it's title and who made it.
---

Initial view of club's artworks.
![Artworks page](user_story1_1.jpg)

Individual artwork displaying dimensions of the work.
![An artwork detail](user_story1_2.jpg)

#### 2 As a patron I would like to buy artworks within my price range and likes
---
Initial artwork sought.
![Artwork coveted](user_story2_1.jpg)

Artwork successfully added to basket.
![Artwork added to basket](user_story2_2.jpg)

Artwork in basket with purchase details ready to be purchased.
![Artwork ready to buy](user_story2_3.jpg)

Purchase details added. Will the purchaser be a one-off, or will they purchase more in the future?
![Commerce](user_story2_4.jpg)
Using STRIPE's test [credit card details](https://stripe.com/docs/payments/accept-a-payment#testing).

Purchaser completing order without logging in (a one-off sale).
![Completing order](user_story2_5.jpg)

Order has succesful feedback and confirmation email sent.

![Order confirmed](user_story2_6.jpg)

- **There is a bug, the order details have not been displayed.**

Now marked as 'Just Sold!' on artworks page.
![Sold](user_story2_7.jpg)

#### 3 As a frequent patron I would like to keep a record of my purchases with the club
---

A 'frequent patron' of the club suggests first registering with the club.

**Registration**

For testing purposes first set up a [dummy maildrop](https://maildrop.cc/inbox/tellulah).

![Register as TellulahBank](register_as_tellulahbank.jpg)

Confirmation email dropped into test mailbox.

![Register 2](register_as_tellulahbank_2.jpg)


Pasted confirmation URL from mailbox.

![Register 3](register_as_tellulahbank_3.jpg)


Password accepted.

![Register 4](register_as_tellulahbank_4.jpg)

Now logged in, 'frequent patron' has an empty wall and can go for a spree to cover it with pictures.

**Spree**

First order.

![First order](user_story3_1.jpg)

Second Order.
![Second Order](user_story3_2.jpg)


Order History section of Tellulah's profile.
![Order History](user_story3_3.jpg)

Each order is linked to order confirmation email details.
![Order Confirmation Detail](user_story3_4.jpg)





**Additional Test: Checking normal logged in user cannot access administration**

Logged in as Tellulah tried to access /admin in URL:

![Admin login restricted](user_login_not_admin.jpg)




#### 4 As a patron I would like to keep a running total of incomplete orders,
            including V.A.T.,
            delivery charges (if not collecting)
            and potential commission to the club.
---

Every time an artwork is added to the basket, there is a pop-up to inform.
![Shopping basket toast](user_story4_1.jpg)

Going to 'Secure Checkout' will display a detailed running total.

![Secure Checkout for totals](user_story4_2.jpg)




#### 5 As a club member I would like to purchase my year's club membership subscription remotely
---
#### 6 As a member of the art club, I may like to have a record of my work that sold via the club's site
---
#### 7 As a club administrator I would like to enter new works of art as images with details such as price, media and dimensions of the piece
---
From Heroku logs :
> 2021-03-26T10:20:17.788918+00:00 app[web.1]: 10.11.223.86 - - 
>[26/Mar/2021:10:20:17 +0000] "GET /artworks/29/ HTTP/1.1" 200 13502 "https://msp4-art-sales.herokuapp.com/artworks/add/" "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"

Checked artwork (id 29) within admin:

![User Story 7 admin](user_story7_admin.jpg)

```https://msp4-art-sales.herokuapp.com/artworks/29/```
![User Story 7 result](user_story7_result.jpg)

#### 8 As a club administrator I would like an idea of sales commissions in order to distribute funds to activities that will benefit the club
---

### Responsiveness
---
Using Google's Mobile Friendly Test Facility.

[Mobile Friendly Test](https://search.google.com/test/mobile-friendly?id=cQq8QMNS74JlrS_CK1sQFg)

- ![Mobile Friendly screen shot](mobile_friendly_test.jpg)

A page loading issue raised by Mobile Friendly can be explained by STRIPE blocking robots....

- ![Mobile Friendly Page Loading Issue](mobile-friendly-load-issue.jpg)
