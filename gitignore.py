import os

files = ['sales-201712', 'sales-201801', 'sales-201802', 'sales-201803', 'sales-201804', 'sales-201805', 'sales-201806', 'sales-201807', 'sales-201808', 'sales-201809', 'sales-201810', 'sales-201811', 'sales-201812', 'sales-201901', 'sales-201902', 'sales-201903', 'sales-201904']
for fil in files:
    file_name = fil
    path = 'data/{}.txt'.format(file_name)
    os.remove(path)