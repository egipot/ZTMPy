# ZTM Section #17 Scripting with Python

from PIL import Image

img = Image.open('./Pokedex_me/pikachu.jpg')
print(img)
#<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=640x640 at 0x257DED33400>

print(img.format)
#JPEG

print(img.size)
#(640, 640)

print(img.mode)
#RGB

print(dir(img))
#prints all the information/details in this img file
#['_Image__transformer', '__array_interface__', '__class__', '__copy__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_category', '_close_exclusive_fp_after_loading', '_copy', '_crop', '_dump', '_ensure_mutable', '_exclusive_fp', '_exif', '_exif_offset', '_expand', '_get_safe_box', '_getexif', '_getmp', '_getxmp', '_min_frame', '_new', '_open', '_reload_exif', '_repr_png_', '_repr_pretty_', '_seek_check', '_size', 'alpha_composite', 'app', 'applist', 'apply_transparency', 'bits', 'close', 'convert', 'copy', 'crop', 'custom_mimetype', 'decoderconfig', 'decodermaxblock', 'draft', 'effect_spread', 'entropy', 'filename', 'filter', 'format', 'format_description', 'fp', 'frombytes', 'get_child_images', 'get_format_mimetype', 'getbands', 'getbbox', 'getchannel', 'getcolors', 'getdata', 'getexif', 'getextrema', 'getim', 'getpalette', 'getpixel', 'getprojection', 'getxmp', 'height', 'histogram', 'huffman_ac', 'huffman_dc', 'icclist', 'im', 'info', 'layer', 'layers', 'load', 'load_djpeg', 'load_end', 'load_prepare', 'load_read', 'mode', 'palette', 'paste', 'point', 'putalpha', 'putdata', 'putpalette', 'putpixel', 'pyaccess', 'quantization', 'quantize', 'readonly', 'reduce', 'remap_palette', 'resize', 'rotate', 'save', 'seek', 'show', 'size', 'split', 'tell', 'thumbnail', 'tile', 'tobitmap', 'tobytes', 'toqimage', 'toqpixmap', 'transform', 'transpose', 'verify', 'width']

