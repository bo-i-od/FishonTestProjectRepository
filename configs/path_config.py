# Fishon 默认相机配置（CameraRegistry 初始化用）
# path_node:   节点路径（该节点 + 子树共享此相机）
# path_camera: 相机节点路径（GameObject.Find 可定位）
# camera_type: "2d" 或 "3d"
DEFAULT_CAMERA_CONFIG = [
    {"path_node": "UICanvas", "path_camera": "UICamera_Front", "camera_type": "2d"},
    {"path_node": "HomeCanvas", "path_camera": "Camera3D", "camera_type": "3d"},
]
