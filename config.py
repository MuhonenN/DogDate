import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
        ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASK_MAIL_SUBJECT_PREFIX = '[Flask]'
    FLASK_MAIL_SENDER = 'DogDate Admin <dogdate@example.com>'
    FLASK_ADMIN = os.environ.get('FLASK_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_POSTS_PER_PAGE = 20
    FLASK_FOLLOWERS_PER_PAGE = 50
    FLASK_COMMENTS_PER_PAGE = 30
    SQLALCHEMY_RECORD_QUERIES = True
    FLASK_SLOW_DB_QUERY_TIME = 0.5
    SSL_REDIRECT = False
    GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
    UPLOAD_FOLDER = 'app/static/uploads/'
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    DB_NAME = 'dogdate'
    DB_USERNAME = 'root'
    DB_PASSWORD = ''
    DB_URL = 'mysql+pymysql://' + DB_USERNAME + ':' + \
        DB_PASSWORD + '@localhost:3306/' + DB_NAME
    SQLALCHEMY_DATABASE_URI = DB_URL


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # email error to the administrators
        import logging
        from logging.handlers import SMTPHandler
        credentials = None
        secure = None
        if getattr(cls, 'MAIL_USERNAME', None) is not None:
            credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
            if getattr(cls, 'MAIL_USE_TLS', None):
                secure = ()
        mail_handler = SMTPHandler(
            mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
            fromaddr=cls.FLASK_MAIL_SENDER,
            toaddrs=[cls.FLASK_ADMIN],
            subject=cls.FLASK_MAIL_SUBJECT_PREFIX + ' Application Error',
            credentials=credentials,
            secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)


class HerokuConfig(ProductionConfig):
    SSL_REDIRECT = True if os.environ.get('DYNO') else False

    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        # handle reverse proxy server headers
        from werkzeug.middleware.proxy_fix import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app)


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'heroku': HerokuConfig,

    'default': DevelopmentConfig
}
