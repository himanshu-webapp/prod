# CRIndia
This is the development version of the code.
In order to use it as a production some changes might be necessary.

Set the environment variables as follows - (These changes are not to be made in file. For details to set the environment variables google it or ask me.)
DJANGO_DEBUG = False
DJANGO_SECRET_KEY = 'some random string of characters like you have in the settings.py of the root.'

These are the required steps - (Site would not function properly without these.)
1. Set the allowed host as per your preference.
2. push on heroku.
3. make a migration
4. create superuser
-> The site should be running. (including the admin panel)

5. To use it properly , then uncomment the 6 lines (3 each) in get_category() and get_services() functions in 
    models.py in services.    
6. Push it again on heroku.
-> Now everything is set up. Add services from admin panel and it will gradually show on the website.

Note: Everytime you add any service or a service category , make sure to restart the server. It won't be reflected
      otherwise.
      
The order in which you should add services - Service Category > Service > Service Images


