from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class List(Base):
    __tablename__ = 'lists'

    id = Column(Integer, primary_key=True)
    list_id = Column(Text)
    name = Column(Text)
    owner_id = Column(Text)
    address = Column(Text)

    def __repr__(self):
        return f'List {self.name}'


class Tweet(Base):
    __tablename__ = 'tweets'

    id = Column(Integer, primary_key=True)
    status_id = Column(Text(32))
    text = Column(Text)
    twitter_user_id = Column(Text(32))
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime)
    favorite_count = Column(Integer)
    is_quote = Column(Boolean)
    is_retweet = Column(Boolean)
    list_id = Column(Integer, ForeignKey("lists.id"), nullable=False)
    reply_count = Column(Integer)
    quote_count = Column(Integer)
    quoted_status_id = Column(Text)
    quoted_screen_name = Column(Text)
    retweet_count = Column(Integer)
    reply_to_screen_name = Column(Text)
    reply_to_status_id = Column(Text)
    in_reply_to_status_id = Column(Text)
    retweet_name = Column(Text)
    source = Column(Text)
    display_text_width = Column(Text)
    retweet_screen_name = Column(Text)
    retweet_status_id = Column(Text)
    retweet_text = Column(Text)
    retweet_created_at = Column(DateTime)
    retweet_verified = Column(Boolean)
    media_type = Column(Text)

    UniqueConstraint('twitter_id', 'list_id', name='unique_tweet')

    def __repr__(self):
        return f'Tweet {self.id}'


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    list_id = Column(Integer, ForeignKey("lists.id"), nullable=False)
    twitter_user_id = Column(Text(32))
    screen_name = Column(Text)
    name = Column(Text)
    followers_count = Column(Integer)
    friends_count = Column(Integer)
    bio = Column(Text)
    account_created_at = Column(DateTime)
    statuses_count = Column(Integer)
    updated = Column(Boolean)
    withheld_scope = Column(Text)
    protected = Column(Boolean)
    verified = Column(Boolean)
    active = Column(Boolean)


class Hashtag(Base):
    __tablename__ = 'hashtags'

    id = Column(Integer, primary_key=True)
    tweet_id = Column(Integer, ForeignKey("tweets.id"), nullable="False")
    text = Column(Text)


class Mention(Base):
    __tablename__ = 'mentions'

    id = Column(Integer, primary_key=True)
    tweet_id = Column(Integer, ForeignKey("tweets.id"), nullable="False")
    screen_name = Column(Text)
    user_str_id = Column(Text)


class Url(Base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True)
    tweet_id = Column(Integer, ForeignKey("tweets.id"), nullable="False")
    url = Column(Text)