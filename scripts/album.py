from photo import Photo
import json, conf

class Album():
    def __init__(self, path, name, root):
        self.path = path
        self.name = name
        self.items_order = []
        self.items_dict = {}
        self.root = root or 0
    
    def sort_dirs(self, dirs, type):
        def _getmtime(entry):
            order_map = {
              'access': 'st_atime',
              'modify': 'st_mtime',
              'create': 'st_ctime'
            }
            order_by = conf.ORDER_ALBUMS_BY_LAST_DO if type == 'album' else conf.ORDER_PHOTOS_BY_LAST_DO
            return getattr(entry.stat(), order_map[order_by])
        
        if type == 'album':
            sort_by = _getmtime if conf.SORT_ALBUMS_BY_TIME else lambda x:x.name
            return sorted(dirs, key=sort_by, reverse=conf.REVERSE_ALBUMS_ORDER)
        if type == 'photo':
            sort_by = _getmtime if conf.SORT_PHOTOS_BY_TIME else lambda x:x.name
            return sorted(dirs, key=sort_by, reverse=conf.REVERSE_PHOTOS_ORDER)
    
    def format(self):
        # dirs = os.listdir(self.path)
        dirs = self.path.iterdir()
        has_child_album = False
        parts = self.path.parts
        album_levels = parts[-self.root:len(parts)] if self.root > 0 else []
        photo_list = []
        album_list = []
        result = {
          'name': self.name,
          'type': 'album',
          'root': self.root,
          'parents': album_levels
        }

        print(f'Processing the album {self.name}')
        
        for i, path in enumerate(dirs):
            if path.is_dir():
                album_list.append(path)
            elif str(path.suffix).endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                photo_list.append(path)
                
        photo_list = self.sort_dirs(photo_list, 'photo')
        album_list = self.sort_dirs(album_list, 'album')

        for path in photo_list:
            photo = Photo(path)
            photo_conf = photo.format()
            if photo_conf:
                self.items_order.append(path.name)
                self.items_dict[path.name] = photo_conf
        
        for path in album_list:
            sub_album = Album(path, path.name, self.root + 1)
            self.items_order.append(path.name)
            self.items_dict[path.name] = sub_album.format()
            has_child_album = True
        
        child_items = {
            'order': self.items_order,
            'dict': self.items_dict
        }

        if has_child_album:
            return {
              **result,
              'items': child_items
            }
        else:
            # write list to album config file
            album_path = conf.ALBUMS_PATH.joinpath('-'.join(album_levels) + '.json')
            print('Write the album config to', album_path)
            conf.write_json(album_path, child_items)

            return {
              **result,
              'path': './' + str(album_path.relative_to(conf.DIR_PATH)),
              'no_sub_album': True
            }
