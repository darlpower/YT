from pytube import YouTube


#yt = YouTube('https://youtube.com/watch?v=XJGiS83eQLk')
yt = YouTube('https://www.youtube.com/watch?v=XUkMY8Sp_AM')
for cap in yt.captions.all():
    print(cap)
caption = yt.captions.get_by_language_code('a.en')
print(caption.generate_srt_captions())

