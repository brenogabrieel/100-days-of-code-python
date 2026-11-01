import subprocess

try:
    # Use the 'where' command to find ChromeDriver path
    chrome_driver_path = subprocess.check_output(["where", "chromedriver.exe"]).decode("utf-8").strip()
    print("ChromeDriver Path:", chrome_driver_path)
except subprocess.CalledProcessError as e:
    print("ChromeDriver not found:", e)