import psutil
import time

# Step 1: Print message
print("Monitoring CPU usage...")

# Step 2: Set threshold
THRESHOLD = 80  # CPU percentage

# Step 3 + Step 4: Monitor continuously with error handling
try:
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)  # Check CPU every 1 second

        if cpu_usage > THRESHOLD:
            print(f"❌ Alert! CPU usage is HIGH: {cpu_usage}%")
        else:
            print(f"CPU usage is normal: {cpu_usage}%")

except KeyboardInterrupt:
    print("\nProgram stopped by user.")

except Exception as e:
    print(f"⚠️ An error occurred: {e}")

