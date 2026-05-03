	# Basic Log Parser
	# Purpose: Extract key fields from simple log lines for SOC triage practice.
	
	def parse_log_line(line):
	    parts = line.split(" ")
	    return {
	        "timestamp": parts[0],
	        "log_level": parts[1],
	        "message": " ".join(parts[2:])
	    }
	
	with open("sample_logs.txt", "r") as f:
	    for line in f:
	        parsed = parse_log_line(line.strip())
        print(parsed)
