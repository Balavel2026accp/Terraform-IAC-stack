from pprint import pprint
import subprocess
import platform
import os 

"""if os.getuid() != 0:
    raise PermissionError("The commands should be ruuning as root user")
"""

class CPU_checks:
## Linux CPUIFO file and read.
    def Show_cpuinfo(self):  
        try:
          Os_name = platform.system()
          if Os_name == "Linux":  
            cpu_information = subprocess.run("cat /proc/cpuinfo", shell=True, capture_output=True, text=True)

          return cpu_information.stdout
        
        except subprocess.CalledProcessError as e:
         return "command failed: ", e.stderr
 
        except FileNotFoundError as a:
         return "Command not found", str(a)

        except NameError as name:
         return "OS type mismatched", str(name), Os_name

        except Exception as f:
         return "UNexpected error", str(f)
              
#Cpu_file = CPU_checks()
#print(Cpu_file.Show_cpuinfo()) 

    def read_cpuinfo(self):
        cpu_info = []
        current_cpu = {}

        with open("/proc/cpuinfo") as file:
            for line in file:
                line = line.strip()
                # Runs only when the line is Empty. 
                if not line:
                    if current_cpu:
                        cpu_info.append(current_cpu)
                        current_cpu = {}
                    continue

                key, value = line.split(":", 1)
                current_cpu[key.strip()] = value.strip()

        # Add the last processor
        if current_cpu:
            cpu_info.append(current_cpu)
        return self.creating_logical_dictinary(cpu_info)

        #return cpu_info
    def creating_logical_dictinary(self, outputdict: list):
           self.outputdict = outputdict
           lenth_list = len(self.outputdict)
           data = ("processor", "vendor_id", "model", "cpu family", "siblings", "cpu cores")
           filtered_list = []
           """for i in range(lenth_list):
              # create empty dictionaries
              globals()[f"processor_dict{i}"] = {}
              raise RuntimeError("Invalid assignment")"""
           for cpu_info in self.outputdict:
              filtered_dict = {}

              for key, value in cpu_info.items():
                 if key in data:
                     filtered_dict[key] = value

              filtered_list.append(filtered_dict)    

           return filtered_list         

    ## HTML creation for CPU information.
    def render_html(self):
        cpu_data = self.read_cpuinfo()

        html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CPU Monitoring Dashboard</title>
    <style>
        :root {
            color-scheme: dark;
            --bg: #0b1120;
            --panel: rgba(15, 27, 52, 0.96);
            --accent: #4dd0e1;
            --accent-soft: #1b93a5;
            --text: #ebf4ff;
            --muted: #8fa4c0;
            --border: rgba(255,255,255,0.08);
            --shadow: 0 24px 80px rgba(0,0,0,0.18);
            font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        }

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            background: radial-gradient(circle at top left, rgba(77, 208, 225, 0.18), transparent 28%),
                        linear-gradient(180deg, #07101f 0%, #070d18 45%, #08101e 100%);
            color: var(--text);
            line-height: 1.5;
        }

        .page-shell {
            width: min(1180px, calc(100% - 32px));
            margin: 0 auto;
            padding: 36px 0 48px;
        }

        .hero {
            display: grid;
            gap: 18px;
            margin-bottom: 30px;
        }

        .hero-title {
            font-size: clamp(2rem, 3vw, 3.1rem);
            margin: 0;
            letter-spacing: -0.04em;
        }

        .hero-copy {
            max-width: 720px;
            color: var(--muted);
            font-size: 1rem;
        }

        .stats-grid {
            display: grid;
            gap: 16px;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        }

        .stat-card {
            background: var(--panel);
            border: 1px solid var(--border);
            border-radius: 26px;
            padding: 22px 24px;
            box-shadow: var(--shadow);
            backdrop-filter: blur(18px);
        }

        .stat-card strong {
            display: block;
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.18em;
            color: var(--muted);
            margin-bottom: 12px;
        }

        .stat-card span {
            display: block;
            font-size: 2rem;
            font-weight: 700;
            color: var(--text);
        }

        .table-panel {
            background: var(--panel);
            border: 1px solid var(--border);
            border-radius: 28px;
            overflow: hidden;
            box-shadow: var(--shadow);
        }

        table {
            width: 100%;
            border-collapse: collapse;
            text-align: left;
            font-size: 0.95rem;
            min-width: 620px;
        }

        thead {
            background: rgba(13, 23, 44, 0.94);
        }

        th, td {
            padding: 18px 20px;
            border-bottom: 1px solid rgba(255,255,255,0.06);
        }

        th {
            color: var(--muted);
            font-weight: 600;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            font-size: 0.78rem;
        }

        tbody tr {
            transition: transform 160ms ease, background 160ms ease;
        }

        tbody tr:hover {
            background: rgba(77, 208, 225, 0.08);
            transform: translateX(2px);
        }

        tbody td {
            color: var(--text);
        }

        .footer-note {
            margin-top: 20px;
            color: var(--muted);
            font-size: 0.88rem;
        }
    </style>
</head>
<body>
    <div class="page-shell">
        <section class="hero">
            <div>
                <h1 class="hero-title">CPU Monitoring Dashboard</h1>
                <p class="hero-copy">A polished performance-focused dashboard built for clarity, speed, and visual impact. Streamlined rendering uses semantic structure and lightweight styling for an ultra-fast browser experience.</p>
            </div>
        </section>

        <section class="stats-grid">
"""

        if cpu_data:
            cpu = cpu_data[0]
            html += f"""
            <article class="stat-card">
                <strong>Processor</strong>
                <span>{cpu.get('processor', 'N/A')}</span>
            </article>
            <article class="stat-card">
                <strong>Vendor</strong>
                <span>{cpu.get('vendor_id', 'N/A')}</span>
            </article>
            <article class="stat-card">
                <strong>Model Name</strong>
                <span>{cpu.get('model name', cpu.get('model', 'N/A'))}</span>
            </article>
            <article class="stat-card">
                <strong>Physical Cores</strong>
                <span>{cpu.get('cpu cores', cpu.get('cores', 'N/A'))}</span>
            </article>
            <article class="stat-card">
                <strong>Threads</strong>
                <span>{cpu.get('siblings', 'N/A')}</span>
            </article>
            <article class="stat-card">
                <strong>Family</strong>
                <span>{cpu.get('cpu family', 'N/A')}</span>
            </article>
"""
        else:
            html += """
            <article class="stat-card">
                <strong>CPU Status</strong>
                <span>No CPU data available</span>
            </article>
"""

        html += """
        </section>

        <section class="table-panel">
            <table>
                <thead>
                    <tr>
                        <th>Processor</th>
                        <th>Vendor ID</th>
                        <th>Model</th>
                        <th>CPU Family</th>
                        <th>Siblings</th>
                        <th>CPU Cores</th>
                    </tr>
                </thead>
                <tbody>
"""

        for cpu in cpu_data:
            html += f"""
                    <tr>
                        <td>{cpu.get('processor', '')}</td>
                        <td>{cpu.get('vendor_id', '')}</td>
                        <td>{cpu.get('model', cpu.get('model name', ''))}</td>
                        <td>{cpu.get('cpu family', '')}</td>
                        <td>{cpu.get('siblings', '')}</td>
                        <td>{cpu.get('cpu cores', '')}</td>
                    </tr>
"""

        html += """
                </tbody>
            </table>
        </section>

        <p class="footer-note">Rendered using lightweight CSS and streamlined HTML for responsive, GPU-friendly presentation across modern browsers.</p>
    </div>
</body>
</html>
"""

        return html
   
              
    
