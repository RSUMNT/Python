liked_songs = { 
    'Bad Habits': 'Ed Sheeran',
    'Im Just ken' : 'Ryan Gosling',
    'Mastermind' : 'Taylor Swift',
    'Uptown Funk' : 'Mark Ronson ft. Bruno Mars',
    'Ghost' : 'Justin Bieber'
}



def write_liked_songs_to_file(liked_songs, file_name):
    file_name = open('diaries2.txt', 'w')
    for title, artist in liked_songs.items():
        file_name.write(f" Liked Songs: \n ({title} - {artist}\n)")



