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
    <title>CPU Information</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background: #fff; color: #111; }
        h1 { margin-top: 0; font-size: 1.8rem; }
        table { width: 100%; border-collapse: collapse; margin-top: 16px; }
        th, td { border: 1px solid #ccc; padding: 8px 10px; }
        th { background: #f0f0f0; text-align: left; }
        p { max-width: 720px; line-height: 1.5; }
    </style>
</head>
<body>
    <h1>CPU Information</h1>
"""

        if cpu_data:
            html += """
    <p>The table below shows detected CPU entries from the system.</p>
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
"""
        else:
            html += """
    <p>No CPU data available.</p>
"""

        html += """
</body>
</html>
"""

        return html
