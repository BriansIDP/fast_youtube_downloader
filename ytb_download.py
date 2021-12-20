import sys, os
import pytube

def downloadVideo(url, output, subtitle='a.en'):
    youtube = pytube.YouTube(url)
    if len(youtube.caption_tracks) == 0 or subtitle not in youtube.captions:
        raise Exception("No subtitle found")
    else:
        caption = youtube.captions[subtitle]
        video = youtube.streams.get_highest_resolution()
        video.download(output)
        with open(os.path.join(output, 'subtitle_{}'.format(subtitle)), 'w') as fout:
            fout.write(caption.xml_captions)

def downloadPlaylist(url, output, subtitle='a.en'):
    p = pytube.Playlist(url)
    print(f'Downloading: {p.title}')
    for url in p.video_urls:
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video_output = os.path.join(output, '_'.join(video.title.split()))
        video.download(video_output)
        if len(youtube.caption_tracks) == 0 or subtitle not in youtube.captions:
            print('No subtitile found for video: {}'.format(youtube.title))
            print('Possible options:')
            print(youtube.caption_tracks)
        else:
            caption = youtube.captions[subtitle]
            with open(os.path.join(video_output, 'subtitle_{}'.format(subtitle)), 'w') as fout:
                fout.write(caption.xml_captions)

if __name__ == "__main__":
    inurl = sys.argv[1]
    outpath = sys.argv[2]
    # downloadVideo(inurl, outpath, subtitle='a.en')
    downloadPlaylist(inurl, outpath, subtitle='a.en')
