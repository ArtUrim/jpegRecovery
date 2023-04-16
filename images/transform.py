from exif import Image

def jopen(fname: str):
    my_image = None
    with open(fname, 'rb') as image_file:
        my_image = Image(image_file)

    return my_image

def jclose( fname:str, jpeg ):
    with open( fname, "wb" ) as image_file:
        image_file.write( jpeg.get_file())

if __name__ == "__main__":

    j = jopen('koliber.jpg')
    if j.get('model'):
        del j['model']
    jclose('koliber.jpg',j)

    j = jopen('leci.jpg')
    j['model'] = 'SiaSjung'
    jclose('leci.jpg',j)

    j = jopen('maluch.jpg')
    j['model'] = 'PENTAX K7'
    jclose('maluch.jpg',j)

    j = jopen('sowy.jpg')
    j['model'] = 'PENTAX K-5 II s'
    jclose('sowy.jpg',j)

    j = jopen('strzygiel.jpg')
    j['model'] = 'PENTAX K-5 II s'
    j['datetime_digitized'] = '2023:04:03 11:23:34'
    jclose('strzygiel.jpg',j)

    j = jopen('szkic.jpg')
    j['model'] = 'PENTAX K-5 II s'
    j['datetime_digitized'] = '2023:04:04 11:23:34'
    jclose('szkic.jpg',j)

    j = jopen('wrobel.jpg')
    j['model'] = 'PENTAX K-5 II s'
    j['datetime_digitized'] = '2023:04:04 15:22:17'
    jclose('wrobel.jpg',j)

    j = jopen('zimorodek.jpg')
    j['model'] = 'PENTAX K-5 II s'
    j['datetime_digitized'] = '2023:04:04 15:22:17'
    jclose('zimorodek.jpg',j)
