import React, { useEffect, useState } from 'react';

function App() {
  const [songs, setSongs] = useState([]);
  const [selectedSong, setSelectedSong] = useState(null);
  const [audio, setAudio] = useState(null);

  // Fetch songs from your FastAPI backend
  useEffect(() => {
    fetch('http://localhost:8000/songs')
      .then((res) => res.json())
      .then((data) => setSongs(data));
  }, []);

  const handleSelect = (song) => {
    setSelectedSong(song);
    if (audio) {
      audio.pause();
    }
    const newAudio = new Audio(song.audio_url);
    setAudio(newAudio);
    newAudio.play();
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h1>🎵 lyric.lv</h1>

      <h2>Choose a song:</h2>
      <ul>
        {songs.map((song) => (
          <li key={song.id}>
            <button onClick={() => handleSelect(song)}>
              {song.title} — {song.artist}
            </button>
          </li>
        ))}
      </ul>

      {selectedSong && (
        <div style={{ marginTop: '2rem' }}>
          <h3>Now Playing: {selectedSong.title}</h3>
          <p>Artist: {selectedSong.artist}</p>
        </div>
      )}
    </div>
  );
}

export default App;