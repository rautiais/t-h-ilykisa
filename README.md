# Tohoilykisa (aka The Clumsiness competition)

The clumsiness competition application keeps track of the users' clumsiness.

The idea behind this application is to determine who is the most clumsy person in the group. There are many ways to exhibit clumsiness, for instance, tripping, falling down while walking (maybe the road is icy or maybe you are just clumsy), falling down while standing (now you are just being clumsy), falling off a vehicle (e.g., a bicycle), bumping into something (e.g., a wall, a chair, a coffee table, another person (spatial awareness is challenging..)), getting a cut or a burn while doing something (e.g., reading a book and getting a paper cut, burning yourself while cooking or baking), hitting your head on a cabinet door, or dropping something for no reason. There might also be a correlation between being clumsy and intoxication levels, which this application considers by checking if the clumsiness occurred while being intoxicated.

In the end, the most important criterion for defining clumsiness is that it is caused by oneself accidentally. It is not about incidents that occur while attempting something potentially harmful but about everyday incidents.

At the moment, working features include registering, logging in and logging out. You can create a new group and join an existing group but both of the features are still a working process. You can also create a new event category but the other features are still lacking. 

Application features:
- The user can create an account and log in and log out.
- The user can join a competition group.
- The user can add a clumsiness event.
- The user can delete a clumsiness event.
- Events are categorized based on the type of clumsiness.
- Within different competition groups, there will be charts to track who has been the most clumsy, divided by categories based on the type of clumsiness.
- The user can view their own competition group's charts.

## Startup instructions

This application cannot be tested on Fly.io. Here are the instructions how to start the application.

Clone this repository to your computer and navigate to its root directory. Create a .env file in the directory and set its contents as follows:
```
DATABASE_URL=<database-local-address>
SECRET_KEY=<secret-key>
```
Activate the virtual environment and install the application dependencies with the commands:
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r ./requirements.txt
```
Define the database schema with the command:
```
$ psql < schema.sql
```
You can start the application with the command:
```
$ flask run
``` 