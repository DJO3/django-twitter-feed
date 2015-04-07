django-twitter-feed3
===================

Really simple app to show a Twitter feed in your Django application.

Schedule a task to update the feed regularly.

Compatible with Python 3 and Django 1.7+.

INSTALL:
--------
`pip3 install git+git://github.com/DJO3/django-twitter-feed3`


Set-up:
-------

1.Add it to your "INSTALLED_APPS" settings:

    INSTALLED_APPS = (
        ...
        'twitter_feed',
        ...
    )

2.Add your twitter account API access in the settings like this:

    TWITTER_FEED_CONSUMER_PUBLIC_KEY = '...'
    TWITTER_FEED_CONSUMER_SECRET = '...'
    TWITTER_FEED_OPEN_AUTH_TOKEN = '...'
    TWITTER_FEED_OPEN_AUTH_SECRET = '...'

3.Run `python manage.py migrate` (if you use South) or `python manage.py syncdb`

4.Run the following command lines to test your Twitter credentials and save the initial feeds:
* `python manage.py update_tweets`
* `python manage.py show_tweets`

5.In a template, show the latest 10 tweets for example:

    {% load twitter_feed_tags %}
    {% latest_tweets 10 %}

6.Customise the template - simply create a copy of `twitter_feed/latest_tweets.html` and edit it.

For example:

	{% load twitter_feed_tags %}

	<div class="tweets">
    	{% for tweet in tweets %}
	      <div class="tweet">
    	    <p>{{ tweet.content|linkify_twitter_status|urlize|url_target_blank }}</p>
        	<p class="date">{{ tweet.published_at|date:"F d, Y" }}</p>
	      </div>
    	{% endfor %}
	</div>
	
7.Make sure `python manage.py update_tweets` is regurlalry called.
------------------------------------------------------------------------

8.Add the following js to your base.html: 

`<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>` 

9.Add the following to your div to get a beautiful twitter feed:   

	{% load twitter_feed_tags %}

	<div class="tweets">
    	{% for tweet in tweets %}
    	    <blockquote class="twitter-tweet" lang="en">
                <a href="https://twitter.com/{{ tweet.screen_name }}/status/{{ tweet.id_str }}"></a>
            </blockquote>
        {% endfor %}
	</div>
	
