class News():
    def __init__(self, news_title, news_contents):
        self.__news_title = news_title
        self.__news_contents = news_contents

    def get_news_title(self):
        return self.__news_title

    def get_news_contents(self):
        return self.__news_contents

    def set_news_title(self, news_title):
        self.__news_title = news_title

    def set_news_contents(self, news_contents):
        self.__news_contents = news_contents