steps:-

1.create virtualenv 
2.Run requirements file
3.Then check .env file for postgresql db setup
4.Run python manage.py makemigrations (To create migration file)
5.Run python manage.py migrate (apply changes migration file to db)
6.Run server using python manage.py runserver