# Music Recommendation System with Python

This project uses the  https://www.kaggle.com/zaheenhamidani/ultimate-spotify-tracks-db/code dataset, you can find it on the link. In the project, i created some functions to build the project. Main purpose of the project is developing a music recommender system with python. It has 2 options. In the first option you can search the database and see some songs you want to search. In the second option you write a song name and an artist name of the song, the model will search the database and find the closest song in the dataset. According to that song it will measure the cosine distance with every other song in the dataset. It'll want you to enter some number of recommendations, and it will give you those recommendations.

You can find my detailed description for the project from the link below.

https://www.kaggle.com/merveeyuboglu/music-recommendation-system-cosine-s

Before I start to say more about the functions here's the detailed features of out data. As you can see, there is lots of features for us to calculate the distance between songs. For object ones, I encoded those features. You can find the implementation in the code.

![image](https://user-images.githubusercontent.com/69505652/124440175-063c4700-dd83-11eb-8ed1-9e641b2fc73a.png)


## Functions

### find_song function

This function is for finding songs in the dataset. As I told before, it searchs the dataset. You can enter a song name or a part of the name, then the programme will find you the tracks.

Here, you can see some examples:

![image](https://user-images.githubusercontent.com/69505652/124439862-9a59de80-dd82-11eb-8cdf-6ef848db1b1f.png)

![image](https://user-images.githubusercontent.com/69505652/124439967-bcebf780-dd82-11eb-9948-8e786c9a1ce6.png)

You can skip entering a name for the song or the artist name. Based on your input, system will search the data and find the songs you want to see. 

### similar tracks

This function is the second option. You may skip entering the name of a track and find closest songs to the artist of you want to see.

![image](https://user-images.githubusercontent.com/69505652/124440437-4c91a600-dd83-11eb-9d23-bf0fc22ef173.png)

In the example above, the user entered a name and an artist name but still you don't have to enter both of them. Here's the user interface:

![image](https://user-images.githubusercontent.com/69505652/124440710-94183200-dd83-11eb-9b38-bcb09b215ad3.png)

The system works inside a while loop, it means that it will run until you enter a 'q' letter. As you can see, you don't have to enter both of the asked inputs. And also I added a number parameter. If you want to see more similar songs, you can just write how many you want from the system. 

## Final Comments

I developed this programme in a really short time, so there might be some errors. If there is any errors, i will be glad if you tell me those things. So i hope you enjoy it. It is a pretty simple programme, so it works kind of slowly. You can download the dataset and the code and run it to try yourself. Note: I developed this programme in VS Code.
