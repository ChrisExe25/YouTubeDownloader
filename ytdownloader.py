from pytube import YouTube


link = input("Inserisci l'URL del video che vuoi scaricare: ")

yt = YouTube(link)
videos = yt.streams.all()

video =list(enumerate(videos))

for i in video:
    print(i)

print("Inserisci il formato desiderato per l'installazione")
dn_option = int(input("inserisci l'opzione: "))
dn_video = videos[dn_option]
dn_video.download()

input("Video Scaricato, premi invio per chiudere.")
