class Document:
    def __init__(self, title: str, url: str, content: str):
        self.title = self.escape(title)
        self.url = self.escape(title)
        self.content = self.escape(content)

    def __call__(self) -> str:
        return '<document>' \
               '<url>%s</url>' \
               '<title>%s</title>' \
               '<snippet>%s</snippet>' \
               '</document>' % (self.url, self.title, self.content)

    @staticmethod
    def escape(s: str) -> str:
        s = s.replace('&', '&amp;')
        s = s.replace('"', '&quot;')
        s = s.replace('\'', '&apos;')
        s = s.replace('<', '&lt;')
        s = s.replace('>', '&gt;')
        return s