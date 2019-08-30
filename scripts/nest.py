import conf, sys, json
from pathlib import Path

class Nest():
    def __init__(self):
        self.resources = []

    def read(self, path):
        with open(path, 'r') as f:
            return json.load(f)
    
    def append_album(self, album=None, photos=None):
        if photos:
            album = {
                'name': album['name'],
                'type': 'photos',
                'parents': album['parents'],
                'list': photos
            }
        
        self.resources.append(album)
    
    def nest_photos(self, album, list_path):
        photos = self.read(list_path)
        # self.append(album=album)
        self.append_album(album=album, photos=photos)
        
    def nest_album(self, album):
        album = album or self.read(album_path)
        if album['type'] == 'album':
            if album.get('no_sub_album'):
                list_path = album['conf_path']
                self.nest_photos(album, list_path)
            else:
                album_list = album.pop('list', None)
                alone_photos = list(filter(lambda i: i['type'] == 'photo', album_list))
                if alone_photos:
                    self.append_album(album=album, photos=alone_photos)
                for item in album_list:
                    sub_album = self.nest_album(item)
    
    def main(self):
        horcrux = self.read(conf.HORCRUX_PATH)
        self.nest_album(horcrux)
        conf.write_json(conf.CONFIG_PATH, self.resources)

if __name__ == '__main__':
    nest_album = Nest()
    sys.exit(nest_album.main())