from math import ceil
from typing import List


class PhotoAlbum:

    MAX_PHOTOS = 4
    DASHES_COUNT = 11

    def __init__(self, pages: int) -> None:
        self.pages = pages
        self.photos: List[List[str]] = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count/cls.MAX_PHOTOS))

    def add_photo(self, label: str):
        for page in range(self.pages):
            if len(self.photos[page]) < 4:
                #slot = len(self.photos[page]) + 1
                self.photos[page].append(label)
                return f"{label} photo added successfully on page " \
                       f"{page + 1} slot {len(self.photos[page])}"
        else:
            return f"No more free slots"

    def display(self):
        message = [
            self.DASHES_COUNT*'-',
        ]
        for page in self.photos:
            message.append(("[] "*len(page)).strip())
            message.append(self.DASHES_COUNT*'-')

        return "\n".join(message)


