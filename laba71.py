import ImageFilter
from PIL import Image
def z71():
    image = Image.open('picture.jpg')
    print(f"Формат: {image.format}")
    print(f"Размер: {image.size}")
    print(f"Цветовая модель: {image.mode}")
    image.show()

def z72():
    image = Image.open('picture.jpg')
    res_img2 = image.reduce(3)
    res_img2.save('picture22.jpg')
    res_img3 = image.transpose(Image.ROTATE_180)
    res_img4 = image.transpose(Image.ROTATE_90)
    res_img3.save('picture33.jpg')
    res_img4.save('picture44.jpg')
    image.show()
    res_img3.show()
    res_img4.show()
def z73():
    a = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpeg"]
    for name in a:
        image = Image.open(name)
        image_f = image.filter(ImageFilter.SHARPEN)
        n = name.replace(".", "new.")
        image_f.save(n)
        image_f.show()
def z74():
    import PyPDF2

    input_file = "zad4.pdf"
    output_file = "zad44.pdf"
    watermark_file = "zad41.pdf"

    with open(input_file, 'rb') as file_input, open(output_file, 'wb') as file_output:
        pdf = PyPDF2.PdfReader(file_input)
        watermark = PyPDF2.PdfReader(open(watermark_file, 'rb'))

        pdf_writer = PyPDF2.PdfWriter()
        first_page = pdf.pages[0]
        watermark_page = watermark.pages[0]

        first_page.merge_page(watermark_page)
        pdf_writer.add_page(first_page)

        pdf_writer.write(file_output)
print(z71())
print(z72())
print(z73())
print(z74())