import os
import subprocess

def convert_flv_to_mp4(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            if filename.lower().endswith('.flv'):  # 仅处理 .flv 文件
                flv_path = os.path.join(root, filename)
                mp4_path = os.path.splitext(flv_path)[0] + '.mp4'
                
                # 构建 FFmpeg 命令（避免手动拼接字符串）
                cmd = [
                    'ffmpeg',
                    '-i', flv_path,
                    '-c:v', 'copy',  # 直接复制视频流
                    '-c:a', 'copy',  # 直接复制音频流
                    '-y',            # 覆盖已存在的文件
                    mp4_path
                ]
                
                # 执行命令并捕获错误
                try:
                    subprocess.run(cmd, check=True)
                    print(f'[成功] 转换完成: {mp4_path}')
                except subprocess.CalledProcessError as e:
                    print(f'[错误] 转换失败: {flv_path}')

if __name__ == '__main__':
    target_dir = r'd:\Users\Administrator\Downloads\flv视频'  # 替换为你的实际路径
    convert_flv_to_mp4(target_dir)
    print("全部转换完成！")
