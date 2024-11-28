class Book:
    def __init__(self, title, page_count):
        self.title = title  # Calls the setter for title
        self.page_count = page_count  # Calls the setter for page_count

    @property
    def title(self):
        """The title property"""
        return self._title  # Return the stored title value

    @title.setter
    def title(self, value):
        """Setter for the title"""
        self._title = value  # Set the title

    @property
    def page_count(self):
        """The page_count property"""
        return self._page_count  # Return the stored page count

    @page_count.setter
    def page_count(self, value):
        """Setter for the page_count. Ensures the page_count is an integer."""
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value  # Set the page count only if it's an integer

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
