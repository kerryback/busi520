import os
file = input("\nNotebook name: ")
os.system(f'jupyter nbconvert {file}.ipynb --to slides --SlidesExporter.reveal_scroll=True')