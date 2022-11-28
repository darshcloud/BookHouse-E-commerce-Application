
# CMPE 272 Project of Group Spartan Devs 
<b>Course Name :</b> Enterprise Software Platforms

<b>Project Name  :</b> Bookhouse 

<b>Application URL :</b> https://bookhouse.space

<b>University Name :</b> [San Jose State University](https://www.sjsu.edu/)



<b>Professor's Name :</b> Andrew Bond

<b>Team Name:</b> Spartan Devs

<b>Team Members:</b> <br/>
[Bhavya Hegde](www.linkedin.com/in/bhavya-hegde-145b9b123)<br/>
[Darshini Venkatesha Murthy Nag](https://www.linkedin.com/in/darshini-venkatesha-murthy-nag-90052756/)<br/>
[Sirisha Polisetty](https://www.linkedin.com/in/sirishapolisetty/)<br/>

## Introduction

Bookhouse is an enterprise ecommerce platform that aims to create a seamless online book shopping experience and helps brick-and-mortar book shops to digitize their businesses. Our website allows its users to browse through a vast collection of books, add books to the cart, and place an order using  payment method with shipping preferences. Our web application has two modes. One is a storefront for users to shop and track their book orders. Another one is admin management, where the bookhouse staff can maintain book stocks and facilitate shipping orders. Bookhouse web application will be developed using the Django framework with login, registration, cart, reviews, order, search, and payment processing capabilities. Bookhouse provides users the convenience of shopping for books from home. Bookhouse storefront will have features like search and pagination to provide ease of use for the  users to search books on the application. 

## Application Features
* Wide variety of books available for purchase
* Various book categories
* Book Search Functionality, either by book name or by category
* Custom Login and SSO login Integration for signing into the application
* Shopping cart and Checkout functionality
* Paypal Integration for payment
* SSL certificate installation
* Jenkins for CI/CD pipeline

## Bookhouse admin Features
* Book administrators can manage book stocks
* Manage book orders
* Addition, Update and Deletion of book details such as book category, book price and book description
* Manage Users

## Additional Application Features
* Dashboard view - Users can view details about current and previous orders and can update profile
* Review and Rating System - Users can post rating and reviews about the book which they have purchased
* Preview of the book content is provided for the users
* Application is deployed on cloud to offer high scalability, security and availability


## Tools and Technologies used
Frontend: HTML, CSS, Bootstrap, Javascript<br/>
Backend: Python Django framework<br/>
Other tools: Jenkins, Visual studio code, PyCharm<br/>
AWS components: EC2, Route 53, ELB, RDS posgres , certificate manager
  
## Architecture Diagram
![bookhouse_architecture](https://user-images.githubusercontent.com/111547793/204049096-8391e996-7997-4bfe-8c8b-30d1100f2d29.png)



## CI/CD Pipeline


## Instructions to run project locally
#### Create a virtual environment
```
python -m venv venv
  ```
#### Activate the virtual environment

* macOS:
```
source venv/bin/activate
```

* Windows:
```

venv\scripts\activate
```

#### Install required dependencies
```
pip install -r requirements.txt
```
#### Set up environment variables
```
touch .env
```
#### We need to add below details in env
```
SECRET_KEY=
DEBUG=True
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_USE_TLS=True
```

#### Run migrations
```
python manage.py makemigrations
python manage.py migrate
```

#### Create an admin user to access the Django Admin interface
```
python manage.py createsuperuser
```

#### Run the application
```
python manage.py runserver
```



## Sample Demo screenshots


## References
AWS Documentation: https://docs.aws.amazon.com/

Book Images: https://www.amazon.com/ 

Deploy django app with https, gunicorn and Nginx : https://realpython.com/django-nginx-gunicorn/
