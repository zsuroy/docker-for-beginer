# 使用 nginx 官方基础镜像
FROM nginx:alpine

# 将本地的 index.html, style.css 和 avatar.jpg 复制到镜像中的 nginx html 目录下
COPY index.html /usr/share/nginx/html
COPY style.css /usr/share/nginx/html
COPY entrypoint.sh /entrypoint.sh
COPY suroy.png /usr/share/nginx/html/

# 给予 entrypoint.sh 可执行权限
RUN chmod +x /entrypoint.sh

# 运行 entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
