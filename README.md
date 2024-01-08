# Py2Pdf: Python Code to PDF Converter

This Python script converts Python code (.py files) to PDF files with syntax highlighting using enscript and ps2pdf.

It also allows you to specify:
- the page orientation (portrait or landscape)
- the font name and size
- the code color palette:  b/w or color
- the file tile
- the header presence / absence


Please refer to https://linux.die.net/man/1/enscript for the complete list of esnscript arguments

## Prerequisites

- [enscript](https://www.gnu.org/software/enscript/): A command-line tool to convert text files to PostScript, which is then used to generate the PDF.
- [ps2pdf](https://www.ghostscript.com/doc/current/Ps2pdf.htm): A tool that comes with Ghostscript to convert PostScript files to PDF.
- Python 3.x

## Installation

Make sure you have enscript and ps2pdf installed on your system. Install the required Python libraries by running:

```bash
pip install fpdf
```

## Usage
git clone https://github.com/your-username/your-repo.git

cd your-repo

## Run

Modify the desired settings from line 47

```bash
path_to_py = ''  # Path to folder
py_name = 'test_input.py'  # Input file name
pdf_name = 'test_output.pdf'  # Output file name

# Set here your desired pdf output structure
settings = {'font': 'Courier',
            'font-size': '8',
            'orientation': 'landscape',  # portrait
            'color': 'false'  # true
            }
```
```bash
python3 py2pdf.py
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
The script uses the fpdf library for PDF generation.

Syntax highlighting is performed using the enscript library.