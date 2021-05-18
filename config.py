SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Emxhcrc0@localhost:5432/lifetech_mobile'
# PRODUCTION_SQL_DATABASE_URI = 'postgresql+psycopg2://mocitftfgbveqp:1601d005562710902e913d49e4363259a04fe64cd0a4ba97f084ab057035815d@ec2-184-73-198-174.compute-1.amazonaws.com:5432/d46s610u0nlckl'

# NOTE: This is exactly the URI that heroku created and gave to me to connect to the database. However, it is my understanding that the portion of the URI that says
# postgres has been changed to be required to have it say 'postgresql' instead of just 'postgres'. I ran into issues earlier with this when I was trying to deploy to
# the local host. Above, I have tried modifiying the URI, but I still need to test it.
PRODUCTION_SQLALCHEMY_DATABASE_URI = 'postgres://mocitftfgbveqp:1601d005562710902e913d49e4363259a04fe64cd0a4ba97f084ab057035815d@ec2-184-73-198-174.compute-1.amazonaws.com:5432/d46s610u0nlckl'
