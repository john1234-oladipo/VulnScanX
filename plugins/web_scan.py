import requests
from bs4 import BeautifulSoup

class WebVulnerabilityScanner:
    def scan(self, target):
        findings = []
        
        # Check for common web vulnerabilities
        if self._check_sqli(target):
            findings.append({
                "type": "Web",
                "id": "WEB-001",
                "risk": "High",
                "description": "Potential SQL Injection vulnerability",
                "fix": "Use parameterized queries"
            })
        
        if self._check_xss(target):
            findings.append({
                "type": "Web",
                "id": "WEB-002",
                "risk": "Medium",
                "description": "Potential XSS vulnerability",
                "fix": "Implement output encoding"
            })
            
        return findings
    
    def _check_sqli(self, target):
        test_payload = "' OR '1'='1"
        try:
            response = requests.get(f"http://{target}/search?q={test_payload}", timeout=5)
            return "error in your SQL syntax" in response.text.lower()
        except:
            return False
    
    def _check_xss(self, target):
        test_payload = "<script>alert('XSS')</script>"
        try:
            response = requests.get(f"http://{target}/search?q={test_payload}", timeout=5)
            return test_payload in response.text
        except:
            return False
