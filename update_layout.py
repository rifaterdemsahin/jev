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
        <div class="max-w-7xl mx-auto px-4 py-3 flex flex-col md:flex-row gap-4 md:gap-8 text-sm font-medium overflow-x-auto whitespace-nowrap">
            <!-- Theory -->
            <div class="flex items-center gap-4">
                <span class="text-indigo-400 text-xs uppercase tracking-widest font-bold">Theory</span>
                <a href="index.html" class="hover:text-white text-indigo-200 transition">🏠 Arch</a>
                <a href="before-after.html" class="hover:text-white text-indigo-200 transition">🔄 Before/After</a>
                <a href="eval.html" class="hover:text-white text-indigo-200 transition">⚖️ Eval</a>
                <a href="cost.html" class="hover:text-white text-indigo-200 transition">💰 Cost</a>
            </div>
            <!-- Setup -->
            <div class="flex items-center gap-4 md:border-l border-indigo-700 md:pl-8">
                <span class="text-indigo-400 text-xs uppercase tracking-widest font-bold">Setup</span>
                <a href="prepare.html" class="hover:text-white text-indigo-200 transition">🛠️ Prep</a>
                <a href="prompt.html" class="hover:text-white text-indigo-200 transition">🧠 Prompt</a>
                <a href="async.html" class="hover:text-white text-indigo-200 transition">⚡ Async</a>
            </div>
            <!-- Execution -->
            <div class="flex items-center gap-4 md:border-l border-indigo-700 md:pl-8">
                <span class="text-indigo-400 text-xs uppercase tracking-widest font-bold">Execution</span>
                <a href="ollama.html" class="hover:text-white text-indigo-200 transition">🦙 Ollama</a>
                <a href="ollama-install.html" class="hover:text-white text-indigo-200 transition">💻 Install</a>
                <a href="frontier.html" class="hover:text-white text-indigo-200 transition">🚀 Hybrid</a>
                <a href="hermes.html" class="hover:text-white text-indigo-200 transition">🤖 Hermes</a>
            </div>
        </div>
    </nav>"""

new_footer = """    <!-- Footer -->
    <footer class="bg-gray-900 text-gray-400 py-12 text-center mt-12 flex flex-col items-center gap-6 border-t border-gray-800">
        <div class="flex items-center gap-3 bg-gray-800 px-5 py-2.5 rounded-full shadow-inner border border-gray-700">
            <span class="flex h-3 w-3 relative">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
                <span class="relative inline-flex rounded-full h-3 w-3 bg-green-500"></span>
            </span>
            <span class="text-sm font-mono text-green-400 tracking-wide">Deployment Status: All Systems Operational</span>
        </div>
        <p class="text-sm">&copy; 2026 JEV Project. Building the ultimate Second Brain.</p>
        <a href="https://rifaterdemsahin.github.io/jev/" target="_blank" class="text-indigo-400 hover:text-white underline transition text-sm">View Live on GitHub Pages</a>
    </footer>"""

for f in os.listdir('.'):
    if f.endswith('.html'):
        with open(f, 'r') as file:
            content = file.read()
        
        # Replace nav (handle both with and without the comment just in case)
        if '<!-- Shared Navigation -->' in content:
            content = re.sub(r'    <!-- Shared Navigation -->\n    <nav.*?</nav>', new_nav, content, flags=re.DOTALL)
        else:
            content = re.sub(r'    <nav.*?</nav>', new_nav, content, flags=re.DOTALL)
            
        # Replace footer
        if '<!-- Footer -->' in content:
            content = re.sub(r'    <!-- Footer -->\n    <footer.*?</footer>', new_footer, content, flags=re.DOTALL)
        else:
            content = re.sub(r'    <footer.*?</footer>', new_footer, content, flags=re.DOTALL)
            
        with open(f, 'w') as file:
            file.write(content)
