Scrapy Redirect Middleware
==========================

This redirect middleware is a direct clone of the Scrapy redirect middleware 
with just one extra line of code. Current middleware do not collect redirect status codes
which maybe useful for the ranking model.

```python
response.meta['redirect_urls'] # <---- redirected urls
response.meta['redirect_status_code'] # <---- redirected HTTP status code
response.meta['redirect_times'] # <---- total number of redirects
```

These fields are present only if you enable redirect middleware in the `settting.py` file:
* `REDIRECT_ENABLED = True`
* `HTTPERROR_ALLOWED_CODES = range(200,400)` or
* `HTTPERROR_ALLOW_ALL = True`

## Installation 
```
pip install .
```

## Configuration
```python
DOWNLOADER_MIDDLEWARES = {
    'scrapy_redirect.RedirectMiddleware': 600,
    'scrapy_redirect.MetaRefreshMiddleware': 580, 
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware': None
}
```



