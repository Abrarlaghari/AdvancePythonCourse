class NewsPublisher():
    def __init__(self) -> None:
        '''publish a stream of events '''
        self.__subscribers = []
        self.latest_news = None
    # obeservables exposes attach and detach


    def attach(self, new_sub):
        self.__subscribers.append(new_sub)
    def detach(self):
        self.__subscribers.pop()
    def iter_subscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def notify_subs(self):
        return [type(x).__name__ for x in self.__subscribers]

    def add_new(self, news):
        self.latest_news = news
    def get_news(self):
        return f'latest news {self.latest_news}'
