	# VirusTotal URL Enrichment (Mock Version)
	# Purpose: Show understanding of enrichment workflows without needing an API key.
	
	def enrich_url(url):
	    # Mock response for learning purposes
	    return {
	        "url": url,
	        "malicious": False,
	        "categories": ["technology", "business"],
	        "notes": "Mock data for SOC automation learning."
	    }
	
	test_urls = ["http://example.com", "http://test.com"]
	
	for u in test_urls:
    print(enrich_url(u))
