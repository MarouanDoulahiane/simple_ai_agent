import psutil

def get_system_usage(_):
	"""
	Retrieves the system usage statistics and top application usage.

	Returns:
		dict: A dictionary containing:
			- 'cpu_usage': Current CPU usage percentage.
			- 'memory_usage': Current memory usage percentage.
			- 'disk_usage': Current disk usage percentage.
			- 'top_processes': A list of top processes by CPU usage, each represented as a dictionary with:
				- 'name': Process name.
				- 'pid': Process ID.
				- 'cpu_usage': CPU usage percentage.
	"""
	# Get system usage
	cpu_usage = psutil.cpu_percent(interval=1)
	memory_usage = psutil.virtual_memory().percent
	disk_usage = psutil.disk_usage('/').percent

	# Get top processes by CPU usage
	processes = []
	for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
		try:
			processes.append(proc.info)
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass

	# Sort processes by CPU usage in descending order and take the top 2
	top_processes = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)[:2]

	return {
		'cpu_usage': cpu_usage,
		'memory_usage': memory_usage,
		'disk_usage': disk_usage,
		'top_processes': top_processes
	}