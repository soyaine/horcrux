# Horcrux
Generate your own online photograph gallery easily.

![demo](https://raw.githubusercontent.com/soyaine/horcrux/gh-pages/assets/imxie-demo.png)

## Features
- Simple but beautiful UI.
- Auto-watermark your photos.
- Auto-generate thumbnails for better load speed.
- Sort photos by time, modify as you like, and keep it when you add new photos.
- Keep the order when you put new photos in.
- Support multi-level albums.
- Based on Jekyll and GitHub Pages.

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
name: Horcrux
instagram: your_ins_account_id
```

Remove all resources under `./photos/`, then create folder in it, the folder name will shown as headline of a group of photos. Copy some photos into it. 
```bash
photos
├── 2019
│    ├── Duo
│    │   ├── 07.jpg
│    │   ├── 08.jpg
│    │   ├── 09.jpg
│    └── Hey
│        ├── 02.jpg
│        └── 1.jpg
└── Mey
    ├── 02.jpg
    └── 1.jpg
```

> **⚠️NOTE** 
> 
> Please always keep your own original photo files in other place, because the watermark will change the original one. 
> 
> When you first try this, just put several photos in, to see wheather you like the watermark effect or not.

Double click the `setup.command`, the process is doing:
- Generate thumbnails with the suffix of `.min.jpg`
- Watermark original photos with `name` value set in `_config.yml`
- Traverse all folders and files, generate a file `_data/config.json`

Run and greet your gallery in locally by [Jekyll](https://help.github.com/en/articles/setting-up-your-github-pages-site-locally-with-jekyll).
```
$ jekyll serve --watch
```

Git push to the remote branch `gh-pages`, then it will be online. 🎉
```
$ git add .
$ git commit -m "init gallery"
$ git push -u origin gh-pages
```

## Make It Yours
If you have run successfully locally, here are more details you can reform it. The following is the default settings of Horcrux, almost all config are set in `_config.yml`:

### Headline and Instagram Link

```yml
name: Horcrux # Headline of the page, watermark text

instagram: ins_id
```

- The value of `name` is both the website headline and the watermark text.
- There is a text link to your Instagram page at the bottom of the page, just set it blank if you don't want.

### Albums and photos process

```yml
# How to process the photos and albums to config
process:
  keep_order: True
  nested_album:
    separator: ' · '
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
```

**`sort_by_time`, `order_by`, `reverse`:**

- Sort the albums (folder under `photos`) by create time, from new to old.
- Sort the photos by name.

**`keep_order`:**
- When you change the `order` value in JSON under `_data`, and add new photos or new albums, then double click `setup.command`, a new `config.json` file will be generated, all old order set manually will be retained.
- If you just modify `order` without new photo added, you can just double click `config.command`, which will read all JSON files (Horcrux.json and others under albums folder), and regenerate the `config.json` file.

**`separator`:**
- If you created nested folders under the `photos` folder, Horcrux can handle it too.
- The album which path in `./photos/2019/duo/`, its displayed title in page will be: **DUO** · 2019, spliced by `separator` ` · `.


**`watermark`:**
- Watermark the original photos.
- The text of the watermark is the value of `name`.
- The position is in the middle of the bottom of the photo.

### Gallery Style

```yml
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
```

**`column`:**
- In wide screen, photos divided into 3 columns.
- In small screen, photos divided into 2 columns.

**`frame_padding`, `column_gap`, `row_gap`:**
- Each photo has a white square frame background. The white gap between photo and frame outer border is 10px.
- In wide screen, the spacing between columns is 30px, the same for rows.
- In small screen, the spacing between columns is 10px, the same for rows.

### Color Palette

Most of the color palette is defined in `./sass/base.scss`, you can change them to your color.

```scss
$background: #fafafa;
$surface: #fff;

$title: #5f5f5f;
$subtitle: #868686;
$text: #C8C8C8;
$link: #98A3AA;
```

- `$background`: whole page's background color
- `$surface`: the color of photo square frame

## Acknowledgments
The idea of generating album JSON for using Jekyll and GitHub Pages is inspired by AndyZhang's [gallery](https://github.com/andyzg/gallery).

Special thanks to my friend [Hugo <img src="https://avatars2.githubusercontent.com/u/11666634?s=460&v=4" width="20" height="20">](https://github.com/xcc3641), the photographs both in the mockup above and in the live demo were taken by him. In the beginning, I just wanted to write a tool for him to share photography. Later I found it can be open-sourced. So there is Horcrux, he named it.

## Author
© [Soyaine](https://github.com/soyaine)

## Support
If you have any question about Horcrux, feel free to start an [issue](https://github.com/soyaine/horcrux/issues/new). 

You can also reach out to me by email [soyaine1@gmail.com](mailto:soyaine1@gmail.com)

## License
MIT
