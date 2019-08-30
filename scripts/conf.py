from pathlib import Path
import json, yaml


REPO_DIR = Path.cwd()
DIR_PATH = Path(__file__).parent.parent
PHOTOS_PATH = DIR_PATH.joinpath('photos/')
ALBUMS_PATH = DIR_PATH.joinpath('_data/albums')
HORCRUX_PATH = DIR_PATH.joinpath('_data/Horcrux.json')
CONFIG_PATH = DIR_PATH.joinpath('_data/config.json')
CONF_YAML_PATH = DIR_PATH.joinpath('_config.yml')

DEBUG = False

MIN_WIDTH = 600
copyright = '@Soyaine'
fontsize = 40
fontfamily = 'Eczar-Medium.ttf'
watermark_rotate = 0
SIGN_THUMBNAIL = False
SIGN_ORIGINAL = True

SORT_ALBUMS_BY_TIME = True
REVERSE_ALBUMS_ORDER = True
ORDER_ALBUMS_BY_LAST_DO = 'access'  # modify, create

SORT_PHOTOS_BY_TIME = False
REVERSE_PHOTOS_ORDER = True
ORDER_PHOTOS_BY_LAST_DO = 'access'

Path.mkdir(ALBUMS_PATH, exist_ok=True)

def write_json(path, data):
    with open(path, 'w') as f:
        f.write(json.dumps(data, indent=2, separators=(',', ': ')))

with open(CONF_YAML_PATH, 'r') as config:
    site_conf = yaml.load(config)
    copyright = '@' + site_conf['name']
    
    process = site_conf['process']
    if process:
        album_conf = process['album']
        photo_conf = process['photo']
        watermark_conf = photo_conf['watermark']

        MIN_WIDTH = photo_conf.get('min_width', MIN_WIDTH)
        fontsize = watermark_conf.get('fontsize', fontsize)
        fontfamily = watermark_conf.get('fontfamily', fontfamily)
        watermark_rotate = watermark_conf.get('rotate', watermark_rotate)

        SIGN_THUMBNAIL = watermark_conf.get('thumbnail', SIGN_THUMBNAIL)
        SIGN_ORIGINAL = watermark_conf.get('original', SIGN_ORIGINAL)

        SORT_ALBUMS_BY_TIME = album_conf.get('sort_by_time', SORT_ALBUMS_BY_TIME)
        REVERSE_ALBUMS_ORDER = album_conf.get('reverse', REVERSE_ALBUMS_ORDER)
        ORDER_ALBUMS_BY_LAST_DO = album_conf.get('order_by', ORDER_ALBUMS_BY_LAST_DO)

        SORT_PHOTOS_BY_TIME = photo_conf.get('sort_by_time', SORT_PHOTOS_BY_TIME)
        REVERSE_PHOTOS_ORDER = photo_conf.get('reverse', REVERSE_PHOTOS_ORDER)
        ORDER_PHOTOS_BY_LAST_DO = photo_conf.get('order_by', ORDER_PHOTOS_BY_LAST_DO)