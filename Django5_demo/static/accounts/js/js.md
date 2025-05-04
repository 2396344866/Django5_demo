# JavaScript 核心知识点（20%代码解决80%问题）

## 一、变量与作用域
```javascript
// 1. let/const 块级作用域
let name = 'John';
const PI = 3.14;

// 2. 变量提升（避免使用var）
console.log(tmp); // undefined
var tmp = 5;
```

## 二、数据类型与操作
```javascript
// 1. 类型判断
typeof 42; // "number"
Array.isArray([1,2]); // true

// 2. 常用类型转换
Number('123'); // 123
String(123); // "123"
Boolean(0); // false

// 3. 解构赋值
const [a, b] = [1, 2];
const {name, age} = {name: 'Alice', age: 30};
```

## 三、函数核心
```javascript
// 1. 箭头函数
const sum = (a, b) => a + b;

// 2. 默认参数
function greet(name = 'Guest') {
  return `Hello ${name}`;
}

// 3. 剩余参数
function sumAll(...nums) {
  return nums.reduce((a, b) => a + b, 0);
}
```

## 四、数组高频方法
```javascript
const numbers = [1, 2, 3, 4];

// 1. map - 数据转换
const doubled = numbers.map(n => n * 2); // [2,4,6,8]

// 2. filter - 数据过滤
const evens = numbers.filter(n => n%2 === 0); // [2,4]

// 3. reduce - 数据聚合
const total = numbers.reduce((sum, n) => sum + n, 0); // 10

// 4. 展开运算符
const newArr = [...numbers, 5, 6];
```

## 五、对象操作
```javascript
// 1. 属性简写
const name = 'Bob';
const user = { name }; // {name: 'Bob'}

// 2. 对象合并
const obj1 = {a: 1};
const obj2 = {b: 2};
const merged = {...obj1, ...obj2}; // {a:1, b:2}

// 3. 可选链（ES2020）
const street = user?.address?.street;
```

## 六、DOM操作
```javascript
// 1. 元素选择
document.querySelector('#main');
document.querySelectorAll('.item');

// 2. 内容操作
element.textContent = 'New text';
element.innerHTML = '<strong>安全内容</strong>';

// 3. 样式操作
element.style.color = 'red';
element.classList.add('active');

// 4. 事件委托
document.querySelector('#list').addEventListener('click', event => {
  if(event.target.matches('li')) {
    console.log('List item clicked');
  }
});
```

## 七、异步处理
```javascript
// 1. Promise基础
fetchData()
  .then(data => process(data))
  .catch(error => console.error(error));

// 2. async/await
async function loadData() {
  try {
    const data = await fetchData();
    return data;
  } catch (error) {
    handleError(error);
  }
}

// 3. 并行请求
const [users, posts] = await Promise.all([fetchUsers(), fetchPosts()]);
```

## 八、ES6+关键特性
```javascript
// 1. 模板字符串
const message = `Hello ${name}, you have ${count} messages`;

// 2. 模块化
// math.js
export const add = (a, b) => a + b;

// app.js
import { add } from './math.js';

// 3. 空值合并运算符
const value = input ?? 'default';
```

## 九、错误处理
```javascript
try {
  JSON.parse(invalidJson);
} catch (err) {
  console.error('解析失败:', err.message);
}
```

## 十、性能优化技巧
1. **事件委托**：减少事件监听器数量
2. **防抖节流**：优化高频事件处理
3. **虚拟滚动**：处理长列表渲染
4. **缓存DOM查询**：避免重复查询

## 高频问题解决方案
1. 数组去重：`[...new Set(arr)]`
2. 深拷贝：`JSON.parse(JSON.stringify(obj))`（注意局限性）
3. 检测对象为空：`Object.keys(obj).length === 0`
4. 日期格式化：使用 `toLocaleDateString()`
5. URL参数解析：`new URLSearchParams(window.location.search)`

掌握这些核心知识点可覆盖日常开发80%的需求，建议重点练习数组方法、异步处理和DOM操作这三个最高频领域。