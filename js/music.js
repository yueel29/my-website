/**
 * Background music player for the local always.mp4 audio track.
 */

class RomanticMusicPlayer {
  constructor(audioId = 'background-music') {
    const audio = document.getElementById(audioId);
    if (!(audio instanceof HTMLAudioElement)) {
      throw new Error(`Background music element "${audioId}" was not found.`);
    }

    this.audio = audio;
    this.audio.loop = true;
    this.isPlaying = !this.audio.paused;

    this.audio.addEventListener('play', () => {
      this.isPlaying = true;
    });
    this.audio.addEventListener('pause', () => {
      this.isPlaying = false;
    });
    this.audio.addEventListener('ended', () => {
      this.isPlaying = false;
    });
    this.audio.addEventListener('error', () => {
      this.isPlaying = false;
    });
  }

  pause() {
    this.audio.pause();
    this.isPlaying = false;
  }

  async toggle() {
    if (this.isPlaying) {
      this.pause();
      return false;
    }

    await this.audio.play();
    return true;
  }
}

window.RomanticMusicPlayer = RomanticMusicPlayer;
