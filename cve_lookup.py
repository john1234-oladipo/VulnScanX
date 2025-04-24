import requests

class CVEChecker:
    def __init__(self, api_key=None):
        self.base_url = "https://services.nvd.nist.gov/rest/json/cves/1.0"
        self.api_key = api_key
        
    def lookup(self, software, version):
        params = {
            "keyword": f"{software} {version}",
            "resultsPerPage": 20
        }
        headers = {"apiKey": self.api_key} if self.api_key else {}
        
        try:
            response = requests.get(self.base_url, params=params, headers=headers)
            response.raise_for_status()
            return self._parse_cves(response.json())
        except Exception as e:
            print(f"CVE lookup failed: {e}")
            return []
    
    def _parse_cves(self, data):
        return [
            {
                "type": "CVE",
                "id": item["cve"]["CVE_data_meta"]["ID"],
                "risk": "High",
                "description": item["cve"]["description"]["description_data"][0]["value"],
                "fix": "Check NVD for patches"
            }
            for item in data.get("result", {}).get("CVE_Items", [])
        ]
