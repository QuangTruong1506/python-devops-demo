import random
import time
import logging

# Cấu hình logging để gửi cảnh báo
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Hàm lấy mức sử dụng CPU
def get_cpu_usage():
    # Mô phỏng CPU nếu không có psutil
    return random.uniform(0, 100)

# Hàm thực hiện hành động của agent
def devops_agent(cpu_usage):
    if cpu_usage > 90:
        logging.warning(f"CPU cao bất thường: {cpu_usage}% - Đang khởi động lại dịch vụ...")
        return "Khởi động lại dịch vụ"
    elif cpu_usage > 80:
        logging.warning(f"CPU tăng cao: {cpu_usage}% - Đang gửi cảnh báo...")
        return "Gửi cảnh báo"
    else:
        return "Không cần hành động"

# Hàm mô phỏng môi trường DevOps
def simulate_devops_environment():
    print("Khởi động Agent Giám sát CPU DevOps...")
    for _ in range(10):
        cpu_usage = get_cpu_usage()
        action = devops_agent(cpu_usage)
        print(f"Mức sử dụng CPU: {cpu_usage:.1f}% -> Hành động: {action}")
        time.sleep(2)  # Đợi 2 giây giữa các lần kiểm tra

# Chạy mô phỏng
if __name__ == "__main__":
    simulate_devops_environment()