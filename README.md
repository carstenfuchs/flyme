# FlyMe

FlyMe is an online logbook and management software for private pilots and associations.

This software helps with common tasks in private aviation.
It is intended for use by individual pilots, flying clubs, owner associations, flight schools and charter services.

The feature set is tailored to private flying:

  - pilot logbooks
  - airplane logbooks
  - compute membership and flight fees
  - reserve airplanes
  - works on smartphones, tablets and desktop PCs
  - ease of use – also when time is short

This software requires a live internet connection.
It is not intended for use in flight, but can well be used immediately thereafter:
Complete your flight records conveniently and quickly even before you leave the cockpit.

Note that this software can *not* replace the keeping of flight records on paper where this is legally required.


## Implementation

This software is implemented as a web application.
It runs in web browsers on mobile devices and desktop PCs.
As such, end users can use it without installing any additional software.

For operators, providing this application requires knowledge of [Python](https://www.python.org) and [Django](https://www.djangoproject.com) in order to install and deploy it on a web server.
At this time, I develop this program for my personal use, hosting it for a couple of friends and myself.
There is no public service yet, but I'll consider this at a later time for demo purposes.
As such, the program is not ready for anyone but experienced Django web developers who can operate it on their own.

FlyMe is open source software developed at [GitHub](https://github.com/carstenfuchs/flyme).
It is licensed under the [MIT license](https://github.com/carstenfuchs/flyme/blob/master/LICENSE).
Contributions are welcome!


## Motivation

A lot of similar software already exists, so why make yet another one?

My main motive was the situation that we frequently experience after a landing:
Taxied to the parking position, engine shut down, a kneeboard full of handwritten notes, some ops time indicator in the panel.
And a hurry:
To get the airplane into the hall before the rain begins or the airport closes, to see the restrooms, to get something tasty to drink.

Similarly, after a day of flying with a glider (or several), we're possibly left with a handwritten list of mixed flights that must be copied into the personal logbook. It's worse if you're an instructor.

In all cases, time is short and we have to copy a lot of boring information into the personal and airplane logbooks:
nicely, cleanly written, no mistakes. On the first try. And without the desire to take it all with home to do it orderly.

Well.

### Not wanted

But here is something that I did **not** want:

A software that requires me to select the airplane that I have used from a pre-made list of choices – in which it is missing.
Either because it's my friend's, one of a charter service, or one that no one has bothered putting into the database yet.
Or one in which I have to search for the proper input field for the off-block time.
One in which the software claims in an obscure message that I made some mistake that I didn't (and thus refuses to save the entire record).
Or one that fails to save only because I forgot to note and cannot remember the take-off time.

From the perspective of the software developer, I also did not want a software that has dozens of data structures
with ever growing complexity where I'd spend more time with getting the permissions management right
than actually working on the useful features.
It's easy to get lost in an exploding effort for minor things. Not wanted.

### Wanted

Back to the things that are *wanted*:

  - A software with which the saving of a flight record *never* fails for bad user input.
  - One that does it's best to find known airplanes and airfields, but lets me get away with free-style input either.
  - One that knows that I cannot have made the landing before the takeoff.
  - One derives as much as possible automatically, but that lets me – if so desired – review and revise the entered data later.
  - And one for which users only have to remember very few and basic rules. No handbook required, but optionally available.

Everything else is about how to make this work.

### Extras

While we're at it, it would be sloppy if we didn't use the opportunity for a couple of extras.

For example, I'm a member of a flight club and independently a member of an owner's association.
Sometimes I do not only wish to see my personal records, but also the airplane logbooks.
Given the personal and airplane logbooks, some monthly or yearly summaries are desirable.

And given all that, even some of the administrative stuff becomes worthwhile, after all:
For example a reservation system or the ability to compute flight costs also for other users of the airplane.
And then we also need a minimal form of rights management (not everywhere where I'm a member am I allowed to see all information about all airplanes).

*But:* All extras are secondary, optional and still as easy to use as promised!
