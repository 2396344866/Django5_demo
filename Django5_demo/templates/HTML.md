# HTML 详细语法与标签属性参考手册

## 一、文档基础结构（标准化注释）

### 1.1 文档类型声明
```html
<!DOCTYPE html>
<!-- 
  作用：声明文档类型为 HTML5
  说明：必须位于文档第一行，不区分大小写
  历史版本：
    HTML4.01 → <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
    XHTML  → <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN">
-->
```

### 1.2 根元素
```html
<html lang="zh-CN">
<!-- 
  必需属性：
    lang - 定义文档语言（影响搜索引擎/屏幕阅读器）
    可选值：
      zh-CN → 简体中文
      en → 英语
      en-US → 美式英语
      ja → 日语
  
  扩展属性：
    xmlns → XHTML 命名空间（XHTML 必须添加）
    示例：<html xmlns="http://www.w3.org/1999/xhtml">
-->
```

### 1.3 头部元素（Head）
```html
<head>
  <!-- 
    内容类型：
      必须包含 <title> 元素
      建议包含 <meta charset>
      可选元素：
        <meta> → 元数据
        <link> → 外部资源
        <style> → 内联样式
        <script> → 脚本文件
        <base> → 基准URL
  -->
  <meta charset="UTF-8">
  <!-- 
    字符编码声明：
      必须位于 <head> 前 1024 字节
      推荐值：UTF-8（覆盖所有Unicode字符）
      历史编码：
        GB2312 → 简体中文
        GBK → 扩展中文
        ISO-8859-1 → 西欧字符
  -->
  
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- 
    视口配置（移动端适配核心）：
      content 参数：
        width → 视口宽度（device-width 表示设备宽度）
        height → 视口高度
        initial-scale → 初始缩放比例（1.0=不缩放）
        minimum-scale → 最小缩放比例
        maximum-scale → 最大缩放比例
        user-scalable → 是否允许缩放（yes/no）
      完整示例：
        content="width=device-width, initial-scale=1.0, maximum-scale=2.0, user-scalable=yes"
  -->
  
  <title>网页标题</title>
  <!-- 
    标题规则：
      长度建议：50-60字符
      SEO优化：包含关键词
      多级结构示例：
        <title>主标题 - 副标题 | 网站名称</title>
  -->
</head>
```

## 二、语义化标签详解

### 2.1 内容分区标签
| 标签        | 语义用途                          | 典型属性                     |
|-------------|-----------------------------------|------------------------------|
| `<header>`  | 页面/区块的页眉                   | 无特殊属性                   |
| `<nav>`     | 导航链接集合                      | aria-label（无障碍标签）     |
| `<main>`    | 页面主体内容（唯一）              | role="main"（兼容旧浏览器）  |
| `<article>` | 独立内容区块（文章/帖子等）       | pubdate（发布日期，HTML5弃用）|
| `<section>` | 文档的通用分组                    | aria-labelledby（关联标题）  |
| `<aside>`   | 侧边栏/附加内容                   | 无                           |
| `<footer>`  | 页面/区块的页脚                   | 无                           |

### 2.2 列表类型对比
```html
<!-- 无序列表 -->
<ul type="disc">
  <!-- 
    type 属性（CSS替代更佳）：
      disc → 实心圆（默认）
      circle → 空心圆
      square → 实心方块
  -->
  <li value="2">Item</li> <!-- 无效属性 -->
</ul>

<!-- 有序列表 -->
<ol type="1" start="5" reversed>
  <!-- 
    type 属性：
      1 → 数字（默认）
      A → 大写字母
      a → 小写字母
      I → 大写罗马数字
      i → 小写罗马数字
    
    start 属性：
      指定起始编号（任何整数值）
    
    reversed 属性：
      布尔值，倒序排列
  -->
  <li value="3">列表项可自定义编号</li>
</ol>
```

