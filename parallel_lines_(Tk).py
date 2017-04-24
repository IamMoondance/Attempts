from tkinter import *

c_width = 800
c_height = 600
c_frame = 15

root = Tk()
draw = Canvas(root, width = c_width, height = c_height, bg = "#ffffff")

lines = []
points = []

# Input correct lines [x1, y1, x2, y2]
print("Enter pair of points of line; empty line to stop")
buf = input()
while buf != '':
    buf = list(map(float, buf.split()))
    if (len(buf) != 4) or ((buf[0] - buf[2] == 0) and (buf[1] - buf[3] == 0)):
        print("Incorrect line!", buf)
    else:
        lines.append(buf)
    buf = input()

# Input points [x, y]
print("Enter coords of points; empty line to stop")
buf = input()
while buf != '':
    points.append(list(map(float, buf.split())))
    buf = input()

# Number of non repeated lines from points
print(len(points)*(len(points)-1)//2,'lines maded using this points')

# Count number of parallel lines
max_parallels = 0
max_parallels_points = [0, 0]

for i in range(len(points)):
    for j in range(i, len(points)):
        parallels = 0
        delt_x = points[i][0] - points[j][0]
        delt_y = points[i][1] - points[j][1]
        # case of equivalent points
        if delt_x == 0 or delt_y == 0:
            continue
        else:
            for line in lines:
                delt_x_l = line[0] - line[2]
                delt_y_l = line[1] - line[3]
                # vector multiply for 2d vectors
                if delt_x * delt_y_l - delt_y * delt_x_l == 0:
                    parallels += 1
        if parallels > max_parallels:
            max_parallels = parallels
            max_parallels_points = [i, j]

print("Max parallel lines is", max_parallels)
print("with points ({:}; {:}) and ({:}, {:})".format(\
      points[max_parallels_points[0]][0], points[max_parallels_points[0]][1],\
      points[max_parallels_points[1]][0], points[max_parallels_points[1]][1]))

# Search offset and scale for graph projection
min_x = max_x = points[0][0]
min_y = max_y = points[0][1]

# Looking in points
for point in points:
    max_x = max(max_x, point[0])
    min_x = min(min_x, point[0])
    max_y = max(max_y, point[1])
    min_y = min(min_y, point[1])

# Looking in line points
for line in lines:
    max_x = max(max_x, line[0], line[2])
    min_x = min(min_x, line[0], line[2])
    max_y = max(max_y, line[1], line[3])
    min_y = min(min_y, line[1], line[3])

c_scale = min((c_width - c_frame)/(max_x - min_x),\
              (c_height - c_frame)/(max_y - min_y))

c_offset_x = c_frame + round((c_width - 2*c_frame - (max_x - min_x)*c_scale)/2)
c_offset_y = c_height - c_frame - round((c_height - 2*c_frame - \
                                         (max_y - min_y)*c_scale)/2)

# Draw axis lines
x = round(c_offset_x - min_x*c_scale)
y = round(c_offset_y + min_y*c_scale)
draw.create_line(0, y, c_width, y, width=2, fill="grey", arrow=LAST)
draw.create_line(x, c_height, x, 0, width=2, fill="grey", arrow=LAST)

# Draw all points
for point in points:
    x = round(c_offset_x + (point[0] - min_x)*c_scale)
    y = round(c_offset_y - (point[1] - min_y)*c_scale)
    draw.create_oval(x - 2, y - 2, x + 2, y + 2, fill="black")

# Draw lines
delt_x = points[max_parallels_points[0]][0] - \
         points[max_parallels_points[1]][0]
delt_y = points[max_parallels_points[0]][1] - \
         points[max_parallels_points[1]][1]

for line in lines:
    x1 = round(c_offset_x + (line[0] - min_x)*c_scale)
    y1 = round(c_offset_y - (line[1] - min_y)*c_scale)
    x2 = round(c_offset_x + (line[2] - min_x)*c_scale)
    y2 = round(c_offset_y - (line[3] - min_y)*c_scale)
    delt_x_l = line[0] - line[2]
    delt_y_l = line[1] - line[3]
    # vector multiply for 2d vectors
    if delt_x * delt_y_l - delt_y * delt_x_l == 0:
        f_color = "green"
    else:
        f_color = "yellow"
    draw.create_line(x1, y1, x2, y2, fill = f_color)
    draw.create_oval(x1 - 2, y1 - 2, x1 + 2, y1 + 2, fill = "blue")
    draw.create_oval(x2 - 2, y2 - 2, x2 + 2, y2 + 2, fill = "blue")

# Draw two special points and line under them
draw.create_line(round(c_offset_x + \
                (points[max_parallels_points[0]][0] - min_x)*c_scale),\
                 round(c_offset_y - \
                (points[max_parallels_points[0]][1] - min_y)*c_scale),\
                 round(c_offset_x + \
                (points[max_parallels_points[1]][0] - min_x)*c_scale),\
                 round(c_offset_y - \
                (points[max_parallels_points[1]][1] - min_y)*c_scale),\
                 fill="green")

for i in max_parallels_points:
    x = round(c_offset_x + (points[i][0] - min_x)*c_scale)
    y = round(c_offset_y - (points[i][1] - min_y)*c_scale)
    draw.create_oval(x - 3, y - 3, x + 3, y + 3, fill="red")

# Update window
draw.pack()
root.mainloop()
