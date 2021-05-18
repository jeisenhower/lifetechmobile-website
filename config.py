# SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Emxhcrc0@localhost:5432/lifetech_mobile'

SQLALCHEMY_DATABASE_URI = 'postgresql://mafaxmxzjhkulo:b93af7d65b75fe86dbdd994693d64b56c14cbfff05810de82992694bd3a41e89@ec2-52-0-114-209.compute-1.amazonaws.com:5432/d15ksnn5cth4p8'
# NOTE: This is exactly the URI that heroku created and gave to me to connect to the database. However, it is my understanding that the portion of the URI that says
# postgres has been changed to be required to have it say 'postgresql' instead of just 'postgres'. I ran into issues earlier with this when I was trying to deploy to
# the local host. Above, I have tried modifiying the URI, but I still need to test it.

# SQLALCHEMY_DATABASE_URI = 'postgres://mafaxmxzjhkulo:b93af7d65b75fe86dbdd994693d64b56c14cbfff05810de82992694bd3a41e89@ec2-52-0-114-209.compute-1.amazonaws.com:5432/d15ksnn5cth4p8'
