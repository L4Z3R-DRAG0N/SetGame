import tkinter as tk
import generator
import project_set_solver as pss

def draw(root, card_set):
    # clear old
    root.create_rectangle(0, 0, 420, 380, fill = "#f0f0f0")
    # index used to determine which card should be drawn
    current_index = 0
    # row
    for i in range(4):
        # col
        for j in range(3):
            # width 80, height 100, inteval 20
            root.create_rectangle(
                (i + 1) * 20 + i * 80,
                (j + 1) * 20 + j * 100,
                (i + 1) * 20 + (i + 1) * 80,
                (j + 1) * 20 + (j + 1) * 100
                )
            card = card_set[current_index]
            # what color
            c = "black"
            if card[2] == 'R':
                c = "#cc0000"
            elif card[2] == 'P':
                c = "#cc00cc"
            elif card[2] == 'G':
                c = "#00cc00"
            # how many
            for x in range(card[3]):
                # fill?
                fill = (card[1] == "F")
                if fill:
                    # what shape
                    if card[0] == "O":
                        root.create_rectangle(
                            (i + 1) * 20 + i * 80 + 10,
                            (j + 1) * 20 + j * 100 + 10 + x * 30,
                            (i + 1) * 20 + (i + 1) * 80 - 10,
                            (j + 1) * 20 + j * 100 + 30 + x * 30,
                            outline = c,
                            fill = c
                            )
                    elif card[0] == "S":
                        root.create_oval(
                            (i + 1) * 20 + i * 80 + 10,
                            (j + 1) * 20 + j * 100 + 10 + x * 30,
                            (i + 1) * 20 + (i + 1) * 80 - 10,
                            (j + 1) * 20 + j * 100 + 30 + x * 30,
                            outline = c,
                            fill = c
                        )
                    elif card[0] == "D":
                        root.create_polygon(
                            (i + 1) * 20 + i * 80 + 10,
                            (j + 1) * 20 + j * 100 + 20 + x * 30,
                            (i + 1) * 20 + i * 80 + 40,
                            (j + 1) * 20 + j * 100 + 10 + x * 30,
                            (i + 1) * 20 + i * 80 + 70,
                            (j + 1) * 20 + j * 100 + 20 + x * 30,
                            (i + 1) * 20 + i * 80 + 40,
                            (j + 1) * 20 + j * 100 + 30 + x * 30,
                            outline = c,
                            fill = c
                            )
                else:
                    # what shape
                    if card[0] == "O":
                        root.create_rectangle(
                            (i + 1) * 20 + i * 80 + 10,
                            (j + 1) * 20 + j * 100 + 10 + x * 30,
                            (i + 1) * 20 + (i + 1) * 80 - 10,
                            (j + 1) * 20 + j * 100 + 30 + x * 30,
                            outline = c
                            )
                    elif card[0] == "S":
                        root.create_oval(
                            (i + 1) * 20 + i * 80 + 10,
                            (j + 1) * 20 + j * 100 + 10 + x * 30,
                            (i + 1) * 20 + (i + 1) * 80 - 10,
                            (j + 1) * 20 + j * 100 + 30 + x * 30,
                            outline = c
                        )
                    elif card[0] == "D":
                        root.create_polygon(
                            (i + 1) * 20 + i * 80 + 10,
                            (j + 1) * 20 + j * 100 + 20 + x * 30,
                            (i + 1) * 20 + i * 80 + 40,
                            (j + 1) * 20 + j * 100 + 10 + x * 30,
                            (i + 1) * 20 + i * 80 + 70,
                            (j + 1) * 20 + j * 100 + 20 + x * 30,
                            (i + 1) * 20 + i * 80 + 40,
                            (j + 1) * 20 + j * 100 + 30 + x * 30,
                            outline = c,
                            fill = "#f0f0f0"
                            )
                    # if line
                    if card[1] == "L":
                        root.create_line(
                            (i + 1) * 20 + i * 80 + 20,
                            (j + 1) * 20 + j * 100 + 10 + x * 30,
                            (i + 1) * 20 + (i + 1) * 80 - 20,
                            (j + 1) * 20 + j * 100 + 30 + x * 30,
                            fill = c
                        )

            current_index += 1


root = tk.Tk()

root.geometry("550x380")

canvas = tk.Canvas(root, width=420, height=380)
canvas.pack(side = "left")

# generate card set
card_set = generator.gen_set()
draw(canvas, card_set)
ans = pss.solve(card_set)
print(card_set)
print(ans)

frame = tk.Frame()

def refresh():
    card_set = generator.gen_set()
    draw(canvas, card_set)
tk.Button(frame, text = "refresh", width = 15, height = 3, bg = "#0088ff", command = refresh).pack(side = "top", pady = "20", padx = "10")

tk.Button(frame, text = "solve", width = 15, height = 3, bg = "#00cc44").pack(side = "top", pady = "20", padx = "10")
frame.pack(side = "left")

root.mainloop()
