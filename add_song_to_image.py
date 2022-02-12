import eyed3

audiofile = eyed3.load('example.mp3')
if (audiofile.tag == None):
    audiofile.initTag()

audiofile.tag.images.set(3, open('cover.jpg','rb').read(), 'image/jpeg')

audiofile.tag.save()