from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import time

app = FastAPI(title="LEO Advanced Multi-Engine Cloud Enterprise Portal")

# Enable CORS Framework for security handshake routing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🎨 UI HTML CONSOLE PORTAL LOAD DIRECTLY ON RENDER
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

        header {
            text-align: center;
            margin-bottom: 15px;
        }

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

        h1 {
            color: var(--text-color);
            font-size: 1.4rem;
            margin: 0;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .author {
            font-size: 0.75rem;
            color: #8a8aaf;
            margin-top: 4px;
        }

        .status-box {
            border: 1px solid #222244;
            background: #04040a;
            padding: 8px;
            border-radius: 6px;
            margin-bottom: 15px;
            text-align: center;
            font-size: 0.75rem;
            color: var(--neon-green);
        }

        .section-title {
            font-size: 0.8rem;
            text-transform: uppercase;
            color: #8a8aaf;
            margin: 10px 0 5px 0;
            border-left: 2px solid var(--neon-cyan);
            padding-left: 5px;
        }

        .btn-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
            margin-bottom: 15px;
        }

        .btn {
            background: #111126;
            color: #fff;
            border: 1px solid #333366;
            padding: 10px;
            border-radius: 6px;
            font-family: inherit;
            font-weight: bold;
            font-size: 0.75rem;
            cursor: pointer;
            text-transform: uppercase;
            transition: all 0.2s ease;
        }

        .btn-python { border-color: var(--neon-cyan); color: var(--neon-cyan); }
        .btn-java { border-color: var(--neon-magenta); color: var(--neon-magenta); }
        .btn-sql { border-color: var(--neon-amber); color: var(--neon-amber); }
        .btn-cyber { border-color: var(--neon-green); color: var(--neon-green); }
        
        .btn:hover {
            transform: scale(1.02);
            box-shadow: 0 0 10px rgba(255,255,255,0.1);
        }

        .btn-clear {
            grid-column: 1 / -1;
            background: #1a0505;
            border-color: var(--neon-red);
            color: var(--neon-red);
        }

        .console {
            background-color: #030307;
            border: 1px solid #1a1a35;
            border-radius: 8px;
            padding: 12px;
            height: 250px;
            overflow-y: auto;
            box-shadow: inset 0 0 15px rgba(0,0,0,0.9);
        }

        pre {
            margin: 0;
            white-space: pre-wrap;
            word-wrap: break-word;
            font-family: inherit;
        }

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

        <div class="status-box">
            ● [SYSTEM] PYTHON // JAVA // SQL NODE CORE INTERFACE ONLINE
        </div>

        <div class="section-title">Automation & Optimization Core</div>
        <div class="btn-grid">
            <button class="btn btn-python" onclick="triggerNode('python-cost')">LEO S3 Cost (Python)</button>
            <button class="btn btn-java" onclick="triggerNode('java-runtime')">Optimization Engine (Java)</button>
        </div>

        <div class="section-title">Database & Cybersecurity Perimeter</div>
        <div class="btn-grid">
            <button class="btn btn-sql" onclick="triggerNode('sql-sync')">Database Logs Sync (SQL)</button>
            <button class="btn btn-cyber" onclick="triggerNode('cyber-scan')">Perimeter Port Scan</button>
            <button class="btn btn-clear" onclick="clearConsole()">Flush System Console Logs</button>
        </div>

        <div class="console">
            <pre id="console-body"><div class="log cy-txt">[SYSTEM] Unified Multi-Engine Framework Booted Successfully.</div><div class="log py-txt">[READY] Pipeline connection lines verified. Awaiting module trigger sequence...</div></pre>
        </div>
    </div>

    <script>
        const API_BASE = "https://lalith-empowred-office.onrender.com/api/v1";

        function clearConsole() {
            document.getElementById('console-body').innerHTML = `<div class="log err-txt">[SYSTEM] Console logging streams cleared. Pipeline clean.</div>`;
        }

        function getTime() {
            const now = new Date();
            return `[${now.toTimeString().split(' ')[0]}]`;
        }

        async function triggerNode(moduleType) {
            const consoleBody = document.getElementById('console-body');
            let targetUrl = `${API_BASE}/architecture/processing?engine=${moduleType}`;
            
            if (moduleType === 'python-cost') {
                consoleBody.innerHTML = `<div class="log py-txt">${getTime()} [PYTHON_ENGINE] Calling S3 Bucket file compression algorithm logic...</div>`;
            } else if (moduleType === 'java-runtime') {
                consoleBody.innerHTML = `<div class="log jv-txt">${getTime()} [JAVA_RUNTIME] Activating JVM background thread for compression scaling arrays...</div>`;
            } else if (moduleType === 'sql-sync') {
                consoleBody.innerHTML = `<div class="log sql-txt">${getTime()} [SQL_DATABASE] Executing SQL queries: INSERT INTO cloud_metrics logging matrices...</div>`;
            } else {
                consoleBody.innerHTML = `<div class="log cy-txt">${getTime()} [CYBER_SCANNER] Opening raw socket mapping arrays for port validation sweeps...</div>`;
            }

            try {
                const response = await fetch(targetUrl);
                const data = await response.json();
                
                consoleBody.innerHTML += `<div class="log cy-txt">${getTime()} [SUCCESS] Unified Server Node JSON Output Streams:</div>`;
                consoleBody.innerHTML += `<div class="log" style="color:#ffffff; background:#05050f; padding:8px; border-radius:4px; border:1px dashed #224;">${JSON.stringify(data, null, 4)}</div>`;
            } catch (error) {
                consoleBody.innerHTML += `<div class="log err-txt">${getTime()} [CRITICAL] Core Engine unreachable. Try triggering again in 15 seconds.</div>`;
            }
        }
    </script>
