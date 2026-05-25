# You're building a smart thermostat alert system:
# 1. If the device_status is "active"
#     1.1 And temperature >35 -> Warn "High temperature alert!"
#     1.2 Else: "Temperature normal"
# 2. If device is off -> "Device is offline"

device_status = "active"
temperature = 39

if device_status == "active":
    if temperature > 35:
        print("High temperature alert!")
    else: 
        print("Temperature is normal.")
else:
    print("Device is offline")
