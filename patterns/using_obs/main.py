from news_pub import NewsPublisher
from email_sub import EmailSubscriber


subs_t = (EmailSubscriber)

def main():
    new_pub = NewsPublisher
    for subsscriber in subs_t:
        subsscriber(new_pub)

        new_pub.add_new('New news')
    new_pub.notify_subs()

if __name__ == '__main__':
    main()
