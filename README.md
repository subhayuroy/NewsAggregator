<h1 align="center">NewsAggregator</h1>
<h3 align="center">What is a News Aggregator?</h3>
It is a web application which aggregates data (news articles) from multiple websites. Then presents the data in one location.

News aggregator service is a very important start of the day.

There are various publications and news sites online. They publish their content on multiple platforms. Now, imagine when you open 10-20 news sites every day. The time you waste to gain information. Information gain is everything in today’s world.

It can give you leverage over those who don’t have it. Now, is there a way we can make it easier? Yes!!

A news aggregator makes this task easier. In a news aggregator, you can select the websites you want to follow. Then the news aggregator collects the articles for you. And, you are just a click away to get information from various websites.

This task otherwise takes too much time on our schedule.

About the Django Project
A news aggregator is a combination of web crawlers and web applications. Both of these technologies have their implementation in Python. That makes it easier for us.

So, our news aggregator will work in 3 steps:

1. It scrapes the web for the articles. (In this Django project, we are scraping a website called theonion)
2. Then it stores the article’s images, links, and title.
3. The stored objects in the database are served to the client. The client gets information in a nice template.
So, that’s how our web app will work.

<h1 align="center">How to access this project?</h1>

1. Push this git command in your command line:
`git@github.com:subhayuroy/NewsAggregator.git`

2. Install all the libraries required:
`pip3 install -r requirements.txt`

3. Depending on your Python version run this command:
`python manage.py runserver`

4. Open this app in:
`http://127.0.0.1:8000/`
