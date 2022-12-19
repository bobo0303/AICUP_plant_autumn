import os, random, shutil, cv2,csv

frompath = r'E:\plant_33_train_val_test_fixed_croped_up\test/'
frompath_c = os.listdir(frompath)

print(frompath_c)

csvv = r'C:\Users\wiwiw\OneDrive\桌面/topk_ids_deit3_large_patch16_224_in21ft1k_public.csv'
csvvv = r'C:\Users\wiwiw\OneDrive\桌面/topk_ids_deit3_large_patch16_224_in21ft1k_private.csv'

with open(csvv, newline='') as crop_csv_file:
	crop_csv_rows = csv.reader(crop_csv_file)
	with open(csvvv, newline='') as crop_csv_file2:
		crop_csv_rows2 = csv.reader(crop_csv_file2)
		with open(r'C:\Users\wiwiw\OneDrive\桌面/topk_ids_deit3_large_patchtv16_224_in21ft1k_new.csv', 'w') as f:
			writeCsv = csv.writer(f)
			writeCsv.writerow(['filename', 'label'])
			for row in crop_csv_rows:
				writeCsv.writerow([row[0],frompath_c[int(row[1])]])
			for row2 in crop_csv_rows2:
				writeCsv.writerow([row2[0], frompath_c[int(row2[1])]])


