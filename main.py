import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# reading the csv
df = pd.read_csv('ece_results_3_1', header=0)
df = df[df['grade'] != 'COMPLETED']
df = df.reset_index(drop=True)

# mapping grade points according to grade
grades_array = np.array(df['grade'])
grades_map = {
    'O': 10,
    'S': 9,
    'A': 8,
    'B': 7,
    'C': 6,
    'D': 5,
    'F': 0,
    'ABSENT': 0,
}
for i, grade in np.ndenumerate(grades_array):
    grades_array[i] = int(grades_map[grades_array[i]])
df['grade_points'] = grades_array

# calculating sgpa for each student and storing it in array
i = 0
sgpa_array = []
while (i < len(grades_array)):
    sgpa_array.append(round((sum(grades_array[i + 0:i + 5]) * 3 + sum(grades_array[i + 5:i + 8]) * 2) / 21, 2))
    i += 8
sgpa_array = np.array(sgpa_array)

# make a new df with each students sgpa
sgpa_df = df.groupby('htno')
sgpa_df_modified = pd.DataFrame()
sgpa_df_modified['htno'] = pd.DataFrame(sgpa_df)[0]
sgpa_df_modified['sgpa'] = sgpa_array
sgpa_df = sgpa_df_modified
sgpa_df.to_csv('htno_and_sgpa', index = False, header = True)

# plotting
mean_sgpa = round(sgpa_df['sgpa'].mean(), 2)
std_sgpa = round(sgpa_df['sgpa'].std(), 2)
plt.style.use('ggplot')
plt.hist(sgpa_df['sgpa'], color='skyblue', linewidth=1, edgecolor='black')
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], color='black')
plt.yticks(color='black')
plt.xlabel('SGPA', color='darkblue')
plt.ylabel('NO OF STUDENTS', color='darkblue')
plt.title('ECE 3-1 RESULTS', color='green', fontsize=17)
plt.text(1, 50, 'Mean = ' + str(mean_sgpa), color='black', fontsize=15)
plt.show()

# # subject wise analysis
#
# # 1) digital communications (R1631044)
# plt.clf()
# plt.style.use('ggplot')
# dc_df = df[df['subcode'] == 'R1631044']
# plt.ylabel('NO OF STUDENTS', color='darkblue')
# plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], color='black')
# plt.xlabel('GRADE_POINTS', color='darkblue')
# plt.yticks(color='black')
# plt.title('Digital Communications (R16) 2021', color='green', fontsize=17)
# plt.hist(dc_df['grade_points'], color='orange', linewidth=1, edgecolor='black')
# mean_grade_points_dc = round(dc_df['grade_points'].mean(), 2)
# dc_failures = len(dc_df[dc_df['grade_points'] == 0])
#
# plt.text(1.4, 35, 'avg_grade_points = ' + str(mean_grade_points_dc), color='black', fontsize=12)
# plt.text(1.4, 30, 'failures = ' + str(dc_failures), color='black', fontsize=12)
# plt.show()
