## Cosmos自动化测试

### 一.简介
项目基于Cosmos 通讯模型对Cosmos 小核/插件做自动化测试,测试场景涵盖: UI自动化测试和接口自动化测试。
采用KDT + DDT 模式组织测试用例,支持边界测试、异常测试、压力测试、回归测试。
[开发方案](http://172.20.200.191:8003/pages/viewpage.action?pageId=904728130)

### 二.安装说明
```
# 进入跟目录
cd cosmos
# 安装依赖包
pip install -r requirements.txt

# 执行全部用例
pytest -v
```

### 三.目录结构
```
├─src                           // 主目录
│  ├─Application                // 应用层 (负责构建测试用例)
│  │  ├─Sdk                     // 应用层-小核通讯能力
│  │  │  ├─Event                // 应用层-小核通讯能力-事件模型
│  │  │  ├─Invoke               // 应用层-小核通讯能力-方法模型
│  │  │  ├─Repository           // 应用层-小核通讯能力-数据模型
│  │  │  ├─Widget               // 应用层-小核通讯能力-插件相关
│  │  ├─TestCase                // 应用层-测试用例
│  │  │  ├─Boundary             // 应用层-测试用例-边界测试
│  │  │  │  └─DataToChart       // 应用层-测试用例-边界测试-智能图表 
│  │  │  ├─Exception            // 应用层-测试用例-异常测试
│  │  │  ├─Regression           // 应用层-测试用例-回归测试
│  │  │  └─Stress               // 应用层-测试用例-压力测试
│  │  │      ├─DataToChart      // 应用层-测试用例-压力测试-智能图表
│  │  ├─TestData                // 应用层-测试数据
│  │  ├─TestResult              // 应用层-测试结果
│  ├─Infrastructure             // 基础设施层 (负责提供通用功能)
│  │  ├─Analysis                // 基础设施层-指标分析
│  │  ├─Config                  // 基础设施层-配置 
│  │  ├─Data                    // 基础设施层-数据管理  
│  │  ├─Grpc                    // 基础设施层-Grpc    
│  │  └─Log                     // 基础设施层-日志
│  ├─Presentation               // 展示层 (负责对外提供可视化报告、触发器等)
└─vendor                        // 小核程序
```

### 四.测试流程
#### 测试数据
#### 测试执行
1）准备环境
   按会话 > 模块 > 方法层次, 准备每个用例的测试环境   
2）扫描脚本
   按所有 > 文件夹 > 文件 > 函数/标签层级, 扫描执行的脚本
   其中，标签分为: 测试类型、插件,集中配置在 pytest.ini中
3）执行脚本
```python
pytest src -[options]
```
#### 测试结果
1）指标采集
2）指标分析
3）测试报告

#### 示例
以DataToChart 压力测试为例:
```
1）准备环境
   启动小核 ---> 执行用例 ---> 关闭小核   
2）扫描脚本
3）执行脚本
pytest src -m "Test_Type_Stress"
```

### 五.方法/功能
#### 小核

1. 启动小核
```python
path = "D:/Desktop/Cosmos.Client.Vendor.exe"
param = "-purl http://localhost:8068 -vurl http://{target} -ppid -1 -wm Offline".format(target=GrpcChannel.target)
pid = VendorProcessor.Start(param=param, path=path)
```
2. 通知
3. 关闭


#### 插件
1. 创建插件
```python
value = WidgetProcessor.Create(widgetGuid, widgetVersion, "Visible", "Visible")
```
2. 调用插件方法
```python
WidgetProcessor.Invoke(widgetHandle, "SetSeriesInfo", data)
```


### 六.通用基础设施
#### 数据管理
1. 获取测试数据
```python
daily.GetTestData(code, count, itemKey)
```

#### 指标分析
1. 图片相似度
```python
dist = ImageSimilarity.DiffPicture(reference, compare)
```
2. 根据句柄截图
```python
Profile.SaveWindowPicture(widgetHandle, path):
```
3. 绘制Excel图片
```python
Profile.ShowProfile(filePath)
```

#### 配置
#### 日志
#### Grpc

### 七.补充说明
1. 关于可视化测试报告
```
# 输出测试报告
pytest src -m "Test_Mark" --alluredir  ./Allure/result/
# 可视化报告
allure serve  ./Allure/result/
```