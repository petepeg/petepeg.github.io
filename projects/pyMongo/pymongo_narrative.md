# PyMongo Narrative

### *Briefly describe the artifact. What is it? When was it created?*
The artifact is a fairly basic Application Program Interface (API) for MongoDB written in Python using the pyMogno library. It implements the basic Create, Read, Update, Delete (CRUD) operations as well as a few advanced queries through a RESTful API. It was created early 2020 for my CS-340 class.

### *Justify the inclusion of the artifact in your ePortfolio. Why did you select this item? What specific components of the artifact showcase your skills and abilities in software development? How was the artifact improved?*
I included the item because it shows use of several libraries, use of a database, and development of an API. I think it does a good job of showcasing my knowledge of web API’s as well as my proficiency in Python. With the improvements I made I think it does a good job of showcasing documentation development. The major improvements I made were in error reporting and documentation.

### *Reflect on the process of enhancing and/or modifying the artifact. What did you learn as you were creating it and improving it? What challenges did you face?*
The first thing I did was to go through the code and remove some of the development code I had put in. Mostly strings that returned to the console, which was fine for prototyping, but having actual error codes being returned along the proper channels was preferable. Next, I added docstrings to all my functions with markdown so I could use PDoc3 to generate some basic documentation on how the API functioned. Proper documentation in an API is very important since most of the time people using it are not going to want to look at your code to figure out how to interact with it. I had never worked with PDoc3 before, but it functioned pretty similarly to JavaScript documentation generators, so I found the learning process fairly simple. I was prompted to create the API documentation when I came back to the code and couldn’t remember how it all worked. I had to look it up in my submitted coursework, and that’s when I realized It would have been good to have done this from the start.

[Back](./pymongo)
