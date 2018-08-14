class Document:
    def __init__(self, title: str, url: str, content: str):
        self.title = title
        self.url = url
        self.content = content

    def __call__(self) -> str:
        return '<document>' \
               '<url>%s</url>' \
               '<title>%s</title>' \
               '<snippet>%s</snippet>' \
               '</document>' % (self.url, self.title, self.content)