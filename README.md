# Horcrux
Generate your own online photograph gallery easily.

![demo](https://raw.githubusercontent.com/soyaine/horcrux/readme/assets/imxie-demo.png)

## Features
- Simple but beautiful UI
- Auto watermark your photos
- Auto generate thumbnails for better load speed
- Sort photos by time, ma as you like, and keep it when you add new photos
- Keep the order when you add new photos

## Demo
Here is a live demo: [https://soyaine.github.io/horcrux/](https://soyaine.github.io/horcrux/)

## Quick Start
Fork this repo, or clone to your local.
``` bash
$ git clone git@github.com:soyaine/horcrux.git
```
Make sure you have installed Python3, check current python version.
``` bash
$ python3 -V
```
- If your command `python` rather than `python3` point to Python3, please change the code in two command file, modify `python3 -m venv venv` to `python -m venv venv`.
  ```bash
  # setup.command / config.command
  python -m venv venv 
  ```
- If version < 3 or error, install Python3, and then recheck.
  ```
  $ brew install python3
  $ python3 -V
  ```
- If the check passes, next step.

Change the config in file `_config.yml`, **especially the name**, which will shown as the site header and the watermark text in your photos.

``` yml
name: Soyaine
instagram: your_ins_account
```

Remove all resources under `./photos/`, than create folder in it, the folder name will shown as headline of a group of photos. Copy some photos into it. 
```bash
photos
├── Duo
│   ├── 07.jpg
│   ├── 08.jpg
│   ├── 09.jpg
└── Mey
    ├── 02.jpg
    └── 1.jpg
```
> **⚠️Note** 
> Please always keep your own original photo files in other place, because the watermark will change the original one. 
> 
> When you first try this, just put several photos in, to see wheather you like the watermark effect or not.

Double click the `setup.command`, the process is doing:
- Generate thumbnails with suffix of `.min.jpg`
- Watermark original photos with `name` value set in `_config.yml`
- Traverse all folders and files, generate a file `_data/config.json`

Run and greet your gallery in `http://localhost:4001`
```
$ jekyll serve --watch
```

Git push to remote `gh-pages` branch of your repo, then it will be online. 🎉
```
$ git add .
$ git commit -m "init gallery"
$ git push -u origin gh-pages
```

## Make It Yours
If you have run successfully locally, there are more details you can reform it.

### Default Settings
Here are the default mode of Horcrux, almost all are set in `_config.yml`:
- Sort the albums (folder under `photos`) by create time, from new to old.
- Sort the photos by name.
- When you change the `order` value in json under `_data`, and add new photo or new album, than double click `setup.command`, new `config.json` file will be generated, all old order set manually will be retained.
- If you just modify `order` without new photo added, you just can double click `config.command`, which will read all the json files, and regenerate the `config.json` file.
- Watermark original photo, with fontsize 40 and text is the value of `name`, in the middle of the bottom of the photo.
- In widescreen, photos divided into 3 columns.
- In smallscreen, photos divided into 2 columns.

### Config

```yml
name: Soyaine # Headline of the page, watermark text

frame_padding: 10px # the white gap between photo and outer border

# Widescreen
column: 3 
column_gap: 30px
row_gap: 30px

# Smallscreen
small_screen:
  column: 2
  column_gap: 10px
  row_gap: 10px

# How to process the photos and albums to config
process:
  keep_order: True
  album:
    sort_by_time: True # False: sort by filename
    order_by: create # other two value can be: access, modify
    reverse: True
  photo:
    sort_by_time: False
    order_by: modify
    reverse: True
    min_width: 600
    watermark:
      thumbnail: False
      original: True
      fontsize: 40
      fontfamily: Eczar-Medium.ttf
      rotate: 0

instagram:   # if you don't want show the instagram link below page, just set it blank
```


## Acknowledgments
- Inspired by andyzhang's [gallery](https://github.com/andyzg/gallery)
- Special thanks to my friend [Hugo](https://github.com/xcc3641), the photographs both in the mockup above and in the live demo were taken by him. He is the reason why I write Horcurx (also named by him), and also, the first user of it.

## Author
© [Soyaine](https://github.com/soyaine)

## Support
If you have any question about Horcrux, feel free to start an [issue](https://github.com/soyaine/horcrux/issues/new). 

You can also reach out to me by email [soyaine1@gmail.com](mailto:soyaine1@gmail.com)

## License
MIT
