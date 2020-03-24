## Awwards App

## Author

Buong Patrick

## Description

This application allows users to post,rate and view the project posted by users.

## Setup and installation
##### Clone the repository:  
 ```bash 
 https://github.com/Patrick322/Awwards.git 
```

##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  


##### Navigate into the folder and install requirements with te command:
 ```bash 
pip install -r requirements.txt 
```

##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrations:
 ```bash 
python manage.py makemigrations awwardsapp
 ``` 
 Then Migrate: 
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.

## Database Diagram
![](media/photos/Untitled(1).png)

## Technologies Used
* Python3.6
* Django
* HTML
* Bootstrap

## Contacts
* Email:patrickbuong@gmail.com
* Tel:0797239875
* Github:Patrick322
