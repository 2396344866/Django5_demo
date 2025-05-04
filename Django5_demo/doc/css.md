### 1. 卡片悬浮动画与深度阴影
```css
.card {
    /* ...原有样式保留... */
    box-shadow: 0 10px 20px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.15);
}
```
### 2. 输入框增强效果
```css
.form-control {
    /* ...原有样式保留... */
    background: linear-gradient(to right, #ffffff, #f9f9f9);
    border: 1px solid #ccc;
    transition: all 0.2s ease;
}

.form-control:focus {
    border-color: #0062cc;
    box-shadow: 0 0 12px rgba(0, 98, 204, 0.35);
    background: linear-gradient(to right, #e8f3ff, #d9ecff);
}
```
### 3错误提示脉冲动画
```css
@keyframes pulse {
    0% {
        box-shadow: 0 0 0 0 rgba(220, 53, 69, 0.4);
    }
    70% {
        box-shadow: 0 0 0 10px rgba(220, 53, 69, 0);
    }
    100% {
        box-shadow: 0 0 0 0 rgba(220, 53, 69, 0);
    }
}

.alert-danger {
    /* ...原有样式保留... */
    animation: pulse 2s infinite;
}
```