### 2.3 文本级语义标签
| 标签          | 语义                | 样式默认       | 推荐场景                 |
|---------------|---------------------|----------------|--------------------------|
| `<strong>`    | 重要性强调          | 加粗           | 警告/关键内容            |
| `<em>`        | 语气强调            | 斜体           | 改变句子含义的强调       |
| `<mark>`      | 突出显示            | 黄色背景       | 搜索结果高亮             |
| `<small>`      | 附属细则            | 小号字体       | 免责声明/版权信息        |
| `<time>`       | 时间/日期           | 无             | datetime属性指定机器可读格式 |
| `<code>`       | 代码片段            | 等宽字体       | 内联代码示例             |
| `<abbr>`       | 缩写词              | 虚线下划线     | 配合title属性说明完整形式|

## 三、表单元素深度解析

### 3.1 表单容器
```html
<form 
  action="/submit"
  method="POST"
  enctype="application/x-www-form-urlencoded"
  novalidate
  target="_blank"
>
<!-- 
  关键属性：
    method → 数据传输方式
      GET → 数据附加在URL（可见，长度受限）
      POST → 数据在请求体中（不可见，无长度限制）
    
    enctype → 编码类型：
      application/x-www-form-urlencoded → 默认（键值对）
      multipart/form-data → 文件上传
      text/plain → 纯文本（不推荐）
    
    novalidate → 禁用浏览器验证
    target → 提交响应显示位置
      _self → 当前窗口（默认）
      _blank → 新标签页
      _parent → 父框架
      _top → 顶级窗口
-->
</form>
```

### 3.2 输入类型全集（input type）
```html
<!-- 文本类 -->
<input type="text">     <!-- 单行文本 -->
<input type="password"> <!-- 密码字段 -->
<input type="email">    <!-- 邮箱验证 -->
<input type="tel">      <!-- 电话号码（移动端调出数字键盘） -->
<input type="url">      <!-- URL格式验证 -->
<input type="search">   <!-- 搜索字段（部分浏览器显示清除按钮） -->

<!-- 数字类 -->
<input type="number" 
  min="0" 
  max="100" 
  step="5"
> <!-- 步进按钮控制数值 -->

<!-- 时间类 -->
<input type="date">      <!-- 日期选择器 -->
<input type="time">      <!-- 时间选择器 -->
<input type="datetime-local"> <!-- 本地日期时间 -->
<input type="month">     <!-- 年月选择 -->
<input type="week">      <!-- 年周选择 -->

<!-- 选择类 -->
<input type="radio">     <!-- 单选按钮 -->
<input type="checkbox">  <!-- 复选框 -->
<input type="file" 
  accept=".jpg,.png" 
  multiple
> <!-- 文件上传 -->

<!-- 特殊类型 -->
<input type="color">     <!-- 颜色选择器 -->
<input type="range">     <!-- 滑块控件 -->
<input type="hidden">    <!-- 隐藏字段（不可见但会提交） -->
```

### 3.3 高级表单属性
```html
<!-- 输入验证 -->
<input 
  required               <!-- 必填字段 -->
  pattern="[A-Za-z]{3}" <!-- 正则验证 -->
  minlength="4"         <!-- 最小字符数 -->
  maxlength="20"        <!-- 最大字符数 -->
  min="10"              <!-- 最小值（数字/日期类型） -->
  max="100"             <!-- 最大值 -->
>

<!-- 数据列表 -->
<input list="browsers"> <!-- 关联datalist -->
<datalist id="browsers">
  <option value="Chrome">
  <option value="Firefox">
  <option value="Safari">
</datalist>

<!-- 输入模式 -->
<input 
  inputmode="numeric"   <!-- 虚拟键盘类型 -->
  autocomplete="on"     <!-- 自动填充建议 -->
>
<!-- 
  inputmode 可选值：
    numeric → 数字键盘
    email → 带@的键盘
    tel → 电话号码键盘
    url → 带/.com的键盘
-->
```

## 四、多媒体与嵌入技术

