import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from scipy.spatial import distance

data = pd.read_csv("SpotifyFeatures.csv")
data = data.drop(["track_id","key","mode","time_signature"],1)

# Song finder with song name and artist name

def find_song(word,artist):
    a = 0
    b = 0
    for i in data["track_name"]:
        if word.lower() in i.lower() and artist.lower() in data["artist_name"][a].lower():
            print("Song Name: ",data["track_name"][a],", Artists: ",data["artist_name"][a])
            b+=1
        a+=1
    if b == 0:
        print("Nothing found. Please try something else :)")

# Preprocessing

df = data.copy()

df = df.drop(["artist_name","track_name"],1)

col = ['popularity', 'acousticness', 'danceability', 'duration_ms',
       'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness',
       'tempo', 'valence']
scaler = StandardScaler()
df[col] = scaler.fit_transform(df[col])


encoder = OneHotEncoder(sparse=False, handle_unknown="ignore")
enc = pd.DataFrame(encoder.fit_transform(np.array(df["genre"]).reshape(-1,1)))
enc.columns = df["genre"].unique()

enc.head()

df[enc.columns] = enc
df = df.drop("genre",1)
df.head()


df["name"] = data["track_name"]
df["artist"] = data["artist_name"]

df_2 = df.drop(["artist","name"],1)



def sim_track_find(word,artist):
    a = 0
    b = 0
    song = []
    indexes = []
    for i in data["track_name"]:
        if word.lower() in i.lower() and artist.lower() in data["artist_name"][a].lower():
            song.append(df_2[a:a+1].values)
            indexes.append(a)
            b+=1
        a+=1
    if b == 0:
        print("Nothing found. Please try something else :)")
        return 0
        
    return song[0][0], indexes[0]

def similar_tracks(data,number,song = "",artist = ""):

    if (sim_track_find(song,artist) == 0):
        return 0
    else:
        x=sim_track_find(song,artist)[0]
        index = sim_track_find(song,artist)[1]
    p = []
    count=0
    for i in df_2.values:
        p.append([distance.cosine(x,i),count])
        count+=1
    p.sort()
    song_names = df["name"]
    artist_names = df["artist"]

    print("\nSimilar songs to ",song_names[index]," by ", artist_names[index],"\n")
    for i in range(1,number+1):
        print(i,"- ",song_names[p[i][1]],", ",artist_names[p[i][1]])



song = input("Enter the song name (if you don't want to specify a song name please skip this): ")
artist = input("Enter the artist name (if you don't want to specify an artist name please skip this): ")
num = input("Number of song recommendations: ")

similar_tracks(df,int(num),song,artist)