# Horcrux
Generate your own online photograph gallery easily.

![demo](https://raw.githubusercontent.com/soyaine/horcrux/readme/assets/imxie-demo.png)

## Features
- Simple web page style
- Auto add watermark to your photos
- Auto generate thumbnails for better load speed
- Sort photos as you like
- Keep the order when you add new photos

## Demo
Here is a live demo: [https://soyaine.github.io/horcrux/](https://soyaine.github.io/horcrux/)

## Quick Start

1. Fork this repo, or clone to your local.
    ``` bash
    $ git clone git@github.com:soyaine/horcrux.git
    ```
2. Make sure you have installed Python3.
    - Check current python version
      ``` bash
      $ python -V
      ```
      or 
      ``` bash
      $ python3 -V
      ```
    - If version < 3 or error, install Python3,
      ```
      $ brew install python3
      ```
3. Change the config in file `_config.yml`, especially the name, which will shown as the site header, and the watermark text in your photos.
    ``` yml
    name: Soyaine
    instagram: your_ins_account
    ```
3. Replace the folders in the `./photos/` directory with your own photos, each folder means an album. The folder name will shown as the headline of each album.

4. Double click the `setup.command`, which will generate config json in `_data/` folder.
5. Run and greet your gallery in `localhost:4001`
    ```
    $ jekyll serve --watch
    ```

## Make It Yours

### Default settings


### Config


## Acknowledgments
- Inspired by andyzhang's [gallery](https://github.com/andyzg/gallery)
- Special thanks to my friend [Hugo](https://github.com/xcc3641), the photographs in the mockup above were taken by him. He is the reason why I write Horcurx (also named by him), and also, the first user of it.

## Author
© [Soyaine](https://github.com/soyaine)

## Support
If you have any question about this repo, feel free to start an [issue](https://github.com/soyaine/horcrux/issues/new). 

You can also reach out to me by email [soyaine1@gmail.com](mailto:soyaine1@gmail.com)

## License
MIT
