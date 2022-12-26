from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont


def open_and_watermark():
    filename = filedialog.askopenfile(filetypes=[('JPG Files', '*.jpg'), ('GIF Files', '*.gif')])
    if filename:
        img = Image.open(filename.name)
        image_width, image_height = img.size

        draw = ImageDraw.Draw(img)
        text = "Generic Watermark"
        font = ImageFont.truetype('arial.ttf', 45)
        print(draw.textsize(text, font))

        # # Put the watermark in the lower right corner
        # text_width, text_height = draw.textsize(text, font)
        # x = image_width - text_width - 10
        # y = image_height - text_height - 15

        # Put the watermark in the centre of the image
        x = image_width / 2
        y = image_height / 2
        draw.text((x, y), text, font=font)

        # Saving the image
        new_filename = f'{filename.name.split(".")[-2].split(" / ")[-1]}-watermarked.jpg'
        print(new_filename)
        img.save(new_filename)

        # Open the image
        img = Image.open(new_filename)
        img.show()


if __name__ == "__main__":
    window = Tk()
    window.title("Image Watermarker")
    window.config(padx=100, pady=50, bg="white")

    title_label = Label(text="Image Watermarker", fg="black", bg="white", font=("Courier", 24))
    title_label.pack()

    canvas = Canvas(width=200, height=224, bg="white", highlightthickness=0)
    watermark_example = PhotoImage(file="watermark_example.png")
    canvas.create_image(100, 112, image=watermark_example)
    canvas.pack()

    label = Label(window, text="Click to select an image for watermarking", bg="white", font=("Courier", 14))
    label.pack()

    button = Button(window, text="Browse", command=open_and_watermark)
    button.pack()

    window.mainloop()
