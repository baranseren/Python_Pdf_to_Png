import os
from tkinter import Tk, filedialog
from pdf2image import convert_from_path

def select_pdf_file():
    # Tkinter GUI'sini gizle
    Tk().withdraw()
    file_path = filedialog.askopenfilename(
        title="PDF Dosyasını Seçin",
        filetypes=[("PDF Files", "*.pdf")]
    )
    return file_path

def convert_pdf_to_png(pdf_path):
    if not pdf_path:
        print("PDF dosyası seçilmedi!")
        return

    output_folder = os.path.dirname(pdf_path)
    base_filename = os.path.splitext(os.path.basename(pdf_path))[0]

    print("PDF dosyası işleniyor...")

    images = convert_from_path(pdf_path)

    for i, image in enumerate(images, start=1):
        output_file = os.path.join(output_folder, f"sayfa_{i:04d}.png")
        image.save(output_file, "PNG")
        print(f"{output_file} oluşturuldu.")

    print("Tüm sayfalar PNG formatına dönüştürüldü.")

if __name__ == "__main__":
    pdf_file = select_pdf_file()
    convert_pdf_to_png(pdf_file)