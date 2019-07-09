count = 72

for i in range(count):
    index = i + 1
    print(
        r'"c:\Program Files\Blender Foundation\Blender\blender.exe" '
        r'--background --python ./render_blender.py -- '
        r'--output_folder D:\Projects\SIIE\tiny_model\models_google_poly\{}\rendering\ '
        r'D:\Projects\SIIE\tiny_model\models_google_poly\{}\model.obj'.format(index, index))
print()

for i in range(count):
    index = i + 1
    print(r'meshlabserver  -i D:\Projects\SIIE\tiny_model\models_google_poly\{}\model.obj '
          r'-o D:\Projects\SIIE\tiny_model\models_google_poly\{}\model.xyz '
          r'-s c:\Users\bunny\Desktop\upsample.mlx'.format(index, index))
print()

for i in range(count):
    index = i + 1
    print(r'python 2_generate_normal.py models_google_poly/{}/'.format(index))
    print(r'python 3_camera_transform.py models_google_poly/{}/'.format(index))
print()

for i in range(count):
    index = i + 1
    for j in range(24):
        print(r'Data/models_google_poly/{}/rendering/{:02d}.dat'.format(index, j))
print()

for i in range(count):
    index = i + 1
    for j in range(24):
        print(r'python demo.py --image Data/models_google_poly/{}/rendering/{:02d}.png'.format(index, j))
print()