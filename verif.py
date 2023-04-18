import requests
from albums.request_album_tracks import get_album_tracks
from sample_data_folder.album_sample_data import api_sources_lib
from albums.request_several_albums import get_several_albums


# def verif():
#     response = get_album_tracks('5eA0qtE7Yu29XiMlwoby2G')
#     print(len(response.json()))

print(api_sources_lib.get_albums_list())
print(len(get_several_albums()))
