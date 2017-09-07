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


### Warning

Overusing this library might lead to your IP being blocked by Google Search servers.
Searches through Chrome or another browser might still work but this library will stop working.
I recommend keeping a 15 seconds gap after each usage of this library.
In most cases, much lower gaps or even continuous use of the library will still work but still this is something to be kept in mind.
If you see a 'rate limit' or a 503 error, it's best to stop using the library and try back after some time (~1 minute).


### Inspiration

[google by Mario Vilas](https://breakingcode.wordpress.com/2010/06/29/google-search-python/)
