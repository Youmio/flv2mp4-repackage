import os
import subprocess

def convert_flv_to_mp4(root_dir):
    for root, dirs, files in os.walk(root_dir):
        print(f"扫描目录: {root}")
        for filename in files:
            file_lower = filename.lower()
            if file_lower.endswith('.flv'):
                flv_path = os.path.join(root, filename)
                mp4_path = os.path.splitext(flv_path)[0] + '.mp4'
                print(f"正在转换: {flv_path} → {mp4_path}")
                
                cmd = [
                    'ffmpeg',
                    '-hide_banner',
                    '-loglevel', 'error',
                    '-i', flv_path,
                    '-c:v', 'copy',
                    '-c:a', 'copy',
                    '-y',
                    mp4_path
                ]
                
                try:
                    result = subprocess.run(cmd, check=True, stderr=subprocess.PIPE, text=True)
                    print(f"[成功] 转换完成: {mp4_path}")
                except subprocess.CalledProcessError as e:
                    print(f"[错误] 转换失败: {flv_path}")
                    print(f"错误详情: {e.stderr}")

if __name__ == '__main__':
    # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"目标目录: {script_dir}")
    convert_flv_to_mp4(script_dir)
    print("全部转换完成！")
