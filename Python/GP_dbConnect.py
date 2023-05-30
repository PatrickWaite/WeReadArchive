#this is the template conncection string used for a postgreSQL database with the SQLalchemy  library.
def get_connectionString():
    user = '' #database username
    password = '' #databalse password
    host = '' #ip or url that hosts the database
    port = '' #port needed to access database
    database = '' #database name

    #######postgreSQL connection strings
    return "postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database)
    #return "postgresql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database)
    #return "postgresql+pg8000://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database)

    ########MySQL connection strings
    #return "mysql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database)
    #return "mysql+mysqldb://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database)
    #return "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database)
    
    #########Oracle
    #return "oracle://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database)
    #return "oracle+cx_oracle://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database)


    #information on the connection strings used for SQLAlchemey can be found at the link below
    #Link: https://docs.sqlalchemy.org/en/20/core/engines.html