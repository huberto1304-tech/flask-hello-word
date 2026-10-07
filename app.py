from flask import Flask
app = Flask(__name__)

@app.route('/')
def dj():
    return """
<!DOCTYPE html><html><head>
<meta name='viewport' content='width=device-width, initial-scale=1'>
<style>
body{background:#000;color:#fff;text-align:center;font-family:Arial}
h1{color:#00ff88;text-shadow:0 0 20px #00ff88;font-size:35px}
.cam{font-size:110px;animation:c 2s infinite}
@keyframes c{0%{filter:hue-rotate(0deg) drop-shadow(0 0 20px #0f0)}100%{filter:hue-rotate(360deg) drop-shadow(0 0 20px #0f0)}}
.pad{display:grid;grid-template-columns:1fr 1fr;gap:12px;padding:20px;max-width:380px;margin:auto}
.b{padding:30px;border-radius:18px;border:3px solid #0ff;background:#111;color:#0ff;font-size:19px;font-weight:bold;box-shadow:0 0 15px #0ff}
.b:active{background:#0ff;color:#000;transform:scale(0.92)}
</style></head><body>
<h1>DJ CAMALEON NEON</h1>
<div class="cam">🦎</div>
<h2>🎧 MIXER PRO 🎧</h2>
<div class="pad">
<button class="b" onclick="s(60)">BOOM</button>
<button class="b" onclick="s(800)">CLAP</button>
<button class="b" onclick="s(120)">BASS</button>
<button class="b" onclick="s(1500)">FX NEON</button>
</div>
<script>
function s(f){let a=new AudioContext(),o=a.createOscillator(),g=a.createGain();o.connect(g);g.connect(a.destination);o.frequency.value=f;g.gain.setValueAtTime(1,a.currentTime);g.gain.exponentialRampToValueAtTime(0.01,a.currentTime+.5);o.start();o.stop(a.currentTime+.5)}
</script></body></html>
"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
