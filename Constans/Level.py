from Constans.Valuable import WIDTH,HEIGHT

#level_a constans
w = WIDTH/8
h = 30
offset_w = w/6
offset_h = 10

level_a = [[0,45,w,h], [offset_w+w,45,w,h], [(offset_w+w)*2,45,w,h], [(offset_w+w)*3,45,w,h], [(offset_w+w)*4,45,w,h], [(offset_w+w)*5,45,w,h], [(offset_w+w)*6,45,w,h],
            [0,45+h+offset_h,w,h], [offset_w+w,45+h+offset_h,w,h], [(offset_w+w)*2,45+h+offset_h,w,h], [(offset_w+w)*3,45+h+offset_h,w,h], [(offset_w+w)*4,45+h+offset_h,w,h], [(offset_w+w)*5,45+h+offset_h,w,h], [(offset_w+w)*6,45+h+offset_h,w,h],
            [0,45+(h+offset_h)*2,w,h], [offset_w+w,45+(h+offset_h)*2,w,h], [(offset_w+w)*2,45+(h+offset_h)*2,w,h], [(offset_w+w)*3,45+(h+offset_h)*2,w,h], [(offset_w+w)*4,45+(h+offset_h)*2,w,h], [(offset_w+w)*5,45+(h+offset_h)*2,w,h], [(offset_w+w)*6,45+(h+offset_h)*2,w,h]]

level_b = [[0,45,w,h], [(offset_w+w)*2,45,w,h], [(offset_w+w)*4,45,w,h], [(offset_w+w)*6,45,w,h],
            [0,45+h+offset_h,w,h], [offset_w+w,45+h+offset_h,w,h], [(offset_w+w)*3,45+h+offset_h,w,h], [(offset_w+w)*5,45+h+offset_h,w,h], [(offset_w+w)*6,45+h+offset_h,w,h],
            [offset_w+w,45+(h+offset_h)*2,w,h], [(offset_w+w)*2,45+(h+offset_h)*2,w,h], [(offset_w+w)*3,45+(h+offset_h)*2,w,h], [(offset_w+w)*4,45+(h+offset_h)*2,w,h], [(offset_w+w)*5,45+(h+offset_h)*2,w,h]]

level = [level_a, level_b]