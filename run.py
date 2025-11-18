from main_menu.main_menu import app
from auth_service.routes import service_auth
import multiprocessing
import requests
import time

def auth_service_run():
    print("🔐 Starting Auth Service on port 5001...")
    service_auth.run(host="127.0.0.1", port=5001, debug=False, use_reloader=False)

def check_auth_service_ready():
    for i in range(10):
        try:
            response = requests.get('http://127.0.0.1:5001/api/health', timeout=1)
            if response.status_code == 200:
                print("✅ Auth service is ready!")
                return True
        except:
            print(f"⏳ Waiting for auth service... ({i+1}/10)")
            time.sleep(0.5)
    return False

if __name__ == '__main__':
    auth_process = multiprocessing.Process(target=auth_service_run)
    auth_process.start()
    
    time.sleep(1)
    
    if check_auth_service_ready():
        print("🚀 Starting main application on port 5000...")
        try:
            app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)
        except KeyboardInterrupt:
            print("\n🛑 Stopping services...")
        finally:
            auth_process.terminate()
            auth_process.join()
    else:
        print("❌ Failed to start auth service")
        auth_process.terminate()