does not work on Heroku because it tries to sign in to the account from Ireland (apparently the place where the westeurope servers are located), so instagram detects unauthorized login and won't let us pass through unless we enter 6-digit verification code which will be send to our mail.

works fine on localhost though

uncomment code inside bot.py constructor and comment the rest inside the constructor for it to work on heroku instead on localhost 