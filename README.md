# Let's Get Together

Group generator
Apprenticeship 2018 Coding challenge
This program was written with Python 3.6.5


### Setup Instructions

1.Install requirements:

`pip install -r requirements.txt`

2.Start server:

`python3 app.py`

3.Browse to [`localhost:5000`](http://127.0.0.1:5000/)   



### Running tests
You can run this project's unit tests by calling `python3 tests.py` on the command line.


### Application Instructions

Input each name of an individual who has signed up for "Let's Get Together".
After each name, click `Add Participant` to add that person to the list.  
A note, that duplicate names will not be counted.  Once you have added all of
the names who have signed up, choose the number of people per group from the
dropdown. Once the group size has been chosen, click `Generate Groups` to
generate the random groups, which will displayed.  From this state, you
can click `Regenerate Groups` to shuffle up the current list of participants.
Also from this state, you can change the group size, as well as add more
participants.  
