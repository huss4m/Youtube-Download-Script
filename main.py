from moviepy.audio.io.AudioFileClip import AudioFileClip
from pytube import YouTube
import moviepy.editor as mp
import os
import sys

def download_audio(url, output_path):
    try:

        yt = YouTube(url)
        sys.stdout = open(os.devnull, 'w')

        audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()


        temp_file = audio_stream.download(output_path=output_path)


        output_file = os.path.join(output_path, f"{yt.title}.mp3")


        clip = mp.AudioFileClip(temp_file)
        clip.write_audiofile(output_file, verbose=False)
        sys.stdout = sys.__stdout__


        os.remove(temp_file)

        print("Téléchargement de l'audio au format MP3 terminé avec succès!")
    except Exception as e:
        print(f"Une erreur s'est produite lors du téléchargement de l'audio : {str(e)}")


def download_video(url, output_path):
    try:

        yt = YouTube(url)
        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video_stream.download(output_path=output_path)
        print("Téléchargement de la vidéo terminé avec succès!")

    except Exception as e:
        print(f"Une erreur s'est produite lors du téléchargement de la vidéo : {str(e)}")


def main():

    youtube_url = input("Veuillez entrer l'URL de la vidéo YouTube : ")

    download_option = input("Voulez-vous télécharger une vidéo (v) ou un fichier audio (a) ? ")

    output_path = input("Veuillez entrer le chemin de sortie pour sauvegarder le fichier : ")

    if download_option.lower() == 'v':
        download_video(youtube_url, output_path)
    elif download_option.lower() == 'a':
        download_audio(youtube_url, output_path)
    else:
        print("Option invalide. Veuillez choisir 'v' pour la vidéo ou 'a' pour l'audio.")


if __name__ == "__main__":
    main()
