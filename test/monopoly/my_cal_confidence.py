#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""These functions calculate the similarity of two images of the same size."""

import cv2
import numpy as np
from airtest.aircv.utils import img_mat_rgb_2_gray


def cal_ccoeff_confidence(im_source, im_search, strict_brightness=False):
    """求取两张图片的可信度，使用TM_CCOEFF_NORMED方法."""
    # 扩展置信度计算区域
    im_source = cv2.copyMakeBorder(im_source, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
    # 加入取值范围干扰，防止算法过于放大微小差异
    im_source[0, 0] = 0
    im_source[0, 1] = 255

    im_source_gray, im_search_gray = img_mat_rgb_2_gray(im_source), img_mat_rgb_2_gray(im_search)
    res = cv2.matchTemplate(im_source_gray, im_search_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    base_confidence = max_val

    if strict_brightness:

        # 计算灰度图的亮度差异
        src_brightness = np.mean(im_source_gray)
        sch_brightness = np.mean(im_search_gray)
        brightness_diff = abs(src_brightness - sch_brightness) / 255.0

        # 计算灰度方差差异（置灰图像通常方差较小）
        src_variance = np.var(im_source_gray)
        sch_variance = np.var(im_search_gray)
        variance_diff = abs(src_variance - sch_variance) / (max(src_variance, sch_variance) + 1e-6)

        # 计算灰度直方图差异
        src_hist = cv2.calcHist([im_source_gray], [0], None, [256], [0, 256])
        sch_hist = cv2.calcHist([im_search_gray], [0], None, [256], [0, 256])
        hist_diff = cv2.compareHist(src_hist, sch_hist, cv2.HISTCMP_CORREL)
        hist_penalty = max(0, 1 - hist_diff) * 0.08  # 更温和的直方图惩罚

        # 更温和的惩罚力度
        brightness_penalty = max(0, brightness_diff - 0.05) * 1.5  # 降低亮度惩罚倍数
        variance_penalty = min(variance_diff * 0.15, 0.12)  # 降低方差惩罚

        # 限制总惩罚不超过基础confidence的30%
        total_penalty = brightness_penalty + variance_penalty + hist_penalty
        max_penalty = base_confidence * 0.3  # 最多惩罚30%
        total_penalty = min(total_penalty, max_penalty)

        final_confidence = base_confidence - total_penalty

        return max(0, final_confidence)

    return base_confidence


def cal_brightness_difference(img_src_rgb, img_sch_rgb):
    """计算两张图片的亮度差异."""
    # 转换为灰度图计算平均亮度
    src_gray = cv2.cvtColor(img_src_rgb, cv2.COLOR_BGR2GRAY)
    sch_gray = cv2.cvtColor(img_sch_rgb, cv2.COLOR_BGR2GRAY)

    src_brightness = np.mean(src_gray)
    sch_brightness = np.mean(sch_gray)

    # 计算亮度差异比例
    brightness_diff = abs(src_brightness - sch_brightness) / 255.0
    return brightness_diff


def cal_color_variance(img_src_rgb, img_sch_rgb):
    """计算颜色方差差异，用于检测置灰状态."""
    # 转换为HSV
    src_hsv = cv2.cvtColor(img_src_rgb, cv2.COLOR_BGR2HSV)
    sch_hsv = cv2.cvtColor(img_sch_rgb, cv2.COLOR_BGR2HSV)

    # 计算饱和度方差
    src_sat_var = np.var(src_hsv[:, :, 1])
    sch_sat_var = np.var(sch_hsv[:, :, 1])

    # 饱和度方差差异（置灰图像饱和度方差通常较小）
    sat_var_diff = abs(src_sat_var - sch_sat_var) / (max(src_sat_var, sch_sat_var) + 1e-6)

    return sat_var_diff


def cal_rgb_confidence(img_src_rgb, img_sch_rgb, strict_brightness=False):
    """同大小彩图计算相似度."""

    # 减少极限值对hsv角度计算的影响
    img_src_rgb = np.clip(img_src_rgb, 10, 245)
    img_sch_rgb = np.clip(img_sch_rgb, 10, 245)

    # 转HSV强化颜色的影响
    img_src_hsv = cv2.cvtColor(img_src_rgb, cv2.COLOR_BGR2HSV)
    img_sch_hsv = cv2.cvtColor(img_sch_rgb, cv2.COLOR_BGR2HSV)

    # 扩展置信度计算区域
    img_src_hsv = cv2.copyMakeBorder(img_src_hsv, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
    # 加入取值范围干扰，防止算法过于放大微小差异
    img_src_hsv[0, 0] = 0
    img_src_hsv[0, 1] = 255

    # 计算HSV三通道的confidence，存入hsv_confidence
    src_hsv_channels, sch_hsv_channels = cv2.split(img_src_hsv), cv2.split(img_sch_hsv)
    hsv_confidence = [0, 0, 0]

    for i in range(3):
        res_temp = cv2.matchTemplate(src_hsv_channels[i], sch_hsv_channels[i], cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res_temp)
        hsv_confidence[i] = max_val

    base_confidence = min(hsv_confidence)

    if strict_brightness:

        # 计算亮度差异惩罚
        brightness_diff = cal_brightness_difference(img_src_rgb, img_sch_rgb)
        color_var_diff = cal_color_variance(img_src_rgb, img_sch_rgb)

        # 更温和的惩罚力度
        brightness_penalty = max(0, brightness_diff - 0.08) * 1.5  # 降低亮度惩罚
        color_penalty = min(color_var_diff * 0.3, 0.12)  # 降低颜色惩罚

        # 额外的饱和度检测
        src_hsv_orig = cv2.cvtColor(img_src_rgb, cv2.COLOR_BGR2HSV)
        sch_hsv_orig = cv2.cvtColor(img_sch_rgb, cv2.COLOR_BGR2HSV)

        src_saturation = np.mean(src_hsv_orig[:, :, 1])
        sch_saturation = np.mean(sch_hsv_orig[:, :, 1])
        saturation_diff = abs(src_saturation - sch_saturation) / 255.0

        saturation_penalty = max(0, saturation_diff - 0.08) * 1.2  # 降低饱和度惩罚

        # 限制总惩罚不超过基础confidence的30%
        total_penalty = brightness_penalty + color_penalty + saturation_penalty
        max_penalty = base_confidence * 0.3
        total_penalty = min(total_penalty, max_penalty)

        final_confidence = base_confidence - total_penalty

        return max(0, final_confidence)

    return base_confidence


def cal_ccoeff_confidence_with_alpha(img_src_rgb, img_sch_rgba, strict_brightness=False):
    """带透明通道的灰度相似度计算."""
    # 提取RGB和Alpha通道
    img_sch_rgb = img_sch_rgba[:, :, :3]
    alpha_mask = img_sch_rgba[:, :, 3]

    # 创建掩码 (alpha > 0的区域)
    mask = (alpha_mask > 0).astype(np.uint8) * 255

    if cv2.countNonZero(mask) == 0:
        return 0.0

    # 扩展置信度计算区域 - 同时扩展源图像、模板图像和掩码
    img_src_rgb = cv2.copyMakeBorder(img_src_rgb, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
    img_sch_rgb = cv2.copyMakeBorder(img_sch_rgb, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
    mask = cv2.copyMakeBorder(mask, 10, 10, 10, 10, cv2.BORDER_REPLICATE)

    # 加入取值范围干扰，防止算法过于放大微小差异
    img_src_rgb[0, 0] = 0
    img_src_rgb[0, 1] = 255
    img_sch_rgb[0, 0] = 0
    img_sch_rgb[0, 1] = 255

    # 转换为灰度图
    img_src_gray = img_mat_rgb_2_gray(img_src_rgb)
    img_sch_gray = img_mat_rgb_2_gray(img_sch_rgb)

    # 确保尺寸一致
    if img_sch_gray.shape != mask.shape:
        mask = cv2.resize(mask, (img_sch_gray.shape[1], img_sch_gray.shape[0]))

    # 使用掩码进行模板匹配
    result = cv2.matchTemplate(img_src_gray, img_sch_gray, cv2.TM_CCOEFF_NORMED, mask=mask)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    base_confidence = max_val

    if strict_brightness:
        # 只对非透明区域计算亮度差异
        mask_bool = mask > 0
        if np.any(mask_bool):
            src_masked = img_src_rgb[mask_bool]
            sch_masked = img_sch_rgb[mask_bool]

            if len(src_masked) > 0 and len(sch_masked) > 0:
                # 计算掩码区域的平均亮度
                src_gray_masked = cv2.cvtColor(src_masked.reshape(-1, 1, 3), cv2.COLOR_BGR2GRAY)
                sch_gray_masked = cv2.cvtColor(sch_masked.reshape(-1, 1, 3), cv2.COLOR_BGR2GRAY)

                src_brightness = np.mean(src_gray_masked)
                sch_brightness = np.mean(sch_gray_masked)
                brightness_diff = abs(src_brightness - sch_brightness) / 255.0

                # 更温和的惩罚
                brightness_penalty = max(0, brightness_diff - 0.08) * 1.2

                # 限制惩罚不超过30%
                max_penalty = base_confidence * 0.3
                brightness_penalty = min(brightness_penalty, max_penalty)

                final_confidence = base_confidence - brightness_penalty

                return max(0, final_confidence)

    return base_confidence


def cal_rgb_confidence_with_alpha(img_src_rgb, img_sch_rgba, strict_brightness=False):
    """带透明通道的RGB相似度计算."""
    # 提取RGB和Alpha通道
    img_sch_rgb = img_sch_rgba[:, :, :3]
    alpha_mask = img_sch_rgba[:, :, 3]

    # 创建掩码
    mask = (alpha_mask > 0).astype(np.uint8) * 255

    if cv2.countNonZero(mask) == 0:
        return 0.0

    # 减少极限值对hsv角度计算的影响
    img_src_rgb = np.clip(img_src_rgb, 10, 245)
    img_sch_rgb = np.clip(img_sch_rgb, 10, 245)

    # 转HSV强化颜色的影响
    img_src_hsv = cv2.cvtColor(img_src_rgb, cv2.COLOR_BGR2HSV)
    img_sch_hsv = cv2.cvtColor(img_sch_rgb, cv2.COLOR_BGR2HSV)

    # 扩展置信度计算区域 - 同时扩展源图像、模板图像和掩码
    img_src_hsv = cv2.copyMakeBorder(img_src_hsv, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
    img_sch_hsv = cv2.copyMakeBorder(img_sch_hsv, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
    mask_extended = cv2.copyMakeBorder(mask, 10, 10, 10, 10, cv2.BORDER_REPLICATE)

    # 加入取值范围干扰，防止算法过于放大微小差异
    img_src_hsv[0, 0] = 0
    img_src_hsv[0, 1] = 255
    img_sch_hsv[0, 0] = 0
    img_sch_hsv[0, 1] = 255

    # 计算HSV三通道的confidence，存入hsv_confidence
    src_hsv_channels = cv2.split(img_src_hsv)
    sch_hsv_channels = cv2.split(img_sch_hsv)
    hsv_confidence = [0, 0, 0]

    for i in range(3):
        # 确保掩码和模板通道尺寸一致
        if sch_hsv_channels[i].shape != mask_extended.shape:
            current_mask = cv2.resize(mask_extended, (sch_hsv_channels[i].shape[1], sch_hsv_channels[i].shape[0]))
        else:
            current_mask = mask_extended

        result = cv2.matchTemplate(src_hsv_channels[i], sch_hsv_channels[i], cv2.TM_CCOEFF_NORMED, mask=current_mask)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        hsv_confidence[i] = max_val

    base_confidence = min(hsv_confidence)

    if strict_brightness:
        # 只对非透明区域计算亮度和颜色差异
        mask_bool = (alpha_mask > 0)
        if np.any(mask_bool):
            src_masked_area = img_src_rgb[mask_bool]
            sch_masked_area = img_sch_rgb[mask_bool]

            if len(src_masked_area) > 0 and len(sch_masked_area) > 0:
                # 重塑为图像格式进行颜色空间转换
                src_reshaped = src_masked_area.reshape(-1, 1, 3).astype(np.uint8)
                sch_reshaped = sch_masked_area.reshape(-1, 1, 3).astype(np.uint8)

                # 计算亮度差异
                src_gray_vals = cv2.cvtColor(src_reshaped, cv2.COLOR_BGR2GRAY).flatten()
                sch_gray_vals = cv2.cvtColor(sch_reshaped, cv2.COLOR_BGR2GRAY).flatten()
                brightness_diff = abs(np.mean(src_gray_vals) - np.mean(sch_gray_vals)) / 255.0

                # 计算饱和度差异
                src_hsv_vals = cv2.cvtColor(src_reshaped, cv2.COLOR_BGR2HSV)
                sch_hsv_vals = cv2.cvtColor(sch_reshaped, cv2.COLOR_BGR2HSV)
                src_saturation = np.mean(src_hsv_vals[:, 0, 1])
                sch_saturation = np.mean(sch_hsv_vals[:, 0, 1])
                saturation_diff = abs(src_saturation - sch_saturation) / 255.0

                # 计算饱和度方差差异
                src_sat_var = np.var(src_hsv_vals[:, 0, 1])
                sch_sat_var = np.var(sch_hsv_vals[:, 0, 1])
                sat_var_diff = abs(src_sat_var - sch_sat_var) / (max(src_sat_var, sch_sat_var) + 1e-6)

                # 更温和的惩罚力度
                brightness_penalty = max(0, brightness_diff - 0.08) * 1.5
                saturation_penalty = max(0, saturation_diff - 0.08) * 1.2
                color_penalty = min(sat_var_diff * 0.3, 0.12)

                # 限制总惩罚不超过30%
                total_penalty = brightness_penalty + saturation_penalty + color_penalty
                max_penalty = base_confidence * 0.3
                total_penalty = min(total_penalty, max_penalty)

                final_confidence = base_confidence - total_penalty

                return max(0, final_confidence)

    return base_confidence


def detect_grayscale_button(img_src_rgb, img_sch_rgb, alpha_mask=None):
    """专门检测按钮是否为灰度状态."""
    if alpha_mask is not None:
        # 如果有透明通道，只检测非透明区域
        mask_bool = alpha_mask > 0
        if not np.any(mask_bool):
            return False, 0.0

        src_area = img_src_rgb[mask_bool]
        sch_area = img_sch_rgb[mask_bool]
    else:
        src_area = img_src_rgb.reshape(-1, 3)
        sch_area = img_sch_rgb.reshape(-1, 3)

    # 计算饱和度
    src_hsv = cv2.cvtColor(src_area.reshape(-1, 1, 3), cv2.COLOR_BGR2HSV)
    sch_hsv = cv2.cvtColor(sch_area.reshape(-1, 1, 3), cv2.COLOR_BGR2HSV)

    src_saturation = np.mean(src_hsv[:, 0, 1])
    sch_saturation = np.mean(sch_hsv[:, 0, 1])

    # 如果饱和度差异很大，可能是置灰状态
    saturation_diff = abs(src_saturation - sch_saturation) / 255.0

    # 计算亮度
    src_value = np.mean(src_hsv[:, 0, 2])
    sch_value = np.mean(sch_hsv[:, 0, 2])

    value_diff = abs(src_value - sch_value) / 255.0

    # 更温和的检测标准
    is_grayscale = saturation_diff > 0.12 or value_diff > 0.15
    confidence_penalty = (saturation_diff + value_diff) * 0.8

    return is_grayscale, confidence_penalty