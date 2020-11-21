import os
class Config:
    NEWS_SOURCES_BASE_URL='https://newsapi.org/v2/sources?apiKey=d217044c3128468a9b423f1f23f5cc6d'
    ARTICLES_BASE_URL='https://newsapi.org/v2/everything?sources=bbc-news&apiKey=d217044c3128468a9b423f1f23f5cc6d'
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')

    @staticmethod
    def init_app(app):
        pass
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG=True

config_options={
    'development':DevConfig,
    'production':ProdConfig
}
