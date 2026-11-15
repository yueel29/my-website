/**
 * Falling Tulip Petals Canvas Effect
 * Creates a romantic atmosphere with floating purple & pink tulip petals
 */

class PetalSystem {
  constructor(canvasId) {
    this.canvas = document.getElementById(canvasId);
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    this.petals = [];
    this.maxPetals = 45;
    this.isRunning = true;
    this.wind = 0;
    this.targetWind = 0;
    this.mouseX = 0;

    this.colors = [
      { fill: '#B57EDC', opacity: 0.75 }, // Lavender
      { fill: '#D8B4F8', opacity: 0.8 },  // Soft Lilac
      { fill: '#F5D9F2', opacity: 0.85 }, // Soft Pink
      { fill: '#9D4EDD', opacity: 0.65 }, // Mid Purple
      { fill: '#FAF7FF', opacity: 0.9 }   // Lavender White
    ];

    this.init();
  }

  init() {
    this.resize();
    window.addEventListener('resize', () => this.resize());

    // Wind response to mouse movement
    window.addEventListener('mousemove', (e) => {
      const centerDelta = (e.clientX - window.innerWidth / 2) / (window.innerWidth / 2);
      this.targetWind = centerDelta * 1.5;
    });

    // Populate petals
    for (let i = 0; i < this.maxPetals; i++) {
      this.petals.push(this.createPetal(true));
    }

    this.animate();
  }

  resize() {
    this.canvas.width = window.innerWidth;
    this.canvas.height = window.innerHeight;
  }

  createPetal(randomY = false) {
    const color = this.colors[Math.floor(Math.random() * this.colors.length)];
    return {
      x: Math.random() * this.canvas.width,
      y: randomY ? Math.random() * this.canvas.height : -20,
      size: 10 + Math.random() * 14,
      aspectRatio: 1.4 + Math.random() * 0.8,
      speedY: 1.0 + Math.random() * 1.6,
      speedX: -0.5 + Math.random() * 1.0,
      rotation: Math.random() * Math.PI * 2,
      rotationSpeed: (Math.random() - 0.5) * 0.03,
      swingAngle: Math.random() * Math.PI * 2,
      swingSpeed: 0.02 + Math.random() * 0.03,
      swingRadius: 15 + Math.random() * 25,
      color: color.fill,
      opacity: color.opacity,
      isMiniTulip: Math.random() < 0.25 // 25% are tiny floating tulip blooms
    };
  }

  drawPetal(p) {
    this.ctx.save();
    this.ctx.translate(p.x, p.y);
    this.ctx.rotate(p.rotation);
    this.ctx.globalAlpha = p.opacity;

    if (p.isMiniTulip) {
      // Draw tiny stylized tulip
      const s = p.size * 0.7;
      this.ctx.fillStyle = p.color;
      this.ctx.beginPath();
      this.ctx.moveTo(0, s);
      this.ctx.bezierCurveTo(-s * 0.8, s * 0.2, -s, -s * 0.6, 0, -s);
      this.ctx.bezierCurveTo(s, -s * 0.6, s * 0.8, s * 0.2, 0, s);
      this.ctx.fill();

      // Tulip inner petal highlight
      this.ctx.fillStyle = '#FFFFFF';
      this.ctx.globalAlpha = p.opacity * 0.5;
      this.ctx.beginPath();
      this.ctx.ellipse(0, 0, s * 0.28, s * 0.65, 0, 0, Math.PI * 2);
      this.ctx.fill();
    } else {
      // Draw smooth romantic petal
      const w = p.size;
      const h = p.size * p.aspectRatio;

      this.ctx.fillStyle = p.color;
      this.ctx.beginPath();
      this.ctx.moveTo(0, -h / 2);
      this.ctx.bezierCurveTo(w * 0.85, -h / 4, w * 0.7, h / 2, 0, h / 2);
      this.ctx.bezierCurveTo(-w * 0.7, h / 2, -w * 0.85, -h / 4, 0, -h / 2);
      this.ctx.fill();

      // Soft petal vein
      this.ctx.strokeStyle = '#FFFFFF';
      this.ctx.globalAlpha = p.opacity * 0.35;
      this.ctx.lineWidth = 1;
      this.ctx.beginPath();
      this.ctx.moveTo(0, -h / 2 + 2);
      this.ctx.lineTo(0, h / 2 - 2);
      this.ctx.stroke();
    }

    this.ctx.restore();
  }

  animate() {
    if (!this.isRunning) return;

    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

    // Smooth wind transition
    this.wind += (this.targetWind - this.wind) * 0.05;

    for (let i = 0; i < this.petals.length; i++) {
      const p = this.petals[i];

      p.swingAngle += p.swingSpeed;
      p.x += Math.cos(p.swingAngle) * 0.8 + this.wind + p.speedX;
      p.y += p.speedY;
      p.rotation += p.rotationSpeed;

      this.drawPetal(p);

      // Reset when off-screen
      if (p.y > this.canvas.height + 30 || p.x < -40 || p.x > this.canvas.width + 40) {
        this.petals[i] = this.createPetal(false);
      }
    }

    requestAnimationFrame(() => this.animate());
  }

  toggle() {
    this.isRunning = !this.isRunning;
    if (this.isRunning) {
      this.animate();
    } else {
      this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }
    return this.isRunning;
  }
}

// Global initialization
window.PetalSystem = PetalSystem;
