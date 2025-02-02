import os
import subprocess
import datetime
import shutil
import win32com.client 



project_path = os.getcwd()
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
build_dir = os.path.join(project_path, f"comfyui_{timestamp}") 
icon_path = os.path.join(project_path, "icons", "psewdon1ms_comfyui_icon.ico")
image_name = f"comfyui_docker-comfyui:{timestamp}"  
container_name = f"comfyui_{timestamp}"


os.makedirs(build_dir, exist_ok=True)
shutil.copytree(os.path.join(project_path, "ComfyUI"), os.path.join(build_dir, "ComfyUI"))
shutil.copy(os.path.join(project_path, "docker-compose.yml"), os.path.join(build_dir, "docker-compose.yml"))



compose_file_path = os.path.join(build_dir, "docker-compose.yml")

with open(compose_file_path, "r") as file:
    compose_content = file.read()

compose_content = compose_content.replace("${VOLUME_ROOT}:/comfyui_docker",
                                          f"{os.path.join(build_dir, 'ComfyUI')}:/comfyui")
compose_content = compose_content.replace("${IMAGE_NAME}", image_name)

with open(compose_file_path, "w") as file:
    file.write(compose_content)
print(f"Docker-compose.yml updated in: {compose_file_path}")




print("Docker check...")
docker_status = subprocess.run("docker info", shell=True, capture_output=True, text=True)
if "ERROR" in docker_status.stderr or "Cannot connect to the Docker daemon" in docker_status.stderr:
    print("Ошибка: Docker is not activ. Reboot Docker Desktop and try again.")
    exit(1)



os.chdir(build_dir)
print(f"Building image: {image_name} ...")
subprocess.run("docker-compose build", shell=True)

subprocess.run(f"docker tag comfyui_docker-comfyui:latest {image_name}", shell=True)

print(f"Image built and tagged: {image_name}")



py_file_name = f"run_{timestamp}.py"
py_file_path = os.path.join(build_dir, py_file_name)

with open(py_file_path, "w", encoding="utf-8") as py_file:
    py_file.write(f"""
import subprocess
import os
import webbrowser
import time
import requests



def wait_for_service(url, timeout=360):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                return True
        except requests.exceptions.RequestException:
            pass
        time.sleep(2)
    return False



container_status = subprocess.run("docker ps -q -f name=comfyui", shell=True, capture_output=True, text=True)
build_dir = "{build_dir}"
os.chdir(build_dir)
container_name = "{container_name}"
image_name = "{image_name}"



if container_status.stdout.strip():
    print("Container stopping...")
    subprocess.run("docker-compose -f docker-compose.yml down", shell=True)
else:
    print("Container activation...")
    subprocess.run("docker-compose -f docker-compose.yml up -d", shell=True)
    subprocess.run("start cmd /k docker-compose -f docker-compose.yml logs -f", shell=True)

    print("Waiting for service to start...")
    if wait_for_service("http://127.0.0.1:8188"):
        print("Service is up, opening browser...")
        webbrowser.open("http://127.0.0.1:8188")
    else:
        print("Timeout reached, service is not responding.")
""")

print(f"Python launcher created in: {py_file_path}")



exe_file_name = f"run_{timestamp}.exe"
exe_file_path = os.path.join(build_dir, exe_file_name)

print("Compiling Python script into executable...")

subprocess.run(f'pyinstaller --onefile --noconsole --icon "{icon_path}" "{py_file_path}"', shell=True)

dist_exe_path = os.path.join(build_dir, "dist", exe_file_name)
if os.path.exists(dist_exe_path):
    shutil.move(dist_exe_path, exe_file_path)

dist_dir_path = os.path.join(build_dir, "dist")
if os.path.exists(dist_dir_path):
    shutil.rmtree(dist_dir_path)

subprocess.run("rmdir /s /q build", shell=True)
subprocess.run("del /q run_*.spec", shell=True)



def create_shortcut(target, shortcut_path, description=""):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = os.path.dirname(target)
    shortcut.Description = description
    shortcut.save()

models_target = os.path.join(build_dir, "ComfyUI", "models")
output_target = os.path.join(build_dir, "ComfyUI", "output")
workflows_target = os.path.join(build_dir, "ComfyUI", "user", "default", "workflows")

models_shortcut = os.path.join(build_dir, "models.lnk")
output_shortcut = os.path.join(build_dir, "output.lnk")
workflows_shortcut = os.path.join(build_dir, "workflows.lnk")

try:
    create_shortcut(models_target, models_shortcut, "models")
    create_shortcut(output_target, output_shortcut, "output")
    create_shortcut(workflows_target, workflows_shortcut, "workflows")
except Exception as e:
    print(f"Shortcuts creation error: {e}")


print(f"Final executable file is ready: {exe_file_path}")



input("Process completed. Press any key to exit...")