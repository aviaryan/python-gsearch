# Python Google Search API

Unofficial Google Search API for Python. It uses web scraping in the background and is compatible with both **Python 2 and 3**.


### Why this project?

No such library exists which works out of the box i.e. without requiring any external dependencies.
I did this so that I can use it on my Alfred workflow.
But this turned out to be pretty generic, feel free to use it for your own work.


### Installation

```sh
pip install googlesearch
```


### Using

```sh
> from googlesearch import search

> results = search('Full Stack Developer')  # returns 10 or less results
[ ('Name', 'Link'),
  ('Name', 'Link'),
  ... ]

> results = search('Avi Aryan', num_results=20)  # returns 20 or less results
```


### Inspiration

[google by Mario Vilas](https://breakingcode.wordpress.com/2010/06/29/google-search-python/)
