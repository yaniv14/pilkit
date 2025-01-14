# flake8: noqa

# Required PIL classes may or may not be available from the root namespace
# depending on the installation method used.
try:
    from PIL import Image, ImageColor, ImageChops, ImageEnhance, ImageFile, \
        ImageFilter, ImageDraw, ImageStat, ImageMode
except ImportError:
    try:
        import Image
        import ImageColor
        import ImageChops
        import ImageEnhance
        import ImageFile
        import ImageFilter
        import ImageDraw
        import ImageStat
        import ImageMode
    except ImportError:
        raise ImportError(
            'PILKit was unable to import the Python Imaging Library. Please confirm it`s installed and available on your current Python path.')

try:
    from io import BytesIO as StringIO
except ImportError as exc:
    try:
        from cStringIO import StringIO
    except ImportError:
        try:
            from StringIO import StringIO
        except ImportError:
            raise exc

try:
    string_types = [basestring, str]
except NameError:
    string_types = [str]
