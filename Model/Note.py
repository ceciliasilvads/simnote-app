class Note:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title
    
    def set_content(self, content):
        self.content = content

    def get_content(self):
        return self.content