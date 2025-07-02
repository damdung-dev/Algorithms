import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D

# Đọc dữ liệu
df = pd.read_csv("C:\\ProgramData\\MySQL\\MySQL Server 9.2\\Uploads\\student-scores.csv")

# Chọn các cột điểm
score_columns = [
    "math_score", "history_score", "physics_score", "chemistry_score",
    "biology_score", "english_score", "geography_score"
]
scores = df[score_columns]

# Chuẩn hóa dữ liệu
scaler = StandardScaler()
scores_scaled = scaler.fit_transform(scores)

# SVD
U, S, VT = np.linalg.svd(scores_scaled, full_matrices=False)

# Giảm chiều còn 3 thành phần đầu
S_matrix = np.diag(S[:3])
reduced_data = np.dot(U[:, :3], S_matrix)

# Vẽ biểu đồ 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(reduced_data[:, 0], reduced_data[:, 1], reduced_data[:, 2], c='blue', alpha=0.7)

ax.set_title('Biểu diễn dữ liệu học sinh theo 3 thành phần chính')
ax.set_xlabel('Thành phần chính 1')
ax.set_ylabel('Thành phần chính 2')
ax.set_zlabel('Thành phần chính 3')
plt.show()
