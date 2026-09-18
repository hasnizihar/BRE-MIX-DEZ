import markdown2
from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 12)
        self.cell(0, 10, "BRE Mix Design Project - Final Report", border=False, new_x="LMARGIN", new_y="NEXT", align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

def main():
    report_path = os.path.join("00_PROJECT", "RESEARCH_COMPLETION_REPORT.md")
    
    with open(report_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    
    # Replace unicode characters with ascii equivalents to avoid fpdf encoding issues
    replacements = {
        "—": "-",
        "✓": "[X]",
        "✗": "[ ]",
        "×": "x",
        "≈": "~",
        "µ": "u",
        "°": "deg",
        "³": "^3",
        "²": "^2",
        "≤": "<=",
        "≥": ">=",
        "”": '"',
        "“": '"',
        "’": "'",
        "‘": "'",
        "…": "...",
    }
    
    for old, new in replacements.items():
        md_content = md_content.replace(old, new)
        
    md_content = md_content.replace("> **Project:**", "<b>Project:</b>")
    md_content = md_content.replace("> **Date:**", "<b>Date:</b>")
    md_content = md_content.replace("> **Phase:**", "<b>Phase:</b>")
    md_content = md_content.replace("*Design of Normal Concrete Mixes*", "Design of Normal Concrete Mixes")
    
    # Convert markdown to html
    html_content = markdown2.markdown(md_content, extras=["tables"])
    html_content = html_content.replace("<em>", "").replace("</em>", "")
    
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("helvetica", size=10)
    
    try:
        pdf.write_html(html_content)
    except Exception as e:
        print(f"Error during HTML conversion: {e}")
        pdf.add_page()
        pdf.set_font("courier", size=9)
        pdf.multi_cell(0, 5, text=md_content)
        
    output_file = "FINAL_REPORT.pdf"
    pdf.output(output_file)
    print(f"Successfully created {output_file}")

if __name__ == "__main__":
    main()
