import os
import subprocess

def convert_flv_to_mp3(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            if filename.lower().endswith('.flv'):
                flv_path = os.path.join(root, filename)
                mp3_path = os.path.splitext(flv_path)[0] + '.mp3'
                
                # 构建 FFmpeg 命令
                cmd = [
                    'ffmpeg',
                    '-i', flv_path,          # 输入文件
                    '-vn',                   # 禁用视频流
                    '-acodec', 'libmp3lame', # 指定 MP3 编码器
                    '-ab', '192k',           # 音频比特率 192kbps
                    '-ac', '2',              # 双声道
                    '-y',                    # 覆盖已存在的文件
                    mp3_path
                ]
                
                try:
                    subprocess.run(cmd, check=True, stderr=subprocess.PIPE, text=True)
                    print(f'[成功] 转换完成: {mp3_path}')
                except subprocess.CalledProcessError as e:
                    print(f'[错误] 转换失败: {flv_path}')
                    print(f'错误信息: {e.stderr}')

if __name__ == '__main__':
    target_dir = r''d:\Users\Administrator\Downloads\flv视频'  # 替换为你的实际路径
    convert_flv_to_mp3(target_dir)
    print("全部转换完成！")
