import psutil



def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def get_cpu_load_average():
    return psutil.getloadavg()

def get_cpu_temp():
    if not hasattr(psutil, "sensors_temperatures"):
        raise NotImplementedError("Temperature monitoring not supported on this system.")

    temps =  {}
    try:
        sensor_data = psutil.sensors_temperatures()
        if 'coretemp' in sensor_data:
            for i,entry in enumerate(sensor_data['coretemp'][1:], 1):
                temps[f"Core {i-1}"] = entry.current
    except Exception as e:
        print(f"Error retrieving CPU temperature: {e}")
    print(temps)
    return temps