(function () {
  'use strict';

  var canvases = document.querySelectorAll('.shader-canvas');
  if (!canvases.length) return;

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var vertexSrc = [
    'attribute vec2 position;',
    'void main() {',
    '  gl_Position = vec4(position, 0.0, 1.0);',
    '}'
  ].join('\n');

  // Navy/gold mesh-gradient style noise field, echoing the site palette.
  var fragmentSrc = [
    'precision highp float;',
    'uniform vec2 uResolution;',
    'uniform float uTime;',
    'vec3 navyDeep = vec3(0.024, 0.059, 0.122);',
    'vec3 navyMid  = vec3(0.039, 0.094, 0.188);',
    'vec3 navyLite = vec3(0.090, 0.188, 0.345);',
    'vec3 gold     = vec3(0.788, 0.635, 0.290);',
    '',
    'float noise(vec2 p) {',
    '  return sin(p.x * 3.0) * cos(p.y * 2.6) * 0.5 + 0.5;',
    '}',
    '',
    'void main() {',
    '  vec2 uv = gl_FragCoord.xy / uResolution.xy;',
    '  vec2 p = uv * 2.0 - 1.0;',
    '  p.x *= uResolution.x / uResolution.y;',
    '',
    '  float t = uTime * 0.06;',
    '  float n1 = noise(p * 1.4 + vec2(t, -t * 0.7));',
    '  float n2 = noise(p * 2.1 - vec2(t * 0.5, t));',
    '  float blend = n1 * 0.6 + n2 * 0.4;',
    '',
    '  vec3 color = mix(navyDeep, navyMid, blend);',
    '  color = mix(color, navyLite, pow(blend, 3.0) * 0.5);',
    '',
    '  float goldGlow = smoothstep(0.78, 1.0, n1 * n2 + 0.15);',
    '  color = mix(color, gold, goldGlow * 0.18);',
    '',
    '  float vignette = 1.0 - length(p) * 0.35;',
    '  color *= clamp(vignette, 0.55, 1.0);',
    '',
    '  gl_FragColor = vec4(color, 1.0);',
    '}'
  ].join('\n');

  function compile(gl, type, src) {
    var shader = gl.createShader(type);
    gl.shaderSource(shader, src);
    gl.compileShader(shader);
    if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
      console.warn('Shader compile error:', gl.getShaderInfoLog(shader));
      gl.deleteShader(shader);
      return null;
    }
    return shader;
  }

  function initCanvas(canvas) {
    var gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
    if (!gl) return; // fall back silently to the existing CSS gradient background

    var vs = compile(gl, gl.VERTEX_SHADER, vertexSrc);
    var fs = compile(gl, gl.FRAGMENT_SHADER, fragmentSrc);
    if (!vs || !fs) return;

    var program = gl.createProgram();
    gl.attachShader(program, vs);
    gl.attachShader(program, fs);
    gl.linkProgram(program);
    if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
      console.warn('Program link error:', gl.getProgramInfoLog(program));
      return;
    }
    gl.useProgram(program);

    var quad = new Float32Array([-1, -1, 1, -1, -1, 1, 1, -1, 1, 1, -1, 1]);
    var buffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
    gl.bufferData(gl.ARRAY_BUFFER, quad, gl.STATIC_DRAW);

    var posLoc = gl.getAttribLocation(program, 'position');
    gl.enableVertexAttribArray(posLoc);
    gl.vertexAttribPointer(posLoc, 2, gl.FLOAT, false, 0, 0);

    var uResolution = gl.getUniformLocation(program, 'uResolution');
    var uTime = gl.getUniformLocation(program, 'uTime');

    function resize() {
      var dpr = Math.min(window.devicePixelRatio || 1, 2);
      var w = canvas.clientWidth;
      var h = canvas.clientHeight;
      canvas.width = Math.floor(w * dpr);
      canvas.height = Math.floor(h * dpr);
      gl.viewport(0, 0, canvas.width, canvas.height);
    }

    function render(time) {
      gl.uniform2f(uResolution, canvas.width, canvas.height);
      gl.uniform1f(uTime, reduceMotion ? 0 : time * 0.001);
      gl.drawArrays(gl.TRIANGLES, 0, 6);
      if (!reduceMotion) requestAnimationFrame(render);
    }

    window.addEventListener('resize', resize);
    resize();
    requestAnimationFrame(render);
  }

  canvases.forEach(initCanvas);
})();
