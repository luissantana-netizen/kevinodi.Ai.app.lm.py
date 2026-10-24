<!DOCTYPE html>
<html lang="es" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Odi AI Studio - Finland Edition 🇫🇮</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Marked.js for Markdown Parsing -->
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        stealth: { 
                            950: '#030712',
                            900: '#050a14', 
                            800: '#0b132b', 
                            700: '#1c2541', 
                            border: '#1e3a8a' 
                        },
                        finland: { 
                            blue: '#002f6c', 
                            lightBlue: '#00418c',
                            white: '#ffffff', 
                            cyan: '#00d2ff',
                            cyanHover: '#33dcff'
                        }
                    },
                    fontFamily: { 
                        sans: ['Inter', 'sans-serif'], 
                        mono: ['Fira Code', 'monospace'] 
                    }
                }
            }
        }
    </script>

    <style>
        * {
            box-sizing: border-box;
            user-select: none;
        }
        body { 
            background-color: #050a14; 
            color: #e2e8f0; 
            font-family: 'Inter', sans-serif; 
            overflow: hidden; 
        }
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: #050a14; }
        ::-webkit-scrollbar-thumb { background: #1c2541; border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: #00d2ff; }
        
        .glass-panel { 
            background: rgba(11, 19, 43, 0.75); 
            backdrop-filter: blur(14px); 
            -webkit-backdrop-filter: blur(14px);
            border: 1px solid rgba(30, 58, 138, 0.4); 
        }
        
        .prose pre { 
            background-color: #030712 !important; 
            border: 1px solid #1e3a8a; 
            padding: 0.85rem; 
            border-radius: 0.75rem; 
            overflow-x: auto;
            margin-top: 0.5rem;
            margin-bottom: 0.5rem;
        }
        .prose code { 
            color: #00d2ff; 
            font-family: 'Fira Code', monospace; 
            font-size: 0.85rem;
        }
        .prose p {
            margin-bottom: 0.5rem;
            line-height: 1.5;
        }
        .prose p:last-child {
            margin-bottom: 0;
        }
        
        canvas { touch-action: none; }

        .nordic-glow {
            box-shadow: 0 0 25px -5px rgba(0, 210, 255, 0.25);
        }
        
        .active-tab {
            background: rgba(0, 210, 255, 0.12) !important;
            border-color: rgba(0, 210, 255, 0.4) !important;
            color: #00d2ff !important;
        }
    </style>
</head>
<body class="h-screen w-screen flex flex-col md:flex-row overflow-hidden bg-stealth-900 text-slate-200">

    <!-- MOBILE HEADER -->
    <div class="md:hidden flex items-center justify-between p-3 glass-panel border-b border-stealth-border z-50">
        <div class="flex items-center gap-2.5">
            <div class="w-8 h-8 rounded-lg bg-white flex items-center justify-center text-finland-blue font-bold shadow-md shadow-cyan-500/20 relative overflow-hidden border border-finland-blue">
                <div class="absolute inset-0 flex items-center justify-center">
                    <div class="w-full h-1.5 bg-finland-blue"></div>
                </div>
                <div class="absolute inset-0 flex items-center justify-center">
                    <div class="h-full w-1.5 bg-finland-blue"></div>
                </div>
                <span class="z-10 font-extrabold text-[10px] text-finland-blue bg-white px-0.5 rounded">ODI</span>
            </div>
            <span class="font-bold text-white text-sm tracking-wider">ODI AI 🇫🇮</span>
        </div>
        <button id="toggleMobileMenu" class="text-cyan-400 p-2 text-lg">
            <i class="fa-solid fa-bars"></i>
        </button>
    </div>

    <!-- NAVIGATION SIDEBAR -->
    <aside id="sidebar" class="fixed md:static inset-y-0 left-0 transform -translate-x-full md:translate-x-0 transition-transform duration-300 ease-in-out w-64 glass-panel border-r border-stealth-border flex flex-col justify-between z-40 shrink-0 bg-stealth-900 md:bg-transparent">
        <div>
            <!-- Header Branding -->
            <div class="p-4 border-b border-stealth-border flex items-center justify-between">
                <div class="flex items-center gap-3">
                    <!-- Finnish Flag Cross Logo -->
                    <div class="w-10 h-10 rounded-xl bg-white flex items-center justify-center text-finland-blue font-bold shadow-lg shadow-cyan-500/20 relative overflow-hidden border border-finland-blue shrink-0">
                        <div class="absolute inset-0 flex items-center justify-center">
                            <div class="w-full h-2.5 bg-finland-blue"></div>
                        </div>
                        <div class="absolute inset-0 flex items-center justify-center">
                            <div class="h-full w-2.5 bg-finland-blue"></div>
                        </div>
                        <span class="z-10 font-extrabold text-xs text-finland-blue bg-white px-1 rounded shadow-sm">ODI</span>
                    </div>
                    <div>
                        <h1 class="font-extrabold text-white text-base tracking-wider flex items-center gap-1.5">
                            ODI AI <span class="text-sm">🇫🇮</span>
                        </h1>
                        <p class="text-[10px] text-cyan-400 font-mono tracking-widest uppercase font-semibold">Suomi Studio 3.0</p>
                    </div>
                </div>
                <button id="openSettings" class="text-slate-400 hover:text-cyan-400 p-2 rounded-lg transition-colors">
                    <i class="fa-solid fa-gear text-base"></i>
                </button>
            </div>

            <!-- Navigation Modules -->
            <div class="p-3 space-y-2">
                <label class="text-[10px] font-mono text-slate-400 uppercase tracking-wider px-2 font-semibold">Módulos de Odi</label>
                
                <button data-target="chat-module" class="nav-btn active-tab w-full flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-xs font-semibold border border-transparent transition-all">
                    <i class="fa-solid fa-snowflake text-cyan-400 text-sm"></i> Asistente Odi & Tareas
                </button>
                
                <button data-target="math-module" class="nav-btn w-full flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-xs font-semibold text-slate-400 hover:bg-stealth-800/80 hover:text-white border border-transparent transition-all">
                    <i class="fa-solid fa-calculator text-blue-400 text-sm"></i> Fast-Math Engine
                </button>
                
                <button data-target="draw-module" class="nav-btn w-full flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-xs font-semibold text-slate-400 hover:bg-stealth-800/80 hover:text-white border border-transparent transition-all">
                    <i class="fa-solid fa-palette text-cyan-300 text-sm"></i> Estudio de Dibujo
                </button>
                
                <button data-target="games-module" class="nav-btn w-full flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-xs font-semibold text-slate-400 hover:bg-stealth-800/80 hover:text-white border border-transparent transition-all">
                    <i class="fa-solid fa-gamepad text-emerald-400 text-sm"></i> Minijuegos Arcade
                </button>
            </div>
        </div>

        <!-- Footer API Status -->
        <div class="p-3 border-t border-stealth-border">
            <div id="apiStatus" class="p-2.5 rounded-xl bg-stealth-950/80 border border-stealth-border flex items-center justify-between text-[11px]">
                <div class="flex items-center gap-2">
                    <span id="apiDot" class="w-2.5 h-2.5 rounded-full bg-cyan-400 animate-pulse"></span>
                    <span id="apiText" class="text-slate-300 font-medium">Odi Local Engine</span>
                </div>
                <i class="fa-solid fa-shield-halved text-cyan-400/60"></i>
            </div>
        </div>
    </aside>

    <!-- MAIN CONTENT AREA -->
    <main class="flex-1 bg-stealth-900 relative overflow-hidden flex flex-col h-full">

        <!-- 1. CHAT / AI MODULE -->
        <section id="chat-module" class="module-section flex-1 flex flex-col h-full">
            <div class="px-6 py-3.5 border-b border-stealth-border glass-panel flex justify-between items-center shrink-0">
                <div class="flex items-center gap-2">
                    <i class="fa-solid fa-robot text-cyan-400 text-sm"></i>
                    <span class="text-xs font-bold text-white tracking-wide">Asistente Inteligente Odi AI (Finlandia)</span>
                </div>
                <div class="flex items-center gap-3">
                    <span class="hidden sm:inline-block text-[10px] font-mono bg-cyan-950 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800/50">Nordic Intelligence</span>
                    <button id="clearChat" class="text-xs text-slate-400 hover:text-red-400 transition-colors flex items-center gap-1.5 px-2 py-1 rounded-lg hover:bg-red-500/10">
                        <i class="fa-solid fa-trash text-xs"></i> Limpiar
                    </button>
                </div>
            </div>

            <!-- Chat Message History -->
            <div id="chatBox" class="flex-1 overflow-y-auto p-4 sm:p-6 space-y-4">
                <div class="flex gap-3 max-w-2xl">
                    <div class="w-8 h-8 rounded-lg bg-finland-blue border border-white/20 flex items-center justify-center text-white shrink-0 font-extrabold text-xs shadow-md">
                        🇫🇮
                    </div>
                    <div class="glass-panel p-4 rounded-2xl rounded-tl-none text-xs leading-relaxed text-slate-200 prose">
                        ¡Moi! (¡Hola!) Soy <b>Odi AI</b>, tu asistente virtual con tecnología e inspiración nórdica de Finlandia. 🇫🇮<br><br>
                        Puedo ayudarte a resolver tareas escolares, explicar temas complicados paso a paso, escribir código, o responder cualquier duda. ¿En qué trabajamos hoy?
                    </div>
                </div>
            </div>

            <!-- Quick Suggestions -->
            <div class="px-4 py-2 border-t border-stealth-border/50 bg-stealth-950/40 flex gap-2 overflow-x-auto no-scrollbar">
                <button class="quick-prompt text-[11px] whitespace-nowrap bg-stealth-800/90 hover:bg-stealth-700 text-slate-300 hover:text-cyan-300 px-3 py-1.5 rounded-lg border border-stealth-border transition-all">
                    📚 Resolver problema de trigonometría
                </button>
                <button class="quick-prompt text-[11px] whitespace-nowrap bg-stealth-800/90 hover:bg-stealth-700 text-slate-300 hover:text-cyan-300 px-3 py-1.5 rounded-lg border border-stealth-border transition-all">
                    💻 Explicar bucles en JavaScript
                </button>
                <button class="quick-prompt text-[11px] whitespace-nowrap bg-stealth-800/90 hover:bg-stealth-700 text-slate-300 hover:text-cyan-300 px-3 py-1.5 rounded-lg border border-stealth-border transition-all">
                    🇫🇮 Cuéntame sobre la educación en Finlandia
                </button>
            </div>

            <!-- Input Bar -->
            <div class="p-4 glass-panel border-t border-stealth-border shrink-0">
                <form id="chatForm" class="flex gap-2 max-w-4xl mx-auto">
                    <input type="text" id="chatInput" placeholder="Escribe un mensaje o tarea para Odi AI..." class="flex-1 bg-stealth-950 border border-stealth-border rounded-xl px-4 py-3 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-cyan-400 transition-all font-sans">
                    <button type="submit" class="px-5 py-3 bg-gradient-to-r from-finland-blue to-cyan-500 hover:from-finland-lightBlue hover:to-cyan-400 text-white font-bold rounded-xl text-xs transition-all flex items-center gap-2 shadow-lg shadow-cyan-500/10">
                        <span>Enviar</span>
                        <i class="fa-solid fa-paper-plane text-xs"></i>
                    </button>
                </form>
            </div>
        </section>

        <!-- 2. FAST-MATH ENGINE -->
        <section id="math-module" class="module-section flex-1 hidden p-4 sm:p-6 overflow-y-auto">
            <div class="max-w-3xl mx-auto space-y-5">
                <div class="glass-panel p-5 rounded-2xl border-cyan-500/30">
                    <div class="flex items-center gap-3 mb-2">
                        <div class="w-9 h-9 rounded-xl bg-blue-600/20 border border-blue-500/40 flex items-center justify-center text-blue-400">
                            <i class="fa-solid fa-bolt text-lg"></i>
                        </div>
                        <div>
                            <h2 class="text-base font-bold text-white">Odi Fast-Math Engine</h2>
                            <p class="text-xs text-slate-400">Calculadora de procesamiento instantáneo (0ms latency) para álgebra, trigonometría y expresiones complejas.</p>
                        </div>
                    </div>
                </div>

                <div class="glass-panel p-5 rounded-2xl space-y-4">
                    <label class="text-xs font-semibold text-slate-300 block">Expresión Matemática:</label>
                    <div class="relative">
                        <textarea id="mathInput" rows="3" placeholder="Ejemplos:&#10;• (4444 * 3333) / 12 + sqrt(144)&#10;• sin(45) * cos(45) + pow(2, 8)" class="w-full bg-stealth-950 border border-stealth-border rounded-xl p-3.5 text-xs font-mono text-cyan-300 focus:outline-none focus:border-cyan-400 transition-all leading-relaxed resize-none"></textarea>
                    </div>
                    
                    <div class="flex flex-wrap gap-2 pt-1">
                        <button onclick="insertMath('sqrt(')" class="px-2.5 py-1.5 bg-stealth-800 hover:bg-stealth-700 text-slate-300 rounded-lg text-xs font-mono border border-stealth-border">sqrt()</button>
                        <button onclick="insertMath('sin(')" class="px-2.5 py-1.5 bg-stealth-800 hover:bg-stealth-700 text-slate-300 rounded-lg text-xs font-mono border border-stealth-border">sin()</button>
                        <button onclick="insertMath('cos(')" class="px-2.5 py-1.5 bg-stealth-800 hover:bg-stealth-700 text-slate-300 rounded-lg text-xs font-mono border border-stealth-border">cos()</button>
                        <button onclick="insertMath('tan(')" class="px-2.5 py-1.5 bg-stealth-800 hover:bg-stealth-700 text-slate-300 rounded-lg text-xs font-mono border border-stealth-border">tan()</button>
                        <button onclick="insertMath('pow(')" class="px-2.5 py-1.5 bg-stealth-800 hover:bg-stealth-700 text-slate-300 rounded-lg text-xs font-mono border border-stealth-border">pow(x,y)</button>
                        <button onclick="insertMath('PI')" class="px-2.5 py-1.5 bg-stealth-800 hover:bg-stealth-700 text-slate-300 rounded-lg text-xs font-mono border border-stealth-border">π (PI)</button>
                    </div>

                    <button id="calcMathBtn" class="w-full py-3 bg-gradient-to-r from-blue-600 to-cyan-600 hover:from-blue-500 hover:to-cyan-500 text-white font-bold rounded-xl text-xs flex items-center justify-center gap-2 shadow-lg shadow-cyan-500/10 transition-all">
                        <i class="fa-solid fa-calculator"></i> Calcular con Odi Engine
                    </button>
                </div>

                <div id="mathResultCard" class="hidden glass-panel p-5 rounded-2xl border-cyan-400/50 bg-cyan-950/10 transition-all">
                    <span class="text-[10px] font-mono text-cyan-400 uppercase tracking-widest font-bold block mb-1">Resultado Calculado:</span>
                    <div id="mathOutput" class="text-xl font-mono font-bold text-white break-all"></div>
                </div>
            </div>
        </section>

        <!-- 3. DRAW STUDIO MODULE -->
        <section id="draw-module" class="module-section flex-1 hidden p-4 sm:p-6 overflow-y-auto">
            <div class="max-w-5xl mx-auto space-y-4">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                    <div>
                        <h2 class="text-base font-bold text-white flex items-center gap-2">
                            <i class="fa-solid fa-palette text-cyan-400"></i> Estudio de Dibujo Odi
                        </h2>
                        <p class="text-xs text-slate-400">Dibuja en el lienzo digital o practica con las plantillas guiadas.</p>
                    </div>
                    <div class="flex gap-2">
                        <button id="clearCanvas" class="px-3 py-2 bg-stealth-800 hover:bg-stealth-700 text-slate-200 rounded-xl text-xs font-medium border border-stealth-border transition-colors flex items-center gap-1.5">
                            <i class="fa-solid fa-eraser text-red-400"></i> Limpiar Lienzo
                        </button>
                    </div>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-4 gap-4">
                    <!-- Controls Column -->
                    <div class="glass-panel p-4 rounded-2xl space-y-4 h-fit">
                        <div>
                            <span class="text-xs font-bold text-slate-200 block mb-2">Plantillas Guiadas</span>
                            <div class="space-y-1.5">
                                <button onclick="loadTemplate('star')" class="w-full text-left p-2.5 rounded-xl bg-stealth-950/80 hover:bg-stealth-800 text-xs text-slate-300 hover:text-cyan-300 border border-stealth-border/60 transition-all flex items-center gap-2">
                                    ⭐ Estrella Guiada
                                </button>
                                <button onclick="loadTemplate('cat')" class="w-full text-left p-2.5 rounded-xl bg-stealth-950/80 hover:bg-stealth-800 text-xs text-slate-300 hover:text-cyan-300 border border-stealth-border/60 transition-all flex items-center gap-2">
                                    🐱 Cara de Gato
                                </button>
                                <button onclick="loadTemplate('flag')" class="w-full text-left p-2.5 rounded-xl bg-stealth-950/80 hover:bg-stealth-800 text-xs text-slate-300 hover:text-cyan-300 border border-stealth-border/60 transition-all flex items-center gap-2">
                                    🇫🇮 Bandera de Finlandia
                                </button>
                                <button onclick="loadTemplate('car')" class="w-full text-left p-2.5 rounded-xl bg-stealth-950/80 hover:bg-stealth-800 text-xs text-slate-300 hover:text-cyan-300 border border-stealth-border/60 transition-all flex items-center gap-2">
                                    🚗 Auto Básico
                                </button>
                            </div>
                        </div>

                        <div class="pt-3 border-t border-stealth-border">
                            <label class="text-xs font-semibold text-slate-300 block mb-2">Grosor de Pincel: <span id="brushSizeVal" class="text-cyan-400 font-mono">4px</span></label>
                            <input type="range" id="brushSize" min="1" max="24" value="4" class="w-full accent-cyan-400">
                        </div>

                        <div class="pt-3 border-t border-stealth-border">
                            <label class="text-xs font-semibold text-slate-300 block mb-2">Color de Pincel</label>
                            <div class="flex gap-2">
                                <button onclick="setBrushColor('#00d2ff')" class="w-6 h-6 rounded-full bg-[#00d2ff] ring-2 ring-white/20"></button>
                                <button onclick="setBrushColor('#ffffff')" class="w-6 h-6 rounded-full bg-white ring-2 ring-white/20"></button>
                                <button onclick="setBrushColor('#3b82f6')" class="w-6 h-6 rounded-full bg-blue-500 ring-2 ring-white/20"></button>
                                <button onclick="setBrushColor('#10b981')" class="w-6 h-6 rounded-full bg-emerald-500 ring-2 ring-white/20"></button>
                                <button onclick="setBrushColor('#f43f5e')" class="w-6 h-6 rounded-full bg-rose-500 ring-2 ring-white/20"></button>
                            </div>
                        </div>
                    </div>

                    <!-- Canvas Box -->
                    <div class="lg:col-span-3 glass-panel p-3 rounded-2xl flex items-center justify-center bg-stealth-950 min-h-[380px]">
                        <canvas id="paintCanvas" width="600" height="400" class="w-full h-auto bg-stealth-900 rounded-xl border border-stealth-border cursor-crosshair max-w-full"></canvas>
                    </div>
                </div>
            </div>
        </section>

        <!-- 4. MINIGAMES ARCADE MODULE -->
        <section id="games-module" class="module-section flex-1 hidden p-4 sm:p-6 overflow-y-auto">
            <div class="max-w-2xl mx-auto space-y-4 text-center">
                <div class="glass-panel p-3 rounded-2xl inline-flex gap-2 border-stealth-border">
                    <button id="selectFlappy" class="px-5 py-2.5 bg-cyan-500/20 border border-cyan-400 text-cyan-300 rounded-xl text-xs font-bold transition-all">
                        <i class="fa-solid fa-crow mr-1.5"></i> Flappy Bird
                    </button>
                    <button id="selectDino" class="px-5 py-2.5 bg-stealth-800 border border-transparent text-slate-400 hover:text-white rounded-xl text-xs font-bold transition-all">
                        <i class="fa-solid fa-dragon mr-1.5"></i> Dino Runner
                    </button>
                </div>

                <div class="glass-panel p-3 rounded-2xl inline-block bg-black shadow-2xl relative">
                    <canvas id="gameCanvas" width="400" height="400" class="border border-stealth-border rounded-xl mx-auto bg-slate-950"></canvas>
                </div>

                <div class="p-3 glass-panel rounded-xl text-center max-w-sm mx-auto">
                    <p class="text-xs text-slate-300 font-medium">
                        Presiona <kbd class="px-2 py-1 bg-stealth-800 border border-stealth-border rounded text-cyan-300 font-mono text-[10px]">ESPACIO</kbd> o haz <kbd class="px-2 py-1 bg-stealth-800 border border-stealth-border rounded text-cyan-300 font-mono text-[10px]">CLIC</kbd> para saltar.
                    </p>
                </div>
            </div>
        </section>

    </main>

    <!-- SETTINGS MODAL -->
    <div id="settingsModal" class="hidden fixed inset-0 bg-black/80 backdrop-blur-md z-50 flex items-center justify-center p-4">
        <div class="glass-panel w-full max-w-md p-6 rounded-2xl border-cyan-500/30 space-y-5 shadow-2xl">
            <div class="flex items-center justify-between border-b border-stealth-border pb-3">
                <h3 class="font-bold text-white text-sm flex items-center gap-2">
                    <i class="fa-solid fa-key text-cyan-400"></i> Ajustes de Odi AI Key
                </h3>
                <button id="closeSettings" class="text-slate-400 hover:text-white"><i class="fa-solid fa-xmark"></i></button>
            </div>
            
            <p class="text-xs text-slate-300 leading-relaxed">
                Ingresa tu Gemini API Key para conectar **Odi AI** con respuesta extendida en tiempo real. Si no ingresas clave, Odi utilizará respuestas locales integradas.
            </p>
            
            <div class="space-y-1.5">
                <label class="text-[11px] font-semibold text-slate-300 block">API Key:</label>
                <input type="password" id="apiKeyInput" placeholder="AIzaSy..." class="w-full bg-stealth-950 border border-stealth-border rounded-xl p-3 text-xs text-white font-mono focus:outline-none focus:border-cyan-400">
            </div>

            <div class="flex justify-end gap-2 pt-2">
                <button id="cancelSettings" class="px-4 py-2.5 text-xs text-slate-400 hover:text-white rounded-xl">Cancelar</button>
                <button id="saveSettings" class="px-5 py-2.5 bg-gradient-to-r from-finland-blue to-cyan-500 text-white font-bold rounded-xl text-xs shadow-lg shadow-cyan-500/20">Guardar Cambios</button>
            </div>
        </div>
    </div>

    <!-- MAIN JAVASCRIPT LOGIC -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // STATE & CONFIG
            let apiKey = localStorage.getItem('odi_ai_key') || '';
            let currentColor = '#00d2ff';
            updateApiUI();

            // MOBILE MENU TOGGLE
            const sidebar = document.getElementById('sidebar');
            const toggleMobileMenuBtn = document.getElementById('toggleMobileMenu');
            toggleMobileMenuBtn.addEventListener('click', () => {
                sidebar.classList.toggle('-translate-x-full');
            });

            // MODULE NAVIGATION
            document.querySelectorAll('.nav-btn').forEach(btn => {
                btn.addEventListener('click', () => {
                    document.querySelectorAll('.nav-btn').forEach(b => {
                        b.classList.remove('active-tab');
                        b.classList.add('text-slate-400');
                    });
                    btn.classList.add('active-tab');
                    btn.classList.remove('text-slate-400');

                    document.querySelectorAll('.module-section').forEach(m => m.classList.add('hidden'));
                    const target = btn.dataset.target;
                    document.getElementById(target).classList.remove('hidden');

                    // Close mobile sidebar if open
                    sidebar.classList.add('-translate-x-full');

                    // Init game if selected
                    if (target === 'games-module') {
                        startFlappy();
                    }
                });
            });

            // SETTINGS MODAL HANDLERS
            const settingsModal = document.getElementById('settingsModal');
            document.getElementById('openSettings').onclick = () => settingsModal.classList.remove('hidden');
            document.getElementById('closeSettings').onclick = () => settingsModal.classList.add('hidden');
            document.getElementById('cancelSettings').onclick = () => settingsModal.classList.add('hidden');
            
            document.getElementById('saveSettings').onclick = () => {
                apiKey = document.getElementById('apiKeyInput').value.trim();
                localStorage.setItem('odi_ai_key', apiKey);
                updateApiUI();
                settingsModal.classList.add('hidden');
            };

            function updateApiUI() {
                const dot = document.getElementById('apiDot');
                const txt = document.getElementById('apiText');
                const input = document.getElementById('apiKeyInput');
                input.value = apiKey;

                if (apiKey) {
                    dot.className = "w-2.5 h-2.5 rounded-full bg-emerald-400 shadow-sm shadow-emerald-400";
                    txt.textContent = "Odi AI Conectado";
                } else {
                    dot.className = "w-2.5 h-2.5 rounded-full bg-cyan-400 animate-pulse";
                    txt.textContent = "Odi Local Engine";
                }
            }

            // CHAT ASSISTANT
            const chatForm = document.getElementById('chatForm');
            const chatInput = document.getElementById('chatInput');
            const chatBox = document.getElementById('chatBox');

            // Quick Prompt Buttons
            document.querySelectorAll('.quick-prompt').forEach(btn => {
                btn.addEventListener('click', () => {
                    chatInput.value = btn.innerText.replace(/^[^\s]+\s/, '');
                    chatForm.dispatchEvent(new Event('submit'));
                });
            });

            chatForm.onsubmit = async (e) => {
                e.preventDefault();
                const text = chatInput.value.trim();
                if(!text) return;

                appendMsg('user', text);
                chatInput.value = '';

                if (apiKey) {
                    // API Gemini Integration
                    try {
                        const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key=${apiKey}`, {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({ 
                                systemInstruction: { 
                                    parts: [{ text: "Eres Odi AI, una inteligencia artificial creada con tecnología avanzada de Finlandia. Eres experto en matemáticas, programación, resolución de tareas y explicaciones claras." }] 
                                },
                                contents: [{ parts: [{ text: text }] }] 
                            })
                        });
                        const data = await response.json();
                        const reply = data.candidates?.[0]?.content?.parts?.[0]?.text || 'No pude obtener una respuesta válida.';
                        appendMsg('bot', reply);
                    } catch(err) {
                        appendMsg('bot', '⚠️ Error de conexión con Odi AI. Verifica tu API Key en los Ajustes.');
                    }
                } else {
                    // Local Smart Fallback Responses
                    setTimeout(() => {
                        let localReply = "";
                        const lower = text.toLowerCase();

                        if (lower.includes('hola') || lower.includes('moi')) {
                            localReply = "¡Moi! ¿En qué puedo ayudarte hoy?";
                        } else if (lower.includes('finlandia') || lower.includes('suomi')) {
                            localReply = "Finlandia es famosa por su alto nivel educativo, tecnología avanzada e innovación. ¡Odi AI está inspirado en esa excelencia!";
                        } else if (lower.includes('trigonometria') || lower.includes('math') || lower.includes('matematica')) {
                            localReply = "Para cálculos instantáneos puedes usar nuestro módulo **Fast-Math Engine** en la barra lateral left.";
                        } else {
                            localReply = `🇫🇮 **Odi AI:** He procesado tu consulta: "${text}". Para respuestas avanzadas y extensas en tiempo real, puedes configurar tu Gemini API Key en el ícono de tuerca arriba.`;
                        }
                        appendMsg('bot', localReply);
                    }, 400);
                }
            };

            function appendMsg(role, text) {
                const div = document.createElement('div');
                div.className = `flex gap-3 max-w-2xl ${role === 'user' ? 'ml-auto flex-row-reverse' : ''}`;
                div.innerHTML = `
                    <div class="w-8 h-8 rounded-lg ${role === 'user' ? 'bg-cyan-500/20 text-cyan-300 border-cyan-400/40' : 'bg-finland-blue text-white font-extrabold'} border border-white/20 flex items-center justify-center shrink-0 text-xs shadow-md">
                        ${role === 'user' ? '<i class="fa-solid fa-user"></i>' : '🇫🇮'}
                    </div>
                    <div class="glass-panel p-3.5 sm:p-4 rounded-2xl ${role === 'user' ? 'rounded-tr-none' : 'rounded-tl-none'} text-xs leading-relaxed text-slate-200 prose">
                        ${marked.parse(text)}
                    </div>
                `;
                chatBox.appendChild(div);
                chatBox.scrollTop = chatBox.scrollHeight;
            }

            document.getElementById('clearChat').onclick = () => chatBox.innerHTML = '';

            // FAST-MATH ENGINE
            window.insertMath = (val) => {
                const input = document.getElementById('mathInput');
                input.value += val;
                input.focus();
            };

            document.getElementById('calcMathBtn').onclick = () => {
                const expr = document.getElementById('mathInput').value;
                const card = document.getElementById('mathResultCard');
                const out = document.getElementById('mathOutput');

                try {
                    const clean = expr.replace(/sqrt/g, 'Math.sqrt')
                                     .replace(/sin/g, 'Math.sin')
                                     .replace(/cos/g, 'Math.cos')
                                     .replace(/tan/g, 'Math.tan')
                                     .replace(/pow/g, 'Math.pow')
                                     .replace(/PI/g, 'Math.PI');
                    const result = Function(`'use strict'; return (${clean})`)();
                    out.textContent = result;
                    card.classList.remove('hidden');
                } catch(e) {
                    out.textContent = "Error de sintaxis matemática";
                    card.classList.remove('hidden');
                }
            };

            // DRAW STUDIO LOGIC
            const canvas = document.getElementById('paintCanvas');
            const ctx = canvas.getContext('2d');
            let isDrawing = false;

            const brushSizeInput = document.getElementById('brushSize');
            const brushSizeVal = document.getElementById('brushSizeVal');

            brushSizeInput.oninput = (e) => {
                brushSizeVal.textContent = `${e.target.value}px`;
            };

            window.setBrushColor = (color) => {
                currentColor = color;
            };

            canvas.onmousedown = (e) => {
                isDrawing = true;
                draw(e);
            };
            canvas.onmouseup = () => { isDrawing = false; ctx.beginPath(); };
            canvas.onmousemove = draw;

            canvas.ontouchstart = (e) => {
                isDrawing = true;
                drawTouch(e);
            };
            canvas.ontouchend = () => { isDrawing = false; ctx.beginPath(); };
            canvas.ontouchmove = drawTouch;

            function draw(e) {
                if(!isDrawing) return;
                const rect = canvas.getBoundingClientRect();
                ctx.lineWidth = brushSizeInput.value;
                ctx.lineCap = 'round';
                ctx.strokeStyle = currentColor;

                ctx.lineTo(e.clientX - rect.left, e.clientY - rect.top);
                ctx.stroke();
                ctx.beginPath();
                ctx.moveTo(e.clientX - rect.left, e.clientY - rect.top);
            }

            function drawTouch(e) {
                if(!isDrawing) return;
                const rect = canvas.getBoundingClientRect();
                const touch = e.touches[0];
                ctx.lineWidth = brushSizeInput.value;
                ctx.lineCap = 'round';
                ctx.strokeStyle = currentColor;

                ctx.lineTo(touch.clientX - rect.left, touch.clientY - rect.top);
                ctx.stroke();
                ctx.beginPath();
                ctx.moveTo(touch.clientX - rect.left, touch.clientY - rect.top);
            }

            document.getElementById('clearCanvas').onclick = () => ctx.clearRect(0, 0, canvas.width, canvas.height);

            window.loadTemplate = (type) => {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                ctx.strokeStyle = '#1e3a8a';
                ctx.lineWidth = 2;
                ctx.beginPath();

                if(type === 'star') {
                    ctx.arc(300, 200, 90, 0, Math.PI * 2);
                } else if(type === 'cat') {
                    ctx.arc(300, 200, 70, 0, Math.PI * 2);
                    // Ears
                    ctx.moveTo(240, 150); ctx.lineTo(220, 90); ctx.lineTo(270, 135);
                    ctx.moveTo(360, 150); ctx.lineTo(380, 90); ctx.lineTo(330, 135);
                } else if(type === 'flag') {
                    ctx.rect(180, 120, 240, 160);
                    ctx.moveTo(180, 180); ctx.lineTo(420, 180);
                    ctx.moveTo(260, 120); ctx.lineTo(260, 280);
                } else if(type === 'car') {
                    ctx.rect(180, 200, 240, 60);
                    ctx.rect(220, 150, 160, 50);
                    ctx.arc(230, 260, 20, 0, Math.PI * 2);
                    ctx.arc(370, 260, 20, 0, Math.PI * 2);
                }
                ctx.stroke();
            };

            // MINIGAMES ARCADE
            const gCanvas = document.getElementById('gameCanvas');
            const gCtx = gCanvas.getContext('2d');
            let gameLoopInt = null;

            const flappyBtn = document.getElementById('selectFlappy');
            const dinoBtn = document.getElementById('selectDino');

            flappyBtn.onclick = () => {
                flappyBtn.className = "px-5 py-2.5 bg-cyan-500/20 border border-cyan-400 text-cyan-300 rounded-xl text-xs font-bold transition-all";
                dinoBtn.className = "px-5 py-2.5 bg-stealth-800 border border-transparent text-slate-400 hover:text-white rounded-xl text-xs font-bold transition-all";
                startFlappy();
            };

            dinoBtn.onclick = () => {
                dinoBtn.className = "px-5 py-2.5 bg-cyan-500/20 border border-cyan-400 text-cyan-300 rounded-xl text-xs font-bold transition-all";
                flappyBtn.className = "px-5 py-2.5 bg-stealth-800 border border-transparent text-slate-400 hover:text-white rounded-xl text-xs font-bold transition-all";
                startDino();
            };

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

                    // Bird
                    gCtx.fillStyle = '#00d2ff';
                    gCtx.fillRect(80, birdY, 16, 16);

                    // Pipes
                    gCtx.fillStyle = '#002f6c';
                    pipes.forEach((p) => {
                        p.x -= 2;
                        gCtx.fillRect(p.x, 0, 32, p.top);
                        gCtx.fillRect(p.x, p.top + 110, 32, 400);

                        if(p.x === 80) score++;
                        if(p.x < 96 && p.x + 32 > 80 && (birdY < p.top || birdY > p.top + 110)) {
                            birdY = 200; velocity = 0; score = 0; pipes = [];
                        }
                    });

                    pipes = pipes.filter(p => p.x > -32);

                    gCtx.fillStyle = '#ffffff';
                    gCtx.font = '13px Fira Code';
                    gCtx.fillText(`Puntos: ${score}`, 15, 25);

                    if(birdY > 400 || birdY < 0) { birdY = 200; velocity = 0; }
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

                    gCtx.fillStyle = '#ffffff';
                    gCtx.font = '13px Fira Code';
                    gCtx.fillText(`Distancia: ${Math.floor(score/10)}m`, 15, 25);
                }

                document.onkeydown = (e) => { if(e.code === 'Space' && !isJumping) { velocity = -10; isJumping = true; } };
                gCanvas.onclick = () => { if(!isJumping) { velocity = -10; isJumping = true; } };

                gameLoopInt = setInterval(loop, 1000/60);
            }
        });
    </script>
</body>
</html>
