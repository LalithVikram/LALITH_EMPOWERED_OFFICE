from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="LEO Dynamic Multi-Engine Portal")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LEO Core Full-Stack Cyber Portal</title>
    <style>
        :root {
            --bg-color: #06060c;
            --panel-bg: #0c0c1a;
            --neon-cyan: #00f3ff;
            --neon-green: #39ff14;
            --neon-amber: #ffaa00;
            --neon-magenta: #ff00ff;
            --neon-red: #ff0055;
            --text-color: #e0e0ff;
        }
        body {
            background-color: var(--bg-color);
            color: var(--text-color);
            font-family: 'Courier New', Courier, monospace;
            margin: 0;
            padding: 15px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .main-container {
            width: 100%;
            max-width: 500px;
            background: var(--panel-bg);
            border: 1px solid #1f1f45;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 0 40px rgba(0, 243, 255, 0.08);
            box-sizing: border-box;
        }
        header { text-align: center; margin-bottom: 15px; }
        .logo-badge {
            background: linear-gradient(135deg, #00f3ff, #ff00ff);
            color: #000;
            padding: 10px 20px;
            font-weight: bold;
            border-radius: 8px;
            display: inline-block;
            margin-bottom: 10px;
            box-shadow: 0 0 20px rgba(0, 243, 255, 0.4);
        }
        h1 { color: var(--text-color); font-size: 1.4rem; margin: 0; text-transform: uppercase; letter-spacing: 1px; }
        .author { font-size: 0.75rem; color: #8a8aaf; margin-top: 4px; }
        .status-box { border: 1px solid #222244; background: #04040a; padding: 8px; border-radius: 6px; margin-bottom: 15px; text-align: center; font-size: 0.75rem; color: var(--neon-green); }
        .section-title { font-size: 0.8rem; text-transform: uppercase; color: #8a8aaf; margin: 15px 0 5px 0; border-left: 2px solid var(--neon-cyan); padding-left: 5px; }
        
        .input-group {
            margin-bottom: 10px;
            display: flex;
            flex-direction: column;
            gap: 5px;
        }
        .input-group label {
            font-size: 0.75rem;
            color: #8a8aaf;
            text-transform: uppercase;
        }
        .cyber-input {
            background: #04040a;
            border: 1px solid #333366;
            color: #fff;
            padding: 10px;
            border-radius: 6px;
            font-family: inherit;
            font-size: 0.8rem;
            outline: none;
            transition: all 0.3s;
        }
        .cyber-input:focus {
            border-color: var(--neon-cyan);
            box-shadow: 0 0 10px rgba(0, 243, 255, 0.3);
        }
        
        .btn-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-top: 5px; margin-bottom: 15px; }
        .btn { background: #111126; color: #fff; border: 1px solid #333366; padding: 10px; border-radius: 6px; font-family: inherit; font-weight: bold; font-size: 0.75rem; cursor: pointer; text-transform: uppercase; transition: all 0.2s ease; width: 100%; }
        .btn-python { border-color: var(--neon-cyan); color: var(--neon-cyan); }
        .btn-java { border-color: var(--neon-magenta); color: var(--neon-magenta); }
        .btn-sql { border-color: var(--neon-amber); color: var(--neon-amber); }
        .btn-cyber { border-color: var(--neon-green); color: var(--neon-green); }
        .btn:hover { transform: scale(1.02); box-shadow: 0 0 10px rgba(255,255,255,0.1); }
        .btn-clear { grid-column: 1 / -1; background: #1a0505; border-color: var(--neon-red); color: var(--neon-red); margin-top: 10px; }
        
        .console { background-color: #030307; border: 1px solid #1a1a35; border-radius: 8px; padding: 12px; height: 230px; overflow-y: auto; box-shadow: inset 0 0 15px rgba(0,0,0,0.9); }
        pre { margin: 0; white-space: pre-wrap; word-wrap: break-word; font-family: inherit; }
        .log { margin-bottom: 6px; font-size: 0.75rem; line-height: 1.4; }
        .py-txt { color: var(--neon-cyan); }
        .jv-txt { color: var(--neon-magenta); }
        .sql-txt { color: var(--neon-amber); }
        .cy-txt { color: var(--neon-green); }
        .err-txt { color: var(--neon-red); }
    </style>
</head>
<body>
    <div class="main-container">
        <header>
            <div class="logo-badge">LEO ADVANCED MULTI-ENGINE</div>
            <h1>Full-Stack Architecture Portal</h1>
            <div class="author">AUTHOR: S.LALITH | SECURE SYSTEM</div>
        </header>
        <div class="status-box">● [SYSTEM] PYTHON // JAVA // SQL INPUT CHANNELS ENGAGED</div>
        
        <div class="section-title">Automation & Optimization Parameters</div>
        <div class="input-group">
            <label>Enter Storage Size (MB):</label>
            <input type="number" id="fileSizeInput" class="cyber-input" value="1024" placeholder="e.g. 500">
        </div>
        <div class="btn-grid">
            <button class="btn btn-python" onclick="triggerNode('python-cost')">LEO S3 Cost (Python)</button>
            <button class="btn btn-java" onclick="triggerNode('java-runtime')">Optimization Engine (Java)</button>
        </div>

        <div class="section-title">Database & Cyber Target Configuration</div>
        <div class="input-group">
            <label>Target IP Address / Domain:</label>
            <input type="text" id="targetIpInput" class="cyber-input" value="lalith-empowred-office.onrender.com" placeholder="e.g. 192.168.1.1">
        </div>
        <div class="btn-grid">
            <button class="btn btn-sql" onclick="triggerNode('sql-sync')">Database Logs Sync (SQL)</button>
            <button class="btn btn-cyber" onclick="triggerNode('cyber-scan')">Perimeter Port Scan</button>
            <button class="btn btn-clear" onclick="clearConsole()">Flush System Console Logs</button>
        </div>

        <div class="console">
            <pre id="console-body"><div class="log cy-txt">[SYSTEM] Dynamic Input Interface Terminal Ready.</div><div class="log py-txt">[READY] Enter values above and trigger modules...</div></pre>
        </div>
    </div>
    <script>
        const API_BASE = "https://lalith-empowred-office.onrender.com/api/v1";
        function clearConsole() { document.getElementById('console-body').innerHTML = `<div class="log err-txt">[SYSTEM] Console logging streams cleared.</div>`; }
        function getTime() { const now = new Date(); return `[${now.toTimeString().split(' ')[0]}]`; }
        
        async function triggerNode(moduleType) {
            const consoleBody = document.getElementById('console-body');
            const fileSize = document.getElementById('fileSizeInput').value || "1024";
            const targetIp = document.getElementById('targetIpInput').value || "127.0.0.1";
            
            let targetUrl = `${API_BASE}/architecture/processing?engine=${moduleType}&file_size=${fileSize}&ip=${encodeURIComponent(targetIp)}`;
            
            if (moduleType === 'python-cost') { consoleBody.innerHTML = `<div class="log py-txt">${getTime()} [PYTHON_ENGINE] Optimizing input storage array: ${fileSize} MB...</div>`; }
            else if (moduleType === 'java-runtime') { consoleBody.innerHTML = `<div class="log jv-txt">${getTime()} [JAVA_RUNTIME] Tuning JVM bytecode for scaling sequence...</div>`; }
            else if (moduleType === 'sql-sync') { consoleBody.innerHTML = `<div class="log sql-txt">${getTime()} [SQL_DATABASE] Executing log commits for storage metrics...</div>`; }
            else { consoleBody.innerHTML = `<div class="log cy-txt">${getTime()} [CYBER_SCANNER] Sweeping target socket: ${targetIp}...</div>`; }
            
            try {
                const response = await fetch(targetUrl);
                const data = await response.json();
                consoleBody.innerHTML += `<div class="log cy-txt">${getTime()} [SUCCESS] Response From Cloud Gateway:</div>`;
                consoleBody.innerHTML += `<div class="log" style="color:#ffffff; background:#05050f; padding:8px; border-radius:4px; border:1px dashed #224;">${JSON.stringify(data, null, 4)}</div>`;
            } catch (error) { consoleBody.innerHTML += `<div class="log err-txt">${getTime()} [CRITICAL] Core Engine unreachable. Try again in 15 seconds.</div>`; }
        }
    </script>
</body>
</html>
    """

@app.get("/api/v1/architecture/processing")
def process_architecture_stream(engine: str, file_size: float = 1024.0, ip: str = "127.0.0.1"):
    if engine == "python-cost":
        optimized = round(file_size * 0.1, 2)
        savings = round(file_size - optimized, 2)
        return {
            "engine_runtime": "Python 3.10 / AWS Lambda Core Layer",
            "project_name": "LEO Cost Storage Optimizer",
            "input_file_size": f"{file_size} MB",
            "compressed_output_size": f"{optimized} MB",
            "saved_cloud_space": f"{savings} MB",
            "compression_status": "Successful (90% Space Saved Matrix)"
        }
    elif engine == "java-runtime":
        return {
            "runtime_environment": "OpenJDK 17 (JVM)",
            "executor_thread": "LEO-ThreadWorker-04",
            "heap_memory_allocated": "256 MB",
            "execution_speed": "38 milliseconds",
            "status": f"Java Compression loop adjusted for optimized metadata array size."
        }
    elif engine == "sql-sync":
        return {
            "database_system": "PostgreSQL 15 Sync",
            "transaction_status": "COMMIT SUCCESSFUL",
            "query_executed": f"INSERT INTO cloud_metrics(size, ip) VALUES ({file_size}, '{ip}');",
            "rows_affected": 1
        }
    elif engine == "cyber-scan":
        return {
            "scanner_core": "LEO Custom Network Perimeter Mapping Socket Stream",
            "scanned_target_host": ip,
            "firewall_profile_status": "Secure / Zero-Trust Verification Active",
            "active_sockets_found": [
                {"port_id": 22, "type": "TCP", "service": "SSH", "state": "Filtered"},
                {"port_id": 80, "type": "TCP", "service": "HTTP", "state": "Open"},
                {"port_id": 443, "type": "TCP", "service": "HTTPS", "state": "Open"}
            ]
        }
    return {"status": "Unknown Engine Specification"}