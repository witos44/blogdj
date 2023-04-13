# djblogger

 In this Project we will build a Blog with Latest & Advance Techniques, Like setting environment variables, using pytest and other features

In this Project we have following functionalities:

* Settings for Production and Development
* Loading Secret Data from the Environment variables
* Writing Tests for the Django Application with pytest. And use factory-boy to generate fake data for testing purposes
* Saving Tests into HTML format with pytest-cov
* Class based views
* build URLs at the Application level
* build TEMPLATES folder at the Application level, and then mention it in the settings file, with this code `os.path.join(BASE_DIR, 'templates')`
* build STATIC folder at the Applicaiton level, and then mention it in the settings file, with this code `STATICFILES_DIRS = [
    BASE_DIR / "static"
]`
* Add Google Fonts
* Use Factory-boy and Faker to generate Fake Data for Blog Posts
* htmx is a library that allows you to access modern browser features directly from HTML, rather than using javascript.[Django_HTMX]('https://pypi.org/project/django-htmx/')
