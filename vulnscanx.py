import argparse
from core.scanner import VulnScanner
from core.reporter import ReportGenerator

def main():
    parser = argparse.ArgumentParser(description="VulnScanX - Automated Vulnerability Scanner")
    parser.add_argument("--target", required=True, help="Target IP/Domain")
    parser.add_argument("--scan-type", choices=["quick", "full"], default="quick",
                      help="Scan intensity level")
    parser.add_argument("--report", choices=["html", "pdf"], default="html",
                      help="Report output format")
    parser.add_argument("--output", help="Custom output file path")
    
    args = parser.parse_args()
    
    scanner = VulnScanner()
    results = scanner.run_scan(args.target, args.scan_type)
    
    reporter = ReportGenerator()
    if args.report == "pdf":
        report_path = reporter.generate_pdf(results, args.output or "report.pdf")
    else:
        report_path = reporter.generate_html(results, args.output or "report.html")
    
    print(f"Scan completed! Report saved to {report_path}")

if __name__ == "__main__":
    main()
