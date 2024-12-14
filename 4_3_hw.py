from python_training.task_11_checks import Checks


class Input(Checks):

    def __init__(self, text, loc):
        self.text = text
        super().__init__(loc)

search = Input('text','input#search')
print(search.text + ": " + search.check_text())

class Button(Checks):

    def __init__(self, text, loc):
        self.text = text
        super().__init__(loc)

article = Button('title', 'button#article')
print(article.text + ": " + article.check_text())

class Title(Checks):

    def __init__(self, text, loc):
        self.text = text
        super().__init__(loc)

head = Title('firstTitle', 'title#head')
print(head.text + ": " + head.check_text())

class Link(Checks):

    def __init__(self, text, loc):
        self.text = text
        super().__init__(loc)

url = Link('address', 'link#url')
print(url.text + ": " + url.check_text())