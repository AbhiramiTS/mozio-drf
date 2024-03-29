### BACKEND/PYTHON CODING PROJECT:

Goals:

    - demonstrate proficiency in Django/Python

    - build something that scales gracefully & is easily extensible

    - Write good API docs & Tests


Prompt:

	As Mozio expands internationally, we have a growing problem that many transportation suppliers we'd like to integrate cannot give us concrete zipcodes, cities, etc that they serve. To combat this, we'd like to be able to define custom polygons as their "service area" and we'd like for the owners of these shuttle companies to be able to define and alter their polygons whenever they want, eliminating the need for mozio employees to do this boring grunt work.


    We'd like you to build a JSON REST API to help us solve this problem. Create a Github account if you do not have one already and put all of your source code on github. Your project should have API endpoints to create, update, delete, and retreive information about providers. Batch operations are not necessary except for get. A provider should contain the following information:

    - Name

    - Email

    - Phone Number

    - Language

    - Currency


    Once a provider is created they should be able to start defining service areas. These service areas will be geojson polygons and should be stored in the database in a way that they can be retreived and queried upon easily. There should be endpoints to create, update, delete, and get a polygon. Batch operations are not necessary except for get. A polygon should contain a name and price as well as the geojson information.


    You should create an API endpoint to query this data. It should take a lat/lng pair as arguments and return a list of all polygons that include the given lat/lng. The name of the polygon, provider's name, and price should be returned for each polygon. This operation should be FAST. Mozio has thousand of providers and hundreds of thousands of service areas.

    

    All of this should be built in python/django. Use any extra libraries you think will help, choose whatever database you think is best fit for the task, and use caching as you see fit. Once you finish, write up some API docs (again using any tool you see fit) and make sure your code is well tested. Ensure that your code is clean, follows standard pep8 style (though you can use 120 characters per line) and has comments where appropriate.