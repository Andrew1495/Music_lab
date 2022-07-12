import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Deep Purple")
artist_repository.save(artist_1)


artist_2 = Artist("Foo Fighters")
artist_repository.save(artist_2)


album_1 = Album("Live in Japan", "Rock", artist_1)
album_repository.save(album_1)

album_2 = Album("One by One", "Rock", artist_2)
album_repository.save(album_2)

# result = artist_repository.select_by_id(1)

result = album_repository.select_by_id(1)
print(result.__dict__)

all_artist = artist_repository.select_all()

all_albums = album_repository.select_all()

for artist in all_artist:
    print(artist.__dict__)

for album in all_albums:
    print(album.__dict__)




pdb.set_trace()