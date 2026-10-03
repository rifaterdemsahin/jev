import os
import re

new_nav = """    <!-- Shared Navigation -->
    <nav class="bg-indigo-900 text-white shadow-md sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 py-3 flex flex-wrap justify-between items-center border-b border-indigo-800 gap-4">
            <div class="font-bold text-xl tracking-wide text-indigo-100 flex items-center gap-2">
                <span class="text-2xl">🧠</span> JEV <span class="font-light opacity-70 text-sm hidden sm:inline">Second Brain</span>
            </div>
            <div class="relative w-full sm:w-auto">
                <input type="search" placeholder="Search pages..." class="w-full sm:w-64 px-4 py-1.5 rounded-full text-gray-900 focus:outline-none focus:ring-2 focus:ring-indigo-400 text-sm shadow-inner">
                <span class="absolute right-3 top-1.5 text-gray-400">🔍</span>
            </div>
        </div>
        <div class="max-w-7xl mx-auto px-4 py-3 flex flex-col md:flex-row gap-4 md:gap-8 text-sm font-medium overflow-x-auto whitespace-nowrap scrollbar-hide">
            <!-- Theory -->
            <div class="flex items-center gap-4">
                <span class="text-indigo-400 text-xs uppercase tracking-widest font-bold">Theory</span>
                <a href="index.html" class="hover:text-white text-indigo-200 transition">🏠 Arch</a>
                <a href="shines.html" class="hover:text-white text-indigo-200 transition">✨ Shines</a>
                <a href="before-after.html" class="hover:text-white text-indigo-200 transition">🔄 Before/After</a>
                <a href="cost.html" class="hover:text-white text-indigo-200 transition">💰 Cost</a>
                <a href="eval.html" class="hover:text-white text-indigo-200 transition">⚖️ Eval</a>
                <a href="performance.html" class="hover:text-white text-indigo-200 transition">⚡ Perf</a>
            </div>
            <!-- Setup -->
            <div class="flex items-center gap-4 md:border-l border-indigo-700 md:pl-8">
                <span class="text-indigo-400 text-xs uppercase tracking-widest font-bold">Setup</span>
                <a href="prepare.html" class="hover:text-white text-indigo-200 transition">🛠️ Prep</a>
                <a href="prompt.html" class="hover:text-white text-indigo-200 transition">🧠 Prompt</a>
                <a href="async.html" class="hover:text-white text-indigo-200 transition">⚡ Async</a>
            </div>
            <!-- Local Mac -->
            <div class="flex items-center gap-4 md:border-l border-indigo-700 md:pl-8">
                <span class="text-indigo-400 text-xs uppercase tracking-widest font-bold">Local</span>
                <a href="ollama.html" class="hover:text-white text-indigo-200 transition">🦙 Ollama</a>
                <a href="macos.html" class="hover:text-white text-indigo-200 transition">🍎 macOS Install</a>
            </div>
            <!-- Agents -->
            <div class="flex items-center gap-4 md:border-l border-indigo-700 md:pl-8">
                <span class="text-indigo-400 text-xs uppercase tracking-widest font-bold">Agents</span>
                <a href="frontier.html" class="hover:text-white text-indigo-200 transition">🚀 Hybrid</a>
                <a href="hermes.html" class="hover:text-white text-indigo-200 transition">🤖 Hermes</a>
            </div>
        </div>
    </nav>"""

for f in os.listdir('.'):
    if f.endswith('.html'):
        with open(f, 'r') as file:
            content = file.read()
        
        # Replace nav
        content = re.sub(r'    <!-- Shared Navigation -->\n    <nav.*?</nav>', new_nav, content, flags=re.DOTALL)
        
        # Replace old ollama-install.html link if it somehow snuck in
        content = content.replace('ollama-install.html', 'macos.html')
            
        with open(f, 'w') as file:
            file.write(content)

# Rename ollama-install.html to macos.html
if os.path.exists('ollama-install.html'):
    os.rename('ollama-install.html', 'macos.html')