### 4.1 图像优化
```html
<img 
  src="image.jpg" 
  alt="描述文本" 
  loading="lazy" 
  decoding="async"
  srcset="image-2x.jpg 2x, image-small.jpg 600w"
  sizes="(max-width: 600px) 100vw, 50vw"
>
<!-- 
  高级属性：
    loading → 加载策略
      eager → 立即加载（默认）
      lazy → 延迟加载（进入视口后加载）
    
    decoding → 解码方式
      sync → 同步解码
      async → 异步解码
      auto → 浏览器决定（默认）
    
    srcset → 响应式图像源
      语法：图像地址 + 宽度描述符（w）或像素密度描述符（x）
    
    sizes → 媒体条件与显示尺寸
      配合srcset使用，定义不同视口下的显示尺寸
-->
```

### 4.2 视频控制
```html
<video 
  controls 
  muted 
  preload="metadata"
  poster="preview.jpg"
>
  <source src="video.mp4" type="video/mp4">
  <track 
    kind="subtitles" 
    src="subs_en.vtt" 
    srclang="en" 
    label="English"
  >
</video>
<!-- 
  关键属性：
    preload → 预加载策略
      none → 不预加载
      metadata → 加载元数据（时长等）
      auto → 加载整个视频（慎用）
    
    poster → 封面图像URL
    
  轨道属性（<track>）：
    kind → 字幕类型
      subtitles → 翻译字幕（默认）
      captions → 音效描述
      chapters → 章节导航
      descriptions → 视频描述
      metadata → 脚本元数据
-->

```

### 4.3 嵌入内容安全
```html
<iframe 
  src="https://example.com" 
  sandbox="allow-scripts allow-same-origin"
  referrerpolicy="no-referrer-when-downgrade"
></iframe>
<!-- 
  安全属性：
    sandbox → 沙箱限制
      可选值：
        allow-forms → 允许提交表单
        allow-popups → 允许弹出窗口
        allow-scripts → 允许执行脚本
        allow-same-origin → 保持同源
    
    referrerpolicy → 控制Referer头
      常用值：
        no-referrer → 不发送
        origin → 仅发送源（协议+域名+端口）
        strict-origin → HTTPS→HTTPS时发送源
-->

```

### 4.4 图标
```html
<!-- 使用 Bootstrap 图标示例（需引入图标库） -->
<i class="bi bi-house"></i>      <!-- 房子图标 -->
<i class="bi bi-alarm"></i>      <!-- 闹钟图标 -->
<i class="bi bi-person"></i>     <!-- 人物图标 -->
<i class="bi bi-bell"></i>       <!-- 铃铛图标 -->
<i class="bi bi-geo-alt"></i>     <!-- 地理位置图标 -->

<!-- 提示：通过 "class" 属性指定图标样式，需提前引入图标库（如 Bootstrap Icons） -->
```

## 五、全局属性参考

### 5.1 通用属性集
| 属性           | 适用元素                  | 功能描述                   |
|----------------|--------------------------|---------------------------|
| `id`           | 所有元素                 | 唯一标识（页面内必须唯一）|
| `class`        | 所有元素                 | CSS类名（多个用空格分隔）|
| `data-*`       | 所有元素                 | 自定义数据属性            |
| `style`        | 所有元素                 | 内联CSS样式（优先级最高）|
| `title`        | 所有元素                 | 提示文本（鼠标悬停显示） |
| `hidden`       | 所有元素                 | 隐藏元素（display:none） |
| `tabindex`     | 可聚焦元素               | 控制Tab键顺序（0/-1/正数）|
| `contenteditable` | 所有元素           | 允许用户编辑内容（布尔值）|
| `draggable`    | 所有元素                 | 启用拖放功能（true/false）|

### 5.2 ARIA 无障碍属性
```html
<div 
  role="navigation" 
  aria-label="主菜单"
  aria-hidden="true"
>
<!-- 
  role → 定义元素角色（补充语义）
    常用值：
      banner → 网站标识区域
      navigation → 导航区域
      main → 主要内容
      complementary → 补充内容
    
  aria-label → 为元素提供标签
  aria-hidden → 对屏幕阅读器隐藏
  aria-describedby → 关联描述元素ID
-->
</div>
```





