from fastapi import APIRouter

router = APIRouter()

lyrics_by_id = {
    1: [
        {"time": 0, "line": "Okay, okay, okay"},
        {"time": 3, "line": "You live in my dream state"},
        {"time": 7, "line": "Relocate my fantasy"},
    ],
    2: [
        {"time": 0, "line": "I'll be the boyfriend in your wet dreams tonight"},
        {"time": 5, "line": "Noses on a rail, little virgin wears the white"},
    ],
    3: [
        {"time": 0, "line": "You're the coffee that I need in the morning"},
        {"time": 4, "line": "You're my sunshine in the rain when it's pouring"},
    ],
}

@router.get("/lyrics{song_id}")
def get_lyrics(song_id: int):
    if song_id in lyrics_by_id:
        return lyrics_by_id[song_id]
    return {"error": "Lyrics not found"}, 404