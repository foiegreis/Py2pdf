"""

Py2pdf - Converts .py files to .pdf files, using enscript library

author: Greta Russi (@foiegreis) 2024

"""

import subprocess
import os
import customtkinter
from customtkinter import filedialog


class App:
    def __init__(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.root = customtkinter.CTk()
        self.root.geometry("650x350")

        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        label_title = customtkinter.CTkLabel(master=self.frame, text="Py2Pdf",
                                             font=("Roboto",20))
        label_title.grid(column=1, row=0, pady=5, padx=5, sticky='e')

    def file_uploader(self, row, text, command):
        """File uploader"""
        label = customtkinter.CTkLabel(master=self.frame, text=f"File {text}: ", font=("Roboto", 13))
        label.grid(column=0, row=row, pady=2, padx=10, sticky='w')
        label_entry = customtkinter.CTkLabel(master=self.frame, text="File", font=("Roboto", 13),
                                             bg_color='white', fg_color='white',
                                             corner_radius=50, width=200,
                                             height=20)
        label_entry.grid(column=1, row=row, pady=2, padx=2)
        button = customtkinter.CTkButton(master=self.frame, text="Select", command=command)
        button.grid(column=2, row=row, pady=2, padx=2)

class py2pdfGUI(App):
    def __init__(self):
        super().__init__()
        # Ade utils
        self.path = ''
        self.py_file = ''
        self.pdf_file = ''

        self.font_size_list = ['6', '7', '8', '9', '10', '11', '12', '13', '14']
        self.font_list = ['Courier', 'Times-Roman', 'Arial']
        self.font = customtkinter.StringVar()
        self.font_size = customtkinter.StringVar()
        self.orientation = customtkinter.StringVar()
        self.colormap = customtkinter.StringVar()

        self.build_gui()
        self.root.mainloop()

    def upload_file(self):
        """Upload file function"""
        # Open a file dialog for file selection
        file_path = filedialog.askopenfilename()

        # Update the corresponding label with the selected file path
        self.py_file = os.path.basename(file_path)
        self.path = os.path.dirname(file_path)

        print('folder path: ', self.path)
        print('py file: ', self.py_file)

        entry = customtkinter.CTkLabel(master=self.frame, text=f"{file_path.split('/')[-1]}",
                                       font=("Roboto", 13),
                                       bg_color='white', fg_color='white',
                                       corner_radius=50, width=200,
                                       height=20)
        entry.grid(column=1, row=1, pady=2, padx=2)

    def get_settings(self):
        self.orientation = self.orientation.get()
        self.colormap = self.colormap.get()
        if self.colormap == 'false':
            self.colormap = '='+self.colormap
        self.font = self.font.get()
        self.font_size = self.font_size.get()

    def radio_option(self, label_text, text_1, opt_1, text_2, opt_2, var, row):
        label = customtkinter.CTkLabel(master=self.frame, text=label_text+': ', font=("Roboto", 13))
        rad_1 = customtkinter.CTkRadioButton(master=self.frame, text=text_1, value=opt_1,
                                                         variable=var)
        rad_2 = customtkinter.CTkRadioButton(master=self.frame, text=text_2, value=opt_2,
                                                         variable=var)
        label.grid(column=0, row=row, pady=10, padx=10, sticky='w')
        rad_1.grid(column=1, row=row, pady=10, padx=10, sticky='w')
        rad_2.grid(column=2, row=row, pady=10, padx=10, sticky='w')

    def optionmenu_callback(self, choice):
        print('choice ', choice)

    def dropmenu(self, label_text, options_list, variable, row):
        label = customtkinter.CTkLabel(master=self.frame, text=label_text+': ', font=("Roboto", 13))
        combobox = customtkinter.CTkOptionMenu(master=self.frame,
                                               values=options_list,
                                               command=self.optionmenu_callback,
                                               variable=variable)
        label.grid(column=0, row=row, pady=10, padx=10, sticky='w')
        combobox.grid(column=1, row=row, pady=10, padx=10, sticky='w')

    def build_gui(self):
        """Build gui"""
        self.file_uploader(1, "select .py file", self.upload_file)
        self.radio_option('Orientation',
                          'portrait', 'portrait',
                          'landscape', 'landscape',
                          self.orientation, 3)

        self.radio_option('Colormap',
                          'bw', 'false',
                          'color', '',
                          self.colormap, 4)

        self.dropmenu('Font', self.font_list, self.font, 5)
        self.dropmenu('Font size', self.font_size_list, self.font_size,6)

        button = customtkinter.CTkButton(master=self.frame, text="Generate pdf", command=self.generate_pdf)
        button.grid(column=2, row=7, pady=10, padx=2)

    def generate_pdf(self):
        input_path = os.path.join(self.path, self.py_file)
        self.pdf_file = self.py_file.split('.')[0] + '.pdf'
        output_path = os.path.join(self.path, self.pdf_file).strip()

        print(input_path)
        print(output_path)
        self.get_settings()

        print('settings: ', self.orientation, self.colormap, self.font, self.font_size)

        # Create PostScript file using enscript
        enscript_command = [
            'enscript',
            f'--output={output_path}',  # Output file path
            '--highlight=python',  # Specify Python syntax highlighting
            '--no-header',  # No header option
            f'--title={self.py_file}',  # Sets title as the file name
            f'--font={self.font}{self.font_size}',  # Font name and size
            f'--{self.orientation}',  # Orientation
            f'--color{self.colormap}',  # Color coded, bool
            input_path  # Input file path
        ]

        postscript_content = subprocess.check_output(enscript_command, universal_newlines=True)

        # Convert PostScript to PDF using ps2pdf
        ps2pdf_command = [
            'ps2pdf',  # Should be available if you have a TeX distribution installed
            '-' if self.orientation.lower() == 'portrait' else '-c',
            f'-o={output_path}'
        ]
        subprocess.run(ps2pdf_command, input=postscript_content, universal_newlines=True)


if __name__ == '__main__':
    app = py2pdfGUI()