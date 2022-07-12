import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_1 = Artist("Deep Purple")
artist_repository.save(artist_1)


artist_2 = Artist("Foo Fighters")
artist_repository.save(artist_2)


album_1 = Album("Live in Japan", "Rock", artist_1)
album_repository.save(album_1)

album_2 = Album("One by One", "Rock", artist_2)
album_repository.save(album_2)

pdb.set_trace()