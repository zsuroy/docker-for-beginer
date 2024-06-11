import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 创建一个绘图区域
fig, ax = plt.subplots(figsize=(6, 6))

# 设置背景颜色
fig.patch.set_facecolor('#f4f4f4')
ax.set_facecolor('#f4f4f4')

# 隐藏坐标轴
ax.axis('off')

# 绘制一个大的圆形作为背景
circle = patches.Circle((0.5, 0.5), 0.4, linewidth=2, edgecolor='#333', facecolor='#fff')
ax.add_patch(circle)

# 添加一个小的 Docker logo 样式的鲸鱼
whale_body = patches.Rectangle((0.35, 0.4), 0.3, 0.1, linewidth=1, edgecolor='#333', facecolor='#333')
whale_tail = patches.Polygon([[0.35, 0.45], [0.3, 0.5], [0.35, 0.5]], closed=True, linewidth=1, edgecolor='#333', facecolor='#333')
ax.add_patch(whale_body)
ax.add_patch(whale_tail)

# 添加主页图标
house_base = patches.Rectangle((0.45, 0.5), 0.1, 0.15, linewidth=1, edgecolor='#333', facecolor='#999')
house_roof = patches.Polygon([[0.45, 0.65], [0.55, 0.65], [0.5, 0.7]], closed=True, linewidth=1, edgecolor='#333', facecolor='#333')
ax.add_patch(house_base)
ax.add_patch(house_roof)

# 添加文本
plt.text(0.5, 0.3, 'Docker Homepage', horizontalalignment='center', verticalalignment='center', fontsize=12, color='#333')

# 显示图像
plt.show()
