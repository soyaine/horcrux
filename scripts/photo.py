import conf
import os
from PIL import Image, ImageDraw, ImageFont


class Photo():
    def __init__(self, path):
        self.path = path
        self.min_path = ''
        self.pil_image = Image.open(self.path).convert('RGBA')
        self.witdh, self.height = self.pil_image.size
        self.size = self.pil_image.size

        min_file = self.path.stem + '.min' + self.path.suffix
        self.min_path = self.path.with_name(min_file)
    
    @property
    def is_min(self):
        return self.path.match('*.min.jpg')
    
    @property
    def has_min(self):
        return self.min_path.exists()
    
    def format(self):
        if self.is_min:
            return None
        
        if not self.has_min:
            if conf.SIGN_ORIGINAL:
                signed_image = self.mark_image(self.pil_image, conf.fontsize)
                self.save_image(signed_image, self.path)
            
            # resize
            ratio = float(conf.MIN_WIDTH) / self.size[0]
            new_image_size = tuple([int(x*ratio) for x in self.size])

            if conf.SIGN_THUMBNAIL:
                if not conf.SIGN_ORIGINAL:
                    signed_image = self.mark_image(self.pil_image, conf.fontsize)
                signed_image.thumbnail(new_image_size, Image.ANTIALIAS)
                self.save_image(signed_image, self.min_path)
            else:
                min_image = self.pil_image.copy()
                min_image.thumbnail(new_image_size, Image.ANTIALIAS)
                self.save_image(min_image, self.min_path)

        relative_path = str(self.path.relative_to(conf.DIR_PATH))

        # return basic info
        return {
          "type": 'photo',
          'width': self.size[0],
          'height': self.size[1],
          'path': './' + relative_path,
          'min_path': './' + str(self.min_path.relative_to(conf.DIR_PATH))
        }
    
    def save_image(self, img, path):
        if conf.DEBUG:
            img.show()
        else:
            # rgb_img = img.convert('RGB')
            img.save(path, 'PNG')
    
    def mark_image(self, img, fontsize):
        width, height = img.size
        transparent_image = Image.new('RGBA', img.size, (255, 255, 255, 0))
        font = ImageFont.truetype('./assets/font/' + conf.fontfamily, conf.fontsize)
        draw = ImageDraw.Draw(transparent_image)

        t_size = font.getsize(conf.copyright)
        t_w = t_size[0]
        t_h = t_size[1]

        x = (width - t_w) / 2
        y = height - 2 * t_h
        draw.text((x, y), conf.copyright, font=font, fill=(255, 255, 255, 125))
        transparent_image = transparent_image.rotate(conf.watermark_rotate)
        signed_image = Image.alpha_composite(img, transparent_image)
        return signed_image