# 后端：Django 
# HTML调整

### 1. 表单提交处理
原本 HTML 表单里的 `action` 属性要指向 Django 视图函数的 URL。同时，要添加 `csrf_token` 来保证 CSRF 防护。

```html
<form 
  action="{% url 'your_app:submit_form' %}"
  method="POST"
  enctype="application/x-www-form-urlencoded"
  novalidate
  target="_blank"
>
  {% csrf_token %}
  <!-- 表单内容 -->
</form>
```
这里的 `your_app` 指的是 Django 应用的名称，`submit_form` 是对应的视图函数名。

### 2. 静态文件加载
要是用到了图像、视频、图标库这类静态文件，就得借助 Django 的静态文件加载机制。

```html
{% load static %}
<img 
  src="{% static 'image.jpg' %}" 
  alt="描述文本" 
  loading="lazy" 
  decoding="async"
  srcset="{% static 'image-2x.jpg' %} 2x, {% static 'image-small.jpg' %} 600w"
  sizes="(max-width: 600px) 100vw, 50vw"
>
```

### 3. 动态内容渲染
若要展示从后端传来的数据，就得运用 Django 的模板语言。

```html
<h1>{{ page_title }}</h1>
<ul>
  {% for item in item_list %}
    <li>{{ item }}</li>
  {% endfor %}
</ul>
```

### 4. 嵌入 Django 模板标签和过滤器
在需要处理数据或者进行逻辑判断的地方，可以使用 Django 模板标签和过滤器。

```html
<p>当前时间：{{ current_time|date:"Y-m-d H:i:s" }}</p>
```

### 完整示例代码
以下是修改后的 HTML 代码示例：

```html
<!DOCTYPE html>
<!-- 
  作用：声明文档类型为 HTML5
  说明：必须位于文档第一行，不区分大小写
  历史版本：
    HTML4.01 → <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
    XHTML  → <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN">
-->
<html lang="zh-CN">
<!-- 
  必需属性：
    lang - 定义文档语言（影响搜索引擎/屏幕阅读器）
    可选值：
      zh-CN → 简体中文
      en → 英语
      en-US → 美式英语
      ja → 日语
  
  扩展属性：
    xmlns → XHTML 命名空间（XHTML 必须添加）
    示例：<html xmlns="http://www.w3.org/1999/xhtml">
-->
<head>
  <!-- 
    内容类型：
      必须包含 <title> 元素
      建议包含 <meta charset>
      可选元素：
        <meta> → 元数据
        <link> → 外部资源
        <style> → 内联样式
        <script> → 脚本文件
        <base> → 基准URL
  -->
  <meta charset="UTF-8">
  <!-- 
    字符编码声明：
      必须位于 <head> 前 1024 字节
      推荐值：UTF-8（覆盖所有Unicode字符）
      历史编码：
        GB2312 → 简体中文
        GBK → 扩展中文
        ISO-8859-1 → 西欧字符
  -->
  
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- 
    视口配置（移动端适配核心）：
      content 参数：
        width → 视口宽度（device-width 表示设备宽度）
        height → 视口高度
        initial-scale → 初始缩放比例（1.0=不缩放）
        minimum-scale → 最小缩放比例
        maximum-scale → 最大缩放比例
        user-scalable → 是否允许缩放（yes/no）
      完整示例：
        content="width=device-width, initial-scale=1.0, maximum-scale=2.0, user-scalable=yes"
  -->
  
  <title>{{ page_title }}</title>
  <!-- 
    标题规则：
      长度建议：50-60字符
      SEO优化：包含关键词
      多级结构示例：
        <title>主标题 - 副标题 | 网站名称</title>
  -->
</head>
<body>
  <form 
    action="{% url 'your_app:submit_form' %}"
    method="POST"
    enctype="application/x-www-form-urlencoded"
    novalidate
    target="_blank"
  >
    {% csrf_token %}
    <!-- 表单内容 -->
    <!-- 文本类 -->
    <input type="text">     <!-- 单行文本 -->
    <input type="password"> <!-- 密码字段 -->
    <input type="email">    <!-- 邮箱验证 -->
    <input type="tel">      <!-- 电话号码（移动端调出数字键盘） -->
    <input type="url">      <!-- URL格式验证 -->
    <input type="search">   <!-- 搜索字段（部分浏览器显示清除按钮） -->

    <!-- 数字类 -->
    <input type="number" 
      min="0" 
      max="100" 
      step="5"
    > <!-- 步进按钮控制数值 -->

    <!-- 时间类 -->
    <input type="date">      <!-- 日期选择器 -->
    <input type="time">      <!-- 时间选择器 -->
    <input type="datetime-local"> <!-- 本地日期时间 -->
    <input type="month">     <!-- 年月选择 -->
    <input type="week">      <!-- 年周选择 -->

    <!-- 选择类 -->
    <input type="radio">     <!-- 单选按钮 -->
    <input type="checkbox">  <!-- 复选框 -->
    <input type="file" 
      accept=".jpg,.png" 
      multiple
    > <!-- 文件上传 -->

    <!-- 特殊类型 -->
    <input type="color">     <!-- 颜色选择器 -->
    <input type="range">     <!-- 滑块控件 -->
    <input type="hidden">    <!-- 隐藏字段（不可见但会提交） -->
  </form>

  {% load static %}
  <img 
    src="{% static 'image.jpg' %}" 
    alt="描述文本" 
    loading="lazy" 
    decoding="async"
    srcset="{% static 'image-2x.jpg' %} 2x, {% static 'image-small.jpg' %} 600w"
    sizes="(max-width: 600px) 100vw, 50vw"
  >

  <video 
    controls 
    muted 
    preload="metadata"
    poster="{% static 'preview.jpg' %}"
  >
    <source src="{% static 'video.mp4' %}" type="video/mp4">
    <track 
      kind="subtitles" 
      src="{% static 'subs_en.vtt' %}" 
      srclang="en" 
      label="English"
    >
  </video>

  <iframe 
    src="https://example.com" 
    sandbox="allow-scripts allow-same-origin"
    referrerpolicy="no-referrer-when-downgrade"
  ></iframe>

  <!-- 使用 Bootstrap 图标示例（需引入图标库） -->
  <i class="bi bi-house"></i>      <!-- 房子图标 -->
  <i class="bi bi-alarm"></i>      <!-- 闹钟图标 -->
  <i class="bi bi-person"></i>     <!-- 人物图标 -->
  <i class="bi bi-bell"></i>       <!-- 铃铛图标 -->
  <i class="bi bi-geo-alt"></i>     <!-- 地理位置图标 -->

  <!-- 提示：通过 "class" 属性指定图标样式，需提前引入图标库（如 Bootstrap Icons） -->

  <div 
    role="navigation" 
    aria-label="主菜单"
    aria-hidden="true"
  >
    <!-- 
      role → 定义元素角色（补充语义）
      常用值：
        banner → 网站标识区域
        navigation → 导航区域
        main → 主要内容
        complementary → 补充内容
      
      aria-label → 为元素提供标签
      aria-hidden → 对屏幕阅读器隐藏
      aria-describedby → 关联描述元素ID
    -->
  </div>
</body>
</html>
```

#### 视图函数（`views.py`）
```python
from django.http import HttpResponse
from django.shortcuts import render

def submit_form(request):
    if request.method == 'POST':
        # 处理表单数据
        return HttpResponse('表单提交成功')
    return render(request, 'your_template.html')

```

#### URL 配置（`urls.py`）
```python
from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_form, name='submit_form'),
]
```

保证在 `settings.py` 里正确配置静态文件路径
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```