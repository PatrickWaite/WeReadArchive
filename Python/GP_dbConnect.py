#this is the template conncection string used for a postgreSQL database with the SQLalchemy  library.
def get_connectionString():
    user = '' #database username
    password = '' #databalse password
    host = '' #ip or url that hosts the database
    port = '' #port needed to access database
    database = '' #database name
    return "postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database)
    