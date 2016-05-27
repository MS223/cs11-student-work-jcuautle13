class Song(object):

    def __init__(self,title,artist,lyrics):
        self.lyrics = lyrics
        self.title = title
        self.artist = artist

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
    
Imagine = Song("Imagine","John Lennon",["imagine there's no heaven",
                   "you may say i'm a dreamer",
                   "but i'm not the only one"])


Strawberry_Fields_Forever = Song("Strawberry Fields Forever","The Beatles",["Living is easy with eyes closed",
                      "Misunderstanding all you see",
                      "cause I'm going to Strawberry Fields",])
                      
print sing
