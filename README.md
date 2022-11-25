# Spartandevs
CMPE 272 project of group SpartanDevs 

 CMPE272-Enterprise SW Platforms-  : Bookhouse []

University Name : [San Jose State University](https://www.sjsu.edu/)

Course Name : Enterprise Software Platforms - CMPE272

Professor's Name : [Andrew Bond]

Team Name: Spartandevs

- Team Members:
- [Bhavya Hegde](www.linkedin.com/in/bhavya-hegde-145b9b123)
- [Darshini Venkatesha Murthy Nag](https://www.linkedin.com/in/darshini-venkatesha-murthy-nag-90052756/)
- [Sirisha Polisetty](https://www.linkedin.com/in/sirishapolisetty/)

* Bookhouse is an enterprise ecommerce platform that aims to create a seamless online book shopping experience and helps brick-and-mortar book shops to digitize their businesses. Our website allows its users to browse through a vast collection of books, add books to the cart, and place an order using  payment method with shipping preferences. Our web application has two modes. One is a storefront for users to shop and track their book orders. Another one is admin management, where the bookhouse staff can maintain book stocks and facilitate shipping orders. Bookhouse web application will be developed using the Django framework with login, registration, cart, reviews, order, search, and payment processing capabilities. Bookhouse provides users the convenience of shopping for books from home. Bookhouse storefront will have features like search and pagination to provide ease of use for the  users to search books on the application. 

## Application Features
## Admin Features:

## Tools and Technologies used:
* Frontend: HTML,Bootstrap, ChartJs
* Backend: Python Django framework
* Other tools: Jenkins, Visual studio code.
  
## Architecture Diagram
## AWS components
* **Amazon RDS** : 
* **Amazon S3** : 
* **Amazon EC2** : 
#### CI/CD Pipeline


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

