from fastapi import APIRouter
router = APIRouter()

songs = [
    {
        "id": 1, 
        "title": "See You Again", 
        "artist": "Tyler, the Creator",
        "audio_url": "http://localhost:8000/static/see_you_again.mp3"
    },

    {
        "id": 2,
        "title": "Self Control",
        "artist": "Frank Ocean",
        "audio_url": "http://localhost:8000/static/self_control.mp3"
    },

    {
        "id": 3,
        "title": "Best Part",
        "artist": "Daniel Caesar",
        "audio_url": "http://localhost:8000/static/best_part.mp3"
    }
]

@router.get("/songs")
def get_songs():
    return songs

@router.get("/songs/{song_id}")
def get_song(song_id:int):
    for song in songs:
        if song["id"] == song_id:
            return song
    return {"error": "Song not found"}, 404