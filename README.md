# SQL-Target
* BIT网络于信息安全大作业：实现一次SQL注入攻击
* 最终实现：基于布尔盲注与联合查询的`GETSHELL`渗透实战攻击





#### 靶机模板

* `LNMP`框架

* 模板地址：https://github.com/xiabee/LNMP-Docker



#### 项目结构

* 靶机：`./target`
* `POC`：`./poc`



#### 部署方式

```bash
git clone https://github.com/xiabee/SQL-Target
cd ./SQL-Target/target
sudo chmod 777 -R www
# 需要给写入权限，否则无法完成getshell

docker-compose up -d
```



#### POC内容

* 布尔盲注获得`Flag`
* 联合查询写入`WEBSHELL`并连接
