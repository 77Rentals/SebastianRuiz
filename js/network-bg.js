(function () {
  'use strict';

  var canvas = document.getElementById('heroCanvas');
  if (!canvas) return;

  var ctx = canvas.getContext('2d');
  if (!ctx) return;

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var GOLD = [217, 181, 88];
  var GOLD_LITE = [236, 210, 142];

  // Nodes roughly placed to suggest a world map spread: LATAM, North America, Asia.
  var seedPositions = [
    { x: 0.14, y: 0.62, label: 'Bogotá' },
    { x: 0.24, y: 0.40, label: 'Tampa' },
    { x: 0.20, y: 0.78, label: 'Colombia' },
    { x: 0.46, y: 0.30, label: 'Miami' },
    { x: 0.62, y: 0.22, label: 'Silicon Valley' },
    { x: 0.85, y: 0.55, label: 'Shanghai' },
    { x: 0.72, y: 0.72, label: 'Qatar' },
    { x: 0.40, y: 0.60, label: 'LATAM' }
  ];

  var nodes = [];
  var particles = [];
  var dpr = Math.min(window.devicePixelRatio || 1, 2);
  var w = 0, h = 0;

  function resize() {
    w = canvas.clientWidth;
    h = canvas.clientHeight;
    canvas.width = Math.floor(w * dpr);
    canvas.height = Math.floor(h * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  function buildNodes() {
    nodes = seedPositions.map(function (seed, i) {
      return {
        baseX: seed.x,
        baseY: seed.y,
        driftPhase: i * 1.3,
        driftAmpX: 0.015 + (i % 3) * 0.005,
        driftAmpY: 0.02 + (i % 2) * 0.006,
        radius: i % 3 === 0 ? 3.2 : 2.2
      };
    });
  }

  // Connections between node indices: a loose mesh, not fully connected.
  var edges = [
    [0, 1], [0, 2], [1, 3], [3, 4], [4, 5], [5, 6], [3, 5], [0, 7], [7, 4], [2, 7], [1, 4]
  ];

  // Traveling pulses along edges
  function buildParticles() {
    particles = edges.map(function (edge, i) {
      return {
        edge: edge,
        t: (i * 0.37) % 1,
        speed: 0.09 + (i % 4) * 0.025
      };
    });
  }

  function nodePos(node, time) {
    var dx = Math.sin(time * 0.15 + node.driftPhase) * node.driftAmpX;
    var dy = Math.cos(time * 0.12 + node.driftPhase) * node.driftAmpY;
    return { x: (node.baseX + dx) * w, y: (node.baseY + dy) * h };
  }

  function draw(time) {
    ctx.clearRect(0, 0, w, h);

    var positions = nodes.map(function (n) { return nodePos(n, time); });

    // edges
    edges.forEach(function (edge) {
      var a = positions[edge[0]], b = positions[edge[1]];
      var dist = Math.hypot(b.x - a.x, b.y - a.y);
      var maxDist = Math.hypot(w, h) * 0.55;
      var alpha = Math.max(0, 1 - dist / maxDist) * 0.22;
      ctx.strokeStyle = 'rgba(' + GOLD.join(',') + ',' + alpha.toFixed(3) + ')';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(a.x, a.y);
      // gentle curve via quadratic control point
      var mx = (a.x + b.x) / 2 + (b.y - a.y) * 0.06;
      var my = (a.y + b.y) / 2 - (b.x - a.x) * 0.06;
      ctx.quadraticCurveTo(mx, my, b.x, b.y);
      ctx.stroke();
    });

    // traveling pulses
    if (!reduceMotion) {
      particles.forEach(function (p) {
        p.t += p.speed * 0.008;
        if (p.t > 1) p.t -= 1;
        var a = positions[p.edge[0]], b = positions[p.edge[1]];
        var mx = (a.x + b.x) / 2 + (b.y - a.y) * 0.06;
        var my = (a.y + b.y) / 2 - (b.x - a.x) * 0.06;
        var t = p.t;
        var x = (1 - t) * (1 - t) * a.x + 2 * (1 - t) * t * mx + t * t * b.x;
        var y = (1 - t) * (1 - t) * a.y + 2 * (1 - t) * t * my + t * t * b.y;
        var glowAlpha = Math.sin(t * Math.PI) * 0.9;
        var grad = ctx.createRadialGradient(x, y, 0, x, y, 6);
        grad.addColorStop(0, 'rgba(' + GOLD_LITE.join(',') + ',' + glowAlpha + ')');
        grad.addColorStop(1, 'rgba(' + GOLD_LITE.join(',') + ',0)');
        ctx.fillStyle = grad;
        ctx.beginPath();
        ctx.arc(x, y, 6, 0, Math.PI * 2);
        ctx.fill();
      });
    }

    // nodes
    positions.forEach(function (pos, i) {
      var node = nodes[i];
      var pulse = 1 + Math.sin(time * 1.4 + node.driftPhase) * 0.18;
      var r = node.radius * pulse;

      var glow = ctx.createRadialGradient(pos.x, pos.y, 0, pos.x, pos.y, r * 6);
      glow.addColorStop(0, 'rgba(' + GOLD.join(',') + ',0.35)');
      glow.addColorStop(1, 'rgba(' + GOLD.join(',') + ',0)');
      ctx.fillStyle = glow;
      ctx.beginPath();
      ctx.arc(pos.x, pos.y, r * 6, 0, Math.PI * 2);
      ctx.fill();

      ctx.fillStyle = 'rgba(' + GOLD_LITE.join(',') + ',0.9)';
      ctx.beginPath();
      ctx.arc(pos.x, pos.y, r, 0, Math.PI * 2);
      ctx.fill();
    });
  }

  function loop(ts) {
    draw(ts * 0.001);
    if (!reduceMotion) requestAnimationFrame(loop);
  }

  window.addEventListener('resize', resize);
  resize();
  buildNodes();
  buildParticles();
  requestAnimationFrame(loop);
  if (reduceMotion) draw(0);
})();
