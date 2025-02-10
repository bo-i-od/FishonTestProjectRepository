import os
import subprocess
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


def main():
    # 设置输入和输出文件夹
    input_folder = "C:/Users/TU/Desktop/战斗"  # 替换为你的输入文件夹路径
    output_folder = "C:/Users/TU/Desktop/战斗压缩"  # 替换为你的输出文件夹路径

    # 压缩质量设置（可调整）
    crf = 35  # 值越大，文件越小，质量越差

    # 执行批量压缩
    batch_compress_videos(input_folder, output_folder, crf)


if __name__ == "__main__":
    main()
