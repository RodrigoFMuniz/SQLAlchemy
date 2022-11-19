class Shirt:
    def __init__(self, article="size", color="", shirt_size="na", last_worn=0):
        self._article = article
        self._color = color
        self._shirt_size = shirt_size
        self._last_worn = last_worn
    
    def get_shirt(self):
        return self
    
    def __repr__(self):
        return f"'{self._article}','{self._color}','{self._shirt_size}',{self._last_worn}"


# s1 = Shirt(article="long", color="Blue", shirt_size="XG", last_worn=6)
# s1 = Shirt()
# print(s1.get_shirt()._article)