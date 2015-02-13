#-*- coding: utf8 -*-

# http://homepage.divms.uiowa.edu/~luke/xls/glim/glim/node8.html
# http://dbaker.50webs.com/method.html
# http://www.r-bloggers.com/mlb-rankings-using-the-bradley-terry-model/
# http://angrystatistician.blogspot.kr/2013_04_01_archive.html

# http://blog.naver.com/PostView.nhn?blogId=iizs&logNo=91609499
teams = ["KIA", "SK", "Doosan", "Lotte", "Samsung", "Heroes", "LG", "Hanwha"]
wins_losses = [ [81, 4, 48], [80, 6, 47], [71, 2, 60], [66, 0, 67], [64, 0, 69], [60, 1, 72], [54, 4, 75], [46, 3, 84] ]
pyth = [ 1.0 * wins_losses[i][0]**2 / (wins_losses[i][0]**2 + wins_losses[i][2]**2) for i in range(8) ]
print '\n2009년 기준\n팀', teams
print '피타고리안 승률', pyth
# 정확하진 않지만 대략 비슷
print '팀 피타고리안 승률 / 최고 피타고리안 승률', [p / max(pyth) for p in pyth]

# http://ocean.kisti.re.kr/downfile/volume/kss/GCGHDE/2011/v24n5/GCGHDE_2011_v24n5_915.pdf
t = [ "SK", "Doosan", "Lotte", "Samsung", "Hanhwa", "KIA", "Heroes", "LG" ]
data = [ [ [ 60, 65 ], [ 73, 48 ], [ 83, 43 ] ],
         [ [ 63, 60 ], [ 70, 54 ], [ 70, 56 ] ],
         [ [ 50, 73 ], [ 55, 68 ], [ 69, 57 ] ],
         [ [ 73, 50 ], [ 62, 60 ], [ 65, 61 ] ],
         [ [ 67, 57 ], [ 67, 57 ], [ 64, 62 ] ],
         [ [ 64, 59 ], [ 51, 74 ], [ 57, 69 ] ],
         [ [ 70, 55 ], [ 56, 69 ], [ 50, 76 ] ],
         [ [ 47, 75 ], [ 58, 62 ], [ 46, 80 ] ] ]
w_l_total = [ (d[0][0] + d[1][0] + d[2][0], d[0][1] + d[1][1] + d[2][1]) for d in data ]
print '\n2006~08년 기준\n팀', t
print '2006~08 승패 합', w_l_total
pyth = [1.0 * d[0]**2 / (d[0]**2 + d[1]**2) for d in w_l_total]
print '피타고리안 승률', pyth
# 정확하진 않지만 대략 비슷
print '팀 피타고리안 승률 / 피타고리안 승률 총합', [p / sum(pyth) for p in pyth]
pi = [ [ 0.3096, 0.0706, 0.16386 ],
       [ 0.2439, 0.0700, 0.14367 ],
       [ 0.1142, 0.0700, 0.11086 ],
       [ 0.2340, 0.0700, 0.14086 ],
       [ 0.2174, 0.0699, 0.13626 ],
       [ 0.0937, 0.0696, 0.10639 ],
       [ 0.1098, 0.0697, 0.10987 ],
       [ 0, 0, 0.08823 ] ]
