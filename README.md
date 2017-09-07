# Python Google Search API

Unofficial Google Search API for Python. It uses web scraping in the background and is compatible with both **Python 2 and 3**.


### Why this project?

No such library exists which works out of the box i.e. without requiring any external dependencies.
I did this so that I can use it on my [Alfred workflow](https://github.com/aviaryan/alfred-google-search).
But this turned out to be pretty generic, feel free to use it for your own work.


### Installation

```sh
pip install gsearch
```


### Using

```sh
> from gsearch.googlesearch import search

> results = search('Full Stack Developer')  # returns 10 or less results
[ ('Name', 'Link'),
  ('Name', 'Link'),
  ... ]

> results = search('Avi Aryan', num_results=20)  # returns 20 or less results
```

You can also use it as a CLI tool.

```sh
$ gsearch "Why Python is awesome"
```


### Examples

```sh
>>> from gsearch.googlesearch import search
>>> search('Python')
[('Welcome to Python.org', 'https://www.python.org/'), ('Python (programming language) - Wikipedia', 'https://en.wikipedia.org/wiki/Python_(programming_language)'), ('Python tutorial - TutorialsPoint', 'https://www.tutorialspoint.com/python/'), ('Learn Python (Programming Tutorial for Beginners) - Programiz', 'https://www.programiz.com/python-programming'), ('Learn Python | Codecademy', 'https://www.codecademy.com/learn/learn-python'), ('Learn Python | Codecademy', 'https://www.codecademy.com/en/courses/learn-python/lessons/python-syntax/exercises/welcome'), ('Introduction · A Byte of Python', 'https://python.swaroopch.com/'), ('Solve Introduction Questions | Python | HackerRank', 'https://www.hackerrank.com/domains/python')]
>>>
>>> search('Google Search API', num_results=15)
[('Custom Search JSON/Atom API | Custom Search | Google Developers', 'https://developers.google.com/custom-search/json-api/v1/overview'), ('Custom Search | Google Developers', 'https://developers.google.com/custom-search/'), ('Using REST to Invoke the API | Custom Search | Google Developers', 'https://developers.google.com/custom-search/json-api/v1/using_rest'), ('Custom Search Engine - Google', 'https://www.google.com/cse/'), ('What are the alternatives now that the Google web search API has ...', 'https://stackoverflow.com/questions/4082966/what-are-the-alternatives-now-that-the-google-web-search-api-has-been-deprecated'), ('Is there an API for Google search results? - Quora', 'https://www.quora.com/Is-there-an-API-for-Google-search-results'), ('Fetch Google Search Results with the Site Search API - CtrlQ.org', 'https://ctrlq.org/code/20076-google-search-api'), ('Google Custom Search API | ProgrammableWeb', 'https://www.programmableweb.com/api/google-custom-search'), ('Google Search API Alternative | Webhose.io', 'https://webhose.io/google-search-api-alternative'), ('FAROO - Free Search API', 'http://www.faroo.com/hp/api/api.html'), ("Google's Ajax Search API | Search Engine Watch", 'https://searchenginewatch.com/sew/news/2056817/googles-ajax-search-api'), ('Search | GitHub Developer Guide', 'https://developer.github.com/v3/search/'), ('Using the Google SOAP Search API - SEO Chat', 'http://www.seochat.com/c/a/google-optimization-help/using-the-google-soap-search-api/')]
```


### Warning

Overusing this library might lead to your IP being blocked by Google Search servers.
Searches through Chrome or another browser might still work but this library will stop working.
I recommend keeping a 15 seconds gap after each usage of this library.
In most cases, much lower gaps or even continuous use of the library will still work but still this is something to be kept in mind.
If you see a 'rate limit' or a 503 error, it's best to stop using the library and try back after some time (~1 minute).


### Inspiration

[google by Mario Vilas](https://breakingcode.wordpress.com/2010/06/29/google-search-python/) -
A library which does almost the same thing except that it uses external dependencies.
This library also has some additional optimizations to reduce the chances of hitting `rate limit`.
