import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import simulate_devops_environment

try:
    simulate_devops_environment()
except KeyboardInterrupt:
    print("Giám sát bị dừng bởi người dùng.")