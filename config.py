from my_password import password as db_password

class DevelopmentConfig:
    # SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://root:{db_password}@localhost/adv_api_e_commerce'
    SQLALCHEMY_DATABASE_URI = 'postgresql://e_comm_cicd_db_user:DU93U3801dH199ECs4PRO0L2QO6f6B6w@dpg-crqnbhtumphs73br1kjg-a.oregon-postgres.render.com/e_comm_cicd_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = 'SimpleCache'
    DEBUG = True