import subprocess
import os


def generate_pdf(path, py_file, pdf_file, settings):

    input_file = os.path.join(path, py_file)
    output_file = os.path.join(path, pdf_file)

    font = settings['font']
    font_size = settings['font-size']
    orientation = settings['orientation']
    color = settings['color']

    # Create PostScript file using enscript
    enscript_command = [
        'enscript',
        f'--output={output_file}',  # Output file path
        '--highlight=python',  # Specify Python syntax highlighting
        '--no-header',  # No header option
        f'-t {py_file}',  # Sets title as the file name
        f'-f{font}{font_size}',  # Font name and size
        f'--{orientation}',  # Orientation
        f'--color={color}',  # Color coded, bool
        input_file  # Input file path
    ]
    postscript_content = subprocess.check_output(enscript_command, universal_newlines=True)

    # Convert PostScript to PDF using ps2pdf
    ps2pdf_command = [
        'ps2pdf',  # Should be available if you have a TeX distribution installed
        '-' if orientation.lower() == 'portrait' else '-c',
        f'-o={output_file}'
    ]
    subprocess.run(ps2pdf_command, input=postscript_content, universal_newlines=True)


if __name__ == '__main__':
    path_to_py = ''

    py_name = 'fast_slam1.py'
    pdf_name = 'out.pdf'

    # Set here your desired pdf output structure
    settings = {'font': 'Courier',
                'font-size': '8',
                'orientation': 'landscape',  # portrait
                'color': 'false'  # true
                }

    generate_pdf(path_to_py, py_name, pdf_name, settings)
