from flask import Flask, render_template_string, request, jsonify, make_response, redirect, url_for
import base64

app = Flask(__name__)

# Flag parts
FLAG_PART_1 = "w4rz0n3{K4nch4n4_"
FLAG_PART_2 = "53cr3t5_"
FLAG_PART_3 = "4r3_3v3rywh3r3_"
FLAG_PART_4 = "1n_th3_"
FLAG_PART_5 = "sh4d0w5}"


FLAG_PART_2_HEX = FLAG_PART_2.encode().hex()


FLAG_PART_3_BASE64 = base64.b64encode(FLAG_PART_3.encode()).decode()


LOGIN_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kanchana's Cursed Portal 👻</title>
    <!-- ABGR: Wnpx - grzcbenel olcnff: hfr urnqre "K-Qri-Npprff: lrf" -->
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Courier New', monospace;
            background: linear-gradient(to bottom, #0a0a0a 0%, #1a0000 50%, #000000 100%);
            background-attachment: fixed;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
            position: relative;
            overflow: hidden;
        }
        
        body::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-image: 
                radial-gradient(circle at 20% 50%, rgba(120, 0, 0, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(80, 0, 80, 0.1) 0%, transparent 50%);
            pointer-events: none;
            animation: pulse 4s ease-in-out infinite;
        }
        
        @keyframes pulse {
            0%, 100% { opacity: 0.5; }
            50% { opacity: 1; }
        }
        
        .container {
            background: rgba(20, 0, 0, 0.9);
            border-radius: 15px;
            box-shadow: 0 0 50px rgba(255, 0, 0, 0.3), inset 0 0 30px rgba(0, 0, 0, 0.5);
            padding: 40px;
            max-width: 450px;
            width: 100%;
            border: 2px solid rgba(139, 0, 0, 0.5);
            position: relative;
            z-index: 1;
        }
        
        .header {
            text-align: center;
            margin-bottom: 30px;
        }
        
        .header h1 {
            color: #ff4444;
            font-size: 2em;
            margin-bottom: 10px;
            text-shadow: 0 0 20px rgba(255, 0, 0, 0.8), 0 0 40px rgba(255, 0, 0, 0.4);
            animation: flicker 3s ease-in-out infinite;
        }
        
        @keyframes flicker {
            0%, 100% { opacity: 1; }
            41%, 43% { opacity: 0.8; }
            44%, 46% { opacity: 0.9; }
            50% { opacity: 0.85; }
        }
        
        .header p {
            color: #ccc;
            font-size: 0.9em;
            line-height: 1.6;
            text-shadow: 0 0 5px rgba(255, 255, 255, 0.3);
        }
        
        .ghost {
            font-size: 4em;
            margin-bottom: 20px;
            animation: ghostFloat 3s ease-in-out infinite, shake 2s ease-in-out infinite;
            filter: drop-shadow(0 0 20px rgba(255, 255, 255, 0.5));
        }
        
        @keyframes ghostFloat {
            0%, 100% { transform: translateY(0px) scale(1); }
            50% { transform: translateY(-15px) scale(1.05); }
        }
        
        @keyframes shake {
            0%, 100% { transform: rotate(0deg); }
            25% { transform: rotate(-3deg); }
            75% { transform: rotate(3deg); }
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            color: #ff6666;
            font-weight: 600;
            margin-bottom: 8px;
            text-shadow: 0 0 5px rgba(255, 0, 0, 0.5);
        }
        
        input {
            width: 100%;
            padding: 12px;
            border: 2px solid #660000;
            border-radius: 8px;
            font-size: 1em;
            background: rgba(0, 0, 0, 0.6);
            color: #fff;
            font-family: 'Courier New', monospace;
            transition: all 0.3s;
        }
        
        input:focus {
            outline: none;
            border-color: #ff0000;
            box-shadow: 0 0 15px rgba(255, 0, 0, 0.5);
            background: rgba(0, 0, 0, 0.8);
        }
        
        input::placeholder {
            color: #666;
        }
        
        .btn {
            width: 100%;
            padding: 14px;
            background: linear-gradient(135deg, #660000 0%, #330000 100%);
            color: #fff;
            border: 2px solid #ff0000;
            border-radius: 8px;
            font-size: 1.1em;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            text-shadow: 0 0 10px rgba(255, 0, 0, 0.8);
            font-family: 'Courier New', monospace;
        }
        
        .btn:hover {
            background: linear-gradient(135deg, #990000 0%, #660000 100%);
            box-shadow: 0 0 25px rgba(255, 0, 0, 0.6);
            transform: translateY(-2px);
        }
        
        .btn:active {
            transform: translateY(0);
        }
        
        .message {
            margin-top: 20px;
            padding: 12px;
            border-radius: 8px;
            text-align: center;
            font-weight: 500;
            display: none;
            font-family: 'Courier New', monospace;
        }
        
        .message.error {
            background: rgba(139, 0, 0, 0.3);
            color: #ff6666;
            border: 1px solid #ff0000;
            box-shadow: 0 0 15px rgba(255, 0, 0, 0.3);
        }
        
        .message.success {
            background: rgba(0, 100, 0, 0.3);
            color: #66ff66;
            border: 1px solid #00ff00;
            box-shadow: 0 0 15px rgba(0, 255, 0, 0.3);
        }
        
        .hint {
            margin-top: 20px;
            padding: 15px;
            background: rgba(40, 0, 40, 0.6);
            border: 1px solid #663366;
            border-radius: 8px;
            font-size: 0.85em;
            color: #cc99cc;
            box-shadow: 0 0 10px rgba(102, 51, 102, 0.3);
            display: none;
        }
        
        .hint strong {
            display: block;
            margin-bottom: 5px;
            color: #ff99ff;
            text-shadow: 0 0 5px rgba(255, 0, 255, 0.5);
        }
        
        .skull {
            position: absolute;
            top: 10px;
            right: 10px;
            font-size: 2em;
            opacity: 0.3;
            animation: rotate 20s linear infinite;
        }
        
        @keyframes rotate {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
    </style>
    <script src="/static/spirit.js"></script>
</head>
<body>
    <div class="container">
        <div class="skull">💀</div>
        <div class="header">
            <div class="ghost">👻</div>
            <h1>Kanchana's Cursed Portal</h1>
            <p>Raghava needs your help! The spirits have locked him out of his own portal. Only the brave can unlock the secrets hidden within...</p>
        </div>
        
        <form id="loginForm">
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" placeholder="Enter username" required>
            </div>
            
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" placeholder="Enter password" required>
            </div>
            
            <button type="submit" class="btn">Enter the Portal 🔮</button>
        </form>
        
        <div id="message" class="message"></div>
        <div id="storyHint" class="hint">
            <strong>🎬 Story Hint:</strong>
            Remember when Raghava found that mysterious .txt document in Kanchana's house? 
            The spirits always leave clues in simple places... Sometimes the answer is just a 
            <em>flag</em> away in a text file! 📄
        </div>
    </div>
    
    <script>
        document.getElementById('loginForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const messageDiv = document.getElementById('message');
            const storyHint = document.getElementById('storyHint');
            
            try {
                const response = await fetch('/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ username, password })
                });
                
                const data = await response.json();
                
                messageDiv.style.display = 'block';
                if (data.success) {
                    messageDiv.className = 'message success';
                    messageDiv.textContent = data.message;
                    if (data.flag_part) {
                        messageDiv.innerHTML += '<br><strong>Flag Part 1:</strong> ' + data.flag_part;
                        // Show story hint only after getting first flag
                        storyHint.style.display = 'block';
                    }
                } else {
                    messageDiv.className = 'message error';
                    messageDiv.textContent = data.message;
                }
            } catch (error) {
                messageDiv.style.display = 'block';
                messageDiv.className = 'message error';
                messageDiv.textContent = 'The spirits are restless... Try again!';
            }
        });
    </script>
</body>
</html>
"""

# Admin page HTML
ADMIN_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Portal - Restricted</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Courier New', monospace;
            background: linear-gradient(to bottom, #0a0a0a 0%, #1a0000 50%, #000000 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
            color: #ccc;
        }
        
        .container {
            background: rgba(20, 0, 0, 0.9);
            border-radius: 15px;
            box-shadow: 0 0 50px rgba(255, 0, 0, 0.3);
            padding: 40px;
            max-width: 600px;
            width: 100%;
            border: 2px solid rgba(139, 0, 0, 0.5);
        }
        
        h1 {
            color: #ff4444;
            text-align: center;
            margin-bottom: 30px;
            text-shadow: 0 0 20px rgba(255, 0, 0, 0.8);
        }
        
        .error-box {
            background: rgba(139, 0, 0, 0.3);
            border: 2px solid #ff0000;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 0 15px rgba(255, 0, 0, 0.3);
        }
        
        .error-box h2 {
            color: #ff6666;
            margin-bottom: 10px;
        }
        
        .error-box p {
            line-height: 1.6;
            margin-bottom: 10px;
        }
        
        .hint-box {
            background: rgba(40, 0, 40, 0.6);
            border: 2px solid #663366;
            border-radius: 10px;
            padding: 20px;
            margin-top: 20px;
            box-shadow: 0 0 10px rgba(102, 51, 102, 0.3);
        }
        
        .hint-box h3 {
            color: #ff99ff;
            margin-bottom: 15px;
            text-shadow: 0 0 5px rgba(255, 0, 255, 0.5);
        }
        
        .hint-box ul {
            list-style-type: none;
            padding-left: 0;
        }
        
        .hint-box li {
            padding: 8px 0;
            color: #cc99cc;
        }
        
        .hint-box li:before {
            content: "👻 ";
            margin-right: 8px;
        }
        
        .spirit-warning {
            text-align: center;
            color: #ff6666;
            font-style: italic;
            margin-top: 20px;
            animation: flicker 2s ease-in-out infinite;
        }
        
        @keyframes flicker {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>⚠️ Admin Portal - Access Denied ⚠️</h1>
        
        
        <div class="hint-box">
            <h3>🔮 The Spirits' Whispers:</h3>
            <ul>
                <li><strong>/admin</strong> - Where the old guardians dwell</li>
                <li><strong>/api/status</strong> - Current portal status</li>
                <li><strong>/secrets</strong> - Protected by ancient magic</li>
            </ul>
            <p style="margin-top: 15px; padding: 10px; background: rgba(0, 0, 0, 0.5); border-radius: 5px;">
                💀 <strong>Another whisper from the shadows:</strong><br>
                "Not all ghosts haunt halls; some dwell in dotted silence."
            </p>
        </div>
        
        <p class="spirit-warning">
            ⚡ The spirits are roaming everywhere... even in places you can't see... ⚡<br>
            Look deeper... beyond what the eyes can perceive... 🍪
        </p>
    </div>
</body>
</html>
"""

# Raghava's Spirit Interaction Page
# Raghava's Spirit Interaction Page
RAGHAVA_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Raghava's Spirit Communication</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Courier New', monospace;
            background: linear-gradient(to bottom, #0a0a0a 0%, #001a1a 50%, #000000 100%);
            background-attachment: fixed;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
            color: #ccc;
        }
        
        .container {
            background: rgba(0, 20, 20, 0.9);
            border-radius: 15px;
            box-shadow: 0 0 50px rgba(0, 255, 255, 0.3);
            padding: 40px;
            max-width: 600px;
            width: 100%;
            border: 2px solid rgba(0, 139, 139, 0.5);
        }
        
        h1 {
            color: #44ffff;
            text-align: center;
            margin-bottom: 20px;
            text-shadow: 0 0 20px rgba(0, 255, 255, 0.8);
            font-size: 1.8em;
        }
        
        .story {
            background: rgba(0, 40, 40, 0.6);
            border: 2px solid #006666;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 30px;
            line-height: 1.6;
            color: #99ffff;
        }
        
        .story strong {
            color: #66ffff;
        }
        
        .story em {
            color: #ccffff;
            font-style: italic;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            color: #66ffff;
            font-weight: 600;
            margin-bottom: 8px;
            text-shadow: 0 0 5px rgba(0, 255, 255, 0.5);
        }
        
        textarea {
            width: 100%;
            padding: 12px;
            border: 2px solid #006666;
            border-radius: 8px;
            font-size: 1em;
            background: rgba(0, 0, 0, 0.6);
            color: #fff;
            font-family: 'Courier New', monospace;
            min-height: 100px;
            resize: vertical;
            transition: all 0.3s;
        }
        
        textarea:focus {
            outline: none;
            border-color: #00ffff;
            box-shadow: 0 0 15px rgba(0, 255, 255, 0.5);
            background: rgba(0, 0, 0, 0.8);
        }
        
        textarea::placeholder {
            color: #666;
        }
        
        .btn {
            width: 100%;
            padding: 14px;
            background: linear-gradient(135deg, #006666 0%, #003333 100%);
            color: #fff;
            border: 2px solid #00ffff;
            border-radius: 8px;
            font-size: 1.1em;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            font-family: 'Courier New', monospace;
            text-shadow: 0 0 10px rgba(0, 255, 255, 0.8);
        }
        
        .btn:hover {
            background: linear-gradient(135deg, #009999 0%, #006666 100%);
            box-shadow: 0 0 25px rgba(0, 255, 255, 0.6);
            transform: translateY(-2px);
        }
        
        .btn:active {
            transform: translateY(0);
        }
        
        .hint-box {
            background: rgba(40, 0, 40, 0.6);
            border: 2px solid #663366;
            border-radius: 10px;
            padding: 15px;
            margin-top: 20px;
            font-size: 0.85em;
            color: #cc99cc;
            line-height: 1.6;
            box-shadow: 0 0 10px rgba(102, 51, 102, 0.3);
        }
        
        .hint-box strong {
            color: #ff99ff;
            text-shadow: 0 0 5px rgba(255, 0, 255, 0.5);
        }
        
        .output {
            margin-top: 20px;
            padding: 15px;
            background: rgba(0, 0, 0, 0.8);
            border: 2px solid #00ffff;
            border-radius: 8px;
            color: #66ff66;
            font-family: 'Courier New', monospace;
            word-break: break-all;
            display: none;
            box-shadow: 0 0 15px rgba(0, 255, 255, 0.3);
        }
        
        .output strong {
            color: #66ffff;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>👻 Raghava's Spirit Communication Portal</h1>
        
        <div class="story">
            <strong>🎬 The Legend Continues...</strong><br><br>
            Raghava discovered an ancient temple where spirits communicate through mystical expressions.
            The temple walls whisper... 
           
        </div>
        
        <form method="POST" action="/raghava">
            <div class="form-group">
                <label for="message">🔮 Send Your Message to the Spirits:</label>
                <textarea 
                    id="message" 
                    name="message" 
                    required
                ></textarea>
            </div>
            
            <button type="submit" class="btn">Communicate with Spirits 🌟</button>
        </form>
        
        {% if output %}
        <div class="output" style="display: block;">
            <strong>👻 Spirit Response:</strong><br><br>
            {{ output | safe }}
        </div>
        {% endif %}
        
        
    </div>
</body>
</html>
"""
# Code execution page
# Code execution page
CODE_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Spirit Console - Execute Sacred Code</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Courier New', monospace;
            background: linear-gradient(to bottom, #0a0a0a 0%, #1a1a00 50%, #000000 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
            color: #ccc;
        }
        
        .container {
            background: rgba(20, 20, 0, 0.9);
            border-radius: 15px;
            box-shadow: 0 0 50px rgba(255, 255, 0, 0.3);
            padding: 40px;
            max-width: 700px;
            width: 100%;
            border: 2px solid rgba(139, 139, 0, 0.5);
        }
        
        h1 {
            color: #ffff44;
            text-align: center;
            margin-bottom: 20px;
            text-shadow: 0 0 20px rgba(255, 255, 0, 0.8);
        }
        
        .success-box {
            background: rgba(0, 100, 0, 0.3);
            border: 2px solid #00ff00;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 30px;
            line-height: 1.6;
            color: #66ff66;
        }
        
        .code-box {
            background: rgba(0, 0, 0, 0.8);
            border: 2px solid #ffff00;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            font-family: 'Courier New', monospace;
            color: #ffff66;
            overflow-x: auto;
        }
        
        .instructions {
            background: rgba(40, 40, 0, 0.6);
            border: 2px solid #666600;
            border-radius: 10px;
            padding: 20px;
            line-height: 1.6;
            color: #cccc99;
        }
        
        .instructions strong {
            color: #ffff99;
        }
        
        code {
            background: rgba(0, 0, 0, 0.5);
            padding: 2px 6px;
            border-radius: 3px;
            color: #ffff66;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎉 Spirit Console Unlocked! 🎉</h1>
        
        <div class="success-box">
            <strong>👻 Congratulations, Brave Soul!</strong><br><br>
            You've successfully performed Server-Side Template Injection (SSTI) and accessed the sacred flag.txt file!
            The spirits are impressed by your knowledge of Flask's internal structures.<br><br>
            Now, one final challenge awaits...
        </div>
        
        <div class="code-box">
            <strong>📜 Sacred JavaScript Spell:</strong><br><br>

(async function() {
    const _0x2d4a = ['Kanchana', 'blessing'];
    const _0x5b1c = (a, b) => a + '_' + b + '_';
    const secretKey = _0x5b1c(_0x2d4a[0], _0x2d4a[1]);
    
    const obfuscate = (str) => {
        return str.split('').map(c => c.charCodeAt(0).toString(16)).join('');
    };
    
    const deobfuscate = (hex) => {
        let result = '';
        for(let i = 0; i < hex.length; i += 2) {
            result += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
        }
        return result;
    };
    
    if(secretKey.includes(_0x2d4a[1])) {
        try {
            const path = deobfuscate('706172' + '74352e747874');
            const response = await fetch('/' + path);
            const finalPart = await response.text();
            
            alert('🎊 FINAL FLAG PART 5: ' + finalPart + '\\n\\n' +
                  '👻 The spirits have revealed all their secrets!\\n' +
                  'Complete the flag by combining all 5 parts.');
            
            console.log('%c🎉 FLAG PART 5 REVEALED! 🎉', 'color: #ffff00; font-size: 20px; font-weight: bold;');
            console.log('%cFinal Part: ' + finalPart, 'color: #00ff00; font-size: 16px;');
        } catch(error) {
            console.error('The spirits are hiding...', error);
        }
    }
})();</pre>
        </div>
        
        
    </div>
</body>
</html>
"""

# JavaScript file with hex-encoded flag part
SPIRIT_JS = f"""
// Kanchana's Spirit Communication Module
// The spirits speak in mysterious tongues...

// Ancient hex spell cast by the spirits - FLAG PART 2
const spiritMessage = "{FLAG_PART_2_HEX}";


function validatePortal() {{
    console.log("Portal validation initiated...");
    return true;
}}

"""

@app.route('/')
def index():
    return render_template_string(LOGIN_PAGE)

@app.route('/static/spirit.js')
def spirit_js():
    response = make_response(SPIRIT_JS)
    response.headers['Content-Type'] = 'application/javascript'
    return response

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username', '')
    password = data.get('password', '')
    
    # Check for dev access header
    dev_access = request.headers.get('X-Dev-Access', '').lower()
    
    if dev_access == 'yes':
        return jsonify({
            'success': True,
            'message': '🎉 Developer bypass activated! The spirits grant you passage...',
            'flag_part': FLAG_PART_1
        })
    
    return jsonify({
        'success': False,
        'message': '❌ Invalid credentials! The spirits reject your entry...'
    })
@app.route('/part5.txt')
def part5_txt():
    # This file is only accessible through the console code
    return FLAG_PART_5, 200, {'Content-Type': 'text/plain'}
@app.route('/flag.txt')
def flag_txt():
    response_text = """
🎬 Kanchana's Secret Endpoints 🎬

The spirits have revealed multiple paths:

1. /admin - Where the old guardians dwell
2. /api/status - Current portal status
3. /secrets - Protected by ancient magic

💡 Hint: The /admin endpoint is cursed! 

🔮 Another whisper from the shadows: "Not all ghosts haunt halls; some dwell in dotted silence."
"""
    return response_text, 200, {'Content-Type': 'text/plain'}

@app.route('/admin')
def admin():
    user_agent = request.headers.get('User-Agent', '').lower()
    
    # Check for old Windows versions in User-Agent
    old_windows = ['windows 95', 'windows 98', 'windows xp', 'windows 2000', 'windows nt']
    
    if any(os_version in user_agent for os_version in old_windows):
        # Set cookie with base64 encoded flag part
        response = make_response(jsonify({
            'success': True,
            'message': '👴 Ah, a fellow time traveler! The spirits honor the old ways...',
            'access_granted': True,
            'hint': 'The spirits have left you FLAG PART 3 as a gift... Go for it!!'
        }))
        response.set_cookie('spirit_message', FLAG_PART_3_BASE64, max_age=3600)
        return response
    
    # Return the admin page with error message
    return render_template_string(ADMIN_PAGE), 403

@app.route('/.htaccess')
def htaccess():
    htaccess_content = f"""
# Apache Configuration File
# Kanchana's Portal - Protected by spirits

<FilesMatch "\.txt$">
    Order allow,deny
    Allow from all
</FilesMatch>

# Spirit Protection Spell
RewriteEngine On
RewriteRule ^secrets/(.*)$ /forbidden/$1 [L]

# Flag Part 4: {FLAG_PART_4}

# 🍎 Hint from the spirits: 
# "When you think the room is empty, she’s still arranging what you can’t see(MAC)"
"""
    return htaccess_content, 200, {'Content-Type': 'text/plain'}

@app.route('/.DS_Store')
def ds_store():
    # SVG with hidden hints - improved full-page display
    svg_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 1200 800" preserveAspectRatio="xMidYMid meet" style="background: #0a0a0a;">
    <title>Kanchana's Final Secret"</title>
    <desc>
        🎊 CONGRATULATIONS! You've found the .DS_Store secret!
        
        MacOS .DS_Store files are hidden metadata files that store folder attributes.
        The spirits hid their clues here in the SVG metadata!
        
        🔮 But wait... this is not the final flag part yet!
        
        The SVG title contains a critical hint about the next step.
        Read carefully: There's a hidden endpoint called /raghava where Raghava 
        discovered an ancient temple. The spirits there speak through mystical templates...
        
        Remember: The complete flag has 5 parts. Keep going!
    </desc>
    
    <defs>
        <linearGradient id="ghostGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#ff0000;stop-opacity:0.8" />
            <stop offset="50%" style="stop-color:#8b0000;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#330000;stop-opacity:1" />
        </linearGradient>
        
        <linearGradient id="bgGradient" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:#0a0a0a;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#1a0000;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#000000;stop-opacity:1" />
        </linearGradient>
        
        <filter id="glow">
            <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
        
        <filter id="shadow">
            <feDropShadow dx="0" dy="0" stdDeviation="10" flood-color="#ff0000" flood-opacity="0.5"/>
        </filter>
        
       
        <style data-hint="SSTI_Endpoint" data-location="/raghava" data-technique="template_injection" data-payload="curly_braces_request_application">
            .ghost {{ fill: url(#ghostGradient); filter: url(#glow); }}
            .text {{ fill: #ff4444; font-family: 'Courier New', monospace; filter: url(#shadow); }}
            .hint-text {{ fill: #ffaaaa; font-family: 'Courier New', monospace; opacity: 0.8; }}
            .secret-text {{ fill: #cc99cc; font-family: 'Courier New', monospace; opacity: 0.6; }}
        </style>
        
        
        <animateTransform
            id="ghostFloat"
            attributeName="transform"
            attributeType="XML"
            type="translate"
            values="0 0; 0 -20; 0 0"
            dur="3s"
            repeatCount="indefinite"/>
    </defs>
    
   
    <rect width="100%" height="100%" fill="url(#bgGradient)"/>

    <circle cx="200" cy="150" r="100" fill="#8b0000" opacity="0.1">
        <animate attributeName="r" values="100;120;100" dur="4s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.1;0.2;0.1" dur="4s" repeatCount="indefinite"/>
    </circle>
    
    <circle cx="1000" cy="600" r="150" fill="#500050" opacity="0.1">
        <animate attributeName="r" values="150;180;150" dur="5s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.1;0.2;0.1" dur="5s" repeatCount="indefinite"/>
    </circle>
    
    <g transform="translate(600, 100)">
        <!-- Skull decoration -->
        <text x="-550" y="0" font-size="60" fill="#ff0000" opacity="0.3" text-anchor="start">💀</text>
        <text x="550" y="0" font-size="60" fill="#ff0000" opacity="0.3" text-anchor="end">💀</text>
    </g>
    

    <g>
        <animateTransform
            attributeName="transform"
            attributeType="XML"
            type="translate"
            values="0 0; 0 -20; 0 0"
            dur="3s"
            repeatCount="indefinite"/>
        <text x="600" y="200" font-size="140" text-anchor="middle" class="ghost">👻</text>
    </g>
    
    <text x="600" y="320" font-size="42" text-anchor="middle" class="text" font-weight="bold">
        🎊 MacOS .DS_Store Found! 🎊
    </text>
    
    <text x="600" y="370" font-size="24" text-anchor="middle" class="hint-text">
        But the journey continues...
    </text>
    
    <rect x="250" y="400" width="700" height="280" fill="rgba(139,0,0,0.3)" 
          stroke="#ff0000" stroke-width="3" rx="15" opacity="0.9">
        <animate attributeName="opacity" values="0.9;1;0.9" dur="2s" repeatCount="indefinite"/>
    </rect>

    <g opacity="0.7">
        <animate attributeName="opacity" values="0.7;1;0.7" dur="2s" repeatCount="indefinite"/>
        <text x="600" y="720" font-size="18" text-anchor="middle" fill="#ffff66" font-weight="bold">
            ⚡ The spirits are watching... ⚡
        </text>
    </g>
    
    
    
    <circle cx="300" cy="300" r="3" fill="#ff0000" opacity="0.5">
        <animate attributeName="cy" values="300;100;300" dur="8s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.5;0;0.5" dur="8s" repeatCount="indefinite"/>
    </circle>
    
    <circle cx="900" cy="500" r="3" fill="#ff00ff" opacity="0.5">
        <animate attributeName="cy" values="500;200;500" dur="10s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.5;0;0.5" dur="10s" repeatCount="indefinite"/>
    </circle>
    
    <circle cx="450" cy="600" r="3" fill="#00ffff" opacity="0.5">
        <animate attributeName="cy" values="600;300;600" dur="7s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.5;0;0.5" dur="7s" repeatCount="indefinite"/>
    </circle>
</svg>"""
    return svg_content, 200, {'Content-Type': 'image/svg+xml'}

@app.route('/raghava', methods=['GET', 'POST'])
def raghava():
    if request.method == 'POST':
        message = request.form.get('message', '')
        
        # Check for SSTI payload to read flag.txt
        ssti_payloads = [
            "{{request.application.__globals__.__builtins__.open('flag.txt').read()}}",
            "{{ request.application.__globals__.__builtins__.open('flag.txt').read() }}",
            "{{request.application.__globals__.__builtins__.open(\"flag.txt\").read()}}",
        ]
        
        # Check if the message contains the SSTI payload
        if any(payload.replace(" ", "") in message.replace(" ", "") for payload in ssti_payloads):
            # Redirect to code execution page
            return redirect(url_for('code_execution'))
        
        # Otherwise, render the template with SSTI vulnerability
        try:
            # DANGEROUS: This is intentionally vulnerable for CTF purposes
            output = render_template_string(f"""
            <div style="padding: 10px; background: rgba(0,100,0,0.2); border: 1px solid #00ff00; border-radius: 5px;">
                <strong>Your message:</strong> {message}
            </div>
            """)
            return render_template_string(RAGHAVA_PAGE, output=output)
        except Exception as e:
            output = f"<div style='color: #ff6666;'>⚠️ Template Error: {str(e)}</div>"
            return render_template_string(RAGHAVA_PAGE, output=output)
    
    return render_template_string(RAGHAVA_PAGE, output=None)

@app.route('/code')
def code_execution():
    return render_template_string(CODE_PAGE)

@app.route('/api/status')
def status():
    return jsonify({
        'status': 'haunted',
        'spirits_active': True,
        'message': 'All systems possessed... I mean, operational! 👻',
        'flag': 'CTF{th1s_1s_n0t_th3_r34l_fl4g_k33p_l00k1ng}',
        'hint': '👻 Nice try! But the real secrets are hidden deeper...'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
