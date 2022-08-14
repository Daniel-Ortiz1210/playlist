from random import randint
from time import sleep



class Song:
    def __init__(self, title, next=None, prev=None):
        self.title = title
        self.next = next
        self.prev = prev
        self.lenght = randint(5, 6)
    

# Add to next
# Add to lail
# Erase by position
# Erase all
# See historial


class Playlist:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.current_items = []
        self.historial = []
    
    def add_to_last(self, song):
        
        if self.head is None:
            self.head = song
            self.tail = self.head
        else:
            self.tail.next = song
            song.prev = self.tail
            self.tail = song
        
        self.current_items.append(song)


    def add_next(self, song):

        if self.head is None:
            self.head = song
            self.tail = self.head
        else:
            song.next = self.head
            self.head.prev = song
            self.head = song
        
        self.current_items.insert(0, song)


    def see_my_playlist(self):

        if len(self.current_items) == 0:
            print("No hay canciones en tu playlist")
            exit()

        for i in range(len(self.current_items) - 1 , - 1, - 1):
            print(self.current_items[i].title)
    
    def play_songs(self):        

        while len(self.current_items) > 0 and self.head is not None:

            print(f'Reproduciendo {self.head.title}')
            
            self.historial.append(self.head)
            
            sleep(self.head.lenght)
            
            if self.head.next == None:
                self.historial.append(self.head)
                self.current_items.pop(0)
                break

            self.head = self.head.next

            self.head.prev = None
            
            self.current_items.pop(0)


song1 = Song("Payphone")
song2 = Song("Hello")
song3 = Song("Sorry")
song4 = Song("Fast Car")
song5 = Song("Finesse")


playlist = Playlist()


playlist.add_to_last(song1)
playlist.add_to_last(song2)
playlist.add_to_last(song3)

playlist.add_next(song4)


playlist.play_songs()

playlist.see_my_playlist()