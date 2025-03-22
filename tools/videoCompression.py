import os
import subprocess
import time
from pathlib import Path


def compress_video(input_path, output_path, crf=23):
    """
    压缩视频文件
    :param input_path: 输入视频路径
    :param output_path: 输出视频路径
    :param crf: 压缩质量（0-51，0为无损，23为默认，51质量最差）
    """
    try:
        # ffmpeg命令
        command = [
            'ffmpeg',
            '-i', str(input_path),  # 输入文件
            '-c:v', 'libx264',  # 视频编码器
            '-crf', str(crf),  # 压缩质量
            '-c:a', 'aac',  # 音频编码器
            '-preset', 'medium',  # 压缩速度
            '-an',  # 去除音频
            str(output_path)  # 输出文件
        ]

        # 执行命令
        subprocess.run(command, check=True)
        print(f"成功压缩: {input_path.name}")

    except subprocess.CalledProcessError as e:
        print(f"压缩失败 {input_path.name}: {str(e)}")


def batch_compress_videos(input_folder, output_folder, crf=23):
    """
    批量压缩文件夹中的视频
    :param input_folder: 输入文件夹路径
    :param output_folder: 输出文件夹路径
    :param crf: 压缩质量
    """
    # 创建输出文件夹
    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)

    # 获取所有MP4文件
    input_path = Path(input_folder)
    video_files = list(input_path.glob('*.mp4'))

    print(f"找到 {len(video_files)} 个MP4文件")

    # 批量处理视频
    for video_file in video_files:
        output_file = output_path / f"{video_file.name}"
        compress_video(video_file, output_file, crf)

def get_subfolders(path):
    """获取指定目录下的直接子文件夹路径列表"""
    subfolders = []
    # 确保路径存在且是目录
    if not os.path.isdir(path):
        return []

    # 遍历目录条目
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        # 过滤出目录且不包含隐藏文件 (可选)
        if os.path.isdir(full_path) and not entry.startswith('.'):
            subfolders.append(full_path)

    return subfolders

def record_start(file_name):
    live_video = subprocess.Popen(
        'ffmpeg -f gdigrab -offset_x 0 -offset_y 70 -video_size 730x355 -i title="MainProject - Entry - Android - Unity 2021.3.30f1 <DX11>"  -vcodec libx264 -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -pix_fmt yuv420p {} -y -crf 32 -framerate 15 -tune fastdecode -preset slow -g 30 -an'.format(
            file_name), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    return live_video
def record_end(live_video):
    # 发送q指令给ffmpeg，退出录屏
    live_video.stdin.write('q'.encode("GBK"))
    live_video.communicate()





def main():
    # 设置输入和输出文件夹
    input_folder = "C:/Users/TU/Desktop/装备"  # 替换为你的输入文件夹路径
    output_folder = "C:/Users/TU/Desktop/装备测试"  # 替换为你的输出文件夹路径


    # 执行批量压缩

    batch_compress_videos(input_folder, output_folder)


if __name__ == "__main__":
    main()