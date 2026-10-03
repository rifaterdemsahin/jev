import os
import re

new_nav = """    <!-- Shared Navigation -->
    <nav class="bg-indigo-800 text-white p-4 shadow-md sticky top-0 z-50 flex flex-col xl:flex-row justify-between items-center gap-4">
        <div class="flex flex-wrap gap-4 font-medium justify-center items-center text-sm">
            <a href="index.html" class="hover:text-indigo-300 transition">🏠 Arch</a>
            <a href="before-after.html" class="hover:text-indigo-300 transition">🔄 Before/After</a>
            <a href="prompt.html" class="hover:text-indigo-300 transition">🧠 Prompt</a>
            <a href="ollama.html" class="hover:text-indigo-300 transition">🦙 Ollama Intro</a>
            <a href="ollama-install.html" class="hover:text-indigo-300 transition">💻 Install Local</a>
            <a href="prepare.html" class="hover:text-indigo-300 transition">🛠️ System Prep</a>
            <a href="async.html" class="hover:text-indigo-300 transition">⚡ Async</a>
            <a href="cost.html" class="hover:text-indigo-300 transition">💰 Cost</a>
            <a href="eval.html" class="hover:text-indigo-300 transition">⚖️ Eval</a>
            <a href="frontier.html" class="hover:text-indigo-300 transition">🚀 Hybrid</a>
            <a href="hermes.html" class="hover:text-indigo-300 transition font-bold text-indigo-200 border-b-2 border-indigo-200">🤖 Hermes Bot</a>
        </div>
        <div class="relative">
            <input type="search" placeholder="Search pages..." class="px-4 py-1.5 rounded-full text-gray-900 focus:outline-none focus:ring-2 focus:ring-indigo-400 text-sm w-48 md:w-64">
            <span class="absolute right-3 top-1.5 text-gray-400">🔍</span>
        </div>
    </nav>"""

for f in os.listdir('.'):
    if f.endswith('.html'):
        with open(f, 'r') as file:
            content = file.read()
        
        # Regex to find existing nav
        pattern = r'    <!-- Shared Navigation -->\n    <nav class="bg-indigo-800 text-white.*?    </nav>'
        content = re.sub(pattern, new_nav, content, flags=re.DOTALL)
        
        with open(f, 'w') as file:
            file.write(content)
