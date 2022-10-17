from ytmusicapi import YTMusic
import os


SENDER_CREDS = "headers_auth_sender.json"
RECEIVER_CREDS = "headers_auth_receiver.json"
yt_sender = None
yt_receiver = None


def create_credentials(file_name: str) -> None:
    """
    create creditials for a user
    :param: file_name:str
    """
    if not os.path.exists(file_name):
        YTMusic.setup(filepath=file_name)


def prompt_users_for_details() -> None:
    """
    Prompt user to enter credential for the different users
    """
    print("Credentials for the sending account")
    create_credentials(SENDER_CREDS)
    
    print("",end="\n\n")
    print("Credentials for the receiving account")
    create_credentials(RECEIVER_CREDS)


def setup_objects() -> None:
    """
    setup the objects to make requests from
    """
    global yt_sender, yt_receiver

    yt_sender = YTMusic(SENDER_CREDS)
    yt_receiver = YTMusic(RECEIVER_CREDS)


def get_playlists() -> list:
    """
    Grab all the playlists and return as a list
    :return: list
    """

    data = yt_sender.get_library_playlists()  # type: ignore
    
    playlists = []
    for i in data:
        data_object = {
            "title" : i.get("title", ""),
            "id" : i.get("playlistId", ""),
            "description" : i.get("description", "")
        }
        playlists.append(data_object)

    return playlists


def create_playlist(playlist_object: dict) -> None:
    """
    creates a single playlist in player object
    :param: dict
    """

    print(playlist_object)
    tracks = yt_sender.get_playlist(playlistId=playlist_object["id"], limit=None).get("tracks", [])   # type: ignore
    tracks = list(map(lambda a : a.get("videoId", ""), tracks))

    answer = input("Would you like to copy this playlist? [y/n]: ").lower()
    if answer == "n": return

    answer = input("Would you like changes these details? [y/n]: ").lower()
    if answer == 'y':
        title = input("Title: ")
        description = input("Description: ")
        yt_receiver.create_playlist(title, description, "UNLISTED", tracks) # type: ignore
        return
        

    yt_receiver.create_playlist(playlist_object["title"], playlist_object["description"], "UNLISTED", tracks) # type: ignore
    

def create_playlists(playlist_list: list) -> None:
    """
    create playlist from the list of playlists
    :param: list
    """
    for i in playlist_list:
        create_playlist(i)


def main():
    prompt_users_for_details()
    setup_objects()
    playlists = get_playlists()
    create_playlists(playlists)


if __name__=="__main__":
    main()