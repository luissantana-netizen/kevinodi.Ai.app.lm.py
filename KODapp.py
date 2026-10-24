import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Odi AI Studio - Finland Edition",
    page_icon="🇫🇮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
        #MainMenu, footer, header {visibility: hidden;}
        .block-container { padding: 0rem !important; max-width: 100% !important; }
        iframe { width: 100vw !important; height: 100vh !important; border: none !important; }
    </style>
""", unsafe_allow_html=True)

html_app = """
<!DOCTYPE html>
<html lang="es" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Odi AI Studio - Finland Edition</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        stealth: { 900: '#050a14', 800: '#0b132b', 700: '#1c2541', border: '#1e3a8a' },
                        finland: { blue: '#002f6c', white: '#ffffff', cyan: '#00d2ff' }
                    },
                    fontFamily: { sans: ['Inter', 'sans-serif'], mono: ['Fira Code', 'monospace'] }
                }
            }
        }
    </script>
    <style>
        body { background-color: #050a14; color: #e2e8f0; font-family: 'Inter', sans-serif; overflow: hidden; }
        ::-webkit-scrollbar { width: 5px; }
        ::-webkit-scrollbar-thumb { background: #1c2541; border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background: #00d2ff; }
        .glass-panel { background: rgba(11, 19, 43, 0.85); backdrop-filter: blur(12px); border: 1px solid rgba(30, 58, 138, 0.6); }
        .prose pre { background-color: #030712 !important; border: 1px solid #1e3a8a; padding: 0.75rem; border-radius: 0.5rem; }
        .prose code { color: #00d2ff; font-family: 'Fira Code', monospace; }
        canvas { touch-action: none; }
    </style>
</head>
<body class="h-screen flex flex-col md:flex-row select-none">

    <aside class="w-full md:w-64 glass-panel border-r border-stealth-border flex flex-col justify-between z-40 shrink-0">
        <div>
            <div class="p-4 border-b border-stealth-border flex items-center justify-between">
                <div class="flex items-center gap-2.5">
                    <div class="w-9 h-9 rounded-xl bg-white flex items-center justify-center text-finland-blue font-bold shadow-lg shadow-cyan-500/20 relative overflow-hidden border border-finland-blue">
                        <div class="absolute inset-0 flex items-center justify-center">
                            <div class="w-full h-2 bg-finland-blue"></div>
                        </div>
                        <div class="absolute inset-0 flex items-center justify-center">
                            <div class="h-full w-2 bg-finland-blue"></div>
                        </div>
                        <span class="z-10 font-extrabold text-xs text-finland-blue bg-white px-0.5 rounded">ODI</span>
                    </div>
                    <div>
                        <h1 class="font-bold text-white text-sm tracking-wider flex items-center gap-1">
                            ODI AI <span class="text-xs">🇫🇮</span>
                        </h1>
                        <p class="text-[9px] text-cyan-400 font-mono tracking-widest uppercase">Suomi Studio 3.0</p>
                    </div>
                </div>
                <button id="openSettings" class="text-gray-400 hover:text-cyan-400 p-1.5"><i class="fa-solid fa-gear"></i></button>
            </div>

            <div class="p-3 space-y-1.5">
                <label class="text-[10px] font-mono text-gray-400 uppercase px-2">Módulos de Odi</label>
                <button data-target="chat-module" class="nav-btn w-full flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-medium text-cyan-400 bg-cyan-500/10 border border-cyan-500/30">
                    <i class="fa-solid fa-snowflake text-cyan-400"></i> Asistente Odi & Tareas
                </button>
                <button data-target="math-module" class="nav-btn w-full flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-medium text-gray-400 hover:bg-stealth-800 hover:text-white">
                    <i class="fa-solid fa-calculator text-blue-400"></i> Math Fast-Engine
                </button>
                <button data-target="draw-module" class="nav-btn w-full flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-medium text-gray-400 hover:bg-stealth-800 hover:text-white">
                    <i class="fa-solid fa-palette text-cyan-300"></i> Aprende a Dibujar
                </button>
                <button data-target="games-module" class="nav-btn w-full flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-medium text-gray-400 hover:bg-stealth-800 hover:text-white">
                    <i class="fa-solid fa-gamepad text-emerald-400"></i> Minijuegos (Arcade)
                </button>
            </div>
        </div>

        <div class="p-3 border-t border-stealth-border">
            <div id="apiStatus" class="p-2.5 rounded-xl bg-stealth-800 border border-stealth-border flex items-center gap-2 text-[11px]">
                <span id="apiDot" class="w-2 h-2 rounded-full bg-emerald-400"></span>
                <span id="apiText" class="text-gray-300">Motor Odi AI Listo</span>
            </div>
        </div>
<!-- BANNER ADSENSE ODI AI -->
<div style="margin-top: 20px; padding: 10px; text-align: center;">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2829063535565810" crossorigin="anonymous"></script>
    <ins class="adsbygoogle"
         style="display:block"
         data-ad-client="ca-pub-2829063535565810"
         data-ad-slot="5529007236"
         data-ad-format="auto"
         data-full-width-responsive="true"></ins>
    <script>
         (adsbygoogle = window.adsbygoogle || []).push({});
    </script>
</div>        
    </aside>

    <main class="flex-1 bg-stealth-900 relative overflow-hidden flex flex-col">

        <section id="chat-module" class="module-section flex-1 flex flex-col h-full">
            <div class="px-6 py-3 border-b border-stealth-border glass-panel flex justify-between items-center">
                <span class="text-xs font-semibold text-gray-200"><i class="fa-solid fa-robot text-cyan-400 mr-2"></i>Asistente Inteligente Odi AI (Finlandia)</span>
                <button id="clearChat" class="text-xs text-gray-400 hover:text-red-400"><i class="fa-solid fa-trash mr-1"></i>Limpiar</button>
            </div>
            <div id="chatBox" class="flex-1 overflow-y-auto p-4 sm:p-6 space-y-4">
                <div class="flex gap-3 max-w-2xl">
                    <div class="w-8 h-8 rounded-lg bg-blue-600 border border-white flex items-center justify-center text-white shrink-0 font-bold text-xs">🇫🇮</div>
                    <div class="glass-panel p-3.5 rounded-2xl rounded-tl-none text-xs leading-relaxed text-gray-200">
                        ¡Moi! (¡Hola!) Soy <b>Odi AI</b>, tu asistente virtual inteligente desde Finlandia. Puedo resolver tareas escolares, explicarte cualquier tema paso a paso, realizar análisis o programar. ¿En qué te ayudo hoy?
                    </div>
                </div>
            </div>
            <div class="p-4 glass-panel border-t border-stealth-border">
                <form id="chatForm" class="flex gap-2 max-w-3xl mx-auto">
                    <input type="text" id="chatInput" placeholder="Pregúntale lo que sea a Odi AI..." class="flex-1 bg-stealth-800 border border-stealth-border rounded-xl px-4 py-2.5 text-xs text-white focus:outline-none focus:border-cyan-400">
                    <button type="submit" class="px-4 py-2.5 bg-gradient-to-r from-blue-600 to-cyan-500 text-white font-bold rounded-xl text-xs"><i class="fa-solid fa-paper-plane"></i></button>
                </form>
            </div>
        </section>

        <section id="math-module" class="module-section flex-1 hidden p-6 overflow-y-auto">
            <div class="max-w-2xl mx-auto space-y-4">
                <div>
                    <h2 class="text-lg font-bold text-white"><i class="fa-solid fa-bolt text-cyan-400 mr-2"></i>Odi Fast-Math Engine (0ms Latencia)</h2>
                    <p class="text-xs text-gray-400">Calculadora de respuesta inmediata para operaciones matemáticas avanzadas, álgebra y trigonometría.</p>
                </div>
                <div class="glass-panel p-4 rounded-2xl space-y-3">
                    <textarea id="mathInput" rows="3" placeholder="Ejemplo: (4444 * 3333) / 12 + sqrt(144) o sin(45)" class="w-full bg-stealth-800 border border-stealth-border rounded-xl p-3 text-xs font-mono text-cyan-300 focus:outline-none focus:border-cyan-400"></textarea>
                    <button id="calcMathBtn" class="w-full py-2.5 bg-blue-600 hover:bg-blue-500 text-white font-bold rounded-xl text-xs flex items-center justify-center gap-2">
                        <i class="fa-solid fa-calculator"></i> Calcular con Odi Engine
                    </button>
                </div>
                <div id="mathResultCard" class="hidden glass-panel p-4 rounded-2xl border-cyan-500/40">
                    <span class="text-[10px] font-mono text-cyan-400 uppercase">Resultado Exacto:</span>
                    <div id="mathOutput" class="text-lg font-mono font-bold text-white mt-1"></div>
                </div>
            </div>
        </section>

        <section id="draw-module" class="module-section flex-1 hidden p-6 overflow-y-auto">
            <div class="max-w-4xl mx-auto space-y-4">
                <div class="flex justify-between items-center">
                    <div>
                        <h2 class="text-lg font-bold text-white"><i class="fa-solid fa-palette text-cyan-400 mr-2"></i>Estudio de Dibujo Odi</h2>
                        <p class="text-xs text-gray-400">Dibuja libremente o practica guiándote con las plantillas.</p>
                    </div>
                    <div class="flex gap-2">
                        <button id="clearCanvas" class="px-3 py-1.5 bg-stealth-800 text-gray-300 rounded-lg text-xs hover:text-white"><i class="fa-solid fa-eraser mr-1"></i>Limpiar</button>
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
                    <div class="glass-panel p-3 rounded-xl space-y-2">
                        <span class="text-[11px] font-semibold text-gray-300 block">Guías de Dibujo</span>
                        <button onclick="loadTemplate('star')" class="w-full text-left p-2 rounded-lg bg-stealth-800 text-xs text-gray-300 hover:text-cyan-400">⭐ Estrella</button>
                        <button onclick="loadTemplate('cat')" class="w-full text-left p-2 rounded-lg bg-stealth-800 text-xs text-gray-300 hover:text-cyan-400">🐱 Cara de Gato</button>
                        <button onclick="loadTemplate('flag')" class="w-full text-left p-2 rounded-lg bg-stealth-800 text-xs text-gray-300 hover:text-cyan-400">🇫🇮 Cruz Finlandia</button>
                        <div class="pt-2 border-t border-stealth-border">
                            <label class="text-[10px] text-gray-400 block mb-1">Grosor de pincel:</label>
                            <input type="range" id="brushSize" min="1" max="20" value="3" class="w-full">
                        </div>
                    </div>
                    <div class="md:col-span-3 glass-panel p-2 rounded-xl flex items-center justify-center bg-slate-950">
                        <canvas id="paintCanvas" width="550" height="350" class="bg-stealth-900 rounded-lg border border-stealth-border cursor-crosshair"></canvas>
                    </div>
                </div>
            </div>
        </section>

        <section id="games-module" class="module-section flex-1 hidden p-6 overflow-y-auto">
            <div class="max-w-2xl mx-auto space-y-4 text-center">
                <div class="flex justify-center gap-3">
                    <button id="selectFlappy" class="px-4 py-2 bg-blue-600/30 border border-cyan-400 text-cyan-300 rounded-xl text-xs font-bold">Flappy Bird</button>
                    <button id="selectDino" class="px-4 py-2 bg-stealth-800 border border-stealth-border text-gray-400 rounded-xl text-xs font-bold">Dino Runner</button>
                </div>

                <div class="glass-panel p-3 rounded-2xl inline-block bg-black">
                    <canvas id="gameCanvas" width="400" height="400" class="border border-stealth-border rounded-xl"></canvas>
                </div>
                <p class="text-[11px] text-gray-400">Presiona <span class="font-mono text-cyan-400">ESPACIO</span> o haz <span class="font-mono text-cyan-400">CLIC</span> en la pantalla para saltar.</p>
            </div>
        </section>

    </main>

    <div id="settingsModal" class="hidden fixed inset-0 bg-black/80 backdrop-blur-sm z-50 flex items-center justify-center p-4">
        <div class="glass-panel w-full max-w-md p-6 rounded-2xl border-cyan-500/30 space-y-4">
            <h3 class="font-bold text-white text-sm"><i class="fa-solid fa-key text-cyan-400 mr-2"></i>Ajustes de Odi AI Key</h3>
            <p class="text-xs text-gray-400">Ingresa tu API Key para conectar Odi AI con respuesta ilimitada en tiempo real.</p>
            <input type="password" id="apiKeyInput" placeholder="AIzaSy..." class="w-full bg-stealth-800 border border-stealth-border rounded-xl p-2.5 text-xs text-white font-mono">
            <div class="flex justify-end gap-2">
                <button id="closeSettings" class="px-4 py-2 text-xs text-gray-400 hover:text-white">Cancelar</button>
                <button id="saveSettings" class="px-4 py-2 bg-blue-600 text-white font-bold rounded-xl text-xs">Guardar</button>
            </div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            let apiKey = localStorage.getItem('odi_ai_key') || '';
            updateApiUI();

            document.querySelectorAll('.nav-btn').forEach(btn => {
                btn.addEventListener('click', () => {
                    document.querySelectorAll('.nav-btn').forEach(b => {
                        b.classList.remove('bg-cyan-500/10', 'border-cyan-500/30', 'text-cyan-400');
                        b.classList.add('text-gray-400');
                    });
                    btn.classList.add('bg-cyan-500/10', 'border-cyan-500/30', 'text-cyan-400');
                    btn.classList.remove('text-gray-400');

                    document.querySelectorAll('.module-section').forEach(m => m.classList.add('hidden'));
                    document.getElementById(btn.dataset.target).classList.remove('hidden');

                    if(btn.dataset.target === 'games-module') startFlappy();
                });
            });

            document.getElementById('openSettings').onclick = () => document.getElementById('settingsModal').classList.remove('hidden');
            document.getElementById('closeSettings').onclick = () => document.getElementById('settingsModal').classList.add('hidden');
            document.getElementById('saveSettings').onclick = () => {
                apiKey = document.getElementById('apiKeyInput').value.trim();
                localStorage.setItem('odi_ai_key', apiKey);
                updateApiUI();
                document.getElementById('settingsModal').classList.add('hidden');
            };

            function updateApiUI() {
                const dot = document.getElementById('apiDot');
                const txt = document.getElementById('apiText');
                if(apiKey) {
                    dot.className = "w-2 h-2 rounded-full bg-emerald-400 shadow-sm shadow-emerald-400";
                    txt.textContent = "Odi AI Conectado";
                } else {
                    dot.className = "w-2 h-2 rounded-full bg-cyan-400 animate-pulse";
                    txt.textContent = "Odi Engine Local";
                }
            }

            const chatForm = document.getElementById('chatForm');
            const chatInput = document.getElementById('chatInput');
            const chatBox = document.getElementById('chatBox');

            chatForm.onsubmit = async (e) => {
                e.preventDefault();
                const text = chatInput.value.trim();
                if(!text) return;

                appendMsg('user', text);
                chatInput.value = '';

                if(apiKey) {
                    try {
                        const res = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${apiKey}`, {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({ 
                                system_instruction: { parts: [{ text: "Eres Odi AI, una inteligencia artificial creada con inspiración y tecnología avanzada de Finlandia. Responde de manera amable, precisa, eficiente y experta." }] },
                                contents: [{ parts: [{ text: text }] }] 
                            })
                        });
                        const data = await res.json();
                        const ans = data.candidates[0].content.parts[0].text;
                        appendMsg('bot', ans);
                    } catch(err) {
                        appendMsg('bot', '⚠️ Error en la conexión de Odi AI. Revisa tu API Key.');
                    }
                } else {
                    setTimeout(() => {
                        appendMsg('bot', `🇫🇮 **Odi AI:** Has consultado: "${text}". Para recibir análisis profundos y explicaciones en tiempo real, guarda tu API Key en la tuerca superior.`);
                    }, 500);
                }
            };

            function appendMsg(role, text) {
                const div = document.createElement('div');
                div.className = `flex gap-3 max-w-2xl ${role === 'user' ? 'ml-auto flex-row-reverse' : ''}`;
                div.innerHTML = `
                    <div class="w-8 h-8 rounded-lg ${role === 'user' ? 'bg-cyan-500/20 text-cyan-400' : 'bg-blue-600 text-white font-bold'} border border-current flex items-center justify-center shrink-0 text-xs">
                        ${role === 'user' ? '<i class="fa-solid fa-user"></i>' : '🇫🇮'}
                    </div>
                    <div class="glass-panel p-3.5 rounded-2xl ${role === 'user' ? 'rounded-tr-none' : 'rounded-tl-none'} text-xs leading-relaxed text-gray-200">
                        ${marked.parse(text)}
                    </div>
                `;
                chatBox.appendChild(div);
                chatBox.scrollTop = chatBox.scrollHeight;
            }

            document.getElementById('clearChat').onclick = () => chatBox.innerHTML = '';

            document.getElementById('calcMathBtn').onclick = () => {
                const expr = document.getElementById('mathInput').value;
                const card = document.getElementById('mathResultCard');
                const out = document.getElementById('mathOutput');

                try {
                    const clean = expr.replace(/sqrt/g, 'Math.sqrt')
                                     .replace(/sin/g, 'Math.sin')
                                     .replace(/cos/g, 'Math.cos')
                                     .replace(/tan/g, 'Math.tan')
                                     .replace(/pi/gi, 'Math.PI');
                    const res = Function(`'use strict'; return (${clean})`)();
                    out.textContent = res;
                    card.classList.remove('hidden');
                } catch(e) {
                    out.textContent = "Error de formato matemático";
                    card.classList.remove('hidden');
                }
            };

            const canvas = document.getElementById('paintCanvas');
            const ctx = canvas.getContext('2d');
            let drawing = false;

            canvas.onmousedown = () => drawing = true;
            canvas.onmouseup = () => { drawing = false; ctx.beginPath(); };
            canvas.onmousemove = draw;

            function draw(e) {
                if(!drawing) return;
                const rect = canvas.getBoundingClientRect();
                ctx.lineWidth = document.getElementById('brushSize').value;
                ctx.lineCap = 'round';
                ctx.strokeStyle = '#00d2ff';

                ctx.lineTo(e.clientX - rect.left, e.clientY - rect.top);
                ctx.stroke();
                ctx.beginPath();
                ctx.moveTo(e.clientX - rect.left, e.clientY - rect.top);
            }

            document.getElementById('clearCanvas').onclick = () => ctx.clearRect(0, 0, canvas.width, canvas.height);

            window.loadTemplate = (type) => {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                ctx.strokeStyle = '#1e3a8a';
                ctx.lineWidth = 2;
                ctx.beginPath();
                if(type === 'star') {
                    ctx.arc(275, 175, 80, 0, Math.PI * 2);
                } else if(type === 'cat') {
                    ctx.arc(275, 175, 60, 0, Math.PI * 2);
                } else if(type === 'flag') {
                    ctx.rect(175, 125, 200, 100);
                    ctx.moveTo(175, 175); ctx.lineTo(375, 175);
                    ctx.moveTo(235, 125); ctx.lineTo(235, 225);
                }
                ctx.stroke();
            };

            const gCanvas = document.getElementById('gameCanvas');
            const gCtx = gCanvas.getContext('2d');
            let gameLoopInt = null;

            document.getElementById('selectFlappy').onclick = () => startFlappy();
            document.getElementById('selectDino').onclick = () => startDino();

            function startFlappy() {
                clearInterval(gameLoopInt);
                let birdY = 200, velocity = 0, score = 0;
                let pipes = [];

                function loop() {
                    velocity += 0.4;
                    birdY += velocity;

                    if(Math.random() < 0.02) pipes.push({ x: 400, top: Math.random() * 150 + 50 });

                    gCtx.fillStyle = '#050a14';
                    gCtx.fillRect(0, 0, 400, 400);

                    gCtx.fillStyle = '#00d2ff';
                    gCtx.fillRect(80, birdY, 15, 15);

                    gCtx.fillStyle = '#002f6c';
                    pipes.forEach((p) => {
                        p.x -= 2;
                        gCtx.fillRect(p.x, 0, 30, p.top);
                        gCtx.fillRect(p.x, p.top + 100, 30, 400);

                        if(p.x === 80) score++;
                        if(p.x < 80 && p.x + 30 > 80 && (birdY < p.top || birdY > p.top + 100)) {
                            birdY = 200; velocity = 0; score = 0; pipes = [];
                        }
                    });

                    pipes = pipes.filter(p => p.x > -30);

                    gCtx.fillStyle = '#fff';
                    gCtx.font = '14px Fira Code';
                    gCtx.fillText(`Score: ${score}`, 15, 25);

                    if(birdY > 400) { birdY = 200; velocity = 0; }
                }

                document.onkeydown = (e) => { if(e.code === 'Space') velocity = -6; };
                gCanvas.onclick = () => velocity = -6;

                gameLoopInt = setInterval(loop, 1000/60);
            }

            function startDino() {
                clearInterval(gameLoopInt);
                let dinoY = 320, velocity = 0, isJumping = false, score = 0;
                let obstacles = [];

                function loop() {
                    if(isJumping) {
                        velocity += 0.6;
                        dinoY += velocity;
                        if(dinoY >= 320) { dinoY = 320; isJumping = false; }
                    }

                    if(Math.random() < 0.015) obstacles.push({ x: 400 });

                    gCtx.fillStyle = '#050a14';
                    gCtx.fillRect(0, 0, 400, 400);

                    gCtx.strokeStyle = '#1e3a8a';
                    gCtx.beginPath(); gCtx.moveTo(0, 340); gCtx.lineTo(400, 340); gCtx.stroke();

                    gCtx.fillStyle = '#00d2ff';
                    gCtx.fillRect(60, dinoY, 20, 20);

                    gCtx.fillStyle = '#002f6c';
                    obstacles.forEach((o) => {
                        o.x -= 3;
                        gCtx.fillRect(o.x, 320, 15, 20);

                        if(o.x < 80 && o.x + 15 > 60 && dinoY >= 300) { score = 0; obstacles = []; }
                    });

                    obstacles = obstacles.filter(o => o.x > -20);
                    score++;

                    gCtx.fillStyle = '#fff';
                    gCtx.font = '14px Fira Code';
                    gCtx.fillText(`Distance: ${Math.floor(score/10)}m`, 15, 25);
                }

                document.onkeydown = (e) => { if(e.code === 'Space' && !isJumping) { velocity = -10; isJumping = true; } };
                gCanvas.onclick = () => { if(!isJumping) { velocity = -10; isJumping = true; } };

                gameLoopInt = setInterval(loop, 1000/60);
            }
        });
    </script>
</body>
</html>
"""

components.html(html_app, height=920, scrolling=False)
