import math
import matplotlib.pyplot as plt
import numpy as np

testing = input('Use the testing mode? All the values are determined automatically (Yes/No): ').lower().strip() == 'yes'

if testing is True:
    scatter_yes = False
else:
    print('Use ".scatter?" (The plot is made of dots)')
    scatter_yes = input('Otherwise, ".plot_surface" is used. (The plot is made of the surface) (Yes/No): ').lower().strip() == 'yes'
if testing is True:
    wave_lang = 4
    wave_amplitude = 2
else:
    wave_lang = float(input('Wavelength (m): '))
    wave_amplitude = float(input('Wave amplitude (m): '))

k = 2*np.pi / wave_lang


def wave(x):
    y = wave_amplitude * np.sin(k*x + 0)
    return y


if testing is True:
    s = 40
else:
    s = int(input('Square area size (one side) (m): '))

y_s = []
x_s = []


for h in np.arange(s):
    for l in np.arange(s):
        x_s.append(h)
        y_s.append(l)
if testing is True:
    x_source_1 = 20
    y_source_1 = 35
    x_source_2 = 20
    y_source_2 = 5
else:
    x_source_1 = float(input('X-coordinate of the first source (m): '))
    y_source_1 = float(input('Y-coordinate of the first source (m): '))
    x_source_2 = float(input('X-coordinate of the second source (m): '))
    y_source_2 = float(input('Y-coordinate of the second source (m): '))

while x_source_1 > s or y_source_1 > s:
    print('The area does not contain the coordinates you used for the first source.')
    print('Please input different coordinates for the first source:')
    x_source_1 = float(input('X-coordinate of the first source (m): '))
    y_source_1 = float(input('Y-coordinate of the first source (m): '))

while x_source_2 > s or y_source_2 > s:
    print('The area does not contain the coordinates you used for the second source.')
    print('Please input different coordinates for the second source:')
    x_source_2 = float(input('X-coordinate of the second source (m): '))
    y_source_2 = float(input('Y-coordinate of the second source (m): '))

distance_1 = []
distance_2 = []

for i, j in zip(x_s, y_s):
    lang_distance_1 = math.sqrt((x_source_1 - i) ** 2 + (y_source_1 - j) ** 2)
    lang_distance_2 = math.sqrt((x_source_2 - i) ** 2 + (y_source_2 - j) ** 2)

    distance_1.append(lang_distance_1)
    distance_2.append(lang_distance_2)

if testing is True:
    print('The distances has been calculated')

y_when_x_is_distance_1 = []
y_when_x_is_distance_2 = []

for q in distance_1:
    y_when_x_is_distance_1.append(wave(q))

if testing is True:
    print('The heights for the distances from the first source have been calculated')

for q in distance_2:
    y_when_x_is_distance_2.append(wave(q))

if testing is True:
    print('The heights for the distances from the second source have been calculated')

z_final_height = []

for he_1, he_2 in zip(y_when_x_is_distance_1, y_when_x_is_distance_2):
    he_all = (he_1 + he_2)
    z_final_height.append(he_all)

if testing is True:
    print('The final heights for each point have been calculated')

z_o_for_red_thing = [0] * s**2

z_sources = []
sub = round(max(z_final_height) + 1, 0)
sub_2 = 0
while sub != round(min(z_final_height), 0):
    z_sources.append(sub)
    sub -= 1
    sub_2 += 1

if testing is True:
    print('The points of the sources have been created')

x_source_1 = [x_source_1] * sub_2
y_source_1 = [y_source_1] * sub_2
x_source_2 = [x_source_2] * sub_2
y_source_2 = [y_source_2] * sub_2

if testing is True:
    print('The points of the sources have been corrected')

if scatter_yes is False:
    z_final_height = np.array(z_final_height).reshape(s, s)
    x_s = np.array(x_s).reshape(s, s)
    y_s = np.array(y_s).reshape(s, s)
    z_o_for_red_thing = np.array(z_o_for_red_thing).reshape(s, s)
    if testing is True:
        print('The arrays for all the points and heights have been created')

fig = plt.figure(figsize=(7, 4))
ax_3d = fig.add_subplot(projection='3d')

if testing is True:
    print('The figure has been created')

ax_3d.set_xlabel('x, (m)')
ax_3d.set_ylabel('y, (m)')
ax_3d.set_zlabel('z (Height), (m)')

if testing is True:
    print('The axes have been named')

if scatter_yes is False:
    ax_3d.plot3D(x_source_1, y_source_1, z_sources, color='red')
    ax_3d.plot3D(x_source_2, y_source_2, z_sources, color='red')
    ax_3d.plot_surface(x_s, y_s, z_final_height, cmap='plasma', alpha=0.9)
else:
    ax_3d.plot3D(x_source_1, y_source_1, z_sources, color='red')
    ax_3d.plot3D(x_source_2, y_source_2, z_sources, color='red')
    ax_3d.scatter(x_s, y_s, z_final_height)

plt.show()
