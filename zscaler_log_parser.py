	# Zscaler Log Parser (Simplified)
	# Purpose: Practice understanding ZIA/ZPA log fields.
	
	def parse_zscaler_log(line):
	    fields = line.split(",")
	    return {
	        "timestamp": fields[0],
	        "user": fields[1],
	        "action": fields[2],
	        "url_or_app": fields[3],
	        "result": fields[4]
	    }
	
	with open("zscaler_sample_logs.csv", "r") as f:
	    for line in f:
        print(parse_zscaler_log(line.strip()))
