import conf, sys, json
from pathlib import Path

class Nest():
    def __init__(self):
        self.resources = []

    def read(self, path):
        print('read', conf.DIR_PATH.joinpath(path))
        abs_path = conf.DIR_PATH.joinpath(path)
        with open(abs_path, 'r') as f:
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
    
    def convert_child_items(self, items):
        items_dict = items['dict']
        items_order = items['order']
        child_list = [items_dict.get(k) for k in items_order if k in items_dict]
        return child_list
    
    def nest_photos(self, album, list_path):
        items = self.read(list_path)
        photos = self.convert_child_items(items)
        # self.append(album=album)
        self.append_album(album=album, photos=photos)
        
    def nest_album(self, album):
        if album['type'] == 'album':
            if album.get('no_sub_album'):
                list_path = album['path']
                self.nest_photos(album, list_path)
            else:
                album_list = self.convert_child_items(album['items'])
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