def remove_url_anchor(url):
    if "#" in url:
        return url[:url.index("#")]
    else:
        return url
