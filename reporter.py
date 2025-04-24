from jinja2 import Template
from weasyprint import HTML
import os

class ReportGenerator:
    def __init__(self, template_dir="templates"):
        self.template_dir = template_dir
        
    def generate_html(self, scan_data, output_file="report.html"):
        with open(f"{self.template_dir}/report_template.html") as f:
            template = Template(f.read())
        
        html = template.render(
            target=scan_data["target"],
            findings=sorted(scan_data["findings"], key=lambda x: x["risk"], reverse=True),
            scan_date=scan_data.get("scan_date", "N/A")
        )
        
        with open(output_file, "w") as f:
            f.write(html)
        return output_file
    
    def generate_pdf(self, scan_data, output_file="report.pdf"):
        html_file = self.generate_html(scan_data, "temp.html")
        HTML(html_file).write_pdf(output_file)
        os.remove(html_file)
        return output_file