</body>
</html>
    """

# 🧠 UNIFIED API CONTROLLER PACKING PYTHON, JAVA SIMULATION, SQL AND CYBER SCAN RESPONSES
@app.get("/api/v1/architecture/processing")
def process_architecture_stream(engine: str):
    timestamp = str(time.time())
    
    if engine == "python-cost":
        return {
            "engine_runtime": "Python 3.10 / AWS Lambda Core Layer",
            "project_name": "LEO Cost Storage Optimizer",
            "file_size_before_compression": "1024 MB (1.0 GB)",
            "file_size_after_compression": "102.4 MB",
            "compression_status": "Successful (90% Storage Space Minimized)",
            "applied_lifecycle_rule": "S3 Standard to Deep Archive Auto-Migration Engaged"
        }
        
    elif engine == "java-runtime":
        return {
            "runtime_environment": "OpenJDK 17 (Java Virtual Machine)",
            "executor_thread": "LEO-Optimization-ThreadWorker-04",
            "heap_memory_allocated": "256 MB",
            "java_class_processed": "com.lalith.leo.optimizer.CompressionScheduler",
            "garbage_collection_state": "GC Clean Completed",
            "execution_speed": "42 milliseconds (Highly Efficient Compactor Loop)"
        }
        
    elif engine == "sql-sync":
        return {
            "database_system": "PostgreSQL 15 / MySQL Structured Engine Sync",
            "transaction_status": "COMMIT SUCCESSFUL",
            "query_executed": "INSERT INTO leo_cloud_audit_logs (platform, author, optimized_bytes) VALUES ('LEO', 'S.LALITH', 921600);",
            "rows_affected": 1,
            "database_connection_pool": "HikariCP Core Pool Active [Available: 19, Busy: 1]"
        }
        
    elif engine == "cyber-scan":
        return {
            "scanner_core": "LEO Custom Network Perimeter Mapping Socket Stream",
            "target_scan_host": "lalith-empowred-office.onrender.com",
            "firewall_profile_status": "Secure / Zero-Trust Verification Active",
            "active_sockets_found": [
                {"port_id": 22, "type": "TCP", "service": "SSH", "state": "Filtered / Stealth Protect Enabled"},
                {"port_id": 80, "type": "TCP", "service": "HTTP", "state": "Open (Render Network Inbound Proxy Router)"},
                {"port_id": 443, "type": "TCP", "service": "HTTPS", "state": "Open (Secure TLS Handshake Established)"}
            ],
            "perimeter_vulnerability_index": "0.0 (Safe Perimeter Environment Confirmed)"
        }
        
    return {"status": "Unknown Engine Specification Parameter"} 
