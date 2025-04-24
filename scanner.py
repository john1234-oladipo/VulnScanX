import nmap
import yaml
from plugins.port_scan import PortScanner
from plugins.web_scan import WebVulnerabilityScanner
from cve_lookup import CVEChecker

class VulnScanner:
    def __init__(self, config_file="config.yaml"):
        with open(config_file) as f:
            self.config = yaml.safe_load(f)
        self.nm = nmap.PortScanner()
        self.cve_checker = CVEChecker(api_key=self.config.get('nvd_api_key'))
        
    def run_scan(self, target, scan_type="quick"):
        results = {
            "target": target,
            "scan_type": scan_type,
            "findings": []
        }
        
        # Run modular scans
        if scan_type in ["quick", "full"]:
            results["findings"].extend(PortScanner().scan(target))
            
        if scan_type == "full":
            results["findings"].extend(WebVulnerabilityScanner().scan(target))
            results["findings"].extend(self._check_cves(results["findings"]))
            
        return results
    
    def _check_cves(self, findings):
        cve_results = []
        for item in findings:
            if "service" in item and "version" in item:
                cves = self.cve_checker.lookup(item["service"], item["version"])
                cve_results.extend(cves)
        return cve_results
