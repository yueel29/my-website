/**
 * Main Application Logic
 * Website: "My Baby" - Romantic Purple Tulip Garden
 */

document.addEventListener('DOMContentLoaded', () => {
  const welcomeScreen = document.getElementById('welcome-screen');
  const welcomeEnvelope = document.getElementById('welcome-envelope');
  const welcomePetalBurst = document.getElementById('welcome-petal-burst');

  if (welcomeScreen && welcomeEnvelope && welcomePetalBurst) {
    document.body.classList.add('intro-active');
    Array.from(document.body.children).forEach((element) => {
      if (element !== welcomeScreen) {
        element.inert = true;
      }
    });

    welcomeEnvelope.addEventListener('click', () => {
      if (welcomeScreen.classList.contains('is-opening')) return;

      welcomeEnvelope.disabled = true;
      welcomeScreen.classList.add('is-opening');
      toggleMusicPlayback();

      const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      const particleCount = reducedMotion ? 48 : (window.innerWidth <= 600 ? 130 : 170);
      const maxDistance = Math.hypot(window.innerWidth, window.innerHeight) * 0.72;

      for (let index = 0; index < particleCount; index += 1) {
        const isTulip = index % 5 === 0;
        const particle = document.createElement(isTulip ? 'img' : 'span');
        const angle = Math.random() * Math.PI * 2;
        const distance = 60 + Math.sqrt(Math.random()) * maxDistance;
        const size = isTulip ? 58 + Math.random() * 70 : 24 + Math.random() * 52;

        particle.className = isTulip ? 'welcome-burst-tulip' : 'welcome-burst-petal';
        if (isTulip) {
          particle.src = 'images/decorations/purple-tulip.svg';
          particle.alt = '';
        }

        particle.style.setProperty('--burst-x', `${Math.cos(angle) * distance}px`);
        particle.style.setProperty('--burst-y', `${Math.sin(angle) * distance}px`);
        particle.style.setProperty('--burst-size', `${size}px`);
        particle.style.setProperty('--burst-rotation', `${Math.random() * 720 - 360}deg`);
        particle.style.animationDelay = `${Math.random() * 180}ms`;
        if (reducedMotion) {
          particle.style.animationDuration = '0.35s';
        }
        welcomePetalBurst.appendChild(particle);
      }

      const revealDelay = reducedMotion ? 450 : 1650;
      const fadeDuration = reducedMotion ? 250 : 650;

      window.setTimeout(() => {
        welcomeScreen.classList.add('is-leaving');
        document.body.classList.add('home-revealing');
        window.setTimeout(() => {
          welcomeScreen.hidden = true;
          document.body.classList.remove('intro-active');
          Array.from(document.body.children).forEach((element) => {
            if (element !== welcomeScreen) {
              element.inert = false;
            }
          });
          window.scrollTo(0, 0);
        }, fadeDuration);
        window.setTimeout(() => {
          document.body.classList.remove('home-revealing');
        }, fadeDuration + 1000);
      }, revealDelay);
    }, { once: true });
  }

  // 1. Initialize the always-on canvas petals system
  if (window.PetalSystem) {
    new window.PetalSystem('petals-canvas');
  }

  // 2. Initialize Romantic Music Player
  let musicPlayer = null;
  if (window.RomanticMusicPlayer) {
    musicPlayer = new window.RomanticMusicPlayer();
  }

  const musicToggleBtn = document.getElementById('music-toggle');
  const musicWidget = document.getElementById('music-widget');
  const musicError = document.getElementById('music-error');
  let updateMusicControl = () => {};
  let toggleMusicPlayback = () => {};
  if (musicToggleBtn && musicWidget && musicPlayer) {
    let swipeStart = null;
    let suppressClick = false;

    updateMusicControl = () => {
      const playing = musicPlayer.isPlaying;
      const collapsed = musicWidget.classList.contains('collapsed');
      const label = musicToggleBtn.querySelector('.music-label');
      const controlLabel = collapsed
        ? (playing ? 'Show music controls; melody is playing' : 'Show music controls')
        : (playing ? 'Pause romantic melody' : 'Play romantic melody');

      if (label) {
        label.textContent = playing ? 'Pause' : 'Play';
      }
      musicToggleBtn.setAttribute('aria-label', controlLabel);
      musicToggleBtn.setAttribute('aria-pressed', String(playing));
      musicToggleBtn.setAttribute('aria-expanded', String(!collapsed));
      musicToggleBtn.title = controlLabel;
      musicToggleBtn.classList.toggle('is-playing', playing);
    };

    toggleMusicPlayback = () => {
      if (musicError) {
        musicError.textContent = '';
      }

      musicPlayer.toggle()
        .then(updateMusicControl)
        .catch((error) => {
          musicPlayer.pause();
          updateMusicControl();
          if (musicError) {
            musicError.textContent = 'This browser could not play images/always.mp4. Check support for this audio format.';
          }
          console.error('Background music playback failed:', error);
        });
    };

    musicToggleBtn.addEventListener('click', () => {
      if (suppressClick) {
        suppressClick = false;
        return;
      }

      if (musicWidget.classList.contains('collapsed')) {
        musicWidget.classList.remove('collapsed');
        updateMusicControl();
        return;
      }

      toggleMusicPlayback();
    });

    musicWidget.addEventListener('pointerdown', (event) => {
      if (event.pointerType === 'mouse' && event.button !== 0) return;
      swipeStart = { x: event.clientX, y: event.clientY };
    });

    document.addEventListener('pointerup', (event) => {
      if (!swipeStart) return;

      const deltaX = event.clientX - swipeStart.x;
      const deltaY = event.clientY - swipeStart.y;
      swipeStart = null;

      if (deltaX > 55 && deltaX > Math.abs(deltaY)) {
        musicWidget.classList.add('collapsed');
        suppressClick = true;
        updateMusicControl();
        window.setTimeout(() => {
          suppressClick = false;
        }, 0);
      }
    });

    document.addEventListener('pointercancel', () => {
      swipeStart = null;
    });

    updateMusicControl();
  }

  // 3. Sticky Navbar & Scroll Spy
  const navbar = document.getElementById('navbar');
  const navLinks = document.querySelectorAll('.nav-link');
  const sections = document.querySelectorAll('section[id]');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }

    // Scroll spy
    let current = '';
    sections.forEach((section) => {
      const sectionTop = section.offsetTop - 120;
      const sectionHeight = section.offsetHeight;
      if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach((link) => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${current}`) {
        link.classList.add('active');
      }
    });
  });

  // Mobile Menu Toggle
  const mobileToggle = document.getElementById('mobile-toggle');
  const navMenu = document.getElementById('nav-menu');
  if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', () => {
      navMenu.classList.toggle('open');
    });

    // Close on link click
    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('open');
      });
    });
  }

  // 4. Live Days Together Counter
  const startDate = new Date(2026, 0, 5);

  const countDays = document.getElementById('counter-days');
  const countHours = document.getElementById('counter-hours');
  const countMinutes = document.getElementById('counter-minutes');
  const countSeconds = document.getElementById('counter-seconds');

  function updateLoveCounter() {
    const now = new Date();
    const diff = Math.max(0, now - startDate);

    const totalSeconds = Math.floor(diff / 1000);
    const days = Math.floor(totalSeconds / (3600 * 24));
    const hours = Math.floor((totalSeconds % (3600 * 24)) / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds % 60;

    if (countDays) countDays.textContent = String(days).padStart(3, '0');
    if (countHours) countHours.textContent = String(hours).padStart(2, '0');
    if (countMinutes) countMinutes.textContent = String(minutes).padStart(2, '0');
    if (countSeconds) countSeconds.textContent = String(seconds).padStart(2, '0');
  }

  updateLoveCounter();
  setInterval(updateLoveCounter, 1000);

  // 5. Photo Carousel Logic
  const track = document.getElementById('carousel-track');
  const playToggle = document.getElementById('carousel-play-toggle');
  const assetsNote = document.getElementById('carousel-assets-note');
  const animationModal = document.getElementById('photo-animation-modal');
  const animationDialog = document.getElementById('photo-animation-dialog');
  const animationBackdrop = document.getElementById('photo-animation-backdrop');
  const animationClose = document.getElementById('photo-animation-close');
  const animationStage = document.getElementById('photo-animation-stage');
  const motionToggle = document.getElementById('photo-animation-motion-toggle');

  if (track && playToggle && assetsNote) {
    const totalPhotos = 20;
    const photoFiles = Array.from({ length: totalPhotos }, (_, index) => `m${index + 1}.jpg`);
    const loadedPhotos = new Set();
    let animationPhotosCreated = false;
    let animationReturnFocus = null;
    const originalSet = document.createElement('div');
    originalSet.className = 'carousel-set';

    photoFiles.forEach((file, index) => {
      const photoNumber = index + 1;
      const photoPath = `images/photos/${file}`;
      const slide = document.createElement('div');
      slide.className = 'carousel-slide';
      slide.dataset.photoIndex = String(photoNumber);
      slide.setAttribute('data-lightbox', '');
      slide.setAttribute('data-img-src', photoPath);
      slide.setAttribute('data-title', `My Baby - Photo ${String(photoNumber).padStart(2, '0')}`);
      slide.setAttribute('data-subtitle', 'Captured in purple light');
      slide.setAttribute('role', 'button');
      slide.tabIndex = 0;
      slide.setAttribute('aria-label', `View photo ${photoNumber} of ${totalPhotos}`);

      const image = document.createElement('img');
      image.src = photoPath;
      image.alt = `Photo ${photoNumber} of my baby`;
      image.loading = photoNumber === 1 ? 'eager' : 'lazy';
      image.decoding = 'async';

      const placeholder = document.createElement('div');
      placeholder.className = 'carousel-placeholder';
      placeholder.setAttribute('aria-hidden', 'true');

      const mark = document.createElement('span');
      mark.className = 'carousel-placeholder-mark';
      mark.textContent = '🌷';

      const title = document.createElement('strong');
      title.textContent = `Photo ${String(photoNumber).padStart(2, '0')} of ${totalPhotos}`;

      const instruction = document.createElement('span');
      instruction.className = 'carousel-placeholder-instruction';
      instruction.textContent = `Loading ${file}`;

      placeholder.append(mark, title, instruction);
      slide.append(image, placeholder);
      originalSet.appendChild(slide);
    });

    const cloneSet = originalSet.cloneNode(true);
    cloneSet.classList.add('carousel-set-clone');
    cloneSet.setAttribute('aria-hidden', 'true');
    cloneSet.querySelectorAll('.carousel-slide').forEach((slide) => {
      slide.classList.add('carousel-slide-clone');
      slide.removeAttribute('role');
      slide.removeAttribute('tabindex');
    });
    track.replaceChildren(cloneSet, originalSet);

    const slides = Array.from(track.querySelectorAll('.carousel-slide'));

    function updateAssetsNote() {
      assetsNote.hidden = loadedPhotos.size === totalPhotos;
    }

    function layoutAnimationPhotos() {
      if (!animationPhotosCreated || !animationStage) return;

      const compactLayout = window.matchMedia('(max-width: 560px)').matches;
      const columns = compactLayout ? 4 : 5;
      const columnStep = compactLayout ? 23.3 : 18.5;
      const firstColumn = compactLayout ? 15 : 13;
      const rowStep = compactLayout ? 17 : 18.5;
      const firstRow = compactLayout ? 16 : 20.5;

      Array.from(animationStage.children).forEach((photo, index) => {
        const column = index % columns;
        const row = Math.floor(index / columns);
        const horizontalJitter = ((index * 7) % 9 - 4) * (compactLayout ? 0.6 : 1.35);
        const verticalJitter = ((index * 5) % 9 - 4) * (compactLayout ? 0.7 : 1.2);

        photo.style.setProperty('--photo-x', `${firstColumn + column * columnStep + horizontalJitter}%`);
        photo.style.setProperty('--photo-y', `${firstRow + row * rowStep + verticalJitter}%`);
        photo.style.setProperty('--photo-rotation', `${((index * 17) % 31) - 15}deg`);
        photo.style.setProperty('--photo-size', `${compactLayout ? 42 + ((index * 9) % 21) : 76 + ((index * 13) % 28)}px`);
        photo.style.setProperty('--float-delay', `${-((index % 7) * 0.35)}s`);
      });
    }

    function createAnimationPhotos() {
      if (animationPhotosCreated || !animationStage) return;

      photoFiles.forEach((file, index) => {
        const photoNumber = index + 1;
        const photo = document.createElement('figure');
        photo.className = 'photo-animation-item';
        photo.setAttribute('aria-label', `Photo ${photoNumber} of ${totalPhotos}`);

        const image = document.createElement('img');
        image.alt = `Photo ${photoNumber} of my baby`;
        image.loading = 'eager';
        image.decoding = 'async';
        image.addEventListener('error', () => {
          photo.classList.add('is-missing');
          image.remove();
        }, { once: true });

        const fallback = document.createElement('span');
        fallback.className = 'photo-animation-fallback';
        fallback.textContent = `Photo ${String(photoNumber).padStart(2, '0')}`;
        fallback.setAttribute('aria-hidden', 'true');

        photo.append(image, fallback);
        animationStage.appendChild(photo);
        image.src = `images/photos/${file}`;
      });

      animationPhotosCreated = true;
      layoutAnimationPhotos();
    }

    function openPhotoAnimation() {
      if (!animationModal || !animationStage || !animationClose || !motionToggle) return;

      createAnimationPhotos();
      layoutAnimationPhotos();
      animationReturnFocus = document.activeElement;
      animationStage.classList.remove('is-paused');
      motionToggle.setAttribute('aria-pressed', 'false');
      motionToggle.textContent = 'Pause Motion';
      animationModal.classList.add('is-open');
      animationModal.setAttribute('aria-hidden', 'false');
      document.body.classList.add('photo-animation-open');
      window.requestAnimationFrame(() => animationClose.focus());
    }

    function closePhotoAnimation() {
      if (!animationModal || !animationModal.classList.contains('is-open')) return;

      animationModal.classList.remove('is-open');
      animationModal.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('photo-animation-open');
      if (animationReturnFocus instanceof HTMLElement) {
        animationReturnFocus.focus();
      }
    }

    playToggle.addEventListener('click', openPhotoAnimation);
    animationClose?.addEventListener('click', closePhotoAnimation);
    animationBackdrop?.addEventListener('click', closePhotoAnimation);
    motionToggle?.addEventListener('click', () => {
      const isPaused = animationStage.classList.toggle('is-paused');
      motionToggle.setAttribute('aria-pressed', String(isPaused));
      motionToggle.textContent = isPaused ? 'Resume Motion' : 'Pause Motion';
    });

    animationDialog?.addEventListener('keydown', (event) => {
      if (event.key !== 'Tab') return;

      const focusableElements = Array.from(animationDialog.querySelectorAll('button:not([disabled])'));
      const firstElement = focusableElements[0];
      const lastElement = focusableElements[focusableElements.length - 1];
      if (event.shiftKey && document.activeElement === firstElement) {
        event.preventDefault();
        lastElement.focus();
      } else if (!event.shiftKey && document.activeElement === lastElement) {
        event.preventDefault();
        firstElement.focus();
      }
    });

    document.addEventListener('keydown', (event) => {
      if (!animationModal?.classList.contains('is-open')) return;
      if (event.key === 'Escape') closePhotoAnimation();
    });

    window.addEventListener('resize', layoutAnimationPhotos);

    slides.forEach((slide) => {
      const image = slide.querySelector('img');
      const photoNumber = Number(slide.dataset.photoIndex);
      const isClone = slide.classList.contains('carousel-slide-clone');

      image.addEventListener('load', () => {
        slide.classList.add('has-photo');
        slide.classList.remove('carousel-slide--missing');
        slide.querySelector('.carousel-placeholder')?.remove();
        if (!isClone) {
          loadedPhotos.add(photoNumber);
          updateAssetsNote();
        }
      });

      image.addEventListener('error', () => {
        slide.classList.add('carousel-slide--missing');
        slide.classList.remove('has-photo');
        image.remove();
        slide.removeAttribute('data-lightbox');
        slide.removeAttribute('data-img-src');
        slide.removeAttribute('role');
        slide.removeAttribute('tabindex');
        const instruction = slide.querySelector('.carousel-placeholder-instruction');
        if (instruction) {
          instruction.textContent = `Add ${photoFiles[photoNumber - 1]} to images/photos`;
        }

        if (!isClone) {
          updateAssetsNote();
        }
      }, { once: true });
    });

    track.querySelectorAll('.carousel-slide-clone img').forEach((image) => {
      image.loading = 'eager';
    });

    updateAssetsNote();
  }

  // 6. Lightbox Modal
  const lightbox = document.getElementById('lightbox-modal');
  const lightboxImg = document.getElementById('lightbox-img');

  const lightboxClose = document.getElementById('lightbox-close');

  function openLightbox(src, title, subtitle) {
    if (!lightbox) return;
    lightboxImg.src = src;
    lightboxImg.alt = title || 'Romantic Photo';
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    if (!lightbox) return;
    lightbox.classList.remove('active');
    lightbox.classList.remove('photo-lightbox');
    document.body.style.overflow = '';
  }

  if (lightboxClose) {
    lightboxClose.addEventListener('click', closeLightbox);
  }

  if (lightbox) {
    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox) closeLightbox();
    });
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && lightbox && lightbox.classList.contains('active')) {
      closeLightbox();
    }
  });

  // Attach Lightbox to Carousel, Scrapbook, and food gallery images
  document.querySelectorAll('[data-lightbox]').forEach(el => {
    const showLightbox = () => {
      const src = el.getAttribute('data-img-src') || el.querySelector('img')?.src;
      const title = el.getAttribute('data-title') || el.querySelector('h3, h4')?.textContent;
      const subtitle = el.getAttribute('data-subtitle') || el.querySelector('p, .polaroid-date')?.textContent;
      if (src) {
        const isPhoto = el.classList.contains('food-photo') || el.classList.contains('carousel-slide');
        lightbox?.classList.toggle('photo-lightbox', isPhoto);
        openLightbox(src, title, subtitle);
      }
    };

    el.addEventListener('click', showLightbox);

    if (el.classList.contains('food-photo') || el.classList.contains('carousel-slide')) {
      el.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          showLightbox();
        }
      });
    }
  });

  // 7. Scrapbook Filtering
  const filterBtns = document.querySelectorAll('.filter-btn');
  const scrapbookItems = document.querySelectorAll('.scrapbook-item');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filterValue = btn.getAttribute('data-filter');

      scrapbookItems.forEach(item => {
        const itemCategory = item.getAttribute('data-category');
        if (filterValue === 'all' || itemCategory === filterValue) {
          item.style.display = 'block';
          item.style.animation = 'unfoldLetter 0.5s ease forwards';
        } else {
          item.style.display = 'none';
        }
      });
    });
  });

  // 8. Love Letter Interactive Opening
  const envelopeBox = document.getElementById('envelope-box');
  const envelopeSealBtn = document.getElementById('envelope-seal-btn');
  const letterPaper = document.getElementById('letter-paper');
  const sealBackBtn = document.getElementById('btn-seal-back');
  const openLetterCta = document.getElementById('open-letter-cta');

  function openLoveLetter() {
    if (!letterPaper) return;
    letterPaper.classList.add('open');
    if (envelopeBox) {
      envelopeBox.style.display = 'none';
    }
    // Scroll smoothly to letter
    letterPaper.scrollIntoView({ behavior: 'smooth', block: 'center' });

    // Start the background track if it is not already playing
    if (musicPlayer && !musicPlayer.isPlaying) {
      toggleMusicPlayback();
    }
  }

  function closeLoveLetter() {
    if (!letterPaper || !envelopeBox) return;
    letterPaper.classList.remove('open');
    envelopeBox.style.display = 'block';
    envelopeBox.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }

  if (envelopeSealBtn) envelopeSealBtn.addEventListener('click', (e) => { e.stopPropagation(); openLoveLetter(); });
  if (envelopeBox) envelopeBox.addEventListener('click', openLoveLetter);
  if (openLetterCta) openLetterCta.addEventListener('click', (e) => {
    e.preventDefault();
    document.getElementById('letter').scrollIntoView({ behavior: 'smooth' });
    setTimeout(openLoveLetter, 400);
  });
  if (sealBackBtn) sealBackBtn.addEventListener('click', closeLoveLetter);

  // 9. Romantic Video Player Simulation & Custom Upload
  const videoPlayBtn = document.getElementById('video-play-btn');
  const romanticVideo = document.getElementById('romantic-video');
  const videoPlaceholder = document.getElementById('video-placeholder');
  const videoInput = document.getElementById('video-file-input');
  const uploadVideoBtn = document.getElementById('upload-video-trigger');

  if (videoPlayBtn && romanticVideo && videoPlaceholder) {
    videoPlayBtn.addEventListener('click', () => {
      videoPlaceholder.style.display = 'none';
      romanticVideo.style.display = 'block';
      romanticVideo.play().catch(() => {
        // Fallback animation if no video file source
        renderRomanticVideoCanvas();
      });
    });
  }

  if (uploadVideoBtn && videoInput) {
    uploadVideoBtn.addEventListener('click', () => videoInput.click());
    videoInput.addEventListener('change', (e) => {
      const file = e.target.files[0];
      if (file) {
        const fileURL = URL.createObjectURL(file);
        romanticVideo.src = fileURL;
        videoPlaceholder.style.display = 'none';
        romanticVideo.style.display = 'block';
        romanticVideo.play();
      }
    });
  }

  function renderRomanticVideoCanvas() {
    // If video fails or no file is found, show custom romantic canvas player
    if (videoPlaceholder) {
      videoPlaceholder.style.display = 'flex';
      const title = videoPlaceholder.querySelector('.video-placeholder-title');
      const desc = videoPlaceholder.querySelector('.video-placeholder-desc');
      if (title) title.textContent = "Every Second With You Is Pure Magic";
      if (desc) desc.textContent = "Drop your favorite video clip here or click 'Choose Video Clip' to watch your romantic memories together.";
    }
  }

  // 10. Smooth Back To Top Button
  const backToTopBtn = document.getElementById('back-to-top');
  if (backToTopBtn) {
    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }
});
